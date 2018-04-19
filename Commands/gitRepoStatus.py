import sublime
import sublime_plugin

from ..Core.Controller import *


class gitRepoStatusCommand(sublime_plugin.TextCommand, gitController):
    def run(self, edit):
        self.gitDir = self.get_scoped_path('repo')
        procText = self.run_git_command(["git", "diff-files", "--name-status"], self.gitDir)
        show_output_panel(procText)

    def is_enabled(self):
        return len(str(self.get_git_dir())) != 0
