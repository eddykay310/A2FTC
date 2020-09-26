import shutil, os


home = os.getcwd()
os.makedirs(f"{home}/all_FASTA")

seqfolder_list = ["AM-2","AM-3","AM-4","AM-5"]
group = ["A","B","C","D","E","F","G","H"]
i=0
temp=[]
grouped_filesDIR = []

# Copys files in to one folder
for folder in seqfolder_list:    
    for file in os.listdir(f"{home}/{folder}/FASTA"):
        if file.endswith(".fasta"):
            shutil.copy(os.path.join(f"{home}/{folder}/FASTA",file),f"{home}/all_FASTA")

# Sorting files into subfolders
for i in range(len(group)):
    for file in os.listdir(f"{home}/all_FASTA"):
        if i<len(group) and file.endswith(f"{group[i]}.ab1.fasta"):
            temp.append(os.path.join(f"{home}\\all_FASTA",file))
    if i<len(group):
        os.makedirs(f"{home}/all_FASTA/{group[i]}")
        for path in temp: 
            shutil.move(j,f"{home}\\all_FASTA\\{group[i]}")
        i+=1
    temp.clear()
print("######## Files sorted into folders #########\n")

# Getting grouped files directory into list
for root, directory, files in os.walk(f"{home}\\all_FASTA"):
    grouped_filesDIR.append(root)

# Consolidating fasta files
for DIR in folders[1:]:
    cff = open(f'{DIR}_combined_fasta_files.fasta', 'w')
    for file in os.listdir(DIR):
        sff = open(os.path.join(DIR, file))
        for line in sff:
            cff.write(line)
        sff.close()
    cff.close()
print("######## FASTA files combined into a single file based on groups #######")

# Deleting files created by tandem repeat analysis
print("######## Deleting folders created by the tandem repeat analysis #########\n")
for folder in seqfolder_list:
    shutil.rmtree(folder)