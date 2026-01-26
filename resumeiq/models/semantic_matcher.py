from sklearn.metrics.pairwise import cosine_similarity
from resumeiq.models.embedding_loader import get_embedding

def semantic_match(text1, text2):
    emb1 = get_embedding(text1).reshape(1, -1)
    emb2 = get_embedding(text2).reshape(1, -1)
    return float(cosine_similarity(emb1, emb2)[0][0])
