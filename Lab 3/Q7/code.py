def replace_letter_in_file():
    try:
        with open('replacement_needed.txt', 'r') as file:
            text = file.read()

        print("Original text:", text)

        incorrect_letter = input('Enter the Incorrect Letter: ')
        correct_letter = input("Enter the Correct Letter: ")

        corrected_text = ''
        corrected_text = text.replace(incorrect_letter, correct_letter)

        print("Corrected text:", corrected_text)

        with open('corrected_replacement_needed.txt', 'w') as corrected_file:
            corrected_file.write(corrected_text)

    except FileNotFoundError:
        print("Error: The file 'replacement_needed.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


replace_letter_in_file()
