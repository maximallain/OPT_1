def sequence_finder(path="Data/crossword1.txt"):
    """
    mot croisé : matrice m x n
    variable xij : lettre de la case ij
    """
    print("Sequence finder...")
    with open(path,'r') as file:
        lines=file.readlines()
        m = len(lines)
        n = len(lines[1])
        #trouve les sequences par ligne, sous forme de liste de variables, stockées dans une liste
        sequences_horizontales={}
        sequences_verticales={}
        compteur = 1
        for i in range(0,m-1):
            c=0
            j=0
            while j < n-1:
                if (lines[i][j] == "#") & (c==0) :
                    j+=1
                    c=0
                elif (lines[i][j] == ".") & (c==0) & (lines[i][j+1] == "#") :
                    j+=2
                    c=0
                elif (lines[i][j] == ".") & (c==0) & (lines[i][j+1] == ".") :
                    s=["x"+str(i)+"."+str(j)]
                    c=1
                    j+=1
                elif (lines[i][j] == ".") & (c==1) :
                    s.append("x"+str(i)+"."+str(j))
                    c=1
                    j+=1
                elif (lines[i][j] == "#") & (c==1) :
                    sequences_horizontales["h"+str(compteur)] = s
                    s=[]
                    c=0
                    j+=1
                    compteur += 1
        compteur = 1
        for j in range(0,n-1):
            c=0
            i=0
            while i < m:
                if (i==m-1) & (c==1):
                    i+=1
                    sequences_verticales["v"+str(compteur)] = s
                    s=[]
                    compteur += 1

                elif (i==m-1) & (c==0):
                    i+=1
                elif (lines[i][j] == "#") & (c==0) :
                    i+=1
                    c=0
                elif (lines[i][j] == ".") & (c==0) & (lines[i+1][j] == "#") :
                    i+=1
                    c=0
                elif (lines[i][j] == ".") & (c==0) & (lines[i+1][j] == ".") :
                    s=["x"+str(i)+"."+str(j)]
                    c=1
                    i+=1
                elif (lines[i][j] == ".") & (c==1) :
                    s.append("x"+str(i)+"."+str(j))
                    c=1
                    i+=1
                elif (lines[i][j] == "#") & (c==1) :
                    sequences_verticales["v"+str(compteur)] = s
                    s=[]
                    c=0
                    i+=1
                    compteur += 1

        return sequences_horizontales,sequences_verticales



