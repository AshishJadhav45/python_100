# default function
def name (fname,lname):
    print("My name is ",fname,lname)
name("captain","America")

# keyword argument

def name (fname,lname):
    print("hello" ,fname, lname)
name(fname="Neo",lname="nothing")

# required argument
# its compulsory to declare a variable data you can ignore that otherwise its throw a error

# variable length argument
def name(*name):
    print("Hello",name[0],name[1],name[2])
name("james","anderson","obama")