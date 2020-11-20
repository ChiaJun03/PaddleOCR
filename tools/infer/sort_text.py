class Word_Data:
    def __init__(self,word,x,y):
        self.word = word
        self.x = x
        self.y = y

def sort_func_y(input):
    return input.y

def sort_func_x(input):
    return input.x

def sort_text(words, height, width):
    diff_y = height * 0.005
    diff_x = width * 0.01

    words.sort(key = sort_func_y)
    

    sentences = [] # list of sentence
    sentence = []
    sentence.append(words[0]) 
    temp = 0
    for index in range(1,len(words)):
        if abs(words[index].y - words[temp].y) < diff_y:
            sentence.append(words[index])
        else:
            sentence.sort(key=sort_func_x)
            if abs(sentence[0].x - words[index].x) < diff_x or abs(words[temp].y - words[index].y) > 1.5*diff_y:
                sentences.append(sentence)
                temp = index
                sentence = []
                sentence.append(words[temp])
            else:
                sentence.append(words[index])

    for sentence in sentences:
        sentence.sort(key = sort_func_x)
        temp = ''
        for word in sentence:
            temp += word.word + ' '
        print(temp)
    
    return sentences
