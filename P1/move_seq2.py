from score_seqs import score_seqs

def move_seq2(seq1, seq2):
    if len(seq2) > len(seq1):
      seq1, seq2 = seq2, seq1
    gaps = (len(seq1))* '-'
    result = [seq1+gaps[:-2]]
    for i in range(len(seq1)+1):
      head = gaps[:i]
      tail = gaps[i:]
      filled_gap = head+seq2+tail
      result.append(filled_gap)
    return result

def print_scores(seq1, seq2, match, mismatch, gap):
    options = move_seq2(seq1,seq2)
    scores = list()
    print(options[0])
    for i in range(len(options)-1):
      scores.append(score_seqs(options[0], options[i+1], match, mismatch, gap))
      print(options[i+1], scores[i])
