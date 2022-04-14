from nQueue import *

class wrongType(Exception):
    pass

def Palindromo(frase):
    try:
        if(type(frase) == str):
            str1 = ""
            lst = Queue()
            letters = [x for x in frase if x.isalpha()]
            for letter in letters: lst.addFirst(letter)
            while not(lst.isEmpty()):
                str1 += lst.first()
                lst.removeFirst()
            return True if str1 == frase.replace(" ","") else False
        else:
            raise wrongType
    except wrongType:
        print("input msut be a string")

def get_frases():
    while(True):
        palin = (input("Enter a word or a phrase to know if is a palindrome or not: \n"))
        if palin == "": break
        print(f"{palin}: E Palindromo\n") if Palindromo(palin) else print(f"{palin}: Nao e Palindromo\n") 
def main():
    get_frases()
    
if __name__=="__main__":
    main()