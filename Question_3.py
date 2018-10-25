
def function_a(val):
        val=int(val)
        if val in range(4,11) :
                return True
        else:
                return False

def function_b(list1):
        
        if len(list1)>0:
                
                return 'NOT EMPTY'
        else:
                return 'EMPTY'



def function_c(filename,str):
        try:
                
               with open(filename,'a') as r:
                       r.write(str+"\n")
        except IOError :
                print("file is not writable or filepath is not valid")


                

testc("D:\\Cloud\\python\\Python_examples\\test_file.txt","testingexp1")


def function_d(*args):
        if len(args)==1:        
                list1=[x*2 for x in args[0] ]
                return list1
        if len(args)==0:        
                list1=[]
                return list1

