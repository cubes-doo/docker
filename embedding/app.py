import os
from fastapi import FastAPI
from pydantic import BaseModel,Field
from sentence_transformers import SentenceTransformer
from typing import Literal

# Load the sentence-transformers model once on startup
#for all-mpnet-base-v2 is for english
#model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

MODEL_NAME  = os.getenv("MODEL_NAME", "intfloat/multilingual-e5-large")
MODEL_CACHE = os.getenv("MODEL_CACHE", "/models")  # ovde ćemo spustiti model tokom build-a

# Učitavanje iz prethodno skinutog cache-a
model = SentenceTransformer(MODEL_NAME, cache_folder=MODEL_CACHE)

app = FastAPI(title="E5 Embed API", version="1.0.0")


# Define the input structure expected by the API
class VectorRequest(BaseModel):
    needle: str = Field(..., min_length=1, description="Input text") #input text
    normalize: bool = True  #whether to normalize the vector or not (normalize for cosine similariy or K NN, dont normalise for dot product...)
    prefix: Literal["query", "passage"] = "query" #prefix can be "query" or "passage"| prefix is for search term, passage is for article that we compare with
    # query is for question or search object , passage is for article or object that we compare with
    # example: query => veslo za sup | passage => adidas terex patike/janka za vetar/ sup daska/ sup veslo 150cm

# endpoint to convert text to vector 
@app.post("/to-vector")
def to_vector(req: VectorRequest):
    # prefix is always with : and whitespace
    prefix = req.prefix+": "
    # combine prefix and needle
    full_input = prefix + req.needle.strip()
    # create vector embeding, we convert to numpy array for easier handling
    vector_embedding = model.encode(full_input,convert_to_numpy=True,normalize_embeddings=req.normalize,show_progress_bar=False)

    # retrun the vector as a list 
    return {
        "vector": vector_embedding.tolist()
    }