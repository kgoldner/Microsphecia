app not project should be git resository
right now, we should all have own project on computers, no need for git repository
do not subclass the user model, if need to create a onetoonefield on a separate model

to access path:
	echo $PATH
		ls /usr/local/bin # for commands
	#to access python path
	start a shell
	import sys
	sys.path
	dir(this) #tells you things maybe
	this.__file__ #gives path or something maybe
	
modules have definitions
package is a folder of modules -- indicated to python by __init__.py files

import cheese
	looks for cheese.py or cheese directory containing __init__.py relatively then on python path

from cheese import gruyere
	looks for gruyere.py in cheese, or looks for function, class, or 
	variable inside of cheese.py or cheese/__init__.py

if want to use from cheese import *, maybe have the __init__.py file import all modules

WHEN YOU IMPORT.  you are running that file!  so it is best if the files do not actually
do things, but rather just contain definitions
