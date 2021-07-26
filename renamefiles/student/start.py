import random
import string
import os
from sys import argv

dir_ = argv[1]

os.mkdir("/task/student/" + dir_)

progs = "#include <stdio.h> \n #include <string.h> \n int pal(char *str){ \n int i,j, k = 1; \n if(str==NULL) \n return -1; \n for (i = 0, j = strlen (str) - 1; i <= j; ++i, --j){ \n while(str[i]==' ')i++; \n while(str[j]==' ')j--; \n if(i>j) break; \n if (str [i] != str[j]) { \n k= 0; \n break; \n } \n } \n return k; \n}" 
secret = " " 
for i in range(50):
	path = os.path.join("/task/student", dir_)
	level = int(random.choice(string.digits))
	for k in range(level):
		dir_name = ''.join(random.choice(string.ascii_letters) for k in range(5))
		path = os.path.join(path, dir_name)
		os.mkdir(path)
    
	path = os.path.join(path, str(random.choice(string.ascii_letters)) + ".c")
	file = open(path,"w")
	file.write(progs)
	file.write("\n")
	file.close()

file = open("/task/student/secret", "w")
file.write(secret)
file.close()