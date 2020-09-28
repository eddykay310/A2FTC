import tkinter as tk 
from tkinter import filedialog, Text
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
    for homeDIR in folders:

        fileDIR = fr'{baseDIR}\\trf409.dos64.exe'
        subprocess.call([fileDIR,f"{homeDIR}\combined_fasta_file.fasta","2", "7", "7", "80", "10", "50", "2000"])

        # Opens summary html with default browser
        for file in os.listdir(homeDIR):
            if file.endswith(".summary.html"):
                filepath = os.path.realpath(file)
                webbrowser.open('file://' + filepath)

        # Moving html files to web_results folder
        if not os.path.exists(f"{homeDIR}/web_results"):
            os.makedirs(f"{homeDIR}/web_results")

        resultssourcefiles = os.listdir(baseDIR)
        resultsdestinationpath = f"{homeDIR}\web_results"

        for file in resultssourcefiles:
            if file.endswith('.html'):
                shutil.move(os.path.join(baseDIR,file), os.path.join(resultsdestinationpath,file))

    print("\n\n###### Results files moved to FASTA folder #######\n")

def delselfol(folders):
    # Deleting redundant files
    # for homeDIR in folders:
    #     sourcefiles = os.listdir(homeDIR)
        # for file in sourcefiles:
        #     if file.endswith('.ab1'):
        #         os.remove(os.path.join(homeDIR,file))
    for widget in tleftframe.winfo_children():
        widget.destroy()
    
    folders.clear()
        
                
    # shutil.rmtree(f"{homeDIR}\\FASTA")  
    print("####### Deleting selected folders ########\n")

    # print ('''
    #         This program can only be run once in the present folder.\n
    #         To run it again, the FASTA and web_results folder, and the
    #         combined_fasta_file.fasta file must be deleted.\n
    #         ######################################################\n
    #         The combined_fasta_file.fasta file contains all your sequences in fasta format
    #         and tandem repeat finder results can be found in the web_results folder.
    #         Use the first file (the summary file) in the web_results folder to navigate thorough your results.

    #         ''')

def abiFolders(homeDIR):
    for widget in tleftframe.winfo_children():
        widget.destroy()

    folderName = filedialog.askdirectory(initialdir=homeDIR,title="Select Folder")
    if folderName != "":
        folders.append(folderName)

    for folder in folders:
        folderlabel = tk.Label(tleftframe,text=folder,bg="gray")
        folderlabel.pack()

############################################################################################
home = os.getcwd()
if not os.path.exists(f"{home}/all_FASTA"):
    os.makedirs(f"{home}/all_FASTA")

seqfolder_list = ["AM-2","AM-3","AM-4","AM-5"]
group = ["A","B","C","D","E","F","G","H"]
grouped_filesDIR = []
bfolders = []

def botabiFolders(home):
    for widget in bleftframe.winfo_children():
        widget.destroy()

    folderName = filedialog.askdirectory(initialdir=home,title="Select Folder")
    if folderName != "":
        bfolders.append(folderName)

    for folder in bfolders:
        folderlabel = tk.Label(bleftframe,text=folder,bg="gray")
        folderlabel.pack()

def sortFiles(seqfolder_list,home,group):
    i=0
    temp=[]

    # Copys files in to one folder
    for folder in seqfolder_list:
        if not os.path.exists(home):
            os.makedirs(f"{home}/all_FASTA")     
            for file in os.listdir(f"{home}/{folder}/FASTA"):
                if file.endswith(".fasta"):
                    shutil.copy(os.path.join(f"{home}/{folder}/FASTA",file),f"{home}/all_FASTA")

    # Sorting files into subfolders
    for i in range(len(group)):
        for file in os.listdir(f"{home}/all_FASTA"):
            if i<len(group) and file.endswith(f"{group[i]}.ab1.fasta"):
                temp.append(os.path.join(f"{home}\\all_FASTA",file))
        if i<len(group) and not os.path.exists(f"{home}/all_FASTA/{group[i]}"):
            os.makedirs(f"{home}/all_FASTA/{group[i]}")
            for path in temp: 
                shutil.move(path,f"{home}\\all_FASTA\\{group[i]}")
            i+=1
        temp.clear()
    print("######## Files sorted into folders #########\n")

    # Getting grouped files directory into list
    for rootDIR, directory, files in os.walk(f"{home}\\all_FASTA"):
        grouped_filesDIR.append(rootDIR)
    return grouped_filesDIR

def consolidateFasta(grouped_filesDIR):
    # Consolidating fasta files
    for DIR in grouped_filesDIR[1:]:
        cff = open(f'{DIR}_combined_fasta_files.fasta', 'w')
        for file in os.listdir(DIR):
            sff = open(os.path.join(DIR, file))
            for line in sff:
                cff.write(line)
            sff.close()
        cff.close()
    print("######## FASTA files combined into a single file based on groups #######")

def deltrfFiles(seqfolder_list):
    # Deleting files created by tandem repeat analysis
    print("######## Deleting folders created by the tandem repeat analysis #########\n")
    for folder in seqfolder_list:
        shutil.rmtree(folder)

###################################################################################################
root = tk.Tk()
root.title("ABI-2-FASTA-consolidator ")
# root.iconbitmap("to_do_list_apps.ico")
root.geometry('800x600')

introinfo = tk.Label(root,text="Find explanation on how to use this progam at this github rpepository (https://github.com/eddykay310/ABI-2-FASTA-consolidator)")
introinfo.pack()
downlabel = tk.Label(root,text="Copyright (c) 2020, A2FtC. All rights reserved.")
downlabel.place(relwidth=0.9,relheight=0.05,relx=0.05,rely=0.94)

topframe = tk.Frame(root,bg="#c2beba")
topframe.place(relwidth=0.9,relheight=0.4,relx=0.05,rely=0.08)
bottomframe = tk.Frame(root,bg="#c2beba")
bottomframe.place(relwidth=0.9,relheight=0.4,relx=0.05,rely=0.51)

trightframe = tk.Frame(topframe,bg="#c2beba")
trightframe.place(relwidth=0.25,relheight=0.8,relx=0.725,rely=0.05)
tleftframe = tk.Frame(topframe,bg="white")
tleftframe.place(relwidth=0.65,relheight=0.9,relx=0.025,rely=0.05)

brightframe = tk.Frame(bottomframe,bg="#c2beba")
brightframe.place(relwidth=0.25,relheight=0.6,relx=0.725,rely=0.05)
bleftframe = tk.Frame(bottomframe,bg="white")
bleftframe.place(relwidth=0.65,relheight=0.7,relx=0.025,rely=0.2)

distcharlab = tk.Label(bottomframe,text="Distinct label")
distcharlab.place(relwidth=0.15,relheight=0.1,relx=0.025,rely=0.05)
distchar = tk.Entry(bottomframe)
distchar.place(relwidth=0.495,relheight=0.1,relx=0.18,rely=0.05)

choose = tk.Button(trightframe,text="Choose Folders",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:abiFolders(baseDIR))
choose.pack()
a2f = tk.Button(trightframe,text="ABI->FASTA",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:abi2Fasta(folders))
a2f.pack()
combineFASTA = tk.Button(trightframe,text="Combine FASTA",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:combineFasta(folders))
combineFASTA.pack()
trf = tk.Button(trightframe,text="Tandem Repeat Finder",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:runTRF(baseDIR,folders))
trf.pack()
dbf = tk.Button(trightframe,text="Delete Base Files",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:delselfol(folders))
dbf.pack()

bchoose = tk.Button(brightframe,text="Choose Folders",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:botabiFolders(home))
bchoose.pack()
sortFASTA = tk.Button(brightframe,text="Sort FASTA Files",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:sortFiles(seqfolder_list,home,group))
sortFASTA.pack()
scombineFASTA = tk.Button(brightframe,text="Combine FASTA",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:consolidateFasta(grouped_filesDIR))
scombineFASTA.pack()
deltrf = tk.Button(brightframe,text="Delete TRF Files",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:deltrfFiles(seqfolder_list))
deltrf.pack()

tleftframelabel = tk.Label(tleftframe,anchor='nw',justify='left',)
tleftframelabel.pack()



root.mainloop()