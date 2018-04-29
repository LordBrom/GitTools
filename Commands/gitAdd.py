import sublime
import sublime_plugin

from ..Core.Controller import *

class gitAddCommand(sublime_plugin.TextCommand, gitController):
    def run(self, edit):
        self.gitDir = self.get_git_dir();
        if len(self.gitDir) == 0:
            return;

        self.confirmList = ['Add current file to repo', 'Add current directory to repo']
        sublime.active_window().show_quick_panel(self.confirmList, self.do_Add)

    def do_Add(self, index):
        # print('added')
        self.scope = ''
        if index == -1 :
            return
        elif index == 0:
            self.gitDir = self.get_scoped_path('file')
            self.scope = 'File'
        else:
            self.gitDir = self.get_scoped_path('dir')
            self.scope = 'Directory'

        self.gitRoot = self.get_scoped_path('repo')
        self.gitDir = self.get_scoped_path('file')
        procText = self.run_git_command([ "git", "add", self.gitDir], self.gitRoot);
        procText = procText.strip( ).split( '\n' )[-1].strip( );

        if "Illegal target" in procText:
            procText = "Could not add file(s); check for conflicts or other issues."
        else:
            # print(procText)
            procText = "Added file(s) to repo"
        sublime.status_message(procText);

    def is_enabled(self):
        return len(str(self.get_git_dir())) != 0
