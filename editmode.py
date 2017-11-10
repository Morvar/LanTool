# coding: utf-8
from collections import OrderedDict
from scene import Scene
from buildmode import initialized_build_mode
import constants
import utils

def initialized_edit_mode(project):
	#projectname retrieval to be implemented
	project_name = ""
	#specify the title
	title = f"Edit Mode [{project_name}]"
	#wordlist retrieval to be implemented
	wordlist = {}
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

	def additionalWordForms():
		forms = {}
		print("Add additional forms (enter empty line when done) ")
		while True:
			print("Label: ")
			l = input(constants.input_prompt).strip()
			if not l:
				break
			else:
				print("Form: ")
				f = input(constants.input_prompt).strip()
				if not f:
					break
			forms[l] = f
			print("Added new form " + l + " : " + f)
		return forms

	def add(scene, args):
		#if no arguments were given, don't execute
		if not args:
			utils.print_missing_arg("dictionary form")
			return
		#if there were more than one additional argument, don't execute
		if len(args) > 1:
			utils.print_invalid_arg(args[1])
			return
		dictionary_form = args[0].strip()
		print("Part of speech (leave empty if not applicable): ")
		part_of_speech = input(constants.input_prompt).strip()
		print("Meaning (leave empty if not applicable): ")
		meaning = input(constants.input_prompt).strip()
		forms = additionalWordForms()
		new_entry = WordlistEntry(dictionary_form, forms, part_of_speech, meaning)
		wordlist[dictionary_form] = new_entry
		print("Added " + dictionary_form + " to word list")

	def save(scene, args):
		pass

	def exit_editmode(scene, args):
		while True:
			print("Do you want to exit " + title + "? (yes/no)")
			i = input(constants.input_prompt)
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

class WordlistEntry:
	def __init__(self, dictionary_form, forms = None, part_of_speech = None, meaning = None):
		self.dictionary_form = dictionary_form
		self.forms = forms
		self.part_of_speech = part_of_speech
		self.meaning = meaning
