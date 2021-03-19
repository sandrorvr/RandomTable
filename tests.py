import pandas as pd
import numpy as np
from RandomTable import RandomTable

df = pd.DataFrame(np.random.randint(0,1000,size=(10,10)))
print('==========================')
print(df)
df.columns = list('abcdefghij')
obj = RandomTable(df)
data = obj.transform()
print(data)
