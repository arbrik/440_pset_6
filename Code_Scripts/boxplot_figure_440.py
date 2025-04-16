import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

def distance_reader(directory):
    """
    This function reads in the distance files from the given directory and
    processes them into a dictionary of distances for subsequent plotting.
    Input: directory - the directory containing the distance files
    Output: fresh_distance_dict - a dictionary where the keys are the filenames
    and the values are lists of distances, repeated by their frequencies.
    """
    # Create an empty dictionary to hold the distances:
    fresh_distance_dict = dict()
    for filename in os.listdir(directory):
        # Print the filename to keep track of progress:
        print(f"Processing file: {filename}")
        file_path = os.path.join(directory, filename)
        # Import the processed file, making sure it is a tsv file:
        if filename.endswith('.tsv'):
            # Make a list that will store the repeated distances.
            # "statistical" in the name indicates that the distances are
            # already processed and in multiples based on frequencies.
            statistical_distances = []
            # Read in the file:
            processed_distances = pd.read_csv(file_path, sep=',')
            # Iterate over the rows of the dataframe and append the distances:
            for i in range(len(processed_distances)):
                statistical_distances += [processed_distances['distance'][i]]*\
                         processed_distances['weight'][i]
            # Save the distances to the dictionary:
            fresh_distance_dict[filename] = statistical_distances
    print("Done with this directory of samples.")
    return fresh_distance_dict


# Assuming the current working directory is the same as the script's directory.
# Access the directory of healthy pre-processed samples:
directory_healthy = "../Data_Files/healthy_patient_samples/"
# Import and further process the saved tsv files:
healthy_statistical_dict = distance_reader(directory_healthy)
# Access the directory of diseased (SLE) pre-processed samples:
directory_sle = "../Data_Files/SLE_patient_samples/"
# Import and further process the saved tsv files:
lupus_statistical_dict = distance_reader(directory_sle)

 
# Convert the dictionaries to dataframes:
healthy_statistical_df = pd.DataFrame.from_dict(healthy_statistical_dict, 
                                                orient='index')
print("Dictionary of healthy distances complete.")
lupus_statistical_df = pd.DataFrame.from_dict(lupus_statistical_dict, 
                                              orient='index')
print("Dictionary of lupus distances complete.")
# Transpose the dataframes for easier plotting:
healthy_statistical_df = healthy_statistical_df.T
lupus_statistical_df = lupus_statistical_df.T

# Plot the averge distances for each sample as a boxplot:
# First create a dictonary to hold the average distances for each group:
averages_dict = {'healthy': [], 'lupus': []}
# Then calculate the average distance for each sample:
for column in healthy_statistical_df.columns:
    averages_dict['healthy'].append(np.mean(healthy_statistical_df[column]))
for column in lupus_statistical_df.columns:
    averages_dict['lupus'].append(np.mean(lupus_statistical_df[column]))
# Convert the dictionary to a dataframe and transpose it for plotting:
averages_df = pd.DataFrame.from_dict(averages_dict, orient='index')
averages_df = averages_df.T
# Since there are only two groups, we can use a boxplot to visualize the data:
# We can print the averages themselves to see the group average distances:
print(averages_df)
# Plot the data as a boxplot, with a title, x and y labels, and save the figure:
plt.figure(figsize=(10, 6))
sns.boxplot(data=averages_df, palette=["blue", "red"])
plt.title('Average Distances for Healthy Volunteers and Lupus Patients', 
          fontsize=17)
plt.xlabel('Analysis Group', fontsize=15)
plt.xticks([0, 1], ['Healthy Volunteers', 'Lupus Patients'], fontsize=15)
plt.ylabel('Average Distance to Autoantibody Sequences', fontsize=15)
plt.savefig('healthy_lupus_distances_boxplot.png', dpi=300, bbox_inches='tight')
