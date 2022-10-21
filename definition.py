import pandas as od
import pandas as pd


class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pd.read_csv('data.csv')
        term = tuple(df.loc[df['word']==self.term]['definition'])
        return term

d = Definition(term='sun')
print(d.get())