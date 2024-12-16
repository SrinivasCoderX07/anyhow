from models.collaborative_model import collaborative_recommend
from models.content_model import recommend_content

# Hybrid Recommendation System
def hybrid_recommend(user_id, interaction_sparse, interaction_matrix, top_n=5):
    collaborative_scores = collaborative_recommend(interaction_sparse, interaction_matrix).loc[user_id]
    content_scores = recommend_content(user_id, interaction_matrix, top_n=None)
    hybrid_scores = 0.7 * collaborative_scores + 0.3 * content_scores
    return hybrid_scores.sort_values(ascending=False).index[:top_n]