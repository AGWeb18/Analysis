import pandas as pd
import Levenshtein

file = "tracking_codes4.csv"
fuzzy_df = pd.read_csv(file)

df = fuzzy_df["Event"]
df.replace("([\W+])","",regex=True, inplace=True)
fuzzy_df["Event"] = df.str.lower()
fuzzy_df.Event.sort_values()
fuzzy_df.Event.str.strip()


distance_df = fuzzy_df[["Event","Count"]]
distance_df = distance_df.iloc[:-1,:]
tracking_codes = ["adj", "mobs", "std","6100","bronte","sherb","ib"]

def create_df_tracking(df, track_code):
    track_name = str(track_code) + "-frame"
    track_count = str(track_code) + "-Count"
    track_name = df.Event.str.contains(str(track_code))
    track_count = df[track_name].Count.sum()
    return (df[track_name], "The count of " + str(track_code) + " is: " + str(track_count))
    



for i in tracking_codes:
    output = create_df_tracking(distance_df, i)
    print(output[0])
    print(output[1])
    print("="*40)


#distance_df.to_csv("editdistance_trackingcodes3.csv")
