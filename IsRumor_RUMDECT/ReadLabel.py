# Author: Hong Sheng Liu
# Date: 2023-05-24
# Version: 1.0
import pandas as pd
import os
import re
import xlrd
# Read the data from the Excel file, with the first line being the column name
excel_data = pd.read_excel('D:\MachineLearning\IsRumor\output.xlsx', sheet_name='Sheet1', header=0)

result_data = []

# Open the txt file and read the data line by line
with open(r'E:\Rumor\weibo\rumdect\Weibo.txt', 'r') as txt_file:
    for line in txt_file:
        # Regularly match each row to find the required information
        match_obj = re.findall(r'eid:(\d+)\s+label:(\d+)', line)
        if match_obj:
            eid = match_obj[0][0]
            label = match_obj[0][1]
            # Save results in a list
            result_data.append(label)

# Write the results to excel_data’s label column
for i in range(0,len(excel_data)):
    label = result_data[i]
    excel_data.at[i, "label"] = str(label)

# Write the results back to the original Excel file
excel_data.to_excel('D:\MachineLearning\IsRumor\output.xlsx', index=False)