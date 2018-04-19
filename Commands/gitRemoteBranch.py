import sublime
import sublime_plugin

from ..Core.Controller import *
from ..Core.History import *

class gitRemoteBranch(sublime_plugin.TextCommand, gitController):
    def run(self, scope):
        self.dir = self.get_scoped_path('repo')
        branches = self.run_git_command(["git", "branch", "-r"], self.dir)
        self.branches = branches.split( '\n' )
        sublime.active_window().show_quick_panel(self.branches, self.sel_remote_branch)

    def sel_remote_branch(self, index):
        try:
            branchName = self.branches[index]
            if index == -1:
                pass
            elif branchName == 'New Branch':
                self.new_branch()
            else:
                self.do_set_branch(branchName)

        except ValueError:
            pass

    def new_branch():
        sublime.active_window().show_input_panel("Remote Brach Name:", "", self.do_set_branch, None, None)


    def do_set_branch(self, branchName):
        cmd = self.run_git_command(["git", "branch", "--set-upstream-to", branchName.strip()], self.dir)
        sublime.status_message( cmd.strip() );