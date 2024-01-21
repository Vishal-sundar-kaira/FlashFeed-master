import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import nltk

# Download the 'punkt' and 'stopwords' resources
nltk.download('punkt')
nltk.download('stopwords')

# Send an HTTP request to the website
url = 'https://khelnow.com/kabaddi/2024-01-pkl-10-pun-vs-tam-dream11-predictions'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all text from the parsed HTML
    all_text = soup.get_text()

    # Tokenize the text into sentences and words
    sentences = sent_tokenize(all_text)
    word_tokens = [word_tokenize(sentence) for sentence in sentences]

    # Preprocess the sentences (remove stop words and convert to lowercase)
    stop_words = set(stopwords.words("english"))
    preprocessed_sentences = [
        [word.lower() for word in word_tokens[i] if word.lower() not in stop_words]
        for i in range(len(word_tokens))
    ]

    # Ensure all preprocessed sentences have the same length
    max_length = max(len(sentence) for sentence in preprocessed_sentences)
    preprocessed_sentences = [sentence + [''] * (max_length - len(sentence)) for sentence in preprocessed_sentences]

    # Convert lists to numerical arrays (crucial fix for cosine_distance)
    preprocessed_sentences = [np.array(sentence) for sentence in preprocessed_sentences]

    # Calculate similarity matrix
    num_sentences = len(preprocessed_sentences)
    similarity_matrix = np.zeros((num_sentences, num_sentences))

    for i in range(num_sentences):
        for j in range(num_sentences):
            if i != j:
                similarity_matrix[i][j] = cosine_distance(preprocessed_sentences[i], preprocessed_sentences[j])

    # Convert similarity matrix to scores
    sentence_scores = np.sum(similarity_matrix, axis=1)

    # Sort sentences by score in descending order
    sorted_sentences = [sentence for _, sentence in sorted(zip(sentence_scores, sentences), reverse=True)]

    # Extract the top N sentences for the summary
    summary_sentences = sorted_sentences[:3]  # Adjust the number based on your preference

    # Print the summary
    summary = ' '.join(summary_sentences)
    print(summary)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
