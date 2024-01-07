import pandas as pd
import numpy as np


def load_data(df, df_import, col_name_set, label):
    for idx, (column_name, column_content) in enumerate(df_import.items()):
        df.loc[label + col_name_set[idx]] = column_content.to_numpy()
    return df


def load_set_of_data(df, label_set, file_set, file_loc):
    for idx in range(len(label_set)):
        label = label_set[idx]
        filename = file_set[idx]
        df_import = pd.read_csv(file_loc + filename + ".csv")
        df = load_data(df, df_import, col_name_set, label)
        print("File: ", filename, "loaded.")
    return df


# Data description
col_name_set = [
    ("S1", "Left"),
    ("S2", "Left"),
    ("S3", "Left"),
    ("S4", "Left"),
    ("S5", "Left"),
    ("S6", "Left"),
    ("S7", "Left"),
    ("S8", "Left"),
    ("S9", "Left"),
    ("S10", "Left"),
    ("S11", "Left"),
    ("S12", "Left"),
    ("S13", "Left"),
    ("S14", "Left"),
    ("S15", "Left"),
    ("S16", "Left"),
    ("S17", "Left"),
    ("S1", "Right"),
    ("S2", "Right"),
    ("S3", "Right"),
    ("S4", "Right"),
    ("S5", "Right"),
    ("S6", "Right"),
    ("S7", "Right"),
    ("S8", "Right"),
    ("S9", "Right"),
    ("S10", "Right"),
    ("S11", "Right"),
    ("S12", "Right"),
    ("S13", "Right"),
    ("S14", "Right"),
    ("S15", "Right"),
    ("S16", "Right"),
    ("S17", "Right"),
]
label_set = [
    ("Hip", "Ortho"),
    ("Knee", "Ortho"),
    ("Ankle", "Ortho"),
    ("Hip", "NoOrtho"),
    ("Knee", "NoOrtho"),
    ("Ankle", "NoOrtho"),
]
file_loc = "../data/caren_gait_analysis_data/"
file_set = [
    "hip_ortho",
    "knee_ortho",
    "ankle_ortho",
    "hip_no_ortho",
    "knee_no_ortho",
    "ankle_no_ortho",
]


# Create a DataFrame with the multi-index and 101 columns for the time series data
joint_levels = ["Hip", "Knee", "Ankle"]
orthosis_levels = ["Ortho", "NoOrtho"]
subject_levels = ["S{}".format(i) for i in range(1, 18)]
side_levels = ["Left", "Right"]

multi_index = pd.MultiIndex.from_product(
    [joint_levels, orthosis_levels, subject_levels, side_levels],
    names=["Joint", "Orthosis", "Subject", "Side"],
)

gait_df = pd.DataFrame(index=multi_index, columns=["T" + str(i) for i in range(101)])

# Load data
load_set_of_data(gait_df, label_set, file_set, file_loc)

# Preview data
gait_df.head(40)

# Save data
gait_df.to_pickle("../data/caren_gait_analysis_data/gait_ortho.pkl")
print("Saved to pickle.")
