# ABI-2-FASTA-TFR-Consolidator

## ABI-2-FASTA & Tandem Repeat Finding
This is a python program that takes folders that contain  **.abi** sequencing files 
and converts them to **FASTA** files using the [Biopython](https://biopython.org/wiki/SeqIO)
package. Individual FASTA files are combined to a single fasta file **(combined_fasta_file)**
and the [Tandem Repeat Finder](https://github.com/Benson-Genomics-Lab/TRF#using-command-line-version-of-tandem-repeats-finder)
by the Benson Genomics Lab is used to generate tandem repeats in the combined FASTA file. Place tfr in the same directory as
the app.py or A2FTC.py files

## Sorting for Phylogenetic Analysis
Files can be sorted using unique consistent strings from the file names of individual FASTA files in
into desired folders based on chosen folder names. Sorted files are combined to a single file using 
into a single FASTA file