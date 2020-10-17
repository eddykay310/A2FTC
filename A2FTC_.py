import os
from Bio import SeqIO
import shutil
import subprocess
import webbrowser


# Converts files from abi to fasta
baseDIR = os.getcwd()
homeDIR = os.getcwd()
sourcefiles = os.listdir(homeDIR)
destinationpath = f"{homeDIR}\FASTA"
folders = []

def abi2Fasta(folders):
    
    for homeDIR in folders:
        counter = 0
        
        for filename in os.listdir(homeDIR):
            
            if filename.endswith(".ab1"):
                # print(filename)
                count = SeqIO.convert(f"{homeDIR}\\{filename}", "abi", f"{homeDIR}\\{filename}.fasta", "fasta")
                counter+=1
        print (f"\n\n####### {counter} files were converted #########")

        # Moves fasta files to created FASTA folder
        if not os.path.exists(f"{homeDIR}/FASTA"):
            os.makedirs(f"{homeDIR}/FASTA")

        destinationpath = f"{homeDIR}\FASTA"
        # print(destinationpath)

        for file in os.listdir(homeDIR):
            # print(file)
            if file.endswith('.fasta'):
                shutil.move(os.path.join(homeDIR,file), os.path.join(destinationpath,file))
        print("\n\n###### FASTA files moved to FASTA folder #######")

# Combines single fasta files in to a single combined fasta file. This is if the files have been grouped to your liking else use the sort_cons.py file
def combineFasta(folders):

    for homeDIR in folders:
        DIR = f"{homeDIR}\FASTA"

        if not os.path.exists(f"{homeDIR}\combined_fasta_file.fasta"):
            cff = open(f"{homeDIR}\combined_fasta_file.fasta", 'w')

            for file in os.listdir(DIR):
                sff = open(os.path.join(DIR, file))
                for line in sff:
                    cff.write(line)
                sff.close()
            cff.close()
        print("\n\n######## FASTA files combined into a single file #######")

def runTRF(baseDIR,folders):

    # Runs tandem repeat finder program with set parameters
    for DIR in folders:

        fileDIR = fr'{baseDIR}\\trf409.dos64.exe'
        subprocess.call([fileDIR,f"{DIR}\combined_fasta_file.fasta","2", "7", "7", "80", "10", "50", "2000"])

        # Moving html files to web_results folder
        if not os.path.exists(f"{DIR}/web_results"):
            os.makedirs(f"{DIR}/web_results")

        resultssourcefiles = os.listdir(baseDIR)
        resultsdestinationpath = f"{DIR}\web_results"

        for file in resultssourcefiles:
            if file.endswith('.html'):
                shutil.move(os.path.join(baseDIR,file), os.path.join(resultsdestinationpath,file))

         # Opens summary html with default browser
        for item in os.listdir(f"{DIR}\web_results"):
            if item.endswith(".summary.html"):
                filepath = f"{DIR}\web_results\{item}"
                print(filepath)
                webbrowser.open('file:///' + filepath.replace(os.sep, '/'))

    print("\n\n###### Results files moved to FASTA folder #######\n")







