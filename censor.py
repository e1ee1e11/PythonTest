def censor(text, word):
    final = []
    for check in text.split(' '):
        if check != word:
            final.append(check)
        else:
            final.append("*" * len(check))
    return " ".join(final) 

print censor("this hack is wack hack", "hack") 
