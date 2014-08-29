import sublime, sublime_plugin


class AccessbilityToggleSettingsCommand(sublime_plugin.ApplicationCommand):

    """Enables/Disables settings"""

    def run(self, setting):
        s = sublime.load_settings('Accessbility-sublime-package.sublime-settings')
        s.set(setting, not s.get(setting, False))
        sublime.save_settings('Accessbility-sublime-package.sublime-settings')

    def is_checked(self, setting):
        s = sublime.load_settings('Accessbility-sublime-package.sublime-settings')
        return s.get(setting, False)
