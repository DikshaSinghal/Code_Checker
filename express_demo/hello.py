import sys
import subprocess
import os
from subprocess import Popen, PIPE


# file = sys.argv[1]
file = "../express_demo/codes/HelloWorld.cpp"
input = "../express_demo/inputs/inp.txt"
output = "../express_demo/outputs/out.txt"

filename, file_extension = os.path.splitext(file)
# print(filename)
# print(file_extension)

def executeCpp(file):

	subprocess.run("g++ " + file + " -o obj2.exe")
	myinput = open(input)
	myoutput = open(output,'w')
	p = subprocess.Popen("obj2.exe", stdin=myinput, stdout=myoutput)

def executeC(file):

	myinput = open(input)
	myoutput = open(output, 'w')
	subprocess.run("g++ " + file + " -o obj1.exe")
	p = subprocess.Popen("obj1.exe", stdin=myinput, stdout=myoutput)
	p.wait()

def executePython(file):

	myinput = open(input)
	myoutput = open(output, 'w')
	p = subprocess.run("python " + file, stdin=myinput, stdout=myoutput)


if file_extension == '.cpp':
	# print("extension cpp checked")
	executeCpp(file)

elif file_extension == '.c':
	# print("extension c checked")
	executeC(file)

elif file_extension == '.py':
	# print("extension py checked")
	executePython(file)
