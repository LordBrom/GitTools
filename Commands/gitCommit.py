import sublime
import sublime_plugin

from ..Core.Controller import *
from ..Core.History import *

class gitCommitCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit, showHistory = False, doPush = False):


		if showHistory:
			print(gitHistory.getHistory(includeNewLogOption = True))


		self.path = self.get_git_dir()
		if len(self.path) == 0:
			return;


		self.path = self.get_scoped_path(git_settings().get('commit_scope', 'file'))
		self.dir = self.get_scoped_path('repo')

		print(self.path)
		print(self.dir)

		message = "test Message"
		self.run_git_command(["git", "commit", "-m", message, self.dir], self.dir)

