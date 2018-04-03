import sublime
import sublime_plugin

from ..Core.Controller import *

class gitCommitCommand(sublime_plugin.TextCommand, gitController):
    def run(self, edit):
    	print("Commit!! jk")