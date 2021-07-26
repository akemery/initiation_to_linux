#!/bin/python3
import sys
import os

dirnames = ["home", "usr", "dev" , "var", "proc", "etc", "www", "inet", "lib", "local"]

filenames = ["come.doc", "agoue.avi", "lokossa.doc"]

for i in range(100):
    if i < 10:
        path = os.path.join("/task/student", dirnames[i%10] )
        os.mkdir(path)
        path = os.path.join(path, filenames[i%3])
    else:
        path = os.path.join("/task/student", dirnames[i%10] )
        path = os.path.join(path, dirnames[i%7])
        try:
            os.mkdir(path)
            path = os.path.join(path, filenames[i%3])   
        except:
             continue
    file=open(path, "w")
    file.close()