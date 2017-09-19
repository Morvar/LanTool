import os
from constants import projects_path, filename_extension
#temporary import
from random import randint

def list_project_entries():
	entries = os.listdir(projects_path)
	for file in entries:
		print("▪ " + file)

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
 
