import pandas as pd
import numpy as np

class RandomTable(pd.DataFrame):
    def __init__(self,df):
        super().__init__(data=None)
        self.df = df


    def randommizeNotStr(self):
        pass
    def randommizeJson(self):
        pass

    def transform(self):
        for column in self.df.columns:
            # se a coluna for do tipo != string
                self.df[column].apply(self.randommizeNotStr)
            #else:
                # se coluna for um json:
                    self.df[column].apply(self.randommizeJson)
                #else:
                    self.df[column].apply(lambda x: np.random.choice(list(x),len(x),replace=False))
