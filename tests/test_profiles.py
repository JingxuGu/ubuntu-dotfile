import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SYSTEMS = json.loads((ROOT / 'systems.json').read_text())


class ProfileLayoutTests(unittest.TestCase):
    def test_every_snapshot_file_is_preserved_from_its_source_commit(self):
        for profile, system in SYSTEMS.items():
            base = ROOT / 'dotfile' / profile
            manifest = json.loads((base / 'snapshot.json').read_text())
            for item in manifest['files']:
                with self.subTest(profile=profile, path=item['path']):
                    original = subprocess.check_output(
                        ['git', 'show', system['source_commit'] + ':' + item['path']], cwd=ROOT)
                    self.assertEqual((base / item['path']).read_bytes(), original)

    def test_source_helpers_and_plugin_patch_are_preserved(self):
        files = {
            'ubuntu-26.04-niri': ['restore.py', 'plugins.json', 'patches/dms-mpvpaper.patch',
                                 'fonts/jetbrains-mono.json', 'theming/dms/pipeline.json'],
            'ubuntu-22.04-gnome': ['restore.py', 'gnome.py', 'gnome/settings.json',
                                  'gnome/blur-my-shell.json', 'tests/test_gnome.py', 'tests/test_restore.py'],
        }
        for profile, names in files.items():
            for name in names:
                with self.subTest(profile=profile, path=name):
                    original = subprocess.check_output(
                        ['git', 'show', SYSTEMS[profile]['source_commit'] + ':' + name], cwd=ROOT)
                    self.assertEqual((ROOT / 'dotfile' / profile / name).read_bytes(), original)

    def test_docs_have_configuration_items_for_both_systems(self):
        for profile in SYSTEMS:
            for name in ['README.md', 'desktop.md', 'terminal.md', 'input-method.md', 'screenshots.md', 'packages.md']:
                with self.subTest(profile=profile, document=name):
                    self.assertTrue((ROOT / 'docs' / profile / name).is_file())
        self.assertEqual((ROOT / '.chezmoiroot').read_text().strip(), 'chezmoi')

    def test_niri_snapshot_restore_works_from_its_new_location(self):
        tool = ROOT / 'dotfile/ubuntu-26.04-niri/restore.py'
        with tempfile.TemporaryDirectory() as directory:
            for options in [['--apply'], []]:
                result = subprocess.run(['python3', str(tool), '--home', directory, *options],
                                        capture_output=True, text=True, check=True)
            self.assertIn('0 file(s) would change.', result.stdout)
            text = (Path(directory) / '.config/fastfetch/config.jsonc').read_text()
            self.assertNotIn('/home/grainrain', text)


if __name__ == '__main__':
    unittest.main()
