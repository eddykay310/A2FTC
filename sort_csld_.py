import shutil, os


home = os.getcwd()
all_fasta = os.path.join(home, "all_FASTA")

seqfolder_list = ["AM-2","AM-3","AM-4","AM-5"]
group = ["A","B","C","D","E","F","G","H"]
grouped_filesDIR = []
bfolders = []

def sortFiles(seqfolder_list,home,group):
    i=0
    temp=[]
    all_fasta = os.path.join(home, "all_FASTA")

    if not os.path.exists(home):
        os.makedirs(all_fasta)
    # Copys files in to one folder
    for folder in seqfolder_list:
        for file in os.listdir(fr"{home}\\{folder}\\FASTA"):
            if file.endswith(".fasta"):
                shutil.copy(os.path.join(f"{home}/{folder}/FASTA",file),f"{home}/all_FASTA")

    # Sorting files into subfolders
    for i in range(len(group)):
        for file in os.listdir(f"{home}/all_FASTA"):
            if i<len(group) and file.endswith(f"{group[i]}.ab1.fasta"):
                temp.append(os.path.join(f"{home}\\all_FASTA",file))
        if i<len(group) and not os.path.exists(f"{home}/all_FASTA/{group[i]}/FASTA"):
            os.makedirs(f"{home}/all_FASTA/{group[i]}/FASTA")
            for path in temp: 
                shutil.move(path,f"{home}\\all_FASTA\\{group[i]}\\FASTA")
            i+=1
        temp.clear()
    print("######## Files sorted into folders #########\n")

    # Getting grouped files directory into list
    for rootDIR, directory, files in os.walk(f"{home}\\all_FASTA"):
        grouped_filesDIR.append(rootDIR)
    return grouped_filesDIR

def consolidateFasta(grouped_filesDIR):
    # Consolidating fasta files
    if grouped_filesDIR:
        for DIR in grouped_filesDIR[1:]:
            # print(DIR)
            fasta_dir = os.path.join(DIR,'FASTA')
            cff = open(os.path.join(fasta_dir, 'combined_fasta_files.fasta'), 'w')
            for item in os.listdir(fasta_dir):
                # print(item)
                sff = open(os.path.join(fasta_dir, item))
                for line in sff:
                    cff.write(line)
                sff.close()
            cff.close()
    else:
        for rootDIR, dir_, files in os.walk(f"{home}\\all_FASTA"):
            fasta_dir = os.path.join(dir_,'FASTA')
            cff = open(os.path.join(fasta_dir, 'combined_fasta_files.fasta'), 'w')
            for item in os.listdir(fasta_dir):
                # print(item)
                sff = open(os.path.join(fasta_dir, item))
                for line in sff:
                    cff.write(line)
                sff.close()
                
            cff.close()
    print("######## FASTA files combined into a single file based on groups #######")
