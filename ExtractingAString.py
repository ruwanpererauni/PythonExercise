'''
@author: Ruwan Perera
'''
print("starting the program")
with open('userprofile.txt','r') as f:
#    for line in f:
#        print(line)
    for line in f.read().split("\n"):
        if (line=="***"):
            print ("starting the file ")
        elif (line=="User ID"):
            print (line)
        else :
            print ("0")
