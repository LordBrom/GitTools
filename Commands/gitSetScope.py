import sublime
import sublime_plugin
import os.path
import subprocess
import functools
import datetime

from ..Core.Controller import *

class gitSetScopeCommand(sublime_plugin.ApplicationCommand, gitController):

    def run(self, scope):
        git_settings().set('commit_scope', scope)
        sublime.save_settings('Preferences.sublime-settings')
        sublime.status_message( "Commit scope set to " + scope );

    def is_checked(self, scope):
        selScope = git_settings().get('commit_scope', 'file')
        return selScope == scope
