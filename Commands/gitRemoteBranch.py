import sublime
import sublime_plugin

from ..Core.Controller import *
from ..Core.History import *

class gitRemoteBranch(sublime_plugin.TextCommand, gitController):
    def run(self, scope):
		self.dir = self.get_scoped_path('repo')
    	branches = self.run_git_command(["git", "branch"], self.dir)
    	print('gitRemoteBranch')
    	print(branches)