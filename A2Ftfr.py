import os
from Bio import SeqIO
import shutil
import subprocess
import webbrowser


# Converts files from abi to fasta
homeDIR = os.getcwd()
counter = 0

for filename in os.listdir(homeDIR):
    if filename.endswith(".ab1"):
        count = SeqIO.convert(filename, "abi", f"{filename}.fasta", "fasta")
        counter+=1
print (f"####### {counter} files were converted #########")

# Moves fasta files to created FASTA folder
os.makedirs(f"{homeDIR}/FASTA")
sourcefiles = os.listdir(homeDIR)
destinationpath = f"{homeDIR}\FASTA"

for file in sourcefiles:
    if file.endswith('.fasta'):
        shutil.move(os.path.join(homeDIR,file), os.path.join(destinationpath,file))
print("###### FASTA files moved to FASTA folder #######")

# Combines single fasta files in to a single combined fasta file. This is if the files have been grouped to your liking else use the sort_cons.py file
DIR = f"{homeDIR}\FASTA"
cff = open('combined_fasta_file.fasta', 'w')

for file in os.listdir(DIR):
    sff = open(os.path.join(DIR, file))
    for line in sff:
        cff.write(line)
    sff.close()
cff.close()
print("######## FASTA files combined into a single file #######")

# Runs tandem repeat finder program with set parameters
fileDIR = fr'{homeDIR}\\trf409.dos64.exe'
subprocess.call([fileDIR,"combined_fasta_file.fasta","2", "7", "7", "80", "10", "50", "2000"])

# Opens summary html with default browser
for file in sourcefiles:
    if file.endswith('.summary.html'):
        filepath = os.path.realpath(file)
        webbrowser.open('file://' + filepath)

# Moving html files to web_results folder
os.makedirs(f"{homeDIR}/web_results")
ssourcefiles = os.listdir(homeDIR)
sdestinationpath = f"{homeDIR}\web_results"

for file in ssourcefiles:
    if file.endswith('.html'):
        shutil.move(os.path.join(homeDIR,file), os.path.join(sdestinationpath,file))
print("###### FASTA files moved to FASTA folder #######\n")

# Deleting redundant files
for file in sourcefiles:
    if file.endswith('.html') or file.endswith('.fasta'):
        os.remove(os.path.join(homeDIR,file))
              
shutil.rmtree(f"{homeDIR}\\FASTA")  
print("####### Deleting redundant files ########\n")

print ('''
            This program can only be run once in the present folder.\n
            To run it again, the FASTA and web_results folder, and the
            combined_fasta_file.fasta file must be deleted.\n
            ######################################################\n
            The combined_fasta_file.fasta file contains all your sequences in fasta format
            and tandem repeat finder results can be found in the web_results folder.
            Use the first file (the summary file) in the web_results folder to navigate thorough your results.

            ''')





