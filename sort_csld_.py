import shutil, os


home = os.getcwd()
seqfolder_list = []
group = []
all_fasta = os.path.join(home, "all_FASTA")
grouped_filesDIR = []
bfolders = []

def sortFiles(seqfolder_list,home,group):
    i=0
    temp=[]

    if not os.path.exists(all_fasta):
        os.makedirs(all_fasta)

    # Copying files in to one folder
    print("\nCopying FASTA files to all_FASTA folder")
    try:
        for folder in seqfolder_list:
            for file in os.listdir(fr"{home}\\{folder}\\FASTA"):
                if file.endswith(".fasta"):
                    shutil.copy(os.path.join(f"{home}/{folder}/FASTA",file),f"{home}/all_FASTA")
    except Exception as e:
        print(e)

    # Sorting files into subfolders
    try:
        for i in range(len(group)):
            print("Sorting group",group[i])
            for file in os.listdir(os.path.join(home,"all_FASTA")):
                if i<len(group) and file.endswith(f"{group[i]}.ab1.fasta"):
                    temp.append(os.path.join(f"{home}\\all_FASTA",file))
            if i<len(group) and not os.path.exists(f"{home}/all_FASTA/{group[i]}/FASTA"):
                os.makedirs(f"{home}/all_FASTA/{group[i]}/FASTA")
                for path in temp: 
                    shutil.move(path,f"{home}\\all_FASTA\\{group[i]}\\FASTA")
                i+=1
            temp.clear()
        print("\nFiles sorted into folders\n")
    except Exception as e:
        print(e)

def consolidateFasta(grouped_filesDIR):

    #  Getting grouped files directory into list
    for folder in os.listdir(all_fasta):
        print(folder)
        if os.path.isdir:
            grouped_filesDIR.append(os.path.join(all_fasta,folder))
    print("\nFolders found:", grouped_filesDIR)

    # Consolidating fasta files
    for folder in grouped_filesDIR:
        print("combining FASTA files in:",folder)
        DIR = os.path.join(folder, "FASTA")
        combined_fasta_dir = os.path.join(folder, "combined_fasta_file.fasta")
        cff = open(combined_fasta_dir, 'w')

        for file in os.listdir(DIR):
            sff = open(os.path.join(DIR, file))
            for line in sff:
                cff.write(line)
            sff.close()
        cff.close()

