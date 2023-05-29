# Author: Hong Sheng Liu
# Date: 2023-05-24
# Version: 1.0
import pandas as pd
import re


# Define regular expression patterns containing URLs
url_pattern = re.compile(r'(https?://\S+)')

# Reading Excel Tables
df = pd.read_excel('D:\MachineLearning\IsRumor\output.xlsx')

# Find URLs in Text Columns
urls = []
for text in df['文本']:
    matches = re.findall(url_pattern, str(text))
    urls.append(matches)

# Write the number of URLs to a new colum
df['URL 数量'] = [len(lst) for lst in urls]


# Save Excel Table
df.to_excel('D:\MachineLearning\IsRumor\output.xlsx', index=False)