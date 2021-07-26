import random
import string
import os
from sys import argv

dir_ = argv[1]
number = int(argv[2])
random_choice = int(argv[3])%50


os.mkdir("/task/student/" + dir_)

secret =" " 
i=0
while i<50:
	file_name = "student/" + dir_ + "/" + str(random.choice(string.ascii_letters)) + ".txt"
	file = open(file_name,"w")
	if i == random_choice :
		secret = file_name
		file.write(str(number))
	else:
		file.write(str(number*2*i))
	file.close()
	i=i+1

file = open("/task/student/secret", "w")
file.write(secret)
file.close()