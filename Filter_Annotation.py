import os, openpyxl, argparse, sys, pdb

#Parser to get input file from command line
#If this were to be used in a pipeline it would be quite straight forward to run this script over multiple files
parser = argparse.ArgumentParser(description='Filter VEP Output based on Transcript, Impact and gnomAD AF', add_help=True)
parser.add_argument('-f', action="store", dest="VEP_File", help="Location of VEP output file", required=True)
args = parser.parse_args()
original_file= args.VEP_File

#Opens an Excel workbook to store the output
#Excel chosen as it's quite user friendly for clinical scientists to open to start variant interpretation
wb = openpyxl.Workbook()
ws1 = wb.active
ws1.title = "Filtered Annotation"

#Gets and stores the NM numbers for transcript
transcript_file="Cardiac_Transcripts.bed"
if os.path.exists(transcript_file):
    with open(transcript_file,"rt") as file:
        transcripts=[]
        for line in file:
            transcripts.append(line.strip().split("\t")[0].split(".")[0])
else:
    print("Unable to find transcript file")
    print(f"Ensure {transcript_file} is in same location as script")
    sys.exit()
        
with open(original_file,"rt") as file1:
    #writes the headers
    headers=file1.readline().split("\t")
    if "gnomAD_AF" not in headers:
        print("Cannot find gnomAD allele frequencies in VEP output")
        print("Check if gnomAD allele frequencies were selected in VEP configuration")
        sys.exit()
    ws1.append(headers)
    for line in file1:
        #makes dict of headers:values
        variant=dict(zip(headers,line.split("\t")))
        #checks variant is in transcript list and has correct impact
        if (variant["Feature"].split(".")[0] in transcripts) and (variant["IMPACT"] in ("HIGH","MODERATE")):
            #adds variant if it doesn't have gnomAD AF
            if variant["gnomAD_AF"]=="-":
                ws1.append(list(variant.values()))
            #adds variant if it's gnomAD AF if less than 5%
            elif float(variant["gnomAD_AF"])<0.05:
                ws1.append(list(variant.values()))
#saves the Excel workbook                
wb.save(f"{original_file.strip('.txt')}_FILTERED.xlsx")
print(f"Filtered file saved as {original_file.strip('.txt')}_FILTERED.xlsx")
