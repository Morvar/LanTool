from collections import OrderedDict
from scene import Scene
def initialized_edit_mode():
	#specify the title
	title = "Edit Mode"

	#specify the functions
	def enter_buildmode():
		pass

	def browse():
		pass

	def search():
		pass

	def edit():
		pass

	def add():
		pass

	def save():
		pass

	def exit_editmode():
		while True:
			print("Do you want to exit " + title + "? (yes/no)")
			i = input(" > ")
			if i == "yes":
				return False
			if i == "no":
				break
			else:
				print("Error: Unrecognized command")

	#specify the commands and which functions they will use
	commands = OrderedDict()
	commands["buildmode"] = ("Enter Build Mode", enter_buildmode)
	commands["browse"] = ("Browse", browse)
	commands["search"] = ("Search word", search)
	commands["edit"] = ("Edit word", edit)
	commands["add"] = ("Add word", add)
	commands["save"] = ("Save changes", save)
	commands["exit"] = ("Exit", exit_editmode)

	#create an edit mode from the Scene class
	edit_mode = Scene(title, commands)
	return edit_mode
