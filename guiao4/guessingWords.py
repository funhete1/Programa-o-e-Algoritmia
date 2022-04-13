from Trie import *

def guessingwords(trie, word):
    if trie.query(word) == []: print("no matches for this word")
    for i in trie.query(word):
        print(i[0])


def main():
    t = Trie()
    with open('palavras1.txt', 'r') as file1,open("palavras2.txt", 'r') as file2:
        for words in file1:
            t.insert(words)
        for words in file2:
            t.insert(file2)
    
    print("search: ", end="\r")
    word = ""
    print("to erase/edit the input enter '.' and type the new word")
    while(True):
        
        char = input(f"search: {word}")
        if char == '.':
            word = ""
            continue
        word += char
        guessingwords(t, word)

if __name__=="__main__":
    main()