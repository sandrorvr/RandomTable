import pandas as pd
import numpy as np
import json

class RandomTable(pd.DataFrame):
    def __init__(self,df):
        super().__init__(data=df)


    def randommizeNotStr(self,el,col):
        return np.random.randint(self[col].min(), self[col].max())
    
    def scanJson(self, el,tan, buffer):
      if type(el) == list:
        i = 0
        while i < tan:
          self.scanJson(el[i], len(el[i]), buffer)
          i +=1
      elif type(el) == str:
        el = json.loads(el)
        self.scanJson(el, len(el), buffer)
      else:
        if type(list(el.values())[0]) == list:
          self.scanJson(list(el.values())[0], len(list(el.values())[0]), buffer)
        else:
          buffer.append(el)
      return buffer

    def randommizeJson(self,el):
        newDict = {}
        dic = json.loads(el)
        keys = list(dic.keys()) if type(dic) == dict else ['LIST']  #list(dic.keys())
        values = self.scanJson(dic,len(dic), [])
        for ob in values:
          for key in ob.keys():
            keyRandom = ''.join(np.random.choice(list(key),len(key),replace=False))
            valueRandom = ''.join(np.random.choice(list(str(ob[key])),len(list(str(ob[key]))),replace=False))
            newDict[keyRandom] = valueRandom

        if len(values) > 1 and keys[0] != 'LIST':
          vetAux = []
          vetAux.append(newDict)
          keyRandom = ''.join(np.random.choice(list(keys[0]),len(keys[0]),replace=False))
          return {keyRandom:vetAux}
        return newDict

    def isJson(self, el):
        return True if (el[0]=='{' or el[1]=='{') and (el[-1]=='}' or el[-2]=='}') else False

    def transform(self):
        for column in self.columns:
            if self[column].dtype != np.object:
                self[column] = self[column].apply(self.randommizeNotStr, col=column)
            else:
                if self.isJson(self[column][0]): # se coluna for um json:
                    self[column] = self[column].apply(self.randommizeJson)
                else:
                    self[column] = self[column].apply(lambda x: np.random.choice(list(x),len(x),replace=False))
        return self
