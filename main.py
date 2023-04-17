import requests
import datetime
from bs4 import BeautifulSoup


def validate_and_execute():

    try:
        # defining input as integer
        number_paras = int(number_paras_input)

        if number_paras >= 5:
            name_date_write()
            pancetta_count()
            reversing_sentences()
        elif number_paras < 5:
            print("You have entered a wrong number!")

    except ValueError:
        print("Wrong input! Please enter a whole number that is 5 or greater.")


def reversing_sentences():

    # reversing paragraphs
    all_paragraphs.reverse()

    for paragraph in all_paragraphs:

        # cleaning and splitting text into sentences
        paragraph = paragraph.text.strip("  ")
        sentences = paragraph.strip().split(".")
        sentences = [s.strip() for s in sentences if s.strip()]

        # reversing sentences
        sentences.reverse()

        # joining sentences back
        reversed_sentences = ". ".join(sentences)

        # appending output to file
        with open('output.txt', 'a') as opened_file:
            opened_file.write(reversed_sentences+"."+"\n")

    print("Paragraphs with reversed sentences have been successfully written to the file output.txt!")


def pancetta_count():

    # initial value
    pancetta = 0

    for paragraph in all_paragraphs:

        # making both values lowercase for search purposes
        if "pancetta".lower() in paragraph.text.lower():
            pancetta += 1

    with open('output.txt', 'a') as opened_file:
        opened_file.write(f"The word 'pancetta' appears in {pancetta} paragraphs.\n")


def name_date_write():

    user_name = "Dmytro"
    current_date = datetime.date.today()

    # cleaning the output file, writing username and date
    with open('output.txt', 'w') as opened_file:
        opened_file.write(f"User: {user_name}, Date: {current_date}\n")


# user input var
number_paras_input = input("Enter a number of paragraphs to request (minimum 5):\n")

# request data vars
req_params = {"paras": number_paras_input, "format": "html"}
r = requests.get("https://baconipsum.com/api?type=meat-and-filler", params=req_params)

# html parser vars
soup = BeautifulSoup(r.text, 'html.parser')
all_paragraphs = soup.find_all("p")

# main
validate_and_execute()





















    # print(reversed_sentences+".")



    #reversed_sentences = []

    # for sentence in sentences_all:
    #     reversed_sentence = " ".join(sentence.split()[::-1])
    #     reversed_sentences.append(reversed_sentence)
    #
    # reversed_paragraph = ". ".join(reversed_sentences)
    # print(reversed_paragraph)
    # print()

# print(r.text)
#
# paragraphs = r.text.split("</p>")
# print(paragraphs)

# sentences = r.text.strip('][')
# print(sentences)
# sentences = sentences.split('","')
# print(sentences)
# sentences = sentences.strip('"')

#sentences.reverse()

# reversed_text = '.'.join(sentences)
#
# print(reversed_text+".")





'''def validate_and_execute():
    try:
        number_paras = int(number_paras_input)
        if number_paras >= 5:
            req_params = {"paras": number_paras, "format": "text"}
            r = requests.get("https://baconipsum.com/api?type=meat-and-filler", params=req_params)
            print(r.text)
        else:
            print("Wrong number! Enter a whole number 5 or more...")
    except ValueError:
        print("Wrong input type! Enter a whole number 5 or more...")'''




'''with open('output.txt', 'w') as opened_file:
    opened_file.write(r.text)'''


