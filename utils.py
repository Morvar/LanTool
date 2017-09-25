import os
from constants import projects_path, filename_extension
#temporary import
from random import randint

def project_entries():
	return os.listdir(projects_path)

def generate_filename():
	#temporary way of generating names
	return str(randint(1, 10))

def new_projectfile():
	while True:
		filename = generate_filename()
		try:
			file = open(projects_path + filename + filename_extension, 'x')
			break
		except FileExistsError as e:
			print(e)
	file.close()
	return file

def remove_projectfile(file_name):
	file_path = projects_path + file_name
	if os.path.isfile(file_path):
		while True:
				print("Delete " + file_path + " (no undo)? (yes/no)")
				i = input(" > ")
				if i == "yes":
					break
				if i == "no":
					return False
				else:
					print("Error: Unrecognized command")
		try:
			os.remove(file_path)
			return True
		except OSError as e:
			print(e)
	else:
		print("Couldn't find " + file_path)
	return False
