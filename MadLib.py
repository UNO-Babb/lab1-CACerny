#MadLib.py
#Name: Caden Cerny
#Date: 8/28/2024
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
  name1 = input("Enter a name: ")
  name2 = input("Enter another name: ")
  number1 = input("Enter a number: ")
  adjective1 = input("Enter an adjective: ")
  noun1 = input("Enter a noun: ")
  adjective2 = input("Enter another adjective: ")
  animal1 = input("Enter a type of animal: ")
  adjective3 = input("Enter another adjective: ")
  verb1 = input("Enter a verb: ")
  adjective4 = input("Enter another adjective: ")
  adjective5 = input("Enter another adjective: ")
  #Print the story with the user supplied words.
  print("Hello my name is spaceman " + name1 + ". I am on my way to planet " + name2 + ". I will be gone for " + number1 + " days. I am very " + adjective1 + " about the trip but I will miss my " + noun1 + ". I have heard that the atmosphere there is " + adjective2 + ". Luckily my pet " + animal1 + " packed me a jacket to keep me " + adjective3 + ". When I land on the planet I will " + verb1 + " for joy. I am " + adjective4 + " to walk on another planet. I could not be more " + adjective5 + " for this trip!")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
