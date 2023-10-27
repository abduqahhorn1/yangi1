d = "Assalomu aleykum hurmatli mexmxolar shu saytga o'ting: https://1xbet.net @username"
def check_link(text:str): 
    if type(text) != str:
        return "Satr kiriting"
    
    print(text)
    text = text.strip().lower().split()
    print(type(text))
    print(text)
    for word in text:
        print(word)
        if word.startswith("https:") or word.startswith("@"):
            return "Reklama tarqatmang"
    return "Qabul qilindi"

check_link(d)

