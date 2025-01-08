#Family name: Samandar
#Student number: 300446112
# Course: ITI 1120
# Assignment Number 2 Part 2
# year 2024

########################
# Question 2.1
########################

def min_enclosing_rectangle (radius,x,y):
#here I have defined the function min_enclosing_rectangle
    if radius < 0:
#as you can see I have made an if condition for none in case if x is negative number
        return None
    return (x-radius,y-radius)
#here according to mathmatiques if we substract radius form x and y we will get the left bottom point of rectangular 
#I used this concept to find the (x,y) axis of bottom left corner of rectangular
print(">>>min_enclosing_rectangle(1,1,1)")
print(min_enclosing_rectangle (1,1,1))
print(">>>min_enclosing_rectangle(4.5, 10, 2)")
print(min_enclosing_rectangle (4.5,10,2))
print(">>>min_enclosing_rectangle(-1, 10, 2)")
print(min_enclosing_rectangle (-1,10,2))
print(">>>min_enclosing_rectangle(500, 1000, 2000)")
print(min_enclosing_rectangle (500, 1000, 2000))

print()

########################
# Question 2.2
########################

def vote_percentage(results):
    count_for_yes = 0
    count_for_no = 0

    for word in results.split():
        count_for_yes += word == "yes"
        count_for_no += word == "no"

    total_count = count_for_yes + count_for_no

    if total_count > 0:
        percentage = ((count_for_yes / total_count)*100)/100
    else:
        percentage = 0

    return percentage

print(">>>vote_percentage('yes yes yes yes yes abstained abstained yes yes yes yes')")
print (vote_percentage("yes yes yes yes yes abstained abstained yes yes yes yes"))
print(">>>vote_percentage('yes yes no yes no yes abstained yes yes no')")
print(vote_percentage("yes yes no yes no yes abstained yes yes no"))
print(">>>vote_percentage('abstained no abstained yes no yes no yes yes yes no')")
print(vote_percentage("abstained no abstained yes no yes no yes yes yes no"))
print(">>>vote_percentage('no yes no no no yes yes yes no')")
print(vote_percentage("no yes no no no yes yes yes no"))

print()

########################
# Question 2.3
########################


def vote_percentage(results):
#as you can witness I've used the last question function again in first part of question 2.3
    count_for_yes = 0
    count_for_no = 0
    
    for word in results.split():
        count_for_yes += word == "yes"
        count_for_no += word == "no"

    total_count = count_for_yes + count_for_no
#there is the same count_for_yes and count_for_no functions and their sum total_count
    return count_for_yes, total_count



def vote():
    results = input("Enter the yes, no, abstained votes one by one and then press enter:")
    count_for_yes, total_count = vote_percentage(results)
#In above part of the function I have connected total_count to vote_percentage(results)
#I will use this relationship to see if count_for_yes with sum of count_for_no is equals to total_count    
    if count_for_yes == total_count:
        print("proposal passes unanimously")
#when count_for_no is equal to zero then total_count will be assigned with count_for_yes value
#in this case count_for_no will be determined by first part whether it's zero or some numbers according to input
#like this I used elif to continue the stream of if function under certian conditions        
    elif count_for_yes >= (2 / 3) * total_count:
        print("proposal passes with super majority")
    elif count_for_yes >= (1 / 2) * total_count:
        print("proposal passes with simple majority")
    else:
        print("proposal fails")
print(">>>vote()")
(vote())
print(">>>vote()")
(vote())
print(">>>vote()")
(vote())
print(">>>vote()")
(vote())

print()        

########################
# Question 2.4
########################

def l2lo(w):
    #from what I witness in outcomes of the function in pdf, it gives us the integer part of (l) in (l,o)
    l = int(w)
    #so I use the above function to change the float that we put as w to integer to find (l)
    o = float((w - l) * 16)
    #above I created a function for (o) that will the substract the integer of (w) in the form of (l) from (w) itself which is float
    #for example: if we enter (w=7.5), it will change it to 7 first (l=7), then substract 7 from 7.5 (w-l) and multiply it with 16
    #I used float here to change back the value of (o) to float as per samples in pdf
    
   
    
    return (l, o)

print(">>>l2lo(7.5)")
print(l2lo(7.5))
print(">>>")
print(">>>l2lo(9.25)")
print(l2lo(9.25))
print(">>>")

