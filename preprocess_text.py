
import os
import re

def preprocess_text(text):
    """
    Preprocess the input text by converting it to lowercase and removing 
    non-alphabetic characters.

    Parameters:
    -----------
    text : str
        The input text to preprocess.

    Returns:
    --------
    str
        The preprocessed text, converted to lowercase and stripped of any 
        characters that are not letters or spaces.
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text
