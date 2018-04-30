mappings = {
	'G': 'C',
	'C': 'G',
	'T': 'A',
	'A': 'U'
}


def to_rna(dna_strand: str) -> str:
	rna_strand = ''
	for nucleotide in dna_strand:
		if mappings.__contains__(nucleotide):
			rna_strand += mappings[nucleotide]
		else:
			raise ValueError(f"Unknown nucleotide found : {nucleotide}")
	return rna_strand
