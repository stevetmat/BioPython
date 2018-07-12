from Bio.Seq import Seq

string = "AGTACACTGGT2"
my_seq = Seq("AGTACACTGGT")
print("Sequence:", my_seq)
print("Lower:", my_seq.lower())
print("Complement:", my_seq.complement())
print("Reverse complement:", my_seq.reverse_complement())
print(string.isdigit())
