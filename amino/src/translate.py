# I have used the three-letter abbreviations for each amino acid.
# For full names, see http://www.carolguze.com/images/biomolecules/AminoAcidJargonStryerBio3.gif

cStop = ["TAA", "TAG", "TGA"]
codons = {"TTT":"Phe", "TTC":"Phe", "TTA":"Leu", "TTG":"Leu",\
          "TCT":"Ser", "TCC":"Ser", "TCA":"Ser", "TCG":"Ser",\
          "TAT":"Tyr", "TAC":"Tyr", "TAA":"STP", "TAG":"STP",\
          "TGT":"Cys", "TGC":"Cys", "TGA":"STP", "TGG":"Trp",\
          "CTT":"Leu", "CTC":"Leu", "CTA":"Leu", "CTG":"Leu",\
          "CCT":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",\
          "CAT":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln",\
          "CGT":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg",\
          "ATT":"Ile", "ATC":"Ile", "ATA":"Ile", "ATG":"Met",\
          "ACT":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",\
          "AAT":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys",\
          "AGT":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg",\
          "GTT":"Val", "GTC":"Val", "GTA":"Val", "GTG":"Val",\
          "GCT":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",\
          "GAT":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu",\
          "GGT":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly"}

# Translates an RNA sequence into amino acids.
# Takes a string of RNA.
# Returns a string of amino acids.
def translate(sequence):
    # find the start codon (ATG) and set the index to begin there
    index = sequence.find("ATG")

    # return error if there is no start codon
    if index < 0:
        return "No start codon found."

    # cut off the sequence before the start codon
    sequence = sequence[index:]

    aminos = ""
    # translate the sequence codon by codon (groups of 3 nucleic acids)
    for i in range(0, len(sequence), 3):
        # break if a stop codon (TAA, TAG, TGA) is encountered
        if sequence[i:i+3] in cStop:
            break
        aminos = aminos + codons[sequence[i:i+3]]

    return aminos

#sequence = raw_input("RNA Sequence: ").strip()
#print translate(sequence)
