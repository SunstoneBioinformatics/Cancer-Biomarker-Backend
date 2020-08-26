#%% Imports
from Bio import Entrez
import numpy as np
import pandas as pd
# %% Identify myself to NCBI
Entrez.api_key = "898f0134b3ebe151bfc94b614f666082d008"
Entrez.email = "leo13361@uvg.edu.gt"

# %% Test query (Works)
#handle = Entrez.einfo()
#result = handle.read()
#handle.close()
#print(result)
# %% BRCA2
handle = Entrez.esearch(db="nucleotide", term='(BRCA1[All Fields] AND ("Homo sapiens"[Organism] OR human[All Fields])) AND "Homo sapiens"[porgn] AND biomol_genomic[PROP]' , retmax="2500" )
record = Entrez.read(handle)
handle.close()
gi_list = record["IdList"]
print(record["Count"])
#print(gi_list)
# %% Download BRCA1
handle = Entrez.efetch(db="nucleotide", id=gi_list, retmode="xml")
records = Entrez.read(handle)
len(records)
# %% Try records/save records
print(records[0]["GBSeq_comment"])

# %%
print(type(records))
#with open("output.dict", "w") as f:
#    f.write(str(records))
# %%
