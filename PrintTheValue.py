'''Question: Print the Value
Write a program that reads a string S. The string S contains a number except the last character. The last character of the string contains T or H or K.

Print the Value by multiplying the number in S with 10 or 100 or 1000 based on the last character.

Last Character	Represents	Value
T	Tens	Multiply the number in string with 10
H	Hundreds	Multiply the number in string with 100
K	Thousands	Multiply the number in string with 1000'''

s=input()
multiply = s[-1]

if multiply =="T":
    val = int(s[:-1]) * 10
    print(val)
elif multiply =="H":
    val = int(s[:-1]) * 100
    print(val)
elif multiply =="K":
    val = int(s[:-1]) * 1000
    print(val)