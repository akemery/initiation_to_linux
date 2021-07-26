import random
import string
import os
from sys import argv

dir_ = argv[1]
number = int(argv[2])
random_choice = int(argv[3])%50


os.mkdir("/task/student/" + dir_)

secret = " " 
i=0
while i<50:
	path = os.path.join("/task/student", dir_)
	level = int(random.choice(string.digits))
	for k in range(level):
		dir_name = ''.join(random.choice(string.ascii_letters) for i in range(5))
		path = os.path.join(path, dir_name)
		os.mkdir(path)
    
	path = os.path.join(path, str(random.choice(string.ascii_letters)) + ".txt")
	file = open(path,"w")
	if i == random_choice :
		secret = path
		file.write(str(number))
	else:
		file.write(str(number*2*i))
	file.close()
	i=i+1

file = open("/task/student/secret", "w")
file.write(secret)
file.close()