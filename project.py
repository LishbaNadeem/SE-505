# Convert European floor number to US floor number
inp = input('Europe floor: ')  # Get input from the user
usf = int(inp) + 1  # Convert input to int and adjust for US floor numbering
print('US floor:', usf)  # Print the US floor number

# Calculate pay based on hours worked and hourly rate
hours = float(input('Enter your hours: '))  # Get hours worked from user
rate = float(input('Enter your rate: '))  # Get hourly rate from user
print('Pay:', hours * rate)  # Calculate and print total pay

# Conditional checks for variable x
x = 0
if x < 2:
    print('small')  # If x is less than 2
elif x < 10:
    print('medium')  # If x is between 2 and 10
else:
    print('large')  # If x is 10 or more
print('All done')  # Indicate completion

# Another set of conditions for variable x
x = 5
if x < 10:
    print('smaller')  # If x is less than 10
if x > 20:
    print('larger')  # If x is greater than 20
print('finis')  # Indicate end of this block

# Additional comparisons with x
x = 5
if x == 5:
    print('Equals 5')  # If x equals 5
if x > 4:
    print('Greater than 4')  # If x is greater than 4
if x <= 5:
    print('Less than or equal to 5')  # If x is less than or equal to 5
if x >= 5:
    print('Greater than or equal to 5')  # If x is greater than or equal to 5
if x < 6:
    print('Less than 6')  # If x is less than 6
if x != 6:
    print('Not equal to 6')  # If x is not equal to 6

# Nested print statements with x
x = 5
print('before 5')  # Print before checking x
if x == 5:
    print('is 5')  # If x equals 5
    print('still 5')  # Additional statement
    print('third 5')  # Additional statement
print('Afterwards 5')  # Print after checking x
print('before 6')  # Print before checking x again
if x == 6:
    print('is 6')  # If x equals 6
    print('still 6')  # Additional statement
    print('third 6')  # Additional statement
print('Afterwards 6')  # Print after checking x again

# Check if x is within a certain range
x = 40
if x > 1:
    print('More than 1')  # If x is greater than 1
if x < 100:
    print('Less than 100')  # If x is less than 100
print('All done')  # Indicate completion

# Check if x is greater or less than 2
x = 4
if x > 2:
    print('bigger')  # If x is greater than 2
else:
    print('smaller')  # If x is less than or equal to 2
print('All done')  # Indicate completion

# Check if x is less than 2 or between 2 and 10
x = 5
if x < 2:
    print('small')  # If x is less than 2
elif x < 10:
    print('medium')  # If x is between 2 and 10
print('All done')  # Indicate completion

# Function definition to print messages
def thing():
    print('Hello')  # Print greeting
    print('fun')  # Print additional message

# Call the function twice
thing()
print('zip')  # Print a separator message
thing()

# Function to print song lyrics
def print_lyrics():
    print('I am a lumberjack')  # Print first line of lyrics
    print('I sleep all night')  # Print second line of lyrics

# Main execution flow
print('yo')  # Print a message
x = x + 2  # Increment x
print(x)  # Print updated value of x
print_lyrics()  # Call the function to print lyrics

# Function to greet based on language
def greet(lang):
    if lang == 'es':
        return 'hola'  # Return greeting in Spanish
    elif lang == 'fr':
        return 'bonjour'  # Return greeting in French
    else:
        return 'hello'  # Return default greeting in English

# Call greet function with different languages and print results
print(greet('en'), 'Glenn')  # Greeting in English
print(greet('es'), 'Sally')  # Greeting in Spanish
print(greet('fr'), 'Michael')  # Greeting in French
