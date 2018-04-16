import sublime
import sublime_plugin

from ..Core.Controller import *

class gitPushCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit):
		print('push')
		# git.exe push --progress "origin" HomeCheckOut:NateHomeCheckout
		self.dir = self.get_scoped_path('repo')
		# branchData = self.run_git_command(["git", "status", "-sb"], self.dir)
		# branchData = branchData.replace("##", "")
		# branchData = branchData.replace("...", ":").strip()
		# branchData = branchData.replace("origin/", "").strip()
		# print(branchData)
		cmd = self.run_git_command(["git", "push", "origin"], self.dir)
		show_output_panel(cmd)

