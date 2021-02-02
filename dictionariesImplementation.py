d ={101:"Ashwini",  103:"Jayashree" , 104:"Rajkumar" ,102:"Abhijit" , 105:"Patil"}          #created dict
print(d)
print(list(d))                         #print list of keys
print(sorted(d))                       #print keys in sorted order
print(d[101])                           #accessing element using key
print(d[104])

Dict1 = {}                              # empty dict
print("empty dictionary")
print(Dict1)
Dict1[0] = "bksub"                      #updated  the value


Dict2 = dict({101:"Ashwini",  103:"Jayashree" , 104:"Rajkumar"})      #created dict using dict method
print(Dict2)

Dict3 = {1: 'Rajkumar', 2: 'Jayshree',
        3:{'A' : 'Ashwini', 'B' : 'Abhijit', 'C' : 'Mithoo'}}             #nested dictionaries
print(Dict3)

Dict3[4] = "ksihrhi"                                    #updated an element
print(Dict3)

print(Dict3.get(3))                                     # Accessig element using get method
#del Dict3[4]                                           # deleting

#print(Dict3)
#print(Dict3.pop(4))                                    #popping
#print(Dict3)

print(Dict3.popitem())                                  #popping key and value both
print(Dict3)