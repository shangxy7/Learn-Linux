abstract : sometimes we have to study some talented works wrote by f77. while, an eccentric argument in the common block is really an pain for us to understand its usage in the code. This little tool can help the coders to

- list which arguments in the common block is used in a .f file
- and count when the value changed

### file system

.
├── coms
├── f77ComAna.py
├── README.md
└── sourceCode

coms : put all the common block here

sourceCode : put all the .f file here

f77ComAna.py : 

- find all the arguments list in the common block
- search each .f file in sourceCode for arguments found last step
- print the result in a .csv file

### bugs and suggestion

[ ] the .f file should contain the common block with include syntax

[ ] pandas instead of .cvs is recommended for more analyses

[ ] no count when the argument is changed in a procedure.