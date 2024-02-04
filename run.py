from folder1.jokes import joke_of_the_day
from folder2.age import age
from folder3.compliment import generate_compliment

def joke() -> None:
    print("Here's the joke of the day:")
    print(joke_of_the_day())

def enter_age(in_age:int) -> None:
    age(in_age)

def compliment(name:str) -> str:
    return generate_compliment(name)

def main():
    "It's time for a joke."
    joke()
    
    input_age = int(input("Enter your age (and be honest): "))
    enter_age(input_age)

    "Now, I'll be a little bit nicer."
    input_name = str(input("Enter your name: "))
    new_compliment = compliment(input_name)
    print(new_compliment)


if __name__ == "__main__":
    main()