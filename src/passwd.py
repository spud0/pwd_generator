"""
    The code here is an offshoot of the Password Generator on repl.it, this code contains the     important details pertinent to the implementation. 
"""

import random
import time
import sys


all_word_choices = []
generated_pwd = []

with open("usr/share/dict/words", 'r') as word_choices: 
    while True: 

        raw_word = word_choices.readline()
        if not raw_word: 
            break
        word = raw_word.replace("\n", "")
        all_word_choices.append(word)

def prefix_pwd_with_num(pwd: str) -> str: 
    r_num = str(random.randint(0, 1000))
    r_num += pwd
    return r_num

def suffix_pwd_with_num(pwd: str) -> str: 
    r_num = str(random.randint(0, 1000))
    pwd += r_num
    return pwd

def clean_word(w: str) -> str: 
    # Remove single apostrophe
    if "'" in w:
        new_w = w.replace("'", "")
    
    return new_w

def select_word(l : List[str]) -> str:
    w = random.choice(l)
    return w

def generate_pwd(length: int) -> str: 
    for _ in range(length): 
        word = select_word(all_word_choices)
        generated_pwd.append(clean_word(word))
    
    pwd = "".join(generated_pwd)
    return pwd





