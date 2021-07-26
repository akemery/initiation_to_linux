import random
import string
import os
from sys import argv

dir_ = argv[1]
number = int(argv[2])
secret_pos = int(argv[3])%50


os.mkdir("/task/student/" + dir_)

secret = " " 
for i in range(50):
	path = os.path.join("/task/student", dir_)
	level = int(random.choice(string.digits))
	for k in range(level):
		dir_name = ''.join(random.choice(string.ascii_letters) for k in range(5))
		path = os.path.join(path, dir_name)
		os.mkdir(path)
    
	path = os.path.join(path, str(random.choice(string.ascii_letters)) + ".txt")
	file = open(path,"w")
	random_lines = ''.join(random.choice(string.digits) for l in range(3))
	file_lines = int(random_lines)
	for l in range(file_lines):
		line = ''.join(random.choice(string.ascii_letters) for k in range(10))
		file.write(line)
		file.write("\n")
	if i == secret_pos :
		secret = path
		file.write(str(number))
	file.close()

file = open("/task/student/secret", "w")
file.write(secret)
file.close()