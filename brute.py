#importing required modules
import requests
from termcolor import colored
import os

#installing Requirements:
print("Installing requirements","."*5)
print("")
os.system('apt install figlet')
print("")
print("Requirements Installed :)")
print("")
os.system('figlet DirBrFors')
print("A Tool created by Jopraveen To bruteforce website directories")
print("")
#getting the website name and saving it in a variable "url"
url = input("Enter the website name with http/https: ")

'''  getting the path of the word list to do bruteforce 
and opening it in read mode  '''
print("\nTo use default wordlist type ./wordlist.txt")
path = input("Enter the path of the wordlist: ")

file = open(path, "r")

#creating a for loop to do bruteforcing
for j in range(20):
        a = file.readline()
        r = requests.get(url+a)
        status = r.status_code

        #assigning colors for each status code
        if status == 200:
                color = 'green'

        elif status == 404:
                color = 'red'

        elif status == 403:
                color = 'yellow'

        else:
                color = 'white'

        #printing the results ASAP
        print(colored("="*40,color))
        print(colored("Path: "+url+a, color))
        print(colored("status code: "+str(status), color))
        print(colored("="*40,color))
        print("")

#closing the file :D
file.close()
