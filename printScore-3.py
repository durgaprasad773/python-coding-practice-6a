'''Question: Print the Score - 3
Write a program that reads a distance D in km and calculates the total score.

For the first 20 km (0 - 20 km), the score for each km is 2.
For the next 40 km (21 - 60 km), the score for each km is 4.
For the distance above 60 km, the score for each km is 6.
Apart from the above scores, there is a bonus score of 30.
The input will be a single line containing an integer representing D. The output should be a single line containing an integer that is the score.

Approach
Read the input distance D.
Calculate the score based on the distance:
If the distance is less than or equal to 20 km, multiply the distance by 2.
If the distance is between 21 and 60 km, calculate the score for the first 20 km and the remaining distance.
If the distance is above 60 km, calculate the score for the first 20 km, the next 40 km, and the remaining distance.
Add the bonus score of 30 to the calculated score.
Print the total score.'''

d=int(input())
bonus=30
if d <= 20:
    print((d*2) + bonus)
elif d>20 and d<=60:
    val = (20*2) + ((d-20)*4) 
    print(val + bonus)
else:
    val = (20*2) + (40*4) +((d-60) *6)
    print(val + bonus)