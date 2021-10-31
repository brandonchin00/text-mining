
#the file that wil be analyze
fp = open('data/Democratic_Party_(United_States).txt', encoding='utf-8')


'''for line in fp: 
    line = line.strip()
    line = line.lower()
    words = line.split(' ')'''


numbers = 0 #this is the variable for the number of words in the text
def word_count():
    """Returns the total of the frequencies in a histogram."""
    print("fp",fp)
    
    text = fp.read()
    words = text.split()
    numbers = len(words)
    return numbers
print('Total number of words:', word_count())

'''this would check the frequency of the words in the text file'''
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
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 0
    print (d)
    return (d)
#freq()

def natural_word():
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    with open('data/Democratic_Party_(United_States).txt','r') as f:
        for line in f:
            score = SentimentIntensityAnalyzer().polarity_scores(line)
            print(score)
#natural_word()

def similarity():
    from thefuzz import fuzz
    fp = open('data/Democratic_Party_(United_States).txt', encoding='utf-8')
    fp = fp.read()
    cp = open('data/Communism.txt', encoding='utf-8')
    cp = cp.read()
    for line in cp and fp:
        ratio = fuzz.ratio(cp, fp)
        print (ratio)
#similarity() 
#I'm not sure how this function works because it just prints out 3


            










