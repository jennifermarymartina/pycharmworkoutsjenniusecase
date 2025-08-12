from Lab36_inheritance import scicalculator


class customer():
    def __init__(self,custid,fname,lname,age,prof):
        self.custid=custid
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof

    def display_custinfo(self):
        print("Customer Id:",self.custid)
        print("FirstName", self.fname)
        print("LastName",self.lname)
        print("Age",self.age)
        print("Profession",self.prof)

    #Static method- can be called using class and not object.
    def about_customer(msg):
        print(msg)

#Create Object for the class customer
c1=customer(1001,"Ramesj"
                 "h", "Kumar",33,"IT")

c1.display_custinfo()
print("===================")
c2=customer(1002,"Vimal","Raj",41,"Teacher")
c2.display_custinfo()
print("===================")
customer.about_customer("Hello")

