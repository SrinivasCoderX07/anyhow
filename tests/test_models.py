import pytest
from preprocess.extract_and_preprocess import interaction_sparse, interaction_matrix
from models.hybrid_model import hybrid_recommend

def test_hybrid_recommend():
    recommendations = hybrid_recommend(user_id=1, interaction_sparse=interaction_sparse, interaction_matrix=interaction_matrix)
    assert len(recommendations) > 0