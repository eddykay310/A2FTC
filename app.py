import tkinter as tk
from tkinter import filedialog, Text, Scrollbar, Listbox
import os
import shutil
import A2FTC_
import sort_csld_
import csv_maker


baseDIR = os.getcwd()
# homeDIR = A2FTC_.homeDIR
# sourcefiles = A2FTC_.sourcefiles
# destinationpath = A2FTC_.destinationpath

def delselfol(folders):
    # Deleting redundant files
    # for homeDIR in folders:
    #     sourcefiles = os.listdir(homeDIR)
        # for file in sourcefiles:
        #     if file.endswith('.ab1'):
        #         os.remove(os.path.join(homeDIR,file))
    for widget in tleftframe.winfo_children():
        widget.destroy()
    for widget in bleftframe.winfo_children():
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

    while True:
        folderName = filedialog.askdirectory(
            initialdir=homeDIR, title="Select Folder")
        if not folderName:
            break
        else:
            folders.append(folderName)

    for folder in folders:
        folderlabel = tk.Label(tleftframe, text=folder, bg="gray")
        folderlabel.pack()

############################################################################################
home = sort_csld_.home
seqfolder_list = sort_csld_.seqfolder_list
group = sort_csld_.group
grouped_filesDIR = sort_csld_.grouped_filesDIR
bfolders = sort_csld_.bfolders

def botabiFolders(home):
    for widget in bleftframe.winfo_children():
        widget.destroy()

    folderName = filedialog.askdirectory(initialdir=home,title="Select Folder")
    if folderName != "":
        bfolders.append(folderName)

    for folder in bfolders:
        folderlabel = tk.Label(bleftframe,text=folder,bg="gray")
        folderlabel.pack()

def deltrfFiles(seqfolder_list):
    # Deleting files created by tandem repeat analysis
    print("######## Deleting folders created by the tandem repeat analysis #########\n")
    for folder in seqfolder_list:
        shutil.rmtree(folder)

###################################################################################################
root = tk.Tk()
root.title("ABI-2-FASTA-consolidator ")
# root.iconbitmap("favicon.ico")
root.geometry('800x600')

foldersub = []
if os.path.isfile("previous_opened_folders.txt"):
    with open("previous_opened_folders.txt", "r") as f:
        prev_folders = f.read()
        prev_folders = prev_folders.split(",")
        foldersub = [item for item in prev_folders if item.strip()]
        f.close()
folders = foldersub

introinfo = tk.Label(root,text="Find explanation on how to use this progam at this github repository (https://github.com/eddykay310/ABI-2-FASTA-consolidator)")
introinfo.pack()
downlabel = tk.Label(root,text="Copyright (c) 2020, A2FTC. All rights reserved.")
downlabel.place(relwidth=0.9,relheight=0.05,relx=0.05,rely=0.94)

topframe = tk.Frame(root,bg="#c2beba")
topframe.place(relwidth=0.9,relheight=0.4,relx=0.05,rely=0.08)
bottomframe = tk.Frame(root,bg="#c2beba")
bottomframe.place(relwidth=0.9,relheight=0.4,relx=0.05,rely=0.51)

trightframe = tk.Frame(topframe,bg="#c2beba")
trightframe.place(relwidth=0.25,relheight=0.9,relx=0.725,rely=0.05)
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

scrollbarT = Scrollbar(tleftframe)
scrollbarT.pack( side = "right", fill = "y" )
scrollbarB = Scrollbar(bleftframe)
scrollbarB.pack( side = "right", fill = "y" )

choose = tk.Button(trightframe,text="Choose Folders",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:abiFolders(baseDIR))
choose.pack()
a2f = tk.Button(trightframe,text="ABI->FASTA",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:A2FTC_.abi2Fasta(folders))
a2f.pack()
combineFASTA = tk.Button(trightframe,text="Combine FASTA",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:A2FTC_.combineFasta(folders))
combineFASTA.pack()
trf = tk.Button(trightframe,text="Tandem Repeat Finder",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:A2FTC_.runTRF(baseDIR,folders))
trf.pack()
df_makerT = tk.Button(trightframe,text="Dataframe Maker",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:csv_maker.csvMaker(baseDIR, folders))
df_makerT.pack()
dbf = tk.Button(trightframe,text="Delete Selected Folders",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:delselfol(folders))
dbf.pack()

bchoose = tk.Button(brightframe,text="Choose Folders",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:botabiFolders(home))
bchoose.pack()
sortFASTA = tk.Button(brightframe,text="Sort FASTA Files",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:sort_csld_.sortFiles(seqfolder_list,home,group))
sortFASTA.pack()
scombineFASTA = tk.Button(brightframe,text="Combine FASTA",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:sort_csld_.consolidateFasta(grouped_filesDIR))
scombineFASTA.pack()
deltrf = tk.Button(brightframe,text="Delete TRF Files",padx=10,pady=6,bg="white",fg="#263D42",command=lambda:deltrfFiles(seqfolder_list))
deltrf.pack()

tleftframelabel = tk.Label(tleftframe,anchor='nw',justify='left',)
tleftframelabel.pack()

for folder in folders:
    folder_label = tk.Label(tleftframe,text=folder,bg="gray")
    folder_label.pack()

root.mainloop()

with open("previous_opened_folders.txt", "w") as f:
    for folder in folders:
        f.write(folder+",")
    f.close()
    