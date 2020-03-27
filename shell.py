import basic

DIGITS = '0123456789+-*/^'
matm = 0

def split(word):
    return [char for char in word]

while True:
    text = input('basic > ')
    if text.strip() == "": continue
    
    lisst = split(text)
    #print(lisst)
    
    for elem in lisst:
        if elem in DIGITS:
            matm=1
            #print("matm")
        else:
            matm=0
            #print("nematm")
    
    if matm == 1:
        #print("matmmmm")
        result, error = basic.runm('<stdin>', text)
    else:
        result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))