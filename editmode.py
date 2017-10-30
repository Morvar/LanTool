from collections import OrderedDict
from scene import Scene
from buildmode import initialized_build_mode
from constants import input_prompt
def initialized_edit_mode(project):
	project_name = "projectname retrieval to be implemented"
	#specify the title
	title = f"Edit Mode [{project_name}]"

	#specify the functions
	def enter_buildmode(scene, args):
		build_mode = initialized_build_mode()
		build_mode.enter()
		# is drawing scene a sane thing to do here?
		scene.draw()
		return

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
			i = input(input_prompt)
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
