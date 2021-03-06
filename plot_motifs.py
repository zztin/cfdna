import matplotlib.pyplot as plt

def plot_kmer_dist(motifs, ind, colors=['blue', "red", "teal", "yellow"], relative = True, figsize = (10,4)):
    plt.figure(figsize=figsize)
    for i, x in enumerate(motifs):
        if relative:
            sum_total = sum(x.values())
            print(x.keys())                      #see how the dictionary is structured
            print(x.values())
        else:
            sum_total = 1
        # x labels should be predefined. (combination of ATGC sorted with alphabetical orders.)
        plt.bar([k for k,v in  sorted(x.items())],[v/sum_total for k,v in  sorted(x.items())], 
                label = f"{ind[i]}", 
                alpha=0.3, 
                color = colors[i]) 
    plt.xticks( rotation='vertical')
    plt.legend()
    plt.show()
    
def plot_all(df, figsize= (10,4)):    
    plot_kmer_dist([df['fwd5']], ["fwd 5' end"], [ "red", "yellow"], figsize= figsize)
    plot_kmer_dist([df['fwd3']], ["fwd 3' end"], [ "blue", "teal"], figsize= figsize)
    plot_kmer_dist([df['fwd5'], df['fwd3']], ["fwd 5' end", "fwd 3' end"], [ "red", "blue"], figsize= figsize)

def plot_all_random(df, figsize= (10,4)):         #overbodig, mag weg 
    plot_kmer_dist([df['fwd5']], ["fwd 5' end"], [ "red", "yellow"], figsize= figsize)
    plot_kmer_dist([df['fwd3']], ["fwd 3'end"], [ "blue", "teal"], figsize= figsize)
    plot_kmer_dist([df['fwd5'], df['fwd3']], ["fwd 5' end", "fwd 3' end"], [ "red", "blue"], figsize= figsize)