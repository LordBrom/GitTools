import sublime
import sublime_plugin

from ..Core.Controller import *
from ..Core.History import *

class gitCommitCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit, showHistory = False):

		self.path = self.get_git_dir()
		if len(self.path) == 0:
			return;

		self.path = self.get_scoped_path(git_settings().get('Git.commit_scope', 'file'))
		self.rootDir = self.get_scoped_path('repo')

		if showHistory:
			self.messageList = gitHistory.get_history(includeNewLogOption = True)
			sublime.active_window().show_quick_panel(self.messageList, self.sel_message)
		else:
			message = gitHistory.get_history(getLast = True)
			if len(message) == 0:
				self.new_message()
			else:
				self.do_commit(message)



	def sel_message(self, index):
		try:
			message = self.messageList[index]

			if index == -1:
				pass
			elif message == 'New Log':
				self.new_message()
			else:
				self.do_commit(message)

		except ValueError:
			pass

	def new_message(self):

		self.message_placeholders = git_settings().get('Git.message_placeholders', ['message'])
		self.placeholders_filled = [];
		self.index = 0;
		self.debug_print(message = self.message_placeholders, first = True, last = True)

		self.message_prompt();


	def message_prompt( self ):
		self.debug_print(message = self.index, first = True, last = True)
		prompt = self.message_placeholders[self.index];
		sublime.active_window().show_input_panel(prompt + ":", "", self.on_submit, None, None)

	def on_submit(self, text):
		try:
			self.placeholders_filled.append(text)

			self.index += 1
			if self.index < len(self.message_placeholders):
				self.message_prompt()

			else:
				finalMessage = git_settings().get('Git.message_template', '[0]')

				for index in range(len(self.message_placeholders)):
					print(index)
					finalMessage = finalMessage.replace("["+ str(index) +"]", self.placeholders_filled[index])

				self.do_commit(finalMessage)

		except ValueError:
			pass


	def do_commit(self, message):
		self.run_git_command(["git", "commit", "-m", message, self.path], self.rootDir)
		gitHistory.add_history(message)

		if git_settings().get('Git.auto_push_after_commit', True) == True:
			print("pushed")
		# 	sublime.active_window().run_command("git_push")

