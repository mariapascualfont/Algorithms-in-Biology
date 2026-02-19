def seq_identity(seq1, seq2):
    if len(seq1) != len(seq2):
      return None
    else:
      count = 0
      total = len(seq1)
      for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
          count += 1
        elif seq1[i] == "-" or seq2[i] == "-":
          total -= 1
    return round(count/total*100,1)
