import pandas as pd
data = {'customerID': [1, 2, 3, 4, 5],
        'reviews': ['good','bad','good','ok','bad']}
df = pd.DataFrame(data)
distribution = df['reviews'].value_counts().sort_index()
print("review ")
print(distribution)
