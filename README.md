**OVERVIEW**
On a high level, this repository contains pre-processed antibody library samples of patients with Systemic Lupus Erythematosus and of healthy volunteers, in addition to a Python script that suffices to generate Figure 3C in the first draft report submitted by Arbri Kopliku and Ryan Lim for 20.440 (Spring 2025 offering) from the provided data. 

The goal of this script is to take the preprocessed datasets by reading all the TSV files, to convert the distances and frequencies present in the data files into workable lists of distances, and then to combine the lists into dataframes. Afterwards, the script calculates the average distance for each sample and displays the data as a boxplot of the healthy volunteers against the SLE patients. The main purpose of Figure 3C was to investigate and report whether the two groups (healthy and SLE) have statistical differences in the average minimal distance between all their CDR3 libraries and any identified auto-CDR3. The statistical analysis in the original project submission is performed via a two-sided Student's t-test with a critical alpha-value of 0.05, which will be included in the updated version of this repository. 

The code script was supplemented with many comments to facilitate interpretation, troubleshooting, and possible future adaptations. Additionally, the code script was enhanced for increased readability, decreased redundancy, and easier reproducibility. Please note that the structures of the raw and processed datasets, including the biological meanings of "distance" and "frequency", are described in more detail in the "DATA" section below.

**DATA**
In a separate part of this project, the script for which will be included in this repo in a future version, the raw data for both patients and volunteers consisted of full antibody libraries, originally produced by Zaslavsky et al. and accessible online on https://www.synapse.org/Synapse:syn62002263. The CDR3 sequences were represented in a separate column and were exctracted without losing the source affiliation (unique ID of the patient or donor). On the other hand, a library of computationally-predicted autoantibodies was curated in a separate part of this project, also not represented in this submission, by locally evaluating the binding of a large library of real patient-derived CDR3 sequences (different patients from a different study) to known auto-antigens in SLE and choosing the binders with the highest scores. The minimal distances between the patients/volunteers from Zaslavsky et al. and the auto-CDR3 library were generated using Levenshtein distances, a form of pair-wise alignment for sequence comparisons (Berger et al., 2021). 

The pre-processed data present in this repository consists of all the unique CDR3 sequences present in each sample library (patients and volunteers), the number of times that particular CDR3 sequence appeared in that particular sample, and the smallest distance between that sequence and any auto-CDR3 in our library. The files are in tsv (tab-separated values) format, but they are in fact separated by commas, and the columns are ordered as "distance, frequency, CDR3 sequence". While 10 healthy volunteer libraries and 10 SLE patient libraries have been included in this repository, and should thus suffice for the creation of Figure 3C, the full submission of this project will contain 50 samples from each group. The original unprocessed (raw) samples were of sizes in the range 500MB-5GB, which is why the preprocessed ones were instead included in this example analysis due to their pruned small sizes compatible with flexible analytical methods (ranging from 200KB-2MB).

Maxim E. Zaslavsky et al. ,Disease diagnostics using machine learning of B cell and T cell receptor sequences.Science387,eadp2407(2025).DOI:10.1126/science.adp2407

B. Berger, M. S. Waterman, and Y. W. Yu, “Levenshtein Distance, Sequence Comparison and Biological Database Search,” IEEE Trans Inf Theory, vol. 67, no. 6, pp. 3287–3294, Jun. 2021, doi: 10.1109/tit.2020.2996543.

**FOLDER STRUCTURE**
With the exception of this README.md file and two repo maintenance files (.gitattributes and .gitignore), this repository is split into three main directories:

-> **Code_Scripts**: This directory contains the Python code script used in the generation of Figure 3C of the final report from the preprocessed data presented elsewhere in this repository. While other scripts used to preprocess the data and produce the other accompanying figures will be included in this directory in future iterations, the current script hosted is illustratively named "boxplot_figure_440.py".

-> **Data_Files** This directory contains the pre-processed datasets used to prepare Figure 3C, but which were in fact used for many other purposes in this project, including training and testing the logistic regression and Random Forest classifiers. This directory leads to a split between two sub-directories: SLE_patient_samples, which accordingly hosts 10 datasets (one for each SLE patient), and healthy_patient_samples, which hosts 10 other datasets (one for each healthy volunteer). Each dataset is a TSV file and contains thousands of rows for three columns: "distance, frequency, CDR3 sequence". Note that the original numerical donor ID from which each sample was collected can be extracted from the names of the corresponding dataset files. Also note that each directory contains the maintenance .gitattributes file, which should be taken into consideration when running loops of code that iterate through every file name with the expectation that they are all the donor tsv libraries.

-> **Figure Plots**: This directory contains the panel that became Figure 3C of the final report, in png format (as produced through the coding script). from the preprocessed data presented elsewhere in this repository. While other panels used to compose the final project figures will be included in this directory in future iterations, the current figure hosted is illustratively named "healthy_lupus_distaances_boxplot".

**INSTALLATION**
The provided script can be executed by first cloning the entire repository to a local directory, navigating to the local directory, and then using the Command Line with "python ./Code_Scripts/boxplot_figure_440.py. Using the pipreqs command, the packages and their versions important for this code were extracted to be:
matplotlib==3.8.0
numpy==2.2.4
pandas==2.2.3
seaborn==0.13.2
python==3.11.7
Alternatively, the code script can be executed in an IDE like Virtual Studio Code or Spyder.
