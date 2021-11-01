# ABI-2-FASTA-TRF-Consolidator

## Table of Contents
- [Purpose](#Purpose)
- [ABI-2-FASTA & Tandem Repeat Finding](#ABI-2-FASTA&TandemRepeatFinding)
- [Sorting for Phylogenetic Analysis](#SortingforPhylogeneticAnalysis)
- [Usage](#Usage)

## Purpose
A2FTC is a simple pipeline to fast track the generation of tandem repeat data based on the tandem repeat finder program by the Benson Genomic Lab. This is help users with no coding skills skip the laborious task of using the online version through the generation of an excel output of all relevant metrics from converting their abi sequence files. Also, unsorted FASTA files can be sorted by using user-entered distinct strings that can be used to sort files and generate a single FASTA file that can be used for downstream clustering analysis.

## ABI-2-FASTA & Tandem Repeat Finding
***A2FTC.py*-** This is a python program that takes folders that contain  **.abi** sequencing files 
and converts them to **FASTA** files using the [Biopython](https://biopython.org/wiki/SeqIO) package. Individual FASTA files are combined to a single FASTA file **(combined_fasta_file)** and the [Tandem Repeat Finder](https://github.com/Benson-Genomics-Lab/TRF#using-command-line-version-of-tandem-repeats-finder) by the Benson Genomics Lab is used to generate tandem repeats in the combined FASTA file. Place **tandem repeat finder** program in the same directory as the app.py or A2FTC.py files.

## Sorting for Phylogenetic Analysis
***sort_csld.py*-** Files can be sorted using unique consistent strings from the file names of individual FASTA files into desired folders based on chosen folder names. Sorted files are combined to a single file using into a single FASTA file.

## Usage
