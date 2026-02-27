def nw_alt1(seq_i, seq_j, match, mismatch, gap):

    match, mismatch, gap = int(match), int(mismatch), int(gap)
    
    # Store the lengths of the sequences
    n_i, n_j = len(seq_i), len(seq_j)

    # Initialize scores and traceback matrices
    scores = [[0 for _ in range (n_j + 1)] for _ in range(n_i + 1)]
    traceback = [[0 for _ in range (n_j + 1)] for _ in range(n_i + 1)]

    # Initialize edges with gaps
    for i in range(1, n_i + 1):
        scores[i][0] = i * gap
        traceback[i][0] = 1 

    for j in range(1, n_j + 1):
        scores[0][j] = j * gap
        traceback[0][j] =  -1

    # Fill the matrices
    for i in range(1, n_i + 1):
        for j in range(1, n_j + 1):
            # Calculate scores for all possibilities
            if seq_i[i-1] == seq_j[j-1]:
                diag = scores[i-1][j-1] + match
            else:
                diag = scores[i-1][j-1] + mismatch

            left = scores[i][j-1] + gap
            up = scores[i-1][j] + gap

            # Choose the best scores
            # Set traceback pointer
            if diag > left and diag > up:
                scores[i][j] = diag
                traceback[i][j] = 0  
                
            elif left >= up: 
                scores[i][j] = left
                traceback[i][j] = -1  
                #here we force that in case of a tie, we go left (deletion). In nw, it went up (insertion), so to provide the same result as before with the sequences put in reverse order, this is the most efficient way to do it.
                
            else:
                scores[i][j] = up
                traceback[i][j] = 1 
                
    # Print scores matrix (for debugging)
    header = 8 * " " + " ".join(f"{c:>3}" for c in seq_j)
    print(header)
    for aa, row in zip(f" {seq_i}", scores):
        print(f"{aa:>3}", " ".join(f"{v:>3}" for v in row))

    # Print traceback matrix (for debugging))
    header = 8 * " " + " ".join(f"{c:>3}" for c in seq_j)
    print("\n" + header)
    for aa, row in zip(f" {seq_i}", traceback):
        print(f"{aa:>3}", " ".join(f"{v:>3}" for v in row))

    # Print optimal score
    print("Optimal score:", scores[n_i][n_j])

    # Prepare for traceback
    aln_i, aln_j = [], []
    i, j = n_i, n_j # fill in; this is the starting point for traceback

    # Traceback
    while i > 0 or j  > 0:  # fill in
        if traceback[i][j] == 0:  # diagonal
                i -= 1
                j -= 1
                aln_i.append(seq_i[i])
                aln_j.append(seq_j[j])
        elif traceback[i][j] == -1:  # left
                j -= 1
                aln_i.append('-')
                aln_j.append(seq_j[j])
        else:  # up, (traceback[i][j] == 1)
                i -= 1
                aln_j.append('-')
                aln_i.append(seq_i[i])

    # Print the alignment
    aln_i = "".join(aln_i[::-1])
    aln_j = "".join(aln_j[::-1])
    print(aln_i)
    print(aln_j)


args = ['THERAT', 'THEBIGCAT', 8, -8, -4 ]
nw(args[0], args[1], args[2], args[3], args[4])
print()
args = ['THEBIGCAT', 'THERAT', 8, -8, -4 ]
nw_alt1(args[0], args[1], args[2], args[3], args[4])
