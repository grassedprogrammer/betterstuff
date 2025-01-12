
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
    lint, lint2 = strfloat_strs(strfloat)
    lint3 = int(lint)
    lint4 = int(lint2)
    return lint3, lint4

##adds two strfloats

def add_strfloats(strfloat1, strfloat2):
    #decoding
    temp_list = []
    ram = 0
    lint, lint2 = strfloat_ints(strfloat1)
    lint3, lint4 = strfloat_ints(strfloat2)
    
    #adding
    
    len_lint = len(lint2)
    len_lint2 = len(lint4)
    temp =  lint2 + lint4
    len_temp = len(str(temp))
    if len_temp > len_lint and len_temp > len_lint2:
        for i in str(temp): temp_list.insert(i, -1)
        ram = list_int(temp_list[0])
        lint+=ram
        temp_list.pop(0)
        ram = None
        for i in temp_list:
            temp = str(temp) + i
    lint+=lint3
    return ints_strfloat(lint, temp)

    #returns str
    pass

#objects

#test
if __name__ == '__main__':
    print(add_strfloats("1.9", "1.9")) 