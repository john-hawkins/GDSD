import random
import pandas as pd
import numpy as np

df = pd.DataFrame()

df['y'] = [random.random() for _ in range(200)]

df['I'] =  [random.random() for _ in range(200)]
 
df['II'] = df['y']  + ( [random.random()/4 for _ in range(200)] )
df['IIa'] = np.where( df['II'] <1.0, df['II'], df['II']-0.2 )

df['II'] = (1-df['y'])  + ( [random.random()/4 for _ in range(200)] )
df['IIb'] = np.where( df['II'] <1.0, df['II'], df['II']-0.2 ) 

df['III'] =  np.where( df['IIa'] < 0.5, df['IIa'], 0.5+ (df['I']/2) )

df['IV'] =  np.where( df['y'] > 0.4, np.where( df['y'] < 0.6, 0.5, 0.5+(df['I']/2) ), 0.5-(df['I']/2) )

df['V'] =  df['y']*df['y']  + ( [random.random()/10 for _ in range(200)] )

df['VI'] = np.where( df['I'] < 0.5, 0.5 - (np.sqrt(df['y'])/2) + (df['I']/10 ), 0.5 + (np.sqrt(df['y'])/2) + (df['I']/10 ) )

df['VII'] = np.where( df['y'] < 0.3, 0.5 + pow(df['IIb'], 2)/4 , np.where( df['y'] > 0.7, 0.5+ pow(df['IIa'],2)/4, 0.7 - pow(df['IIa'],3) ) )


###############################
# Create Figure and Subplots

fig, axes = plt.subplots(4,2, figsize=(10,8), sharex=True, sharey=True, dpi=120)

axes[0,0].scatter(df['I'], df['y'], alpha=0.5)
axes[0,0].set_title('I - Random')

axes[0,1].scatter(df['IIa'], df['y'], alpha=0.5)
axes[0,1].set_title('IIa - Linear Correlation')

axes[1,0].scatter(df['IIb'], df['y'], alpha=0.5)
axes[1,0].set_title('IIb - Linear Anti-Correlation')

axes[1,1].scatter(df['III'], df['y'], alpha=0.5)
axes[1,1].set_title('III - Partial Linear Correlation')

axes[2,0].scatter(df['IV'], df['y'], alpha=0.5)
axes[2,0].set_title('IV - Step Function')

axes[2,1].scatter(df['V'], df['y'], alpha=0.5)
axes[2,1].set_title('V - Non-linear Monotonic')

axes[3,0].scatter(df['VI'], df['y'], alpha=0.5)
axes[3,0].set_title('VI - Non-linear Non-monotonic')

axes[3,1].scatter(df['VII'], df['y'], alpha=0.5)
axes[3,1].set_title('VII - Non-bijective')

plt.savefig('univariate_relationships.png')


