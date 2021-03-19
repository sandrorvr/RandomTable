import pandas as pd
import numpy as np

class RandomTable(pd.DataFrame):
    def __init__(self,df):
        super().__init__(data=None)
        self.df = df


    def randommizeNotStr(self,el):

    def randommizeJson(self):
        pass

    def isJson(self, el):
        return True if (el[0]=='{' or el[1]=='{') and (el[-1]=='}' or el[-2]=='}') False

    def transform(self):
        for column in self.df.columns:
            if self.df[column].dtype != np.object:
                self.df[column].apply(self.randommizeNotStr)
            else:
                if self.isJson(self.df[column][0]) # se coluna for um json:
                    self.df[column].apply(self.randommizeJson)
                else:
                    self.df[column].apply(lambda x: np.random.choice(list(x),len(x),replace=False))
