'''def natural_word():
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    fp = open('data/Democratic_Party_(United_States).txt', encoding='utf-8')
    mylist = list(fp)
    score = SentimentIntensityAnalyzer().polarity_scores(mylist)
    print(score)
natural_word()'''
import requests
from pprint import pprint
def freq():
    d = dict() #creates an empty dictionary
    words=[]
    with open('data/Communism.txt','r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                words.append(word)
                # print(word)  
    # text = fp.read()
    # print("text",text)
    # words = text.split()
    # print(words)
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 0
    pprint (d)
    return (d)
freq()