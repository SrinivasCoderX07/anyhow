from sklearn.decomposition import TruncatedSVD

# Collaborative Filtering (SVD)
def collaborative_recommend(interaction_sparse, interaction_matrix):
    svd = TruncatedSVD(n_components=50, random_state=42)
    latent_matrix = svd.fit_transform(interaction_sparse)
    predicted_matrix = latent_matrix @ svd.components_
    return pd.DataFrame(predicted_matrix, index=interaction_matrix.index, columns=interaction_matrix.columns)
