def score_seqs(seq1, seq2, match, mismatch, gap):
    if len(seq1) != len(seq2):
      return 0
    score = 0
    for i in range(len(seq1)):
      if seq1[i] == seq2[i]:
        if seq1[i] != "-":
          score += match
      elif seq1[i] == "-" or seq2[i] == "-":
        score += gap
      else:
        score += mismatch
    return score
