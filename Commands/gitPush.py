import sublime
import sublime_plugin

from ..Core.Controller import *

class gitPushCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit):
		print('push')