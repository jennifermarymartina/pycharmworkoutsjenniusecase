strData= "This is a test data"
print(strData)
print(strData.split(" "))
print("Starts with : ",strData.startswith("r"))
print("Ends with : ",strData.endswith("a"))
print("Count s :", strData.count("s"))
print(round(125.56))
print(round(125.568343,2))

s1="Bryan"
s2="Britney"
print(s1+s2)
print(s1,s2,"are", "smart kids")
print(s1,s2,"live in", end=" ")
print("Ivory Towers")
print('Ivory Towers')
print("'Ivory' Towers")
print('"Ivory" Towers')
print("\"Ivory\" Towers")

empdata="101, Jenny, Lead, Plano"
print(empdata)
empinfo=empdata.split(",")
print(empinfo)
print("Employee ID",empinfo[0])
print("Employee Name",empinfo[1])
print("Employee Role",empinfo[2])
print("Employee City",empinfo[3])

s3="  ".join(empinfo)
print("After joining the items in the list",s3)
s5="String Slicing"
print("String Slicing")

print("First 5 letters",s5[:5])
print("5 letters from second position",s5[1:6])

name="Jennifer"
print("Index 0", name[0])
print("Index -8", name[-8])
print("Index 1", name[1])
print("Index -7", name[-7])
print("Index 2", name[2])
print("Index -6", name[-6])
#Positive and negative index
'''
0 1  2  3  4  5  6  7 Positive indexing
J  e  n  n  i  f  e  r
-8-7 -6 -5 -4 -3 -2 -1 Negative indexing
'''
#To print entire string
print("Whole string in different ways")
print(name[:])
print(name[::])
print(name[::1])
print("First 4 letters",name[:4])
print("First 4 letters using negative indexing",name[-8:-4])
print("Last 4 letters",name[4:])

#Step value

print(name[0:6:2]) #Output Jni

#To Reverse string
print(name[::-1]) #Output refinnerJ

str1="Messi is the best soccer player"
str2=str1.find("soccer")
print(str2)
str3=str1.find("cricket")#returns -1 on failure
print(str3)
str4=str1.index("soccer") #raises error when substring is not found
print(str4)

print("soccer" in str1) # in keyword returns boolean

l1="Java"
l2="Scala"
l3="Python"
l4="R"

print("Spark supports languages like Java , Scala , Python and R")
print("Spark supports languages like" , l1 , ",", l2 , ",", l3, "and", l4) #commas to add string - only for print
r="Spark supports languages like " + l1 + " , "+ l2 + " , "+ l3 + " and "+ l4
print(r)
r1="Spark supports languages like {} , {} , {} and {}".format(l1,l2,l3,l4)
print(r1)
r2="Spark supports languages like {0} , {1} , {2} and {3}".format(l1,l2,l3,l4)
print(r2)
r3=f"Spark supports languages like {l1} , {l2} , {l3} and {l4}"
print(r3)

a=10
b=20
c=a+b
print(f"Sum of {a} and {b} is {c}")

#Multiline strings

s1="""Python language is easy to learn"
It supports multiple programming paradigm. 
Its an interpreted language."""

print(s1)

#String is immutable - does not change - object is created again and new memory is allocated

s1="Inceptez"
print(id(s1))
s1="Technologies"
print(id(s1))

#s1[0]="Z" #String assignment will throw error as string is immutable