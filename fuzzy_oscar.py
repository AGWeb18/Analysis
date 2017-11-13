import pandas as pd
import tkinter as tk
from tkinter import Label
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import os
import time

wb = Workbook()
ws = wb.active

file = r"Input Files - FuzzyMatchGUI/tracking_codes_nov.csv"
fuzzy_df = pd.read_csv(file, index_col=False)
df = fuzzy_df["Event"]
df.replace("([\W+])","",regex=True, inplace=True)
df.str.strip()
df.drop_duplicates(keep='last')
fuzzy_df["Event"] = df.str.lower()
fuzzy_df[["Event", "Count"]]
fuzzy_df = fuzzy_df.iloc[:,1:]

root = tk.Tk()

def create_df_tracking(_df, track_code):
    track_name = _df.Event.str.contains(str(track_code), na=False)
    track_count = _df[track_name].Count.sum()
    return (_df[track_name], "The count of " + str(track_code) + " is: " + str(track_count))
    
    


class CountApp(tk.Frame):
    ''' An app built to visualize the output of the Oscar code counts.'''
    def __init__(self, master):
        tk.Frame.__init__(self,
                          master,
                          width=500,
                          height=500)
        #  Set the title
        self.master.title("Oscar Code Count")

        #  This allows the size specification to take effect
        self.pack_propagate(0)

        # We'll use the flexible pack layout manager
        self.pack()

        #   The greeting selector
        #   Use a StringVar to access the selectors value
        self.greeting_var = tk.StringVar()
        self.greeting = tk.OptionMenu(self,
                                      self.greeting_var,
                                      "adj", "mobs")
        self.greeting_var.set('adj')


        #   The go button
        self.go_button = tk.Button(self, text="Go",
                                   command=self.printSomething)
        self.export_button = tk.Button(self, text="Export",
                                       command=self.exportSomething)

        #  The label
        self.label = tk.Label(self)
                                   
        #   Put the controls on the form
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.greeting.pack(fill=tk.X, side=tk.TOP)
        self.export_button.pack(fill=tk.X, side=tk.BOTTOM)

        
    
    def printSomething(self):
        global temp_output
        temp_output = create_df_tracking(fuzzy_df, self.greeting_var.get())
        
        label = Label(text= '%s, \n\n %s' % (temp_output[0], temp_output[1]))
        #this creates a new label to the GUI
        label.place(relx=0.5, rely=0.5, anchor='center',bordermode='outside',relheight=0.8, relwidth=0.50)

    def exportSomething(self):
        temp_df = pd.DataFrame(temp_output[0])
        #   Append dataframe to xlsx
        for r in dataframe_to_rows(temp_df, index=False, header=True):
            ws.append(r)
        wb.save("Output Files - FuzzyMatchGUI/CodeCountExport.xlsx")
        label_export = Label(text="Successfully Exported to XLSX to: "+str(os.getcwd()))
        label_export.pack(fill = tk.X, side=tk.BOTTOM)

    
    def run(self):
        ''' Run the app '''
        self.mainloop()


app = CountApp(root)
app.run()
