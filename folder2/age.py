def age(age:int) -> None:
    if age <= 0:
        raise ValueError("Please enter an age greater than 0 (unless you are a baby).")
    elif age <= 17:
        print("Too bad, you're still a child.")
    elif age <= 40:
        print("You're not over the hump yet. Get excited!")
    elif age <= 60:
        print("You're old, but you're not ancient.")
    else:
        print("Your glory years are behind you.")

def main():
    # get input from user
    input_age = int(input("Enter your age (and be honest): "))
    age(input_age)

if __name__ == "__main__":
    main()