#Name: destiney
#Date: 12/11/24

#Initialize
import turtle
t = turtle.Turtle()
age = 0
price = 100
weekday = ""
name = ""
discount = ""
#Functions

#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket
def draw_ticket(name, price, dayofweek, y_location):
    t.goto(0, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    t.goto(100, y_location +215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, y_location +215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, y_location +135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(225, y_location +15)
    t.write(price, font=("Arial", 15), align="right")
#this funtion asks the buyer to put in the informatioin then prints the information on a ticket.
def ticketPrice():
    print("Welcome to the Baby Justin Beiber Sing along experience ticket box!")
    global age, name, weekday, discount, price    
    answer = input("Would you like to buy some tickets? ")
    if answer == "no":
        print("Okay thank you have a good day!")
        quit
    elif answer == "yes":
        age = int(input("What is the age of the ticketholder? ")) #lines 46 to 49 are questions that get the input on what to write on the ticket
        weekday = input("What day are you attending? ")
        name = input("What is the name of the ticketholder? ")
        discount = input("Do you have a discount code? ")
        discode = ""
        weekday = "monday" or "tuesday" or "wednesday" or "thursday" or "friday" or "saturday" or "sunday" #this makes it so there are only a few options for the days and it wont print any word as the day
        if discount == "yes":
            discode = input("Please enter your discount code: ")
        elif discount == "no":
            print("No discount added")
        if discode == "FREEFRIDAY" and weekday == "friday" and 4<=age<=17: #This is for the discount code to work
            price= 0
        elif discode == "SUNDAY10" and weekday == "sunday" and 4<=age<=17: #this also makes a discount code
            price = 90
        elif age <= 3: #this makes the price for certain age ranges
            price = 0
        elif 4<=age<=17 and weekday == "saturday" or weekday == "sunday":
            price = 100
        elif 4<=age<=17 and weekday == "monday" or weekday == "tuesday" or weekday == "wednesday" or weekday == "thrusday" or weekday == "friday": #this is the discounted price
            price =50
        elif age>18:
            price = 100
        else:
            print("Please enter a valid code")
            return ticketPrice()
    draw_ticket(name,price,weekday,0) #this prints the ticket
            

    
#Main
ticketPrice()

