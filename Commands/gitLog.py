import sublime
import sublime_plugin

from ..Core.Controller import *
from ..Core.History import *

class gitLogCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit, showHistory = False):
		self.dir = self.get_scoped_path('repo')

		print(showHistory)

		if showHistory:
			self.messageList = gitHistory.get_history(includeNewLogOption = True, newLogText = 'Custom Search')
			sublime.active_window().show_quick_panel(self.messageList, self.sel_message)
		else:
			self.do_log('')

	def sel_message(self, index):
		try:
			message = self.messageList[index]

			if index == -1:
				pass
			elif message == 'Custom Search':
				self.new_message()
			else:
				self.do_log(message)

		except ValueError:
			pass


	def new_message(self):
		sublime.active_window().show_input_panel("Custom Search:", "", self.do_log, None, None)



	def do_log(self, grepString):
		print('running command')
		cmd = self.run_git_command(["git", "log", "--grep", grepString, "--oneline"], self.dir)
		show_output_panel(cmd)