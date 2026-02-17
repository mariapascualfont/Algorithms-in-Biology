from move_gaps import move_gaps
from score_seqs import score_seqs

def move_gaps_scores(seq1, seq2, match, mismatch, gap):
    """
    >>> move_gaps_scores('THEFASTCAT', 'AFASTCAT', 1, -1, -2)
    THEFASTCAT
    --AFASTCAT 2
    A--FASTCAT 2
    AF--ASTCAT 0
    AFA--STCAT -2
    AFAS--TCAT -4
    AFAST--CAT -6
    AFASTC--AT -8
    AFASTCA--T -10
    AFASTCAT-- -12
    >>> move_gaps_scores('AFASTCAT', 'THEFASTCAT', 1, -1, -2)
    THEFASTCAT
    --AFASTCAT 2
    A--FASTCAT 2
    AF--ASTCAT 0
    AFA--STCAT -2
    AFAS--TCAT -4
    AFAST--CAT -6
    AFASTC--AT -8
    AFASTCA--T -10
    AFASTCAT-- -12
    """
    options = move_gaps(seq1,seq2)
    scores = list()
    print(options[0])
    for i in range(len(options)-2):
      scores.append(score_seqs(options[0], options[i+1], match, mismatch, gap))
      print(options[i+1], scores[i])

move_gaps_scores('AFASTCAT', 'THEFASTCAT', 1, -1, -2)
print()
move_gaps_scores('AFASTCAT', 'THEFASTCAT', 1, -1, -2)
