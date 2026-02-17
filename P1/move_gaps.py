def move_gaps(seq1, seq2):
    if len(seq2) > len(seq1):
      seq1, seq2 = seq2, seq1
    gaps = (len(seq1) - len(seq2))* '-'
    result = [seq1]
    for i in range(len(seq1)):
      head = seq2[:i]
      tail = seq2[i:]
      filled_gap = head+gaps+tail
      result.append(filled_gap)
    return result
