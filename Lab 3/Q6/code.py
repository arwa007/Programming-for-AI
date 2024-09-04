
sent = input("Enter a sentence: ")

def takeSent(sent):
    if sent[-1] == '?':
         with open('myfile6.txt', 'w') as file: 
              file.write(sent)
    else:
         print("That's not a question")

takeSent(sent)
              
