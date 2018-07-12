from Bio import SeqIO


for seq_record in SeqIO.parse("files/ls_orchid.gbk","genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))# prints sequence like Seq('AG...CT', SingleLetterAlphabet())
    print(seq_record.seq) # prints sequence like AGCT
    print(len(seq_record))