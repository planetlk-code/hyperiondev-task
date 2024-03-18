user_input = input("Please enter some text: ")
print(f"You said: \n'{user_input}'.\n")

user_in_filename = input("Enter a filename to save to: ")

try:
    with open(user_in_filename, 'w', encoding='utf-8') as file:
        file.write(user_input) # write to file.

except Exception as err: # catch any error in the writing of the file.
    print("\aError: " + str(err) + '.\n')

print("Done.\n")

