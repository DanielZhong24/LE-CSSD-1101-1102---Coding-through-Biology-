from starter_code import *

with open("wild_type.txt","r") as file:
    wild_type = file.readlines()[2]

with open("patient_1.txt","r") as file:
    patient = file.readlines()[2]


wild_type_rna = transcribe_dna(wild_type)
wild_type_orf = get_orf(wild_type_rna)
wild_type_aa = translate_rna(wild_type_orf)

patient_type_rna = transcribe_dna(patient)
patient_type_orf = get_orf(patient_type_rna)
patient_type_aa = translate_rna(patient_type_orf)

dna_mutation = identify_dna_mutation(wild_type,patient)
aa_mutation = identify_aa_mutation(wild_type_aa,patient_type_aa,dna_mutation[0])

print(visualize_aa_mutation(wild_type_aa,patient_type_aa,aa_mutation[1],aa_mutation[0],3))