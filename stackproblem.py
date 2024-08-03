# Given an expression string
# Write a python program to find whether a given string has balanced parentheses or not. 

# One approach to check balanced parentheses is to use stack. 
# Each time, when an open parentheses is encountered push it in the stack, 
# and when closed parenthesis is encountered, match it with the top of stack and pop it. 
# If stack is empty at the end, return Balanced otherwise, Unbalanced. 

string=(input("Input your string!:"))

class Stack: 
   def __init__(self):
        self.open_list = ["(","[","{"]
        self.close_list = [")","]","}"]
        self.list1=[]
        self.list2=[]
    
   def push(self):
    for i in range(len(string)):
        a=string[i]
        if a in self.open_list:
            self.list1.append(a)
        elif a in self.close_list:
            self.list2.append(a)
    
   def check(self):
       self.value1=len(self.list1)
       self.value2=len(self.list2)
       if self.value1==self.value2:
           return True 
       else:
           return False

Str=Stack() 

Str.push()

val=Str.check() 
if val:
    print("Your parentheses are all closed!")
else: 
    print("You're missing some parentheses! Not closed!")









