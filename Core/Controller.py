import sublime
import sublime_plugin
import os.path
import subprocess
import functools
import datetime

def git_settings():
    return sublime.load_settings( 'GitTools.sublime-settings' )


class gitController():

    def run_git_command(self, params = [], dir = '', stripResult = True):
    	print("Running command")