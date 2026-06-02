while True:
    try:
       x=int(input(("Enter an integer for x: ")))

    except ValueError:
          print("Please enter an integer: ")

    else:
          print(f"You have successfully input a value for X. That is x is {x}")
          break 