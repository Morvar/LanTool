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
 
