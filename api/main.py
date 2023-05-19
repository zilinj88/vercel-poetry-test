from fastapi import FastAPI
from common.constants import MESSAGE
import spacy
from spacy.lang.en.examples import sentences 

app = FastAPI(
    title="Aerial Data API",
    version="0.1.0",
    description="Aerial Data API",
)

@app.get('/')
def api():
  return MESSAGE

@app.get('/spacy-test')
def api_spacy():
  nlp = spacy.load("en_core_web_sm")
  doc = nlp(sentences[0])
  tokens = []
  for token in doc:
    tokens.append({
      "text": token.text,
      "position": token.pos_,
      "dep": token.dep_
    })
  return {
    "text": doc.text,
    "tokens": tokens
  }
