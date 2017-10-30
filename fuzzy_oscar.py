import pandas as pd
import Levenshtein
import re

file = "tracking_codes4.csv"
fuzzy_df = pd.read_csv(file)

df = fuzzy_df["Event"]
df.replace("([\W+])","",regex=True, inplace=True)
fuzzy_df["Event"] = df.str.lower()
fuzzy_df.Event.sort_values()
fuzzy_df.Event.str.strip()

l= []

for i in range(0, len(df)-1):
    curr_row = df[i]
    nxt_row = df[i+1]
    dist = Levenshtein.distance(str(curr_row), str(nxt_row))
    l.append(dist)

l.append(-999)
fuzzy_df["Distance"] = l

distance_df = fuzzy_df[["Event","Count","Distance"]]
distance_df = distance_df.iloc[:-1,:]
tracking_codes = ["adj", "mobs", "6100","bronte"]

def create_df_tracking(df, track_code):
    track_name = str(track_code) + "-frame"
    track_count = str(track_code) + "-Count"
    track_name = df.Event.str.contains(str(track_code))
    track_count = df[track_name].Count.sum()
    return ("The count of " + str(track_code) + " is: " + str(track_count))
    



for i in tracking_codes:
    output = create_df_tracking(distance_df, i)
    print(output)



#distance_df.to_csv("editdistance_trackingcodes3.csv")
