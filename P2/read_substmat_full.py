
def read_substmat_full(filename):
    """Reads a substitution matrix from a file."""
    f=open(filename)
    first = f.readline()
    first.strip()
    first1 = first.split()
    d = dict()
    for i in first1:
        d[i] = 0
    d1 = d.copy()
    for i in d:
        d[i] = d1
        d1 = d1.copy()
    for line in f.readlines():
        line.strip()
        l = line.split()
        count = 1
        for i in d:
            d[i][l[0]] = l[count]
            count+=1

    return d
