try:
    with open (r"myfile.txt") as file:
        content = file.read()

except FileNotFoundError:
    print("File not Found!")
else:
    print("File Found!")
    print(f"The Character count is {len(content)}. The word count is {len(content.split())}.")

finally:
    print("Program ends here.")
