import sublime
import sublime_plugin

from ..Core.Controller import *

class gitPushCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit):
		print('push')
		# git.exe push --progress "origin" HomeCheckOut:NateHomeCheckout
		self.dir = self.get_scoped_path('repo')

		response = self.run_git_command(["git", "push", "origin"], self.dir)

		if '(fetch first)' in response:
			if sublime.ok_cancel_dialog("The repo is out of date. Would you like to fetch the changes, and push again?"):
				sublime.active_window().run_command("git_pull")
				sublime.active_window().run_command("git_push")
				return
			else:
				show_output_panel(response)
				return

		show_output_panel(response)

