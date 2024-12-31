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

##full_val / full value is an string that is used to get the output of classes

full_val = ""

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
    r = int(r)
    return r

##full_value is a function that returns full val

def full_value(integer1, integer2):
    full_val = str(integer1) + "." + str(integer2)
    return full_val

#objects

##adfloat means advanced float
class adfloat:
    def __init__(self, int1, int2):
        self.int1 = int1
        self.int2 = int2
    
    #local vars
    #
    int1 = int1
    local_list2 = []
    local_list3 = []
    ad = False
    lint = 0
    lint2 = 0
    keep = False
    #
    #adds a float to a adfloat
    def add_float(lfloat):
        inte1 = int1
        local_list = []
        float = str(lfloat)
        #inserting
        for i in float:
            Gram.insert(i, -1)
        for i in Gram:
            if i == ".":
                ad = True
                continue
            elif ad == True:
                Gram2.insert(i, -1)
            else:
                local_list.insert(i, -1)
        #adding the values in the lists to ints
        lint3 = len(local_list)
        lint4 = len(Gram2)
        lint = list_int(local_list)
        lint2 = list_int(Gram2)
        Lint = lint + int1
 
a = adfloat(1, 56)
a = adfloat(2, 56)

aaaa = [1,2,3]
b = list_int(aaaa)
print(b + 3)
