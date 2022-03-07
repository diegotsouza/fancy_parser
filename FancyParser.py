import pandas as pd
from IPython.display import display, HTML

class FancyParser():
  def __init__(self, file_list):
    self.files = file_list
    self.df = pd.DataFrame(self. files, columns=['file_path'])

  def add_col_parse(self,  column_to_parse=None, split_string=None, position_split=None, remove_end = ''):

    return self.df[column_to_parse].apply(lambda x : x.split(split_string)[position_split].replace(remove_end,''))

  
  def add_flag(self,  column_to_parse=None, check_substr='' , return_type=None):


    return self.df[column_to_parse].apply(lambda x : return_type[0] if check_substr in x else return_type[1] )

  def __repr__(self):
    self.display_df()
    return 'teste'

  def show_df(self):

    return self.df 

  def display_df(self):
    display(self.df)
    
  def load_from_df(self):
    self.df = pd.read_csv(df_file_to_load ,sep='\t')
 
