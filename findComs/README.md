abstract : sometimes we have to study some talented works written by f77. while, an eccentric argument in the common block is really a pain for us to understand its usage in a .f code. This little device can help the coders to

- list which argument in the common block is used in a .f file
- and count when the argument is changed

### file system

.
├── coms
├── f77ComAna.py
├── README.md
└── sourceCode

coms : put all the common block here

sourceCode : put all the .f file here

f77ComAna.py : 

- find all the arguments listed in the common block
- search each .f file in sourceCode for arguments found last step
- print the result in a .csv file

### bugs and suggestion

[ ] the .f file should contain the common block with *include syntax*

[ ] no count when the argument is changed in a procedure

[ ] pandas instead of .cvs is recommended for more analyses

