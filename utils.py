# coding: utf-8
import os
import constants
from pathlib import Path
import json
import time
#from random import randint

def project_entries():
	file_list = []
	for entry in constants.projects_path.iterdir():
		if entry.is_file() and entry.suffix == constants.filename_extension:
			file_list.append(entry)
		elif entry.is_dir():
			print("utils project_entries: listing files in subdirectories not implemented")
			pass
	return file_list

def get_project_path(name):
	path = (constants.projects_path / name).with_suffix(constants.filename_extension)
	return path

def is_project(name):
	path = get_project_path(name)
	return path.exists()

def generate_filename():
	#return str(randint(1, 10))
	date = "%04i%02i%02i"%time.localtime()[:3]
	if not is_project(date):
		return date
	num = 1
	while True:
		print("iteration" + str(num))
		if not is_project(date + "-" + str(num)):
			return date + "-" + str(num)
		num +=1

def save_project(project, path):
	with path.open("wt") as fd:
		json.dump(project, fd)
	print("Project saved")

def load_project(path):
	with path.open("rt") as fd:
		try:
			r = json.load(fd)
			return r
		except json.JSONDecodeError as e:
			return {"name": path.stem,"wordlist":[]}

def contains_invalid_filename_character(name):
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

def remove_projectfile(name):
	filepath = get_project_path(name)
	if filepath.is_file():
		while True:
			print("Delete " + filepath.stem + " (no undo)? (yes/no)")
			i = input(constants.input_prompt)
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
