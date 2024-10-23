def report_count(token):
    n=0
    with open('corpus.txt','r') as file:
        corpus=file.read()
    
    n=corpus.lower().split().count(token.lower())

    return print("The term ", token, "shows up in the corpus ", n," times.")

