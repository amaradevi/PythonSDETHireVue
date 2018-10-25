class Employee():
        """This is employee clas"""
        def __init__(self,firstname,lastname,pay_rate,yearly_vacation):
                """This is constructor method of employee"""
                self.firstname=firstname
                self.lastname=lastname
                self.pay_rate=pay_rate
                self.yearly_vacation=yearly_vacation
        
        def get_name(self):
                """This function returns the name of contractor"""
                return self.lastname+","+self.firstname

        def get_pay_rate(self):
                """This function returns pay_rate in hourly basis"""
                return float(self.pay_rate)

        def get_yearly_vacation(self):
                """This function returns number of days yearly vacation"""
                return int(self.yearly_vacation)


class Contractor(Employee):
        """This is contractor clas inherited from employee"""
        
        def __init__(self,firstname,lastname,pay_rate,agencyname):
                """This is constructor method of Contractor"""
                yearly_vacation=0
                super().__init__(firstname,lastname,pay_rate,yearly_vacation)
                self.agencyname=agencyname
                
        
        def get_name(self):
                """This function returns the name of contractor"""
                return super().get_name()+"[C]"

        def get_agency(self):
                """This function returns the name of  contractor agency """
                return self.agencyname

        


class Temporary(Employee):
        """This is temporary clas inherited from employee"""
        
        def __init__(self,firstname,lastname,pay_rate,agencyname):
                """This is constructor method of Temporary"""
                yearly_vacation=0
                super().__init__(firstname,lastname,pay_rate,yearly_vacation)
                self.agencyname=agencyname
                
        
        def get_name(self):
                """This function returns the name of temporary employee"""
                return super().get_name()+"[T]"

        def get_agency(self):
                """This function returns the name of temporary agency """
                return self.agencyname


e=Employee('user',"test",12,12)
print(e.get_name())
print(e.get_pay_rate())
print(e.get_yearly_vacation())

e1=Contractor('user1',"test1",24,"ABC")
print(e1.get_name())
print(e1.get_pay_rate())
print(e1.get_yearly_vacation())
print(e1.get_agency())

e2=Temporary('user2',"test2",36,"ABCD")
print(e2.get_name())
print(e2.get_pay_rate())
print(e2.get_yearly_vacation())
print(e2.get_agency())
