import pandas as pd
import numpy as np
from RandomTable import RandomTable

df = pd.DataFrame(np.random.randint(0,1000,size=(4,10)))
df['dic'] = ['{"casa":"mesa"}','{"olho":"abc"}', '{"nada":1}', '{"tudo":1234}']
print(df)
print('==========================')
print(df)
df.columns = list('abcdefghij')
obj = RandomTable(df)
data = obj.transform()
print(data)
