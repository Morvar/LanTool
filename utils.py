import os
from constants import projects_path, filename_extension
from pathlib import Path
#temporary import
from random import randint

#def project_entries():
#	return os.listdir(projects_path)

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
			filepath = (projects_path / name).with_suffix(filename_extension)
			#when name has been successfully generated, break loop
			if not filepath.exists(): break
	#if there was no problem, use the provided name
	else:
		filepath = (projects_path / name).with_suffix(filename_extension)
	try:
		filepath.touch(exist_ok=False)
	except FileExistsError:
		print(f"Error: Project '{name}' already exists")
		return None
	return filepath

def remove_projectfile(file_name):
	filepath = (projects_path / file_name).with_suffix(filename_extension)
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

#def remove_projectfile(file_name):
#	filepath = (projects_path / file_name).with_suffix(filename_extension)
#	if os.path.isfile(file_path):
#		while True:
#				print("Delete " + file_path + " (no undo)? (yes/no)")
#				i = input(" > ")
#				if i == "yes":
#					break
#				if i == "no":
#					return False
#				else:
#					print_unrecognized_command(i)
#		try:
#			os.remove(file_path)
#			return True
#		except OSError as e:
#			print(e)
#	else:
#		print("Couldn't find " + file_path)
#	return False

def print_unrecognized_command(cmd):
	print("Error: Unrecognized command: " + cmd)

def print_invalid_arg(arg):
	print("Error: Invalid argument: " + arg)

def print_missing_arg(missing_arg):
	print("Error: Missing argument: '" + missing_arg + "'")

#def include_filename_extension(file_name):
#	if not file_name.endswith(filename_extension):
#		file_name = f"{file_name}{filename_extension}"
#	return file_name
#
#def exclude_filename_extension(file_name):
#	if file_name.endswith(filename_extension):
#		file_name = f"{file_name}{filename_extension}"
#		print("exclude_filename_extension in utils still not properly implemented")
#	return file_name
