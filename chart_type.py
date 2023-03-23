while True:

    print("Chart Types:");
    print("--------------");
    print("1. Bar");
    print("2. Line"); #presents options to user

    chart_type = input("Enter the chart type you want: "); #asks for input from the user
    print("The chart you chose is: " + chart_type); #Shows the user what they chose
    while True:
            answer = str(input("Is what you chose correct? (y/n): "))#fail system in case the user puts in the incorrect response
            if answer in ("y", "n"):
                break
                print("invalid input.")
            if answer == "y":
                continue
            else:
                print("Restarting")
                break


#Right now it repeats no matter the response but once everything is put together it should work
