#imports

#global vars
#gram stands for global ram / global random-access memory

gram = ""

gram2 = ""

Gram = []

Gram2 = []

#gint stands for global int / global integer

gint = 0

#gbool stands for global bool / global boolean

gbool = False

#full_val / full value is an string that is used to get the output of classes

full_val = ""

#full_value is a function that returns full val

def full_value(integer1, integer2):
    full_val = str(integer1) + "." + str(integer2)
    return full_val

#objects

#adfloat means advanced float
class adfloat:
    def __init__(self, int1, int2):
        self.int1 = int1
        self.int2 = int2
    
    #local vars
    #
    keep = False
    #
    #adds a float to a adfloat
    def add_float(float):
        local_int = 0
        local_list = []
        #inserting
        for i in float:
            Gram.insert(i, -1)
        #cutting
        for i in Gram:
            if i == '.':
                keep = True
            
            if keep == True:
                Gram2.insert(i)
            
            else:
                local_list.insert(i, -1)
        local_int = int("".join(local_list))
        local_int2 = int("".join(Gram2))

a = adfloat(1, 56)
a = adfloat(2, 56)
b = float(full_value(a.int1, a.int2))
c = 0.1
print(b+c)