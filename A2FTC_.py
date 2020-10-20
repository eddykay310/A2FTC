import os
from Bio import SeqIO
import shutil
import subprocess
import webbrowser


# Converts files from abi to fasta
baseDIR = os.getcwd()
homeDIR = os.getcwd()
sourcefiles = os.listdir(baseDIR)
destinationpath = os.path.join(baseDIR, "FASTA")

def abi2Fasta(folders):
    
    for homeDIR in folders:
        counter = 0
        
        for filename in os.listdir(homeDIR):
            
            if filename.endswith(".ab1"):
                # print(filename)
                SeqIO.convert(os.path.join(homeDIR, filename), "abi", os.path.join(homeDIR, f"{filename}.fasta"), "fasta")
                counter+=1
        print (f"\n####### {counter} files were converted #########")

        # Moves fasta files to created FASTA folder
        destinationpath = os.path.join(homeDIR, "FASTA")
        # print(destinationpath)
        if not os.path.exists(destinationpath):
            os.makedirs(destinationpath)

        for file in os.listdir(homeDIR):
            # print(file)
            if file.endswith('.fasta'):
                shutil.move(os.path.join(homeDIR,file), os.path.join(destinationpath,file))
        print("\n###### FASTA files moved to FASTA folder #######")

# Combines single fasta files in to a single combined fasta file. This is if the files have been grouped to your liking else use the sort_cons.py file
def combineFasta(folders):

    for homeDIR in folders:
        DIR = os.path.join(homeDIR, "FASTA")
        combined_fasta_dir = os.path.join(homeDIR, "combined_fasta_file.fasta")
        cff = open(combined_fasta_dir, 'w')

        for file in os.listdir(DIR):
            sff = open(os.path.join(DIR, file))
            for line in sff:
                cff.write(line)
            sff.close()
        cff.close()
        print("\n######## FASTA files combined into a single file #######")

def runTRF(baseDIR,folders):

    # Runs tandem repeat finder program with set parameters
    for DIR in folders:

        fileDIR = fr'{baseDIR}\\trf409.dos64.exe'
        subprocess.call([fileDIR, os.path.join(DIR, "combined_fasta_file.fasta"),"2", "7", "7", "80", "10", "50", "2000"])

        # Moving html files to web_results folder
        web_results_dir = os.path.join(DIR, "web_results")
        if not os.path.exists(web_results_dir):
            os.makedirs(web_results_dir)

        resultssourcefiles = os.listdir(baseDIR)
        resultsdestinationpath = web_results_dir

        for file in resultssourcefiles:
            if file.endswith('.html'):
                shutil.move(os.path.join(baseDIR,file), os.path.join(resultsdestinationpath,file))

         # Opens summary html with default browser
        for item in os.listdir(web_results_dir):
            if item.endswith(".summary.html"):
                filepath = os.path.join(web_results_dir,item)
                # print(filepath)
                webbrowser.open('file:///' + filepath.replace(os.sep, '/'))

    print("\n###### Results files moved to FASTA folder #######\n")







