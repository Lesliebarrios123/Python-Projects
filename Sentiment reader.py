filename3 = "C:/Users/Lesli/PycharmProjects/practice file.txt"
filename0 = "C:/Users/Lesli/PycharmProjects/THE HOUND OF THE BASKERVILLES.txt"
filename1 = "C:/Users/Lesli/PycharmProjects/positive doc.txt"
filename2 = "C:/Users/Lesli/PycharmProjects/Negative list.txt"

def word_frequency(filename):
    with open(filename, 'r') as f:
        text = f.read()
    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.replace(', ', ' ')
    text = text.replace('"', ' ')
    text = text.replace("'", ' ')
    text = text.replace("!", '.')
    text = text.replace("?", '.')
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    text = text.replace('-', ' ')
    text = text.replace('[', ' ')
    text = text.replace(']', ' ')
    text = text.replace(':', ' ')
    text = text.replace(';', ' ')
    text = text.replace("'s", ' ')
    text = text.replace("mrs.", "mrs")
    text = text.replace("mr.", "mister")
    text = text.replace("dr.", "doctor")
    sentences = text.split('. ')
    return sentences

def file_file():
    with open(filename0, 'r') as f:
        thewords = f.read()
    thewords = thewords.split('\n')
    print(thewords)
    return thewords

def Positive_words_list(filename1):
    with open(filename1, 'r') as f:
        Pos_words = f.read()
    Pos_words = Pos_words.split('\n')
    Pos_words.pop()
    Pos_words.pop()
    #print(Pos_words)
    return Pos_words


def Negative_words_list(filename2):
    with open(filename2, 'r') as f:
        Neg_words = f.read()
    Neg_words = Neg_words.split('\n')
    Neg_words.pop()
    Neg_words.pop()
    #print(Neg_words)
    return Neg_words


def proj2(filename):
    Pos_words = Positive_words_list(filename1)
    Neg_words = Negative_words_list(filename2)
    positive_sentiment = 0
    negative_sentiment = 0
    neutral_sentiment = 0
    positive_sentiment0 = 0
    negative_sentiment0 = 0
    neutral_sentiment0 = 0
    positive_sentiment1 = 0
    negative_sentiment1 = 0
    neutral_sentiment1 = 0
    sentences = word_frequency(filename)
    #print(sentences)
    for sentence in sentences:
        #print(sentence)
        words = sentence.split(' ')
        #print(words)
        positive_sentiment0 = 0
        negative_sentiment0 = 0
        for word in words:
            #print(Pos_words)
            if word in Pos_words:
                positive_sentiment0 += 1
            elif word in Neg_words:
                negative_sentiment0 += 1
        if positive_sentiment0 > negative_sentiment0:
            positive_sentiment1 += 1
            #print("Positive: %i" % positive_sentiment1)
        elif positive_sentiment0 < negative_sentiment0:
            negative_sentiment1 += 1
            #print("Negative: %i" % negative_sentiment1)
        else:
            neutral_sentiment1 += 1
            #print("Neutral: %i" % neutral_sentiment1)
    print("Positive: %i" % positive_sentiment1)
    print("Negative: %i" % negative_sentiment1)
    print("Neutral: %i" % neutral_sentiment1)


proj2(filename0)


