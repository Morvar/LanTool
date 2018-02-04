# coding: utf-8
from collections import OrderedDict
from scene import Scene, command
from buildmode import BuildMode
import constants
import utils

class EditMode(Scene):
	def __init__(self, project_path):
		#construct a scene
		title = "Edit Mode"
		super().__init__(title)
		self.project_path = project_path
		self.project = utils.load_project(project_path)
		self.project_name = self.project["name"]
		self.wordlist = self.project["wordlist"]
		#put the project title in the title of the scene
		self.title = f"{title} [{self.project_name}]"
		self.unsaved = False

	if constants.debug:
		print("unsaved: " + str(self.unsaved))

	#specify the functions
	@command("buildmode", "Enter Build Mode")
	def enter_buildmode(self, args):
		buildmode = BuildMode()
		buildmode.enter()
		# is drawing scene a sane thing to do here?
		self.draw()
		return

	@command("show", "Show entry")
	def show(self, args):
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
			#to be implemented
			if self.wordlist:
				print(self.wordlist[0])
		except KeyError:
			print("No match was found for " + word)
			print("to be implemented properly. rn only shows first word entry")

	@command("edit", "Edit entry")
	def edit(self, args):
		pass

	@command("add", "Add entry")
	def add(self, args):
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

		forms = additionalForms()
		conjugation = {}
		conjugation["conjugation_class"] = conjugation_class
		conjugation["stem"] = stem
		conjugation.update(forms)
		new_entry = wordlist_entry(dictionary_form, conjugation, part_of_speech, meaning)
		self.wordlist.append(new_entry)
		print("Added " + dictionary_form + " to word list")
		print("Part of speech:", part_of_speech)
		print("Meaning:", meaning)
		print("Conjugation class:", conjugation_class)
		print("Forms:",str(forms))
		self.unsaved = True
		if constants.debug:
			print("unsaved: " + str(self.unsaved))

	@command("save", "Save project")
	def save(self, args):
		if constants.debug:
			print(f"unsaved: {str(self.unsaved)}")
		#if there were additional arguments, don't execute
		if len(args):
			utils.print_invalid_arg(args[0])
			return
		utils.save_project(self.project, self.project_path)
		self.unsaved = False
		if constants.debug:
			print(f"unsaved: {str(self.unsaved)}")

	@command("exit", "Exit")
	def exit_editmode(self, args):
		if constants.debug:
			print(f"unsaved: {str(self.unsaved)}")
		if self.unsaved:
			while True:
				print("Do you want to save before exiting " + self.title + "? (yes/no)")
				i = input(constants.input_prompt)
				if i == "yes":
					utils.save_project(self.project, self.project_path)
					return False
				if i == "no":
					break
				else:
					print("Error: Unrecognized command")
		return False

#class WordlistEntry:
def wordlist_entry(dictionary_form, conjugation, part_of_speech = None, meaning = None):
	r = {}
	r["dictionary_form"] = dictionary_form
	r["conjugation"] = conjugation
	r["part_of_speech"] = part_of_speech
	r["meaning"] = meaning
	return r
