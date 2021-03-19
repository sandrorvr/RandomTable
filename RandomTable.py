import pandas as pd
import numpy as np

class RandomTable(pd.DataFrame):
    def __init__(self,df):
        super().__init__(data=None)
        self.df = df


    def randommizeNotStr(self,el,col):
        return np.random.randint(self.df[col].min(), self.df[col].max())

    def randommizeJson(self,el):
        dic = Json.loads(el)
        keys = list(dic.keys())
        values = list(dic.values())
        for i in range(len(keys)):
            keys[i] = np.random.choice(list(keys[i]),len(list(keys[i])),replace=False)
            values[i] = np.random.choice(list(values[i]),len(list(values[i])),replace=False)
        return [(k,v) for k,v in zip(keys,values)]

    def isJson(self, el):
        return True if (el[0]=='{' or el[1]=='{') and (el[-1]=='}' or el[-2]=='}') else False

    def transform(self):
        for column in self.df.columns:
            if self.df[column].dtype != np.object:
                self.df[column] = self.df[column].apply(self.randommizeNotStr, col=column)
            else:
                if self.isJson(self.df[column][0]): # se coluna for um json:
                    self.df[column] = self.df[column].apply(self.randommizeJson)
                else:
                    self.df[column] = self.df[column].apply(lambda x: np.random.choice(list(x),len(x),replace=False))
        return self.df


df = pd.DataFrame(np.random.randint(0,1000,size=(10,10)))
print('==========================')
print(df)
df.columns = list('abcdefghij')
obj = RandomTable(df)
data = obj.transform()
print(data)
