#7.2
#Imports microbit module
from microbit import *

#7.2
#Imports random module
import random

#7.5
#Defines a new function named spin_animation() and it takes in the parameter count
#This parameter controls the amount of loops in the animation, and it is a variable
def spin_animation(count):
    
    #7.8
    #Creates a variable named delay with integer value 50
    delay = 50
    
    #7.5
    #Creates a variable named index with the integer value 0
    index = 0
    
    #7.7
    #Creates a variable named loops with the integer value 0
    loops = 0
    
    #7.7
    #This while loop executes the indented code block only while the given condition is satisfied
    #In this case, the code will only run when the value of "loops" is less than the value of "count"
    while loops < count:
        
        #7.7
        #Increments the value of variable loops by 1
        loops = loops + 1
        
        #7.5
        #Chooses and displays a random image of an arrow from a predefined list
        display.show(Image.ALL_ARROWS[index])
        
        #7.8
        #Waits for "delay" number of milliseconds
        #In this case, delay is set to 50
        sleep(delay)
        
        #7.8
        #Increments the value of delay by 5
        delay = delay + 5
        
        #7.5
        #Increments the value of index by 1
        index = index + 1
        
        #7.7
        #This if statement only executes the indented code block if the value of "index" is equal to 8
        if index == 8:
            
            #7.7
            #Sets the value of index to 0
            index = 0

#7.4
#Defines a function named show_random_arrow(), this function takes no parameters.
def show_random_arrow():
    
    #7.2
    #Generates a random number from 0 to 7
    #Assigns this random integer to variable num
    num = random.randrange(8)
    
    #7.2
    #Shows an arrow pointing in a random direction
    #This arrow is taken from a predefined list
    display.show(Image.ALL_ARROWS[num])

#7.3
#This is an infinite while loop, it executes the indented code infinitely
while True:
    
    #7.3
    #This conditional if statement executes the code inside if the function button_a.is_pressed() returns True OR the function button_b.is_pressed() also returns True
    if button_a.is_pressed() or button_b.is_pressed():
        
        #7.5
        #This calls the function and passes in the parameter 30
        spin_animation(30)
        
        #7.4
        #Calls the function show_random_arrow()
        show_random_arrow()
        
