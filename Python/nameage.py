import time

start_time = time.time()

print('What is your name?')

myName = input()
##While loop example
while myName != "Brandon":
    if myName == 'your name':
        print('Not funny dad. Whats your real name?')
        myName=input()
    else:
        print("your are not authorized to run this.")

    print("This is not your name please type your name.")
    myName = input()

print('Hello, ' + myName + '. That is a good name. How old are you?')
myAge = int(input())

#Sample if statements
if myAge < 13:
    print('Learning young, Thats good')
elif myAge == 13:
    print("Your a teenager mow... Thats cool, i guessss")
elif myAge > 13 and myAge < 30:
    print("Still young, still learning....")
elif myAge >= 30 and myAge < 65:
    print("Now your adulting...")
else:
    print (".... youve lived a long time bro?")


time.sleep(1)
programAge = int(time.time() - start_time)
print("%s? Thats's funny, I'm only %s seconds old" % (myAge, programAge))
print("I wish I was %s years old" % (myAge * 2))

time.sleep(3) 
print("I'm tired. I sleep now")