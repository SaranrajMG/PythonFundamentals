#!/usr/bin/python3
from urllib.request import urlopen

def fetch_word():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_items(items):
    for item in items:
        print(items)

def main():
    words = fetch_word()
    print_items(words)

if __name__ == "__main__":
    main()
