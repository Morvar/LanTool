# coding: utf-8
from collections import OrderedDict
from scene import Scene
from buildmode import initialized_build_mode
import constants
import utils

def initialized_edit_mode(path):
	project = utils.load_project(path)
	#print(str(project))
	project_name = project["name"]

	wordlist = project["wordlist"]
	#specify the title of the scene
	title = f"Edit Mode [{project_name}]"
        unsaved = False
	if constants.debug:
		print("unsaved: " + str(unsaved))
	#specify the functions
	def enter_buildmode(scene, args):
		build_mode = initialized_build_mode()
		build_mode.enter()
		# is drawing scene a sane thing to do here?
		scene.draw()
		return

	def browse(scene, args):
		pass

	def show(scene, args):
		#if no arguments were given, don't execute
		if not args:
			utils.print_missing_arg("word")
			return
		#if there were more than one additional argument, don't execute
		if len(args) > 1:
			utils.print_invalid_arg(args[1])
			return
		word = args[0]
		try:
			print(wordlist[0])
		except KeyError:
			print("No match was found for " + word)
			print("to be implemented properly. rn only shows first word entry")

	def edit(scene, args):
		pass

	def additionalForms():
		forms = {}
		print("Add additional forms. These will override any general rules (enter empty line when done) ")
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
			print("Added new form: " + l + " : " + f)
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
		part_of_speech = input(constants.input_prompt).strip().lower()
		print("Meaning (leave empty if not applicable): ")
		meaning = input(constants.input_prompt).strip()
		print("Conjugation class (leave empty if not applicable): ")
		conjugation_class = input(constants.input_prompt).strip()
		print("Stem (leave empty if not applicable): ")
		stem = input(constants.input_prompt).strip()
		forms = additionalForms()
		conjugation = {}
		conjugation["conjugation_class"] = conjugation_class
		conjugation["stem"] = stem
		conjugation.update(forms)
		new_entry = wordlist_entry(dictionary_form, conjugation, part_of_speech, meaning)
		wordlist.append(new_entry)
		print("Added " + dictionary_form + " to word list")
		print("Part of speech:", part_of_speech)
		print("Meaning:", meaning)
		print("Conjugation class:", conjugation_class)
		print("Forms:",str(forms))
		unsaved = True
		if constants.debug:
			print("unsaved: " + str(unsaved))

	def save(scene, args):
		if constants.debug:
			print("unsaved: " + str(unsaved))
		#if there were more than one additional argument, don't execute
		if len(args):
			utils.print_invalid_arg(args[0])
			return
		utils.save_project(project, path)
		unsaved = False
		if constants.debug:
			print("unsaved: " + str(unsaved))

	def exit_editmode(scene, args):
		if constants.debug:
			print("unsaved: " + str(unsaved))
		if unsaved:
			while True:
				print("Do you want to save before exiting " + title + "? (yes/no)")
				i = input(constants.input_prompt)
				if i == "yes":
					utils.save_project(project, path)
					return False
				if i == "no":
					break
				else:
					print("Error: Unrecognized command")
		return False

	#specify the commands and which functions they will use
	commands = OrderedDict()
	commands["buildmode"] = ("Enter Build Mode", enter_buildmode)
	commands["browse"] = ("Browse", browse)
	commands["show"] = ("Show word", show)
	commands["edit"] = ("Edit word", edit)
	commands["add"] = ("Add word", add)
	commands["save"] = ("Save changes", save)
	commands["exit"] = ("Exit", exit_editmode)

	#create an edit mode from the Scene class
	edit_mode = Scene(title, commands)
	return edit_mode

#class WordlistEntry:
def wordlist_entry(dictionary_form, conjugation, part_of_speech = None, meaning = None):
	r = {}
	r["dictionary_form"] = dictionary_form
	r["conjugation"] = conjugation
	r["part_of_speech"] = part_of_speech
	r["meaning"] = meaning
	return r
