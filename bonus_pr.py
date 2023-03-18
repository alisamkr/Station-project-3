import time

#define the countdown function
def countdown(t):   
    for i in range(t):        
        print(str(t-i) + "\n") 
        time.sleep(1)  
    print("Time's up!")

# Taking input from the user
t = input("Enter the time in seconds: ")

# checking if the user input is valid
if t.isdigit():
    t = int(t)
    countdown(t)
else:
    print("Invalid input! Try again.")


