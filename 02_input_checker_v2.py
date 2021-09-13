# checks user choice is 'integer', 'text', or 'image'
def user_choice():

    valid = False
    while not valid:

        response = input("file type (integer / text / image): ").lower()

        text_ok = ["text", "t", "txt"]
        if response in text_ok:
            return "text"

        else:
            print("Please choose a valid file type")
            print()

keep_going = ""
while keep_going == "":

    data_type = user_choice()
    print("You chose", data_type)
    print()