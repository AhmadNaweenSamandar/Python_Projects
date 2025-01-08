#Family name: Samandar
#Student number: 300446112
# Course: ITI 1120
# Assignment Number 1
# year 2024

########################
# Question 1
########################

def mh2kh(s):
    x=s*1.60934
    return x
    
print ('>>> #testing question 1')
print ('>>>')
print ('>>> mh2kh(5)\n',
mh2kh(5))
print ('>>> mh2kh(110.4)\n',
mh2kh(110.4))
print('>>>')
print('>>>')

########################
# Question 2
########################

import math
def pythagorean_pair(a, b):
    c = a**2+b**2
    d = math.sqrt(c)
    
    return int(d)**2 == c
print('>>> #testing question 2')
print('>>>')
print('>>> pythagorean_pair(2,2)\n',
pythagorean_pair(2,2))
print('>>> pythagorean_pair(6,2)\n',
pythagorean_pair(6,2))
print('>>> pythagorean_pair(6,8)\n',
pythagorean_pair(6,8))
print('>>> pythagorean_pair(300,-400)\n',
pythagorean_pair(300,-400))
print('>>>')
print('>>>')


########################
# Question 3
########################


def in_out(xs,ys,side):
    x = float(input('Enter a number for the x coordinate of a query point:'))
    y = float(input('Enter a number for the y coordinate of a query point:'))
    d = (xs <= x <= side  and ys <= y <= side)
    return d
print('>>> #testing question 3')
print('>>>')
print('>>>','in_out(0,0,2.5)')
print (in_out(0,0,2.5))

def in_out(xs,ys,side):
    x = float(input('Enter a number for the x coordinate of a query point:'))
    y = float(input('Enter a number for the y coordinate of a query point:'))
    d = (xs <= x <= side  and ys <= y <= side)
    return d

print('>>>','in_out(2.5,1,2.5)')
print (in_out(2.5,1,1))

def in_out(xs,ys,side):
    x = float(input('Enter a number for the x coordinate of a query point:'))
    y = float(input('Enter a number for the y coordinate of a query point:'))
    d = (xs <= x <= side  or ys <= y <= side)
    return d

print('>>>','in_out(0,0,2.5)')
print (in_out(-2.5,1,2.1))
print('>>>')
print('>>>')

########################
# Question 4
########################

def safe(n):
    return('9'not in str(n)) and  ( n%9 !=0)

print('>>> #testing question 4')
print('>>>')
print('>>>safe(93)')
print(safe(93))
print('>>>safe(82)')
print(safe(82))
print('>>>safe(29)')
print(safe(29))
print('>>>safe(36)')
print(safe(36))
print('>>>safe(9)')
print(safe(9))
print('>>>safe(7)')
print(safe(7))
print('>>>')
print('>>>')

########################
# Question 5
########################

print('>>> #testing question 5')
print('>>>')
def quote_maker(quote, name, year):
    x = year+name+quote
    return x

print('>>> quote_maker("Everything should be made as simple as possible but not simpler.", "Albert Einstein", 1933)')
print( quote_maker(quote = "\"Everything should be made as simple as possible but not simpler.\"'",name = " a person called Albert Einstein said: ",year = "\'In 1933,"))
print('>>>')
print('>>> quote_maker("I would never die for my beliefs because I might be wrong.", "Bertrand Russell", 1951)')
print( quote_maker(quote = "\"I would never die for my beliefs because I migh be wrong.\"'",name = " a person called Bertrand Russell said: ",year = "\'In 1951,"))
print('>>>')
print('>>>')

########################
# Question 6
########################

print('>>> #testing question 6')
print('>>>')

def quote_displayer(quote, name, year):
    x = year+name+quote
    return x
print('>>>quote_displayer()')
print(quote_displayer(input('Give me a quote: '),input('Who said that? '),input('What year did she/he said that? ')))
print('>>>')
print('>>>')

############################
##### Question 7
############################

print('>>> #testing question 7')
print('>>>')
def rps_winner():
    print('>>>rps_winner()')
    print('What choice did player 1 make?')
    player1 = input('Type one of the following options: rock, paper, scissors: ')
    
    print('What choice did player 2 make?')
    player2 = input('Type one of the following options: rock, paper, scissors: ')
    
    player1_wins = (player1 == 'rock' and player2 == 'scissors') or \
                   (player1 == 'scissors' and player2 == 'paper') or \
                   (player1 == 'paper' and player2 == 'rock')
    
    tie = player1 == player2
    
    result = player1_wins
    tie_result = tie

    print(f'Player 1 wins. That is {result}')
    print(f'It is a tie. That is not {not tie_result}.')

print (rps_winner())
print (rps_winner())
print (rps_winner())
print ('>>>')
print ('>>>')


############################
##### Question 8
############################
print('>>> #testing question 8')
print('>>>')
import math
def fun(x):
    y = math.log10 (x+3)/4
    return y
print('>>>fun(7)')
print(fun(7))
print('>>>fun(20)')
print(fun(20))
print('>>>fun(999999997)')
print(fun(999999997))
print('>>>fun(0.1)')
print(fun(0.1))
print('>>>')
print('>>>')

############################
##### Question 9
############################
print('>>> #testing question 9')
print('>>>')

def ascii_name_plaque(x):
    return x
print('ascii_name_plaque("Monica")')
print(' **************\n','*     *      \n','* _',ascii_name_plaque('Monica'),'_  *\n','*     *      \n','**************')
print('ascii_name_plaque("Captain Kara Starbuck Thrace")')
print(' ***************************************\n','*                   *   \n','*',ascii_name_plaque("_Captain Tara 'Starbucks' Thrace_  *\n"),'*                   *      \n','***************************************')
print('ascii_name_plaque("Seven of Nine")')
print(' **********************\n','*          *   \n','*',ascii_name_plaque("_Seven of Nine_  *\n"),'*          *      \n','**********************')

########################
# Question 10
########################
print('>>>draw_court()')
import turtle
def draw_court():
    
    x=turtle.Screen()
    x.bgcolor("green")
    y=turtle.Turtle()
    y.color("white")
    #Here I have created vertical line that divide the ground to two parts
    #Further I created a circle
    
    y.left(90)
    y.forward(300)
    y.penup()
    y.goto(0,120)
    y.setheading(0)
    y.pendown()
    y.circle(30)

    #The line go further to create a square ground
    
    y.left(90)
    y.forward(180)
    y.right(90)
    y.forward(300)
    y.right(90)
    y.forward(300)
    y.right(90)
    y.forward(600)
    y.right(90)
    y.forward(300)
    y.right(90)
    y.forward(300)
    y.right(90)
    y.forward(150)

    #The function now create a half circle in the right side

    y.penup()
    y.goto(300,30)
    y.pendown()
    y.setheading(0)
    y.circle(120,-180)
    y.setheading(0)
    
    #The small circle within half circle in right side will be created
    
    y.penup()
    y.goto(210,120)
    y.setheading(0)
    y.pendown()
    y.circle(30,180)
    y.setheading(0)
    y.penup()
    y.goto(210,120)
    y.pendown()
    y.color("white")
    y.circle(30,-180)
    y.color("white")

    #The following function will create one small and one big square in the righ side
    
    y.setheading(0)
    y.penup()
    y.goto(300,120)
    y.pendown()
    y.forward(-90)
    y.left(-90)
    y.forward(-60)
    y.left(-90)
    y.forward(-90)
    y.right(90)
    y.forward(15)
    y.left(90)
    y.forward(90)
    y.left(90)
    y.forward(90)
    y.left(90)
    y.forward(90)


    #Now the half circle in left side will be created
    y.penup()
    y.goto(-300,30)
    y.pendown()
    y.setheading(0)
    y.circle(120,180)

    #Further the small circle will be created in two pieces collapsing to eachother
    y.penup()
    y.goto(-210,120)
    y.setheading(0)
    y.pendown()
    y.circle(30,180)
    y.setheading(0)
    y.penup()
    y.goto(-210,120)
    y.pendown()
    y.color("white")
    y.circle(30,-180)
    y.color("white")

    #This set of function will create a small square then a bigger one
    
    y.setheading(0)
    y.penup()
    y.goto(-300,120)
    y.pendown()
    y.forward(90)
    y.left(90)
    y.forward(60)
    y.left(90)
    y.forward(90)
    y.right(90)
    y.forward(15)
    y.left(90)
    y.forward(-90)
    y.left(90)
    y.forward(90)
    y.left(90)
    y.forward(-90)
    
    

    #This function create goel point within the square in left side
    y.penup()
    y.goto(-270,147)
    y.pendown()
    y.circle(2)
    #It continues to create line for goal point
    y.setheading(0)
    y.penup()
    y.goto(-290,130)
    y.left(90)
    y.pendown()
    y.forward(40)
    y.right(180)
    y.forward(20)
    y.left(90)
    y.forward(20)
    #Now it's time for goal point in the right side
    y.penup()
    y.goto(270,147)
    y.pendown()
    y.circle(2)
    #The goal point lines will be created
    y.setheading(0)
    y.penup()
    y.goto(290,130)
    y.left(90)
    y.pendown()
    y.forward(40)
    y.left(180)
    y.forward(20)
    y.right(90)
    y.forward(20)
print(draw_court())

############################
##### Question 11
############################

print('>>> #testing question 11')
print('>>>')
def alogical(n):
    x = math.ceil(math.log2(n))
    return x
print('>>>alogical(5.4)')
print(alogical(5.4))
print('>>>alogical(4)')
print(alogical(4))
print('>>>alogical(1000)')
print(alogical(1000))
print('>>>alogical(4200231)')
print(alogical(4200231))


############################
##### Question 12
############################
print('>>> #testing question 12')
print('>>>')
def cad_cashier(price,payment):
    #here I have created a formula for this function 
    x = payment-price
    #since the round off in question was closest to 5 cents; I used round off to multiply x with 20
    #then divide by 20 to get to nearest of 0.05, it will represent the function in two decimal
    y = round(x*20)/20
    return round(y,2)
print('>>>cadcashier(10.58,11)')
print(cad_cashier(10.58,11))
print('>>>cadcashier(98.87,100)')
print(cad_cashier(98.87,100))
print('>>>cadcashier(10.58,15)')
print(cad_cashier(10.58,15))
print('>>>cadcashier(10.55,15)')
print(cad_cashier(10.55,15))
print('>>>cadcashier(10.54,15)')
print(cad_cashier(10.54,15))
print('>>>cadcashier(10.52,15)')
print(cad_cashier(10.52,15))
print('>>>cadcashier(10.50,15)')
print(cad_cashier(10.50,15))
print('>>>')

############################
##### Question 13
############################

def cad_cashier(price, payment):
    # Calculate the change
    x = payment - price
    
    # Round the change to the nearest 0.05 (5 cents)
    y = round(x * 20) / 20.0  # Rounds to nearest 0.05
    
    # Return the rounded change
    return round(y, 2)

def min_CAD_coins(price, payment):
    # Get the change from cad_cashier
    x = cad_cashier(price, payment)
    
    # Convert change to cents (and avoid floating-point issues)
    cents = int(round(x * 100))
    
    # Define coin values in cents
    toonie = 200
    loonie = 100
    quarter = 25
    dime = 10
    nickel = 5
    
    # Calculate the minimum number of coins using integer division
    t = cents // toonie  # Number of toonies
    cents = cents % toonie
    
    l = cents // loonie  # Number of loonies
    cents = cents % loonie
    
    q = cents // quarter  # Number of quarters
    cents = cents % quarter
    
    d = cents // dime  # Number of dimes
    cents = cents % dime
    
    n = cents // nickel  # Number of nickels
    
    # Return the tuple (toonies, loonies, quarters, dimes, nickels)
    return (t, l, q, d, n)

print(min_CAD_coins(10.58,11))
