import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict


def getTextfromPost(url):
    print('Getting your post')
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    # text = ' '.join(map(lambda div: div.text, soup.find_all('div', class_='articles')))
    text = soup.get_text().replace("\n","")
    print(text,"aaya hai")
    text = text.encode('ascii', errors='replace').replace(b"?", b" ").decode('ascii')
    return text


def summarize(text, n):
    print('Summarizing your post')
    text = text.replace('.', '. ')
    sents = sent_tokenize(text)

    if not 0 < n <= len(sents):
        raise ValueError("Invalid value of n for summarization. n should be greater than 0 and less than or equal to the number of sentences.")

    word_sent = word_tokenize(text.lower())
    _stopwords = set(stopwords.words('english') + list(punctuation))

    word_sent = [word for word in word_sent if word not in _stopwords]
    freq = FreqDist(word_sent)

    ranking = defaultdict(int)

    for i, sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]

    sents_idx = nlargest(n, ranking, key=ranking.get)
    return [sents[j] for j in sorted(sents_idx)]


if __name__ == "__main__":
    # url = 'https://indianexpress.com/article/sports/cricket/nepals-sandeep-lamichhane-sentenced-eight-years-in-jail-for-rape-and-ordered-to-pay-hefty-compensation-to-victim-9103602/'
    url = 'https://khelnow.com/kabaddi/2024-01-pkl-10-pun-vs-tam-dream11-predictions'

    text = getTextfromPost(url)
    summary = summarize(text, 4)
    print(text, "now get summarize \n")
    print(summary)
