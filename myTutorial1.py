from urllib.request import urlopen

def fetch_words(): 
    with urlopen('http://sixty-north.com/c/t.txt') as story: 
        storywords = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for words in line_words:
                storywords.append(words)
    for word in storywords:
        print(word)

if __name__ == '__main__':
    fetch_words()