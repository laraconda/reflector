import sublime, sublime_plugin
from sublime import Region


class EventListenerCommand(sublime_plugin.EventListener):
	def on_modified(self, view):
		print 'editing document'            


# view.run_command('eventlistener')