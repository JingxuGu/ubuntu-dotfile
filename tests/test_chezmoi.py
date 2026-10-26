import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOL = os.environ.get('CHEZMOI') or shutil.which('chezmoi')


@unittest.skipUnless(TOOL, 'Set CHEZMOI or install chezmoi for rendering integration tests')
class ChezmoiRenderTests(unittest.TestCase):
    def render(self, profile, device_overrides=False):
        temp = tempfile.TemporaryDirectory(prefix='dotfiles-render-')
        self.addCleanup(temp.cleanup)
        work = Path(temp.name)
        home = work / 'home'
        home.mkdir()
        config = work / 'chezmoi.toml'
        config.write_text(f'''[data]
profile = "{profile}"
deviceName = "test-device"
fontFamily = "{'DejaVu Sans Mono' if device_overrides else 'JetBrainsMono Nerd Font Mono'}"
fontSize = {14.5 if device_overrides else 12.0}
opacity = {0.8 if device_overrides else 0.65}
monitor = "{'HDMI-A-1' if device_overrides else 'DP-2'}"
scale = {1.25 if device_overrides else 1.1}
windowRadius = {16 if device_overrides else 12}
proxyPort = {8888 if device_overrides else 7897}
''')
        args = [str(TOOL), '--source', str(ROOT), '--config', str(config), '--destination', str(home),
                '--cache', str(work / 'cache'), '--persistent-state', str(work / 'state.boltdb')]
        subprocess.run(args + ['apply', '--force'], capture_output=True, text=True, check=True)
        return home, args

    def test_each_system_deploys_its_own_backend_and_excludes_other_desktop(self):
        for profile in ['ubuntu-26.04-niri', 'ubuntu-22.04-gnome']:
            with self.subTest(profile=profile):
                home, args = self.render(profile)
                kitty = (home / '.config/kitty/kitty.conf').read_text()
                self.assertNotIn('/home/grainrain', (home / '.config/fastfetch/config.jsonc').read_text())
                self.assertTrue((home / '.zshrc').is_file())
                if profile.endswith('gnome'):
                    self.assertIn('linux_display_server x11', kitty)
                    self.assertTrue((home / '.config/kitty/colors.conf').is_file())
                    environment = (home / '.config/environment.d/90-fcitx5.conf').read_text()
                    self.assertIn('GLFW_IM_MODULE=ibus', environment)
                    self.assertIn('GTK_IM_MODULE=fcitx', environment)
                    self.assertFalse((home / '.config/niri').exists())
                    self.assertFalse((home / '.config/DankMaterialShell').exists())
                    self.assertFalse((home / '.local/bin/screenshot').exists())
                else:
                    self.assertIn('linux_display_server wayland', kitty)
                    self.assertTrue((home / '.config/niri/config.kdl').is_file())
                    self.assertTrue(os.access(home / '.local/bin/screenshot', os.X_OK))
                    self.assertFalse((home / '.config/kitty/colors.conf').exists())
                    self.assertFalse((home / '.config/environment.d/90-fcitx5.conf').exists())

    def test_device_parameters_render_home_monitor_font_and_opacity(self):
        home, args = self.render('ubuntu-26.04-niri', device_overrides=True)
        kitty = (home / '.config/kitty/kitty.conf').read_text()
        self.assertIn('font_family DejaVu Sans Mono', kitty)
        self.assertIn('font_size 14.5', kitty)
        self.assertIn('background_opacity 0.8', kitty)
        niri = (home / '.config/niri/config.kdl').read_text()
        self.assertIn('output "HDMI-A-1"', niri)
        self.assertIn('scale 1.25', niri)
        self.assertIn('geometry-corner-radius 16', niri)
        self.assertIn(str(home), niri)
        haru = json.loads((home / '.config/haru/config.json').read_text())
        self.assertIn('HDMI-A-1', haru['screens'])

    def test_existing_wallpaper_colors_are_not_overwritten_on_reapply(self):
        home, args = self.render('ubuntu-26.04-niri')
        colors = home / '.config/kitty/dank-theme.conf'
        self.assertTrue(colors.is_file())
        colors.write_text('# freshly generated wallpaper colors\nbackground #112233\n')
        subprocess.run(args + ['apply', '--force'], capture_output=True, text=True, check=True)
        self.assertEqual(colors.read_text(), '# freshly generated wallpaper colors\nbackground #112233\n')

    def test_reinitialization_preserves_existing_device_parameters(self):
        home, args = self.render('ubuntu-26.04-niri', device_overrides=True)
        subprocess.run(args + ['init'], capture_output=True, text=True, check=True)
        subprocess.run(args + ['apply', '--force'], capture_output=True, text=True, check=True)
        kitty = (home / '.config/kitty/kitty.conf').read_text()
        self.assertIn('font_family DejaVu Sans Mono', kitty)
        self.assertIn('background_opacity 0.8', kitty)


if __name__ == '__main__':
    unittest.main()
