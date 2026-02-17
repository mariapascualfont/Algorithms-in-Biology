def seq_identity(seq1, seq2):
    """
    Return the percentage of sequence identity. Exclude positions with gaps on any sequence
    >>> seq_identity("FASTCAT", "FATCAT")

    >>> seq_identity("FASTCAT", "FASTCAT")
    100.0
    >>> seq_identity("FASTCAT", "FASTRAT")
    85.7
    >>> seq_identity("-FASTCAT", "-FASTRAT")
    85.7
    >>> seq_identity("FASTCAT", "FA-TCAT")
    100.0
    >>> seq_identity("FASTCAT", "FAT-CAT")
    83.3
    >>> seq_identity("AFASTCAT", "-FASTRAT")
    85.7
    >>> seq_identity("FASTCAT", "AAAAAAA")
    28.6
    >>> seq_identity("FASTCAT", "AFAAAFA")
    0.0
    """
    if len(seq1) != len(seq2):
      return "The sequences are not of the same length, can't return the identity."
      #Is it better to print and return None?
    
    else:
      count = 0
      total = len(seq1)
      for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
          count += 1
        elif seq1[i] == "-" or seq2[i] == "-":
          total -= 1
    return round(count/total*100,1)

print(seq_identity("FASTCAT", "FASTCAT"))
print(seq_identity("FASTCAT", "FASTRAT"))
print(seq_identity("FASTCAT", "FAT-CAT"))
