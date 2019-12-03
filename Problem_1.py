import pandas as pd

table1= {'Student': ['Ice Bear', 'Panda','Grizzly'], 'Math':[80, 95,79]}
Math= pd.DataFrame(table1, columns=['Student','Math'])

table2= {'Student': ['Ice Bear', 'Panda','Grizzly'], 'Electronics':[85, 81, 83]}
Electronics= pd.DataFrame(table2, columns=['Student','Electronics'])

table3= {'Student': ['Ice Bear', 'Panda','Grizzly'], 'GEAS':[90,79,93]}
GEAS= pd.DataFrame(table3, columns=['Student','GEAS'])

table4= {'Student': ['Ice Bear', 'Panda','Grizzly'], 'ESAT':[93, 89,88]}
ESAT= pd.DataFrame(table4, columns=['Student','ESAT'])

short=pd.merge(Math, Electronics, how='right', on= 'Student')
short1=pd.merge(short, GEAS, how='right', on= 'Student')
shortformat=pd.merge(short1, ESAT, how='right', on= 'Student')
print(shortformat)

longformat=pd.melt(shortformat, id_vars=['Student'], value_vars=['Math','Electronics','GEAS','ESAT'], var_name='Subject', value_name='Grade')
print(longformat)