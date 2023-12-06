import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

aus_reader = pd.read_csv('../processed/aus.csv')
annotations_reader = pd.read_csv('../processed/annotations.csv')

aus_reader['file'] = aus_reader['file'].astype(object).str.replace('.jpg', '')
merged_csv = pd.merge(aus_reader, annotations_reader, on='file')
# merged_csv.to_csv('merged_data.csv', index=False)

grouped_mean = merged_csv.drop(['file','FaceIndex'], axis=1).groupby('valence').mean()
means_values = merged_csv.drop(['file', 'valence','FaceIndex'], axis=1).mean()
absolute_difference = abs(grouped_mean.loc['positive'] - grouped_mean.loc['negative'])

sorted_au_diff = absolute_difference.sort_values(ascending=False)

plt.scatter(sorted_au_diff.index, sorted_au_diff.values,marker='o')
plt.title('Absolute Difference in AU Means (pos. vs neg.)')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.savefig("../processed/au_visualization.png")