# -*- coding: utf-8 -*-
import sublime, sublime_plugin
from sublime import Region
import unicodedata


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#invert_line(self.view, edit)
		replace_char_for_its_mirror(self.view, edit)


def replace_char_for_its_mirror(my_view, edit):
	for i in range(0, my_view.size()):
		region = Region(i, i+1)
		mirror_char = get_mirror_char(my_view.substr(region))
		print mirror_char
	return None


def invert_line(my_view, edit):
	region = Region(0, my_view.size())
	lines = my_view.split_by_newlines(region)
	for region_line in lines:
		line = my_view.substr(region_line)
		line = line[::-1]
		my_view.replace(edit, region_line, line)
	return None


def get_mirror_char(char_to_mirror):
	no_need_to_change_base_chars = ['i', 'l', 'm', 'n', 'o', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '	', ':', '_', '#', ',', '.', '\n', '\'', 'T']
	original_base_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'p', 'q', 'r', 's', 't', '(', ')']
	mirrored_base_chars = ['α', 'd', 'ɔ', 'b', 'ɘ', 'ʇ', 'ǫ', 'ʜ', 'Ⴑ', 'ʞ', 'q', 'p', 'ɿ', 'ƨ', 'ƚ', ')', '(']

	if char_to_mirror in no_need_to_change_base_chars:
		return char_to_mirror
	elif char_to_mirror in original_base_chars:
		return mirrored_base_chars[(original_base_chars.index(char_to_mirror))]

# view.run_command('example')
