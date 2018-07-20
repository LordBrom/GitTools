import sublime
import sublime_plugin

from ..Core.Controller import *

class gitFetchCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit):
		print('pull')

		self.dir = self.get_scoped_path('repo')

		cmd = self.run_git_command(["git", "fetch", "origin"], self.dir)
		show_output_panel(cmd)

