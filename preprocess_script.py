import spacy
import os

nlp = spacy.load('en_core_web_sm')

def preprocess_documents(directory):
    """
    This function reads all the text files in a directory and preprocesses them using the SpaCy library.
    Returns a list of dictionaries, where each dictionary corresponds to a document and contains the processed text as a list of tokens.
    """
    docs = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                text = f.read()
                doc = nlp(text)
                tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct and not token.like_num]
                doc_dict = {"id": filename, "text": tokens}
                docs.append(doc_dict)
    return docs
