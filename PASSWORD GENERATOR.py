import random
import string

def generate_password(length=12, include_letters=True, include_digits=True, include_special_chars=True):
    
    char_sets = ''
    if include_letters:
        char_sets += string.ascii_letters 
    if include_digits:
        char_sets += string.digits  
    if include_special_chars:
        char_sets += string.punctuation  
    
    if not char_sets:
        raise ValueError("At least one character set must be selected")


    password = ''.join(random.choice(char_sets) for _ in range(length))
    
    return password

if __name__ == "__main__":
    print("Generated Password:", generate_password(length=16))
