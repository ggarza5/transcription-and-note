import spacy
import sys

# Load SpaCy model. You may have to download the model first using: python -m spacy download en_core_web_sm
nlp = spacy.load('en_core_web_sm')

def redact_names(line):
    doc = nlp(line)
    redacted_sentence = line
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            redacted_sentence = redacted_sentence.replace(ent.text, "[REDACTED]")
    return redacted_sentence

for line in sys.stdin:
    print(redact_names(line), end='')
