"""Check the optional Kitty blur profile without changing the real desktop."""
from contextlib import redirect_stdout
from io import StringIO
import importlib.util
import os
from pathlib import Path
import tempfile
import unittest

os.environ['GSETTINGS_BACKEND'] = 'memory'
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'kitty_blur_gnome', ROOT / 'dotfile/ubuntu-22.04-gnome/gnome.py')
gnome = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gnome)


class KittyBlurTests(unittest.TestCase):
    def test_apply_and_undo_preserve_input_shortcuts_and_other_components(self):
        try:
            apps = gnome.settings_for('org.gnome.shell.extensions.blur-my-shell.applications')
            panel = gnome.settings_for('org.gnome.shell.extensions.blur-my-shell.panel')
        except ValueError:
            self.skipTest('Blur my Shell application and panel schemas are not installed')
        shell = gnome.settings_for('org.gnome.shell')
        keys = gnome.settings_for('org.gnome.desktop.wm.keybindings')
        sources = gnome.settings_for('org.gnome.desktop.input-sources')
        guarded = [(panel, 'sigma'), (keys, 'switch-input-source'), (sources, 'sources')]
        before = [(s, key, s.get_value(key)) for s, key in guarded]
        originals = [(apps, key, apps.get_user_value(key))
                     for key in apps.props.settings_schema.list_keys()]
        originals += [(shell, key, shell.get_user_value(key)) for key in
                      ('enabled-extensions', 'disabled-extensions', 'disable-user-extensions')]
        try:
            apps.set_boolean('blur', False)
            apps.set_boolean('enable-all', True)
            apps.set_strv('whitelist', ['previous.application'])
            shell.set_strv('enabled-extensions', ['other.extension'])
            shell.set_strv('disabled-extensions', ['blur-my-shell@aunetx', 'other.disabled'])
            shell.set_boolean('disable-user-extensions', True)
            baseline = [(s, key, s.get_user_value(key)) for s, key, _ in originals]
            with tempfile.TemporaryDirectory() as directory, redirect_stdout(StringIO()):
                backup = Path(directory) / 'apply'
                profile = ROOT / 'dotfile/ubuntu-22.04-gnome/gnome/kitty-blur.json'
                gnome.apply_settings(gnome.plan_settings(profile), backup)
                self.assertTrue(apps.get_boolean('blur'))
                self.assertFalse(apps.get_boolean('enable-all'))
                self.assertEqual(apps.get_strv('whitelist'), ['kitty', 'Kitty'])
                self.assertEqual(apps.get_int('opacity'), 255)
                self.assertIn('other.extension', shell.get_strv('enabled-extensions'))
                self.assertIn('other.disabled', shell.get_strv('disabled-extensions'))
                for settings, key, value in before:
                    self.assertTrue(settings.get_value(key).equal(value), key)
                self.assertEqual(gnome.plan_settings(profile), [])
                gnome.apply_settings(gnome.plan_undo(backup / 'gnome-settings.json'),
                                     Path(directory) / 'undo')
                for settings, key, value in baseline:
                    restored = settings.get_user_value(key)
                    if value is None:
                        self.assertIsNone(restored, key)
                    else:
                        self.assertIsNotNone(restored, key)
                        self.assertTrue(restored.equal(value), key)
        finally:
            for settings, key, value in originals:
                if value is None:
                    settings.reset(key)
                else:
                    settings.set_value(key, value)


if __name__ == '__main__':
    unittest.main()
