#You are creating a simple messaging tool that generates a summary message based on the details provided by the user. The function will build and return a message that incorporates all the information given.
# Write a function called build_message(**info) that takes a variable number of keyword arguments representing pieces of information about a person (e.g., name, age, city). The function should return a formatted string that includes all provided pieces of information.

def build_message(**info):
    
    message = ''
    
    for key, value in info.items():
        message += f"The {key} is {value}. "
    
    return message

print(build_message(name='Arwa', age=21, city='Karachi'))
