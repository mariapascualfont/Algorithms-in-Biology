def move_gaps(seq1, seq2):
    """
    Generate alignments by moving gaps in one sequence
    in another sequence.
    >>> move_gaps("THEFASTCAT", "THEFATCAT")
    ['THEFASTCAT', '-THEFATCAT', 'T-HEFATCAT', 'TH-EFATCAT', 'THE-FATCAT', 'THEF-ATCAT', 'THEFA-TCAT', 'THEFAT-CAT', 'THEFATC-AT', 'THEFATCA-T', 'THEFATCAT-']
    >>> move_gaps("THEFASTCAT", "AFASTCAT")
    ['THEFASTCAT', '--AFASTCAT', 'A--FASTCAT', 'AF--ASTCAT', 'AFA--STCAT', 'AFAS--TCAT', 'AFAST--CAT', 'AFASTC--AT', 'AFASTCA--T', 'AFASTCAT--']
    >>> move_gaps("THEFATCAT", "THEFASTCAT")
    ['THEFASTCAT', '-THEFATCAT', 'T-HEFATCAT', 'TH-EFATCAT', 'THE-FATCAT', 'THEF-ATCAT', 'THEFA-TCAT', 'THEFAT-CAT', 'THEFATC-AT', 'THEFATCA-T', 'THEFATCAT-']
    >>> move_gaps("AFASTCAT", "THEFASTCAT")
    ['THEFASTCAT', '--AFASTCAT', 'A--FASTCAT', 'AF--ASTCAT', 'AFA--STCAT', 'AFAS--TCAT', 'AFAST--CAT', 'AFASTC--AT', 'AFASTCA--T', 'AFASTCAT--']
    """
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

print(move_gaps("THEFASTCAT", "THEFATCAT"))
print(move_gaps("AFASTCAT", "THEFASTCAT"))
