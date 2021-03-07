# Repository for code and extra materials for the Advanced Clinical Bioinformatics (BIOL68412) Assignment.

## Files
* Cardiac_Transcripts.bed
  * BED file of genes and transcripts used
* Cardiac_Targets.bed
  * BED file of targets used for analysis. Created using HyperDesign, all exon targets have a 15bp overhang
* Filter_Annotation.py
  * Python script to filter the VEP output 

## Requirements for Filter_Annotation.py
* Python3
  * openpyxl module installed

## Running Filter_Annotation.py
1. Download VEP output in txt format
   * Ensure RefSeq transcripts were used in VEP
   * Ensure gnomAD allele frequencies were included
2. Place VEP txt output in the same location as Filter_Annotation.py and Cardiac_Transcripts.bed
3. Run the script using the _-f_ flag to specify the input file name e.g:
   * _python3 Filter\_Annotation.py -f VEP\_output.txt_
 4. The output file will be named based on the input file e.g:
    * If the input filename was VEP\_output.txt the filtered annotation file will be named VEP\_output\_FILTERED.xlsx
