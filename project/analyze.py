
#the file that wil be analyze
fp1 = open('data/Democratic_Party_(United_States).txt', encoding='utf-8')
cp1 = open('data/Communism.txt', encoding='utf-8')

'''for line in fp: 
    line = line.strip()
    line = line.lower()
    words = line.split(' ')'''


numbers = 0 #this is the variable for the number of words in the text
def word_count():
    """Returns the total of the frequencies in a histogram."""
    print("fp",fp1)
    
    text = fp1.read()
    words = text.split() #this is to divide up the text
    numbers = len(words)
    return numbers
print('Total number of words:', word_count())

numbers2 = 0 #this is the variable for the number of words in the text
def word_count2():
    """Returns the total of the frequencies in a histogram."""
    print("cp1",cp1)
    
    text = cp1.read()
    words = text.split()
    numbers2 = len(words)
    return numbers2
print('Total number of words:', word_count2())

'''this would check the frequency of the words in the text file'''
import requests
from pprint import pprint

def freq():
    d = dict() #creates an empty dictionary
    words=[]
    with open('data/Democratic_Party_(United_States).txt','r') as f:
        for line in f:
            for word in line.split():
                words.append(word)
                # print(word)  
    # text = fp.read()
    # print("text",text)
    # words = text.split()
    # print(words)
    for word in words: #using this, I can tag each word to a specific dictionary ID so that python can tell what word has been repeated
        if word in d:
            d[word] = d[word] + 1 
        else:
            d[word] = 0 
    pprint (d) #this will organize the information outputted
    return (d)
#freq()


def freq2():
    d = dict() #creates an empty dictionary
    words=[]
    with open('data/Communism.txt','r', encoding='utf-8') as f: #I had to use an encoding for this file becuase python could not read the file properly. There was an error with encoding that I had to figure out before the function could run
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
freq2()

def natural_word():
    from nltk.sentiment.vader import SentimentIntensityAnalyzer #imports the necessary module
    with open('data/Democratic_Party_(United_States).txt','r') as f:
        for line in f:
            score = SentimentIntensityAnalyzer().polarity_scores(line) #this will scan each line and output the sentiment of each line in the articles
            print(score)
#natural_word()

def natural_word2():
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    with open('data/Communism.txt','r') as f:
        for line in f:
            score = SentimentIntensityAnalyzer().polarity_scores(line)
            print(score)
#natural_word2()

def similarity():
    from thefuzz import fuzz
    fp = open('data/Democratic_Party_(United_States).txt', encoding='utf-8') 
    fp = fp.read()
    cp = open('data/Communism.txt', encoding='utf-8')
    cp = cp.read()
    for line in cp and fp: #I wanted to scan each line
        ratio = fuzz.ratio(cp, fp) #I discovered that similarity required to inputs. I used the two articles to compare but i can't figure out why the output is only 3. 
        print (ratio)
#similarity() 
#I'm not sure how this function works because it just prints out 3


            










