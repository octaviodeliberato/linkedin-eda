import re, unicodedata, contractions, inflect
import nltk
from nltk import LancasterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

class TextProcessing:
    '''Basic text processing
    Parameters
    ----------
    words: str
        text to be processed
    Return
    ----------
    words: str
        processed text
    '''

    def __init__(self):
        pass

    def remove_html(self, words):
        '''Remove message with html'''
        return re.sub(r'^<p.*</p>', '', words)

    def replace_contractions(self, text):
        """Replace contractions in string of text"""
        return contractions.fix(text)

    def remove_URL(self, sample):
        """Remove URLs from a sample string"""
        return re.sub(r"http\S+", "", sample)

    def remove_non_ascii(self, words):
        """Remove non-ASCII characters from list of tokenized words"""
        return [unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore') for word in words]

    def to_lowercase(self, words):
        """Convert all characters to lowercase from list of tokenized words"""
        return [word.lower() for word in words]

    def remove_punctuation(self, words):
        """Remove punctuation from list of tokenized words"""
        return [re.sub(r'[^\w\s]', '', word) for word in words]

    def replace_numbers(self, words):
        """Replace all interger occurrences in list of tokenized words with textual representation"""
        p = inflect.engine()
        return [p.number_to_words(word) if word.isdigit() else word for word in words]

    def remove_stopwords(self, words):
        """Remove stop words from list of tokenized words"""
        return [word for word in words if word not in stopwords.words('english')]

    def stem_words(self, words):
        """Stem words in list of tokenized words"""
        stemmer = LancasterStemmer()
        return [stemmer.stem(word) for word in words]

    def lemmatize_verbs(self, words):
        """Lemmatize verbs in list of tokenized words"""
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(word, pos='v') for word in words]

    def normalize(self, words):
        words = self.remove_non_ascii(words)
        words = self.to_lowercase(words)
        words = self.remove_punctuation(words)
        words = self.replace_numbers(words)
        words = self.remove_stopwords(words)
        # Remove space
        words = ' '.join(words).replace('  ', ' ').strip().split(' ')
        try:
            words.remove('')
        except:
            pass

        return words

    def preprocess(self, sample):
        sample = self.remove_html(sample)
        sample = self.remove_URL(sample)
        sample = self.replace_contractions(sample)
        # Tokenize
        words = nltk.word_tokenize(sample)

        # Normalize
        words = self.normalize(words)
        # return sample
        return ' '.join(words)