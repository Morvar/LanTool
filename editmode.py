from collections import OrderedDict
from scene import Scene
from buildmode import initialized_build_mode
def initialized_edit_mode(project):
	#specify the title
	title = "Edit Mode"

	#specify the functions
	def enter_buildmode(scene, args):
		build_mode = initialized_build_mode()
		while True:
			build_mode.enter()
			# is this a sane thing to do here?
			scene.draw()
			break

	def browse(scene, args):
		pass

	def search(scene, args):
		pass

	def edit(scene, args):
		pass

	def add(scene, args):
		pass

	def save(scene, args):
		pass

	def exit_editmode(scene, args):
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
