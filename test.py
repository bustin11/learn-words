import random
import sys

def get_random_line(filename):
    word = ''
    while word == '':
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if lines:
                word = random.choice(lines).strip()
            else:
                return "The file is empty."
        return word

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test.py <filename>")
    else:
        file_path = sys.argv[1]
        random_line = get_random_line(file_path)
        print("Random line:", random_line)
