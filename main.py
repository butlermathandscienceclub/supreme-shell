import os
import random
from time import gmtime, strftime

##
cmdstr = ">"
var_e = ""
var_s = ""
nofile = "file/dir not found"
homedir = "/"
intro = "welcome to SupremeShell! "
##

var_t = (" strftime(\"%Y-%m-%d %H:%M:%S\", gmtime()) ")
print(intro)
def exe(cmd):
	print(os.popen(cmd).read())
while True:
	cur_cmd= cmdstr.replace("{path}", os.getcwd()).replace("{un}", os.environ.get("USER")).replace("{t}", eval(var_t) or "").replace("{s}", var_s).replace("{e}", eval(var_e))
	i = input(cur_cmd+" ")
	if i == "exit":
		print("exiting comand shell... ",end="")
		print("done")
		break
	elif i == "cd":
		in_ = input("where to? ")
		try:
			
			os.chdir(in_)
		except:
			print(f"error! {in_} : {nofile} ")
	elif i == "home"		:
		os.chdir(homedir)
	elif i == "help":
		print("kellanshell!")
	else:	
		exe(i)
