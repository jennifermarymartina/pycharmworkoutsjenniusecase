'''Inheritaince is the process of inheriting from one class(parent)
Child class can access all the members and methods of parent class
'''
import math
class calculator:
    def addnum(self,a,b):
        print(f"Sum of {a} amnd {b} is {a+b}")

    def subnum(self,a,b):
        print(f"Subtraction of {a} amn {b} is {a-b}")

    def prodnum(self,a,b):
        print(f"Product of {a} amn {b} is {a*b}")
#Child class scicalculator inherits from parent class by giving calculator class as parameter
class scicalculator(calculator):
    def square(self,a):
        print(f"Square of {a} is {a**2}")

    def cube(self,a):
        print(f"Cube of {a} is {a**3}")

class advcalculator(scicalculator):
    def dollartorupee(self,a):
        print(f"Dollar t of {a} is {a*88}")

    def eurotorupee(self,a):
        print(f"Euro t of {a} is {a*63}")

scalc=scicalculator()
scalc.square(3)
scalc.cube(3)
scalc.prodnum(3,3)
scalc.subnum(3,3)

advcalc=advcalculator()
advcalc.eurotorupee(3)
advcalc.dollartorupee(3)
advcalc.subnum(3,3)
advcalc.prodnum(3,3)
