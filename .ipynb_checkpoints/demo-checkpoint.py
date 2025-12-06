print(40+20)
a=[1,2,3,4,6,5,3,3,2,3,4,5]
print(a)
a.reverse()
print(a)
a.append(23)
print(a)
a.pop()
print(a)
print(a.count(3))
# print(a.)

_tuple=(2,3,4,5,3)#tupples are non modifiable
print(_tuple)
print(_tuple.count(3))

_dictionary={
    "name":"samad"
    ,"age" : 34
}
print(_dictionary)
_dictionary["name"]="ayan"
print(_dictionary.items())
print(_dictionary.keys())


# sets--follows the same set proeprties like unique values 
_animals={"cat","dog","horse","lion","buffalo"}
_pets={"cat","dog"}
print(_animals.intersection(_pets))
print(_animals.difference(_pets))
print(_pets)

def MYfunc():
    a=23
    if a==23:
        print("a is 23")
    def funcinsidefunc():
        print("iam function inside function ",sep="$")
    global salary
    salary=10000
    funcinsidefunc()
print("outside the function",sep="#")
MYfunc()
print("the salary is available globally ",salary)

# for i in a:
#     print(i)

# for i in range(10,1,-1):
#     print(i)
i=0
while i<9:
    print(i)
    i=i+1

a=lambda x,y: x+y #will return x+y
print(a(49,23))
