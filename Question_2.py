
def return_uniquevalues(str1,str2):
        word1,word2=set(str1),set(str2)
        common_chars=word1.intersection(word2)
        uniquechars_str1=word1-common_chars
        uniquechars_str2=word2-common_chars
        uniquechars_str=''.join(uniquechars_str1)+''.join(uniquechars_str2)
        return uniquechars_str



def testa(val):
        val=int(val)
        if val in range(4,11) :
                return True
        else:
                return False

def testb(list1):
        
        if len(list1)>0:
                
                return 'NOT EMPTY'
        else:
                return 'EMPTY'

test1=[]

print(testb(test1))
print(testb(["A","B","C"]))

def testc(filename,str):
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

print(function_d([1,2,"a"]))
print(function_d())
