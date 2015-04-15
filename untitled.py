import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		replace_all_letters_to_a(self.view, edit)

def replace_all_letters_to_a(my_view, edit):
	region = my_view.word(2)
	my_view.replace(edit, region, 'a')
	return None

# view.run_command('example')