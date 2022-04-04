import pandas as pd
from IPython.display import display, HTML

class FancyParser():
  def __init__(self, file_list):
    self.files = file_list
    self.df = pd.DataFrame(self. files, columns=['file_path'] )
    self.__create_name__()


  def __create_name__(self):
    self.df['file_name'] =  self.add_col_parse( column_to_parse='file_path', split_string='/', position_split=-1, remove_end = '')


  def add_col_parse(self,  column_to_parse=None, split_string=None, position_split=None, remove_end = '', new_column=None):
    
    if new_column:
      self.df[new_column] = self.df[column_to_parse].apply(lambda x : x.split(split_string)[position_split].replace(remove_end,''))
    return self.df[column_to_parse].apply(lambda x : x.split(split_string)[position_split].replace(remove_end,''))

  
  def add_flag(self,  column_to_parse=None, check_substr='' , return_type=None, new_column=None):

    if new_column:
      self.df[new_column] = self.df[column_to_parse].apply(lambda x : return_type[0] if check_substr in x else return_type[1] )
    return self.df[column_to_parse].apply(lambda x : return_type[0] if check_substr in x else return_type[1] )


  def add_flag_from_dict(self,  column_to_parse=None, dict_parse=None , return_type=None, new_column=None):
    '''
      ex:
        dict_parse = {'treatment': [1,2,3,'10','s1'] , 'control': [5,6,7,'t1', 't3'] }
        make sure your column_to_parse has the write type
    '''
    dict_parse_use = { v_i:k  for k,v in dict_parse.items() for v_i in v  }
    print (dict_parse_use)
    if new_column:
      self.df[new_column] = self.df[column_to_parse].apply(lambda x : dict_parse_use[x])
    return self.df[column_to_parse].apply(lambda x : dict_parse_use[x])

  def __repr__(self):
    self.display_df()
    return 'teste'

  def show_df(self):

    return self.df 

  def display_df(self):
    display(self.df)
    
  def load_from_df(self):
    self.df = pd.read_csv(df_file_to_load ,sep='\t')
    
  def save_to_df(self, out_path):
    self.df.to_csv(out_path ,sep='\t', index=None)

  def capture_files(self, grouped_by=None):
    out_list = []
    for k,v in self.df.groupby(grouped_by):
      out_list.append([k,v['file_path'].values.tolist()])
    return out_list
