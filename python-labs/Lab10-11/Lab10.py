import re
import os 

target_folder = 'insulin-seq-clean'

if not os.path.exists(target_folder):
    os.makedirs(target_folder)
    print(f"Created new folder: {target_folder}")

with open("preproinsulin-seq.txt", "r") as infile:
    raw_data = infile.read()
    
cleaned_data = re.sub(r'ORIGIN|\d|\/|\s+','',raw_data)

print(f"Total cleaned sequence: {len(cleaned_data)} characters")
lsinsulin = cleaned_data[0:24]
binsulin = cleaned_data[24:54]
cinsulin = cleaned_data[54:89]
ainsulin = cleaned_data[89:110]

insulin_clean_files ={
    'preproinsulin-seq-clean.txt': cleaned_data,
    'lsinsulin-seq-clean.txt': lsinsulin,
    'binsulin-seq-clean.txt': binsulin,
    'cinsulin-seq-clean.txt': cinsulin,
    'ainsulin-seq-clean.txt': ainsulin,
}
for filename, sequence in insulin_clean_files .items():
    full_path = os.path.join(target_folder, filename)

    with open(full_path, 'w') as outfile:
        outfile.write(sequence)
        
    print(f"Saved {len(sequence)} characters to: {full_path}")