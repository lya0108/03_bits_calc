def num_check(question, low):

    valid = False
    while not valid:

        error = "please enter a number that is more than zero""(or equal to) {}".format(low)

        try:

            response = int(input(question))

            if response >= low:
                return response 

            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

keep_going = ""
while keep_going == "":
    print()

    var_integer = num_check()
    width = num_check()
    height = num_check()