import socket, sys

str=input("enter a word (dont use words that have more than 1 of the same letter lmaooo):")
vowels_count=0
vowels_list=['a', 'e', 'i', 'o', 'u']
const_count=0
const_list=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for i in str:
    if i in vowels_list:
        vowels_count+=1

print("The number of vowels in your word is: ")
print(vowels_count)

for i in str:
    if i in const_list:
        const_count+=1
print("the number of const in your word is: ")
print(const_count)



print("The number of total letters is:")
print(const_count + vowels_count)