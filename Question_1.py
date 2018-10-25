def format_zipcode(zip_code): 
	if len(zip_code) <= 5: 
		return '{:>05}'.format(zip_code) 
	if len(zip_code) == 10: 
		return str(zip_code)
	if len(zip_code)== 9: 
		return '{}-{}'.format(zip_code[:5], zip_code[5:])

##1.	If the number of characters in input(zip_code) is less than or equal to 5  , zipcode should be prefix with  0 
## 
##Examples:  print(format_zipcode(“12345”)) - returns 12345
##       print(format_zipcode(“1234”)) - returns “01234”
##       print(format_zipcode(“1”)) - returns “00001”
##       print(format_zipcode(“0”)) - returns “00000”
##      print(format_zipcode(“a”)) - returns “0000a”
##
##2.	If the number of characters in input(zip_code) is greater than 6 and less than 9  , that function should return None 
##Examples: print(format_zipcode("123456"))-   returns  “None”
##  print(format_zipcode("12345a7"))-   returns  “None”
##print(format_zipcode("123456a8"))-   returns  “None”
##3.	If the number of characters in input(zip_code) is  equal to 9 , that function should return “first5chracters - next4characters”
##Examples: print(format_zipcode("123456789"))-   returns  “12345-6789”
##                          print(format_zipcode("012345a78"))-   returns  “01234-5a78”
##           print(format_zipcode("12345678a"))-   returns  “12345-678a”
##          print(format_zipcode("12345-678"))-   returns  “12345—678”
##
##
##4.	If the number of characters in input(zip_code) is  equal to 10, that function should return same str
##Examples: print(format_zipcode("0123456789"))-   returns  “0123456789”
##		     print(format_zipcode("abcdefghij"))  - returns “abcdefghij” 
##
##5.If the number of characters in input(zip_code) is  greater than 10, that function should return “None”
##Examples :
##print(format_zipcode("0123456789123")) – returns “None”
##print(format_zipcode("abcdefghijxcdvaaaaaaaaac12345677889900000sfegfdfdv"))  - return “None”
##
##Other scenarios:
##We also needs to perform the function parameters check
##Ex1: 
##print(format_zipcode())   -  Should throw “TypeError”
##TypeError: format_zipcode() missing 1 required positional argument: 'zip_code'
##
##Ex2:
##print(format_zipcode("1234567891","scqcq”))- Should throw “TypeError”
##TypeError: format_zipcode() takes 1 positional argument but 2 were given
