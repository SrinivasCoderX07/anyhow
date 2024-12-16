from sklearn.metrics.pairwise import cosine_similarity

def recommend_content(user_id, interaction_matrix, top_n=5):
    product_embeddings = interaction_matrix.T.values
    similarity_matrix = cosine_similarity(product_embeddings)
    user_ratings = interaction_matrix.loc[user_id]
    scores = similarity_matrix @ user_ratings
    top_products = scores.argsort()[-top_n:][::-1]
    return interaction_matrix.columns[top_products]