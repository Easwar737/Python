"""We distribute some number of candies, to a row of n = num_people people in the following way:
We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.
Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, 
and so on until we give 2 * n candies to the last person.
This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) 
until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).
Return an array (of length num_people and sum candies) that represents the final distribution of candies."""

# I have manually given the input. This one works perfectly for other testcases too.


candies = 7
num_people = 4
rem_candy=[]
for i in range(num_people):
    rem_candy.append(0)
i=1
j=0
while candies!=0:
    if i>candies:
        i=i-(i-candies)
    rem_candy[j]+=i
    candies-=i
    i+=1
    if j==num_people-1 and candies!=0:
        j=j-(num_people-1)
    else:
        j+=1
return rem_candy