'''Question: Print the Score - 4
Write a program that reads a distance D in km and calculates the total score.

For the first 40 km (0 - 40 km), the score for each km is 2.
For the next 20 km (41 - 60 km), the score for each km is 4.
For the next 60 km (61 - 120 km), the score for each km is 6.
For the distance above 120 km, the score for each km is 8.
Apart from the above scores, there is a bonus score of 50.
The input will be a single line containing an integer representing D. The output should be a single line containing an integer that is the score.'''


d=int(input())
bonus = 50


if d<=40:
    score = d * 2
    print(score + bonus)
elif d>40 and d<=60:
    score = (40*2) + (20*4) + ((d-60) * 4)
    print(score + bonus)
elif d>60 and d<=120:
    score =(40*2) +(20*4) + ((d-60) * 6)
    print(score + bonus)
else:
    score = (40*2) +(20*4) + (60*6) + ((d-120) * 8)
    print(score+bonus)