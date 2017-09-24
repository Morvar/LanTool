from collections import OrderedDict
from scene import Scene
from buildmode import initialized_build_mode
def initialized_edit_mode():
	#specify the title
	title = "Edit Mode"

	#specify the functions
	def enter_buildmode(scene):
		build_mode = initialized_build_mode()
		while True:
			build_mode.enter()
			# is this a sane thing to do here?
			scene.draw()
			break

	def browse(scene):
		pass

	def search(scene):
		pass

	def edit(scene):
		pass

	def add(scene):
		pass

	def save(scene):
		pass

	def exit_editmode(scene):
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
