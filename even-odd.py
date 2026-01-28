while True:
    try:
        a = int(input("Enter a number\n"))
        break
    except ValueError:
        print("That was not a number. Please try again.")

if a % 2 == 0:
    print(f"{a} is an even number")
else:
    print(f"{a} is an odd number")
