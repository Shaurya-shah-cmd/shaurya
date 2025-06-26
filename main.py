import pandas as pd
df1 = pd.DataFrame({ 'a':[1,2,3,4], 'b':[5,6,7,8]} )# index =(1,2,3,4) )
df2 = pd.DataFrame({'a':[10,20,30], 'b':[40,50,60] } , index =(1,2,3) )
print(df1)
print(df2)
print( "\n addition of 2 dataframes \n", df1 + df
