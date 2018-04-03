import sublime
import sublime_plugin

from ..Core.Controller import *

class gitCommitCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit):
		print("Commit!! jk")
		self.path = self.get_git_dir()
		if len(self.path) == 0:
			return;


		self.path = self.get_scoped_path(git_settings().get('commit_scope', 'file'))

		print(self.path)

		message = "'test Message'"

		self.run_git_command([ "git", "commit", "-m", message, "--", self.path])

		print("Commit!! jk")