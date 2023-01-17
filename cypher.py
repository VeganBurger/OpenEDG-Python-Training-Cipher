def cipher(message, birth_month):
    cipheredtext = ""
    for char in message:
        unicodechar = ord(char) # This line will convert all characters we're interating through to their unicode value through the ord() function
        ciphered_val = unicodechar + birth_month # This line ciphers each character by adding the month value to the unicode value of each character
        cipheredtext += chr(ciphered_val) # This line will convert back the modified unicode value to the new ciphered character through the chr() function
    return cipheredtext

birth_month = None
while birth_month is None:
    try:
        birth_month = int(input("Please enter your birth month (1-12): ")) # This line requests input for the user to provide their birth month, and then converts it to an integer so we can operate with it
        if birth_month < 1 or birth_month > 12: # Detects whether the value provided is within the number of the months 1-12
            print("Invalid value. Please provide a valid birth month number between 1 (Jan) and 12 (Dec).")
            birth_month = None # If the value provided is not within the range 1-12, restores the value of birth_month to None, so that the loop starts again
        else:
            pass
    except:
            print("Sorry, something went wrong. Please provide a valid numeric value for your birth month.") # This line displays an error if the value provided is anything but a number

message = input("Please provide the message you would like to cipher: ") # This line requests user input for the message to cipher

ciphered_message = cipher(message, birth_month) # Executes the program cipher(), using the inputs the user provided for message and for birth_month

print("Ciphered message: " + ciphered_message) # Prints the ciphered message
