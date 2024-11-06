import text_utils

string = input("What would you like to perform reverse or capitalize? ")
if string.lower() == "reverse":
    rev_string = input("Please enter the string to reverse: ")
    reversed_string = text_utils.reverse_string(rev_string)
    print(f"The reverse of '{rev_string}' is: {reversed_string}.")
elif string.lower() == "capitalize":
    cap_string = input("Please enter the string to capitalize: ")
    capitalized_string = text_utils.capitalize_string(cap_string)
    print(f"The capitalization of '{cap_string}' is: {capitalized_string}")
else:
    print("Incorrect response. Please try again.")