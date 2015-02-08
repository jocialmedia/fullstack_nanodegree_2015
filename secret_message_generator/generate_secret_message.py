import os
import json
import shutil
import random

def create_secret_message():

    #(1) get home_directory
    home_directory = os.getcwd()

    #(2) create array to translate characters of secret message to filenames of pictures
    names_of_picturefiles = json.loads('{"a" : "a", "b" : "b", "c" : "c", "d" : "d", "e" : "e", "f" : "f", "g" : "g", "h" : "h", "i" : "i", "j" : "j", "k" : "k", "l" : "l", "m" : "m", "n" : "n", "o" : "o", "p" : "p", "q" : "q", "r" : "r", "s" : "s", "t" : "t", "u" : "u", "v" : "v", "w" : "w", "x" : "x", "y" : "y", "z" : "z", " " : "_empty", "." : "_dot", "!" : "_exclamation_mark", "?" : "_question_mark"}')

    #(3) create list of cities
    names_of_cities=["abu_dhabi", "accra", "amsterdam", "ankara",  "athens", "bangok",  "belgrade",  "berlin", "bogota", "bucharest", "budapest", "cairo", "canberra", "capetown", "copenhagen", "dakar", "doha", "dublin", "edinburgh", "hamburg", "hanoi", "helsinki",  "jakarta", "jerusalem", "kiev", "kigali", "lima", "london", "madrid", "manila", "minsk", "moscow", "nikosia", "oslo", "ottawa", "paris", "prague", "quito", "rabat", "riga", "san_marino", "sarajevo", "seattle", "seoul", "shanghai", "singapore", "skopje", "stockholm", "taipeh", "tiflis", "tirana", "tokyo", "tripolis", "tunis", "washington", "wellington", "vienna", "zagreb"]

    #(4) enter secret message (max 58 characters, only letters a-z, space, dot, question mark and exclamation mark)

    # for testing use this: enter_secret_message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .!?"
    enter_secret_message = "Enter secret message here!!!"

    #(5) make sure, everything is lowercase and create array with all characters separated
    secret_message = list(enter_secret_message.lower())

    #(6) loop through secrect message and get filename for every character
    m=0
    for i in range(len(secret_message)):
     if m<secret_message[i]:
        character = secret_message[i]

        #(7) copy the files to a new directory and put them in the right order with the counting variable "i"
        shutil.copy2(home_directory+'/pictures/' + names_of_picturefiles[character] + '.JPG', home_directory+'/output/' + names_of_cities[i] + '.JPG')

    #(8) get a list of citynames, rename the files in the result directory and add a random number to mix it up
    file_list = os.listdir(home_directory + "/output")
    for file_name in file_list:
        if not file_name.startswith('.'):
            os.rename(home_directory + "/output/"+file_name,home_directory + "/output/"+str(random.randint(10,99))+file_name)

create_secret_message()
