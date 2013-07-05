#Abc@1,a B1#,2w3E*,2We#3345

#Then, the output of the program should be:

#Abc@1,2w3E*

#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [*#+@]
#4. Minimum length of transaction password: 4
#5. Maximum length of transaction password: 6
#6. No space is allowed
k=1000
s=""
while k<=1200:

    if k % 7 == 0:
        if k % 5 !=0:

            s+=str(k)+","
    k+=1
print s[:-1]
h=100
y=5
print h/y
