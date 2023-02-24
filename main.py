import json
import os
import re

def search_dictionary(word, dictionary):
    list = []
    word = f" {word} "
    for value in dictionary:
        for value2 in value["transcript"]:
            if value2["text"].count(word):
                occourance = (f"text = \"{value2['text']}\", start = {value2['start']}, url = {value2['url']}")
                occourance = (''.join(occourance.splitlines()))
                print("[" + str(len(list)) + "] " + occourance)
                occourance = occourance + "," + " word = " + word + "\n"
                list.append(occourance)

    if len(list) == 0:
        print("No results found")
    else:
        chooseOption = int(input("\nChoose an option: "))
        while chooseOption > len(list):
            print("Invalid option")
            chooseOption = input("\nChoose an option: ")
        return(list[int(chooseOption)])


data = {}
inputFileLocation = ("./Transcripts/" + input("Enter the name of the transcription file in the Transcripts folder: ")+ ".json")

with open(inputFileLocation, 'r', encoding='cp850') as jsonFile:
    data = json.load(jsonFile)

    #print(data)

with open('input.txt') as f:
    inputList = f.readlines() # read all lines into a list
    inputList = [line.rstrip() for line in inputList] # remove '\n' at the end of each line otherwise it will be searched for with \n at the end
    print(inputList)# print the list to see if it worked

#check if user wants new output file
if input("Do you want to create a new output file? (y/n): ") == "y":
    os.remove("output.txt")


with open('output.txt', 'a') as file:
    count = 0 # count the number of lines in the input file for i didnt work
    while count < len(inputList):
        try:# if the search returns nothing it will throw an error and the program will continue
            file.write(search_dictionary(inputList[count], data))
            count += 1
        except:
            count += 1
            pass

file.close()
f.close()