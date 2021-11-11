import camelot
import pandas as pd
import sys
import os
import glob

file = ""
# Check for command line args, use included PDF as default
if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "Test_Parse.pdf"

# extract all the tables in the PDF file
tables = camelot.read_pdf(file)


# number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
for i in range(0, len(tables)):
    print(tables[i].df)

# Export tables to csv
tables.export("./output_files/output.csv", f="csv")

# Combine output CSVs
os.chdir('./output_files')
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')