import sublime, sublime_plugin
from sublime import Region
from criteria import no_need_to_change_base_chars, original_base_chars, mirrored_base_chars
from criteria import char_that_its_mirror_is_common


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		invert_lines(self.view, edit)
		# replace_char_for_its_mirror(self.view, edit)


def replace_char_for_its_mirror(my_view, edit):
	for i in range(0, my_view.size()):
		region = Region(i, i+1)
		mirror_char = get_mirror_char(my_view.substr(region))
		print mirror_char
	return None


def invert_lines(my_view, edit):
	region = Region(0, my_view.size())
	lines = my_view.split_by_newlines(region)
	for region_line in lines:
		line = my_view.substr(region_line)
		flipped_line = line[::-1]
		for i, char_to_mirror in enumerate(flipped_line):
			mirror_char = get_mirror_char(char_to_mirror).decode('utf-8')
			if char_to_mirror in char_that_its_mirror_is_common:
				flipped_line_list = list (flipped_line)
				flipped_line_list[i] = mirror_char
				flipped_line = ''.join(flipped_line_list)
			else:
				flipped_line = flipped_line.replace(char_to_mirror, mirror_char)
		my_view.replace(edit, region_line, flipped_line)
	return None


def get_mirror_char(char_to_mirror):
	if char_to_mirror in no_need_to_change_base_chars:
		return char_to_mirror
	elif char_to_mirror in original_base_chars:
		index = original_base_chars.index(char_to_mirror)
		char = mirrored_base_chars[index]
		return char
	return char_to_mirror
# view.run_command('example')
	