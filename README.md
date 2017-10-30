# Analysis
- Use for all work-related analysis

#  tracking_codes4.csv -- Details
- This is the input file to fuzzy_oscar.py
- Contains a count of unique key where the value is the number of occurences of that code over the selected period. 
- This data contains the results of the 2016 data only. 

#  fuzzy_oscar.py -- Details
- The objective of this script involves finding event codes which are exact/close matches (defined by an edit distance <=2) and 
creating a count for each of the tracking codes. 
- Once the low level count is created, I've defined a function which will search and sum the count of keys which contain valuable strings. 
- For example: the "adj" key is important to count, however, the 'bronte' count may include results from the 'adj' key. 


#  editdistance_trackingcodes3.csv -- Details
- This is the output of the fuzzy oscar script.
- Currently, this file contains both the individualized count as well as the edit distance calculated. 
- Due to the low number of finite tracking codes, it may be better to create a map to look up against than to rely on fuzzy matching. 
