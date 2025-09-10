import os
import csv

# Define source and destination folders
source_folder = "c:/TV"
destination_folder = "c:/TV_com"
os.makedirs(destination_folder, exist_ok=True)

# Define the range of feature indexes to retain (1-17 and 4124-4125) and their names
feature_names = {
    1: "Shot_Length",
    2: "Motion_Distribution_Mean",
    3: "Motion_Distribution_Variance",
    4: "Frame_Diff_Distribution_Mean",
    5: "Frame_Diff_Distribution_Variance",
    6: "Short_Time_Energy_Mean",
    7: "Short_Time_Energy_Variance",
    8: "ZCR_Mean",
    9: "ZCR_Variance",
    10: "Spectral_Centroid_Mean",
    11: "Spectral_Centroid_Variance",
    12: "Spectral_Roll_Off_Mean",
    13: "Spectral_Roll_Off_Variance",
    14: "Spectral_Flux_Mean",
    15: "Spectral_Flux_Variance",
    16: "Fundamental_Frequency_Mean",
    17: "Fundamental_Frequency_Variance",
    4124: "Edge_Change_Ratio_Mean",
    4125: "Edge_Change_Ratio_Variance"
}

# Sort the feature names by index for consistent column order
sorted_feature_indexes = sorted(feature_names.keys())

# Process each file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".txt"):
        input_path = os.path.join(source_folder, filename)
        output_path = os.path.join(destination_folder, filename.replace(".txt", ".csv"))
        
        with open(input_path, "r") as infile, open(output_path, "w", newline='') as outfile:
            writer = csv.writer(outfile)
            
            # Write header for CSV file
            header = ["label"] + [feature_names[i] for i in sorted_feature_indexes]
            writer.writerow(header)
            
            for line in infile:
                # Extract label and features
                parts = line.strip().split()
                label = parts[0]
                features = parts[1:]
                
                # Filter and retain only specified features
                filtered_features = {int(index): value for index, value in (f.split(":") for f in features)
                                     if int(index) in feature_names}
                
                # Ensure all 18 features + label are present, fill missing with 0.0
                row = [label] + [filtered_features.get(i, "0.0") for i in sorted_feature_indexes]
                
                # Write the processed row to CSV
                writer.writerow(row)

print(f"Processed files saved in {destination_folder}.")
