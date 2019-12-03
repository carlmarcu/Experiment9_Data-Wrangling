import pandas as pd

table1= {'Box': ['Box1', 'Box1','Box1','Box2', 'Box2','Box2'], 
         'Dimension':['Length', 'Width','Height','Length', 'Width','Height'],
         'Value': [6,4,2,5,3,4]}
Boxx= pd.DataFrame(table1, columns=['Box','Dimension','Value'])

tidy=pd.pivot(Boxx, index='Box', columns='Dimension', values='Value' )
print(tidy)

tidy["Volumes"]=tidy.Length*tidy.Height*tidy.Width
print(tidy)
