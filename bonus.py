def element_len(in_list:list) -> list:
    return([len(str(element)) for element in in_list])

def main():
    # These are just samples, feel free to use other lists as needed
    first_list = ['abc', 'dgooy', 'argument']
    second_list = [1246, 667865, 23]

    print(element_len(first_list))
    print(element_len(second_list))

    # Get user input for the list
    input_str = input("Enter elements for the list (comma-separated): ")
    user_list = [element.strip() for element in input_str.split(',')]

    # Print the lengths of elements in the list
    print("Lengths of elements in the list:", element_len(user_list))

if __name__ == "__main__":
    main()