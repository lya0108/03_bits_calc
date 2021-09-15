def num_check(question):


    valid = False
    while not valid:

        error1 = "please enter a number that is more than zero"
        error2 = "please enter a number"
        try:

            response = float(input(question))

            if response > 0:
                return response 

            else:
                print(error1)
                print()

        except ValueError:
            print(error2)
            print()
