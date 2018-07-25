import sublime
import sublime_plugin
import os.path
import subprocess
import functools
import datetime

from ..Core.Controller import *

class gitSetScopeCommand(sublime_plugin.ApplicationCommand, gitController):

	def run(self, scope):
		sublime.load_settings('Preferences.sublime-settings').set('Git.commit_scope', scope)
		sublime.save_settings('Preferences.sublime-settings')
		sublime.status_message( "Commit scope set to " + scope );

	def is_checked(self, scope):
		selScope = git_settings().get('Git.commit_scope', 'file')
		return selScope == scope
