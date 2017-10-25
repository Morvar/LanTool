import os
from constants import projects_path, filename_extension
from pathlib import Path
#temporary import
from random import randint

def project_entries():
	file_list = []
	for entry in projects_path.iterdir():
		if entry.is_file():
			file_list.append(entry)
		elif entry.is_dir():
			print("utils project_entries: listing files in subdirectories not implemented")
			pass
	return file_list

def entries_in_dir(path):
	path.iterdir()

def get_project_path(name):
	return (projects_path / name).with_suffix(filename_extension)

def is_project(name):
	path = get_project_path(name)
	return path.exists()

def get_project(name):
	path = get_project_path(name)
	#make a json object
	print("utils get_project not implemented")

def generate_filename():
	#temporary way of generating names
	return str(randint(1, 10))

def contains_invalid_filename_character(name):
	#return not len(Path(name).parts) == 1
	return not len(Path(name).parts) <= 1

def new_projectfile(name):
	if contains_invalid_filename_character(name):
		print(f"Error: Invalid project name: '{name}'")
		return 
	#if no name was provided, generate one
	if not name:
		while True:
			name = generate_filename()
			filepath = get_project_path(name)
			#when name has been successfully generated, break loop
			if not filepath.exists(): break
	#if there was no problem, use the provided name
	else:
		filepath = get_project_path(name)
	try:
		filepath.touch(exist_ok=False)
	except FileExistsError:
		print(f"Error: Project '{filepath.stem}' already exists")
		return None
	return filepath

def remove_projectfile(file_name):
	filepath = get_project_path(name)
	if filepath.is_file():
		while True:
				print("Delete " + filepath.stem + " (no undo)? (yes/no)")
				i = input(" > ")
				if i == "yes":
					break
				if i == "no":
					return False
				else:
					print_unrecognized_command(i)
		try:
			filepath.unlink()
			return True
		except OSError as e:
			print(e)
	else:
		print(f"Couldn't find {filepath}")
	return False

def print_unrecognized_command(cmd):
	print("Error: Unrecognized command: " + cmd)

def print_invalid_arg(arg):
	print("Error: Invalid argument: " + arg)

def print_missing_arg(missing_arg):
	print("Error: Missing argument: '" + missing_arg + "'")
