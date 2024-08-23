'''Question: Print the Score - 2
Write a program that reads a distance D in km and calculates the total score.

For the first 50 km (0 - 50 km), the score for each km is 3.
For the distance above 50 km, the score for each km is 5.
The input will be a single line containing an integer representing D.

The output should be a single line containing an integer that is the score.'''

d=int(input())

if d <= 50:
    print(d*3)
else:
    v = (50*3) + ((d-50) * 5)
    print(v)