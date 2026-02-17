from move_gaps import move_gaps
from score_seqs import score_seqs

def move_gaps_scores(seq1, seq2, match, mismatch, gap):
    options = move_gaps(seq1,seq2)
    scores = list()
    result = list()
    result.append(options[0])
    for i in range(len(options)-2):
      scores.append(score_seqs(options[0], options[i+1], match, mismatch, gap))
      result.append((options[i+1], scores[i]))
    return result
