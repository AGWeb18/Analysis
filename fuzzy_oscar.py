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


# case specific, word matching 
distance_df = distance_df.iloc[:-1,:]
frame = distance_df.Event.str.contains(("adj" or "ajd"))
adj_df = distance_df[frame]
adj_sum = adj_df.Count.sum()
print(adj_df)
print("The count of ADJ events to occur is:" + str(adj_sum))


frame_mobs = distance_df.Event.str.contains("mobs")
mobs_df = distance_df[frame_mobs]
mobs_sum = mobs_df.Count.sum()
print("=" *40)
print(mobs_df)
print("The count of MOBS events to occur is:" + str(mobs_sum))


#distance_df.to_csv("editdistance_trackingcodes3.csv")
