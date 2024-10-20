from starter_code import *

with open("wild_type.txt","r") as file:
    wild_type = file.readlines()[2]

with open("patient_15.txt","r") as file:
    patient = file.readlines()[2]


wild_type_rna = transcribe_dna(wild_type)
wild_type_orf = get_orf(wild_type_rna)
wild_type_aa = translate_rna(wild_type_orf)
#print(wild_type_aa)

patient_type_rna = transcribe_dna(patient)
patient_type_orf = get_orf(patient_type_rna)
patient_type_aa = translate_rna(patient_type_orf)
#print(patient_type_aa)


dna_mutation = identify_dna_mutation(wild_type,patient)

aa_mutation = identify_aa_mutation(wild_type_aa,patient_type_aa,dna_mutation[0])
print(visualize_aa_mutation(wild_type_aa,patient_type_aa,aa_mutation[1],aa_mutation[0],10))

'''
Handles:
    - Silent: No amino acid mutation.
    - Missense: A mutation that changes only one of the amino acids to another amino acid.
    - Nonsense: A mutation that only results in substitution of an amino acid to an early stop codon.
    - FrameShift: Multiple amino acid changes due to insertion/deletion, with possibility of an early stop.
    Patient 2 is wrong
    Patient 4 is ???
    Patient 14 is ???
    Patient 15 is ???

'''
