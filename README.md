# Analysis
- Python Scripts to parse and count strings matches. 

#  fuzzy_oscar.py -- Details
- The objective of this script involves parsing event codes and creating a count for each of the tracking codes. 
- You can search keywords to extract the count of codes from this list.
- Caveat: the "adj" key is important to count, however, the 'bronte' count may include results from the 'adj' key. 




#  Count of tracking codes -- Details
- This is the custom Excel sheet that is the output of the GUI-app. 
- The directory of this file is presented in the app as well. 


#  tracking_codes4.csv -- Details
- This is the input file to fuzzy_oscar.py
- Contains a count of unique key where the value is the number of occurences of that code over the selected period. 
- This data contains the results of the 2016 data only. 

#  editdistance_trackingcodes3.csv -- Details
- This is the output of the fuzzy oscar script.
- Currently, this file contains both the individualized count as well as the edit distance calculated. 
- Due to the low number of finite tracking codes, it may be better to create a map to look up against than to rely on fuzzy matching. 
