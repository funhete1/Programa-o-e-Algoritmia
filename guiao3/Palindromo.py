from Stack import Stack 

class wrongType(Exception):
    pass

def Palindromo(frase):
    try:
        if(type(frase) == str):
            str1 = ""
            stack = Stack()
            letters = [x for x in frase if x.isalpha()]
            for letter in letters: stack.push(letter)
            while not(stack.isEmpty()):
                str1 += stack.pop()
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