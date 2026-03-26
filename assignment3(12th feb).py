import random

name=input("hiiii whats your name?")
age=int(input("your age will be our secret ,so tell me it is?"))
hobby=input("and your hobbies are!!!")

kid_msgs=[
    "your name is really cute",
    "be good in school okay?",
    "craft can be fun even without gluegun"
]

teen_msgs=[
    "Learn cool stuff ",
    "You're awsome the way your are dont let others convince you otherwise",
    "yes you should totaly be patient with your parents"
]

twenty_msgs=[
    "It will pass and youll get yoru dream life",
    "CLAM DOWN!!YOU HAVE TIME I PROMISE",
    "dont quit"+hobby
]

if age<=10:
    print("hiiiiiii",name+"!",random.choice(kid_msgs))
elif age <= 20:
    print("Hey", name + "!", random.choice(teen_msgs))

elif age <= 30:
    print("Yo", name + "!", random.choice(twenty_msgs))

else:
    print("Hello", name + "! You're experienced now 😄")
    





