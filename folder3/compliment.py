import random

def generate_compliment(name:str) -> str:
    compliments = [
        f"You're as bright as a shining star, {name}!",
        f"Everyone admires your incredible {name} skills!",
        f"{name}, you're the reason people smile around here!",
        f"Your positivity is contagious around here, {name}!"
    ]
    return random.choice(compliments)

def main():
    name = str(input("Enter your name: "))
    compliment = generate_compliment(name)

    print(compliment)

if __name__ == "__main__":
    main()
