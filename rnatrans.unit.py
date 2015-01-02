def codon_table():
    table = """
    UUU F      CUU L      AUU I      GUU V
    UUC F      CUC L      AUC I      GUC V
    UUA L      CUA L      AUA I      GUA V
    UUG L      CUG L      AUG M      GUG V
    UCU S      CCU P      ACU T      GCU A
    UCC S      CCC P      ACC T      GCC A
    UCA S      CCA P      ACA T      GCA A
    UCG S      CCG P      ACG T      GCG A
    UAU Y      CAU H      AAU N      GAU D
    UAC Y      CAC H      AAC N      GAC D
    UAA Stop   CAA Q      AAA K      GAA E
    UAG Stop   CAG Q      AAG K      GAG E
    UGU C      CGU R      AGU S      GGU G
    UGC C      CGC R      AGC S      GGC G
    UGA Stop   CGA R      AGA R      GGA G
    UGG W      CGG R      AGG R      GGG G""" 
#TODO 
    
    codon_dic = {}
    
    for sor in table.split('\n'):
        sor = sor.split(' ')
        sor = filter(lambda x: x!="", sor)
            
        for i in xrange(0,len(sor),2):
            codon_dic[sor[i]] = sor[i+1]
    
    #print codon_dic

    return codon_dic

def readseq(filename):
    f = open(filename, 'r')
    seqstring = f.read().replace('\n','')
    return seqstring

def translate(seqstring):
    codons = []
    start, end = 0, 3
    
    while end <= len(seqstring):
        codon = seqstring[start:end]
        codons.append(codon)
        start, end = start + 3, end + 3
    
    proteinstring = ''
    
    for i in codons:
        peptide = codon_table()[i]
        proteinstring = proteinstring + peptide
    print proteinstring.replace('Stop', '')
    
translate(readseq('rosalind_prot.txt'))
  

#print readseq("seq.txt")
#print codon_table()
