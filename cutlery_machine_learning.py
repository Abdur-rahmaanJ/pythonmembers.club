import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

# df is short for dataframe
df = pd.read_csv("<path here>/cutlery.csv")

D = df['D']
h = df['h']

target = (8, 7.5) # tuple
Dt = target[0] # Dt for D-target
ht = target[1] # ht for h-target

plt.figure(figsize=(14,5)) # size of plot in inches

for i,type_ in enumerate(df['type']): # i list for index type_ for list element
    D_ = D[i]
    h_ = h[i]
    dist = sqrt( (Dt-D_)**2 + (ht-h_)**2 ) # formula
    
    label = '{} \ndist:{}'.format(type_, round(dist, 2))
    if type_ == 'bowl':
        plt.scatter(D_, h_, marker='o', color='red')
        plt.text(D_+0.3, h_, label, fontsize=9)
    elif type_ == 'mug':
        plt.scatter(D_, h_, marker='o', color='blue')
        plt.text(D_+0.3, h_, label, fontsize=9)
    elif type_ == 'plate':
        plt.scatter(D_, h_, marker='o', color='green')
        plt.text(D_+0.3, h_, label, fontsize=9)
        
    plt.scatter(Dt, ht, marker='x', color='green') # target point
    
plt.annotate('target', 
    ha = 'center', va = 'bottom',
    xytext = (Dt-2.5, ht-2),
    xy = (Dt, ht),
    arrowprops = { 'facecolor' : 'green', 'shrink' : 0.05 }) # target arrow
plt.xlabel('diameter')
plt.ylabel('height')
plt.show()
