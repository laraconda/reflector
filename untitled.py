import sublime, sublime_plugin
from sublime import Region
import unicodedata


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		invert_line(self.view, edit)
		# replace_char_for_its_mirror(self.view, edit)


def replace_char_for_its_mirror(my_view, edit):
	for i in range(0, my_view.size()):
		region = Region(i, i+1)
		mirror_char = get_mirror_char(my_view.substr(region))
	return None


def invert_line(my_view, edit):
	region = Region(0, my_view.size())
	lines = my_view.split_by_newlines(region)
	for region_line in lines:
		line = my_view.substr(region_line)
		print line
		line = line[::-1]
		my_view.replace(edit, region_line, line)
	return None


def get_mirror_char(char_to_mirror):
	return None

# view.run_command('example')
