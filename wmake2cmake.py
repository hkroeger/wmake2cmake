#!/usr/bin/env python

import os,sys,shutil

options=open('Make/options', 'r').readlines()
files=open('Make/files', 'r').readlines()

srcfiles=[]
targname=""
defines=[
 "-Dlinux64", "-DWM_DP", "-fpermissive", "-DNoRepository"
]
incs=[
  "include_directories("+os.getenv("FOAM_SRC")+"/foam/lnInclude)", 
  "include_directories("+os.getenv("FOAM_SRC")+"/OSspecific/POSIX/lnInclude)"]
libs=[
  os.getenv("FOAM_LIBBIN")+"/libfoam.so"
]

for l in options:
	opt=l.strip(" \\\n")
	if opt.startswith('-I'):
		arg=opt[2:]
		if (arg.startswith('$(LIB_SRC)')):
			incs.append("include_directories("+os.getenv("FOAM_SRC")+"/"+arg.strip('$(LIB_SRC)')+")")
		else:
			incs.append("include_directories("+os.path.abspath(arg)+")")
	elif opt.startswith('-l'):
		libs.append(os.getenv("FOAM_LIBBIN")+"/lib"+opt[2:]+".so")
		
for l in files:
	ls=l.strip(' \n')
	if l.startswith('EXE'):
		lsp=ls.split('/')
		targname=lsp[-1]
	elif not ls=="":
		srcfiles.append(l)
		
if (os.path.exists("CMakeLists.txt")):
	shutil.copyfile("CMakeLists.txt", "CMakeLists.txt.bak")
		
cm=open("CMakeLists.txt", 'w')

cm.write("cmake_minimum_required(VERSION 3.10)\n\n")
cm.write("project("+targname+")\n\n")
cm.write("add_definitions(\n"+"\n".join(defines)+"\n)\n\n")
cm.write('\n'.join(incs)+"\n\n")
cm.write("add_executable("+targname+'\n'+'\n'.join(srcfiles)+"\n)\n\n")
cm.write("target_link_libraries("+targname+"\n"+'\n'.join(libs)+"\n)\n\n")
