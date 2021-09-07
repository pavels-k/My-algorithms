import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import NearestNeighbors

mark_df = pd.read_csv('data/marks.txt')



print(mark_df)

train, test = train_test_split(mark_df, test_size = 0.2)
print(train)

nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(mark_df)
distances, indices = nbrs.kneighbors(mark_df)