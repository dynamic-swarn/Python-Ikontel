#--------------- 1.Write a python code to show the reverse of a number which is taken through user input. ---------------
num = int(input("Enter a number: "))
rev = 0
while num>0:
	digit = num % 10
	rev = rev * 10 + digit
	num = num // 10
print("Reverse Number is: ",rev)




#--------------- 2. Write a python code to check a number is palindrome or not. ---------------
num = int(input("Enter a number: "))
temp = num
rev = 0

while num > 0:
	digit = num % 10
	rev = rev * 10 + digit
	num = num // 10

if rev == temp:print("Palindrome")
else : print("Not Palindrome")





#--------------- 3. Write a python code to find all the odd and even digit in a user taken number. ---------------

num = int(input("Enter a number: "))

if num % 2 == 0:
	print(num ,"Is Even")
else:
	print(num ,"Is Odd")


#--------------- 4. Write a python code to Reverse the string. ---------------
string = input("Enter a string: ")
print(string[::-1])


#--------------- 5. Write a python code to find the Perfect number. ---------------

num = int(input("Enter a number: "))
i = 1
sum = 0
for i in range(1,num-1):
	if num % i== 0:
		sum = sum + i
		
if num == sum: print("Perfect Number")

else: print("Not Perfect Number")



# --------- 6. Find the length of a string without using len().---------------

string = input("Enter a string: ")
count = 0
for i in string:
    count+=1
print(count) 



#--------------- 7. Find the frequency of each element. ---------------

word = input("Enter the sentence or word: ")
for ch in word:
    count = 0
    for i in word:
        if ch == i:
            count+=1
    print(ch,"=",count)



#--------------- 8. Move all zeros to the end. ---------------
num = [1,0,3,5,0,0,4,0,9,0,8]
lst = []
for i in num:
    if i!=0:
        lst.append(i)
        
for i in num:
    if i == 0:
        lst.append(i)

print(lst)
    


#--------------- 9. Count vowels and consonants. ---------------
word = input("Enter a word: ")
vowel = 0
consonant = 0
for i in word:
    if i in 'aeiouAEIOU':
        vowel+=1
    else: consonant+=1
    
print("vowel",vowel)
print("consonant",consonant)


#--------------- 10. Create a function to find factorial. ---------------
def fact(num):
    f = 1
    for i in range(1,num+1):
        f = f * i
    return f

num = int(input("Enter a number: "))
print("Factorial is: ",fact(num))
