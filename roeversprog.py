# [[file:README.org::*Udvikling af logik][Udvikling af logik:1]]
# Dette er et modul til oversættelse mellem almindelige sprog og røversprog

def oversaet_til_roeversprog(inputtekst):
    return "".join([i+"o"+i if i not in "aeiouy " else i for i in inputtekst ])

def oversaet_fra_roeversprog_til_andet_sprog(inputtekst):
    outputtekst = ""
    i = 0

    while i < len(inputtekst):
        bogstav = inputtekst[i]
        if bogstav.lower() in "aeiouy":
            outputtekst += bogstav
            i += 1
        else:
            outputtekst += bogstav
            i += 3

    return outputtekst

