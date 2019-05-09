# -*- coding: utf-8 -*-
"""
Created on Thu May  2 08:20:48 2019

@author: Anthony Pitts

Random username and password generator.
"""


import subprocess
import string
import random



def __main__():
    [user, passwrd] = generate_random_user_pass()
    print("username: " + user)
    print("password: " + passwrd)
    
def generate_random_user_pass():
    
    username=""
    #capital letter
    username = username + random.choice(string.ascii_uppercase)
    #number
    username = username + random.choice(string.digits)
    #loop for rest of characters
    for i in range(9):
        username = username + random.choice(string.ascii_lowercase)
    #shuffles username
    password = ''.join(random.sample(username,len(username)))

    password=""
    #capital letter
    password = password + random.choice(string.ascii_uppercase)
    #number
    password = password + random.choice(string.digits)
    #special character
    password = password + random.choice("!@#$%*")
    #loop for rest of characters
    for i in range(8):
        password = password + random.choice(string.ascii_lowercase)
    #shuffles password
    password = ''.join(random.sample(password,len(password)))
    
    return [username,password]
    
def upload_file(file):
    #makes all forward slashes double backslashes for windows file system GUI
    file = file.replace("/","\\")
    #sends file path paramater to auto it file - auto it exe handles the file explorer to submit correct file
    exit_code = subprocess.run(["C:\\Users\\antho\\OneDrive\\Documents\\Python Scripts\\UploadFile.exe", file])
    return exit_code.returncode
    #browser.quit()
__main__()