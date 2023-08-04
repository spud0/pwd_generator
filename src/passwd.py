import random
import time
import sys

all_word_choices = []

with open("/usr/share/dict/words", 'r') as word_choices: 
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
    else: 
        return w

def select_word(l : list[str]) -> str:
    w = random.choice(l)
    return w

def generate_pwd(length: int) -> str: 
    generated_pwd = []

    for _ in range(length): 
        word = select_word(all_word_choices)
        generated_pwd.append(clean_word(word))
    
    pwd = "".join(generated_pwd)
    return pwd





