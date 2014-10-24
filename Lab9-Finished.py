############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print "Please enter Celcius"
UserInput = int(raw_input())
print UserInput * 9/5 + 32

############################################
#                                          # 
#                   85pt                   #
#             Who has a fever?             #
############################################

# Create a for loop that will search through temperatureList
# and create a new list that includes only numbers greater than 100

myList = [102,98,96,101,100,99,103,97,98,105]

# Insert for loop here
for x in myList:
    if x > 100:
        print x
        
# This should print [102,101,103,105]


############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.


print "What is your temperature?"
userInput = int(raw_input())
print "Have you been sick in the last 24 hours?"
userInput2 = raw_input()
print "Have you recently travelled to West Africa?"
userInput3 = raw_input()

if userInput >= 105:
    print "Go to the hospital."
else:
    if userInput2 == "yes" and userInput > 102:
        print "Go to the hospital."
    else:
        if userInput > 100 or userInput2 == "yes":
            print "Go to the hospital."
        
if userInput <= 105:
    print "Good news, you can go home."
else:
    if userInput2 == "no" and userInput2 < 102:
        print "Good news, you can go home."
    else: 
        if userInput3 == "no":
            print "Good news, you can go home."
            