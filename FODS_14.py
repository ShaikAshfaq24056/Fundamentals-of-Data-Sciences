import pandas as pd
interaction_data = pd.DataFrame({
    'PostID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Likes': [50, 30, 20, 50, 10, 30, 40, 50, 20, 30]
})
likes_frequency = interaction_data['Likes'].value_counts().sort_index()
print("Frequency distribution of likes among the posts:")
print(likes_frequency)
