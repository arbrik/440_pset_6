import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Import and process the saved tsv files:
directory = 'training_materials_healthy/'
healthy_statistical_dict = dict()
for filename in os.listdir(directory):
    print(f"Processing file: {filename}")
    file_path = os.path.join(directory, filename)
    # Import the processed file:
    if filename.endswith('.tsv'):
        statistical_distances = []
        processed_distances = pd.read_csv(file_path, sep=',')
        for i in range(len(processed_distances)):
            statistical_distances += [processed_distances['distance'][i]]* processed_distances['weight'][i]
        healthy_statistical_dict[filename] = statistical_distances
    

# Import and process the saved tsv files:
directory = 'training_materials_lupus/'
lupus_statistical_dict = dict()
for filename in os.listdir(directory):
    print(f"Processing file: {filename}")
    file_path = os.path.join(directory, filename)
    # Import the processed file:
    if filename.endswith('.tsv'):
        statistical_distances = []
        processed_distances = pd.read_csv(file_path, sep=',')
        for i in range(len(processed_distances)):
            statistical_distances += [processed_distances['distance'][i]]* processed_distances['weight'][i]
        lupus_statistical_dict[filename] = statistical_distances

# Convert the dictionaries to dataframes:
healthy_statistical_df = pd.DataFrame.from_dict(healthy_statistical_dict, orient='index')
print("Healthy statistical distances complete.")
lupus_statistical_df = pd.DataFrame.from_dict(lupus_statistical_dict, orient='index')
print("Lupus statistical distances complete.")

# Plot the averge distances for each sample as a boxplot:
averages_dict = {'healthy': [], 'lupus': []}
for column in healthy_statistical_df.columns:
    averages_dict['healthy'].append(np.mean(healthy_statistical_df[column]))
for column in lupus_statistical_df.columns:
    averages_dict['lupus'].append(np.mean(lupus_statistical_df[column]))
averages_df = pd.DataFrame.from_dict(averages_dict, orient='index')
averages_df = averages_df.T
print(averages_df)
plt.figure(figsize=(10, 6))
sns.boxplot(data=averages_df, palette=["blue", "red"])
#sns.set(font_scale=1.2)
plt.title('Average Distances for Healthy Volunteers and Lupus Patients', fontsize=17)
plt.xlabel('Analysis Group', fontsize=15)
plt.xticks([0, 1], ['Healthy Volunteers', 'Lupus Patients'], fontsize=15)
#plt.xticks(rotation=45)
plt.ylabel('Average Distance to Autoantibody Sequences', fontsize=15)
plt.savefig('healthy_lupus_distances_boxplot.png', dpi=300, bbox_inches='tight')