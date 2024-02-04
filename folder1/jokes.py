def joke_of_the_day():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ]

    import random
    return random.choice(jokes)

def main():
    # Let's hear a joke!
    print(joke_of_the_day())

if __name__ == "__main__":
    main()
