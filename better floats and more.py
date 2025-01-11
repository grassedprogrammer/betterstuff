#imports

#global vars
##gram stands for global ram / global random-access memory

gram = ""

gram2 = ""

Gram = []

Gram2 = []

##gint stands for global int / global integer

gint = 0

##gbool stands for global bool / global boolean

gbool = False

#fuctions

##list_str means list to string

def list_str(list):
    string = ""
    for i in list:
        string = string + str(i)
    return string

##list_int means list to int

def list_int(thing):
    r = list_str(thing)
    R = int(r)
    return R

##ints_strfloat converts two ints to one str float

def ints_strfloat(integer1, integer2)-> str:
    lstr = str(integer1) + "." + str(integer2)
    return lstr

##turns a strfloat into 2 strings

def strfloat_strs(strfloat):
    lstr = ""
    lstr2 = lstr
    lbool = False
    for i in strfloat:
        if i == ".":
            lbool = True
        elif lbool == False:
            lstr = lstr + i
        else:
            lstr2 = lstr2 + i
    return lstr, lstr2

##turns a strfloat into 2 integers

def strfloat_ints(strfloat):
    lint, lint2 = int(strfloat_strs(strfloat))
    return lint, lint2

##adds two strfloats

def add_strfloats(strfloat1, strfloat2):
    #decoding
    
    lint, lint2 = strfloat_ints(strfloat1)
    lint3, lint4 = strfloat_ints(strfloat2)
    
    #adding
    
    for i in 
    
    #returns str
    pass

#objects

#test

a, b = strfloat_strs("123.456")
print("   " + a + " " + b)