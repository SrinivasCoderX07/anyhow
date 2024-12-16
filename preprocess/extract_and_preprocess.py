import os
import zipfile
import pandas as pd
from scipy.sparse import csr_matrix

# Paths
ZIP_PATH = "data\archive.zip""
EXTRACT_PATH = "data/"
CSV_PATH = EXTRACT_PATH + "ratings_Electronics.csv"

# Ensure ZIP extraction
if not os.path.exists(CSV_PATH):
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_PATH)

# Load data
data = pd.read_csv(CSV_PATH, names=["userId", "productId", "rating", "timestamp"])
data.drop("timestamp", axis=1, inplace=True)

# Preprocessing
min_user_ratings = 10
min_product_ratings = 10
filtered_data = data.groupby('userId').filter(lambda x: len(x) >= min_user_ratings)
filtered_data = filtered_data.groupby('productId').filter(lambda x: len(x) >= min_product_ratings)

interaction_matrix = filtered_data.pivot(index="userId", columns="productId", values="rating").fillna(0)
interaction_sparse = csr_matrix(interaction_matrix)