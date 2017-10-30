from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

file = "tracking_codes4.csv"
fuzzy_df = pd.read_csv(file)

df = fuzzy_df["Event"]
df.replace("([\W+])","",regex=True, inplace=True)

l= []

for i in range(0, len(df)-1):
    curr_row = df[i]
    nxt_row = df[i+1]
    dist = fuzz.ratio(str(curr_row), str(nxt_row))
    l.append(dist)

l.append(-999)
fuzzy_df["Distance"] = l

distance_df = fuzzy_df[["Event","Count","Distance"]]

print(distance_df.head())
distance_df.to_csv("editdistance_trackingcodes3.csv")
