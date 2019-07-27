SCOPE
=====

This script creates a CMakeLists.txt from an existing wmake project.
It can then be used to load, edit and compile the application e.g. in QtCreator.

It has yet only been used for a few solvers from OpenFOAM's application 
directory and does not support all finesse of wmake by far. 

Note: was used for foam-extend, name of "libfoam.so" is hardcoded. 
Some autodetection should be added.

Contributions are welcome.

USAGE
=====

* Change into directory of solver/application (the one that contains the "Make" directory)
* source OpenFOAM's bashrc
* execute script => CMakeLists.txt is created
