import pandas as pd
from IPython.display import display, HTML

class FancyParser():
  def __init__(self, file_list):
    '''
    Description:
        This class is used to parse a list of files and return a dataframe with the parsed information.
        Metadata can be included in each columns by using the functions add_col_parse, add_flag, add_flag_from_dict
    Parameters:    
        file_list: list of files to be parsed

    Example:
        file_list = ['file_full_1.txt', 'file_full_2.txt', 'file_empty_3.txt']
        parser = FancyParser(file_list)
        parser.add_col_parse(column_to_parse='file_name', split_string='_', position_split=-1, remove_end = '.txt', new_column='file_number')  # add a column with the file number
        parser.add_flag(column_to_parse='file_name', check_substr='empty', return_type=['empty', 'not_empty'], new_column='file_empty')  # add a column with the file number
        parser.add_flag_from_dict(column_to_parse='file_number', dict_parse={'treatment': [1,3] , 'control': [1] } , new_column='treatment_or_control')  # add a columns using a dictionary as input
        parser.display_df() # display the dataframe with the new columns added using the jupyter notebook interface
        parser.save_to_df(out_path='/path/to/save/file_parsed.txt') # save the dataframe to a file
        parser.capture_files(grouped_by='file_empty') # capture the files grouped by the column 'file_empty'

    '''
    self.files = file_list
    self.df = pd.DataFrame(self. files, columns=['file_path'] )
    self.__create_name__()


  def __create_name__(self):
    '''
    Description:
        This function is used to create the column 'file_name' in the parsed dataframe.
    '''
    self.df['file_name'] =  self.add_col_parse( column_to_parse='file_path', split_string='/', position_split=-1, remove_end = '')


  def add_col_parse(self,  column_to_parse=None, split_string=None, position_split=None, remove_end = '', new_column=None):
    '''
    Description:
        This function is used to create a new column in the parsed dataframe.
    Parameters:
        column_to_parse: str 
            column to be use on the parse function. This column must be present in the dataframe.
        split_string: str
            string to be used to split the column_to_parse
        position_split: int
            position of the element used after split the column_to_parse.
        remove_end: str
            string to be removed from the end of the resultant value after split  and selected by position_split
        new_column: str
            name of the new column created. (This creates a inplace change in the dataframe)
    return:

        Case the new_column is not defined:
            A panda series with the parsing result.
        Case the new_column is defined:
            The FancyParser object will be returned with the new column added.

    '''
    if new_column:
      self.df[new_column] = self.df[column_to_parse].apply(lambda x : x.split(split_string)[position_split].replace(remove_end,''))
    return self.df[column_to_parse].apply(lambda x : x.split(split_string)[position_split].replace(remove_end,''))

  
  def add_flag(self,  column_to_parse=None, check_substr='' , return_type=None, new_column=None):
    '''
    Description:
        This function is used to create a new column in the parsed dataframe by using a binary flag.

    Parameters:
        column_to_parse: str
            column to be use on the parse function. This column must be present in the dataframe.
        check_substr: str
            string to be used to check if the column_to_parse has the substring. EX: 'empty'
        return_type: list
            list of strings to be used to return the binary flag.EX: ['empty', 'not_empty']
        new_column: str
            name of the new column created. (This creates a inplace change in the dataframe)
    return:
        case the new_column is not defined:
            A panda series with the parsing result.
        case the new_column is defined:
            The FancyParser object will be returned with the new column added.


    '''    
    if new_column:
      self.df[new_column] = self.df[column_to_parse].apply(lambda x : return_type[0] if check_substr in x else return_type[1] )
    return self.df[column_to_parse].apply(lambda x : return_type[0] if check_substr in x else return_type[1] )


  def add_flag_from_dict(self,  column_to_parse=None, dict_parse=None, new_column=None):
    '''
    Description:
        This function is used to create a new column in the parsed dataframe by using a dictionary as input.

    
    Parameters:
        column_to_parse: str
            column to be use on the parse function. This column must be present in the dataframe.
        dict_parse: dict
            dictionary to be used to check if the column_to_parse has the substring. EX: {'treatment': [1,3] , 'control': [1] }
            make sure the keys are the same as the return_type
        new_column: str
            name of the new column created. (This creates a inplace change in the dataframe)
    return:
        case the new_column is not defined:
            A panda series with the parsing result.
        case the new_column is defined:
            The FancyParser object will be returned with the new column added.

            
    example:
        dict_parse = {'treatment': ['1','10'] , 'control': ['t1', 't3'] }
        parser.add_flag_from_dict(column_to_parse='file_id', dict_parse=dict_parse, new_column='treatment_or_control')
    '''
    dict_parse_use = { v_i:k  for k,v in dict_parse.items() for v_i in v  }
    print (dict_parse_use)
    if new_column:
      self.df[new_column] = self.df[column_to_parse].apply(lambda x : dict_parse_use[x])
    return self.df[column_to_parse].apply(lambda x : dict_parse_use[x])

  def __repr__(self):
    '''
    Description:
        This function is used to print the FancyParser object.
    '''
    self.display_df()
    return 'teste'

  def show_df(self):
    '''
      Description:
          This function is used to show the FancyParser object.
    '''
    return self.df 

  def display_df(self):
    '''
    Description:
        This function is used to display the FancyParser object.
    '''      
    display(self.df)
    
  def load_from_df(self):
    '''
      Description:
          This function is used to load the FancyParser object from a dataframe.
    '''
    self.df = pd.read_csv(df_file_to_load ,sep='\t')
    
  def save_to_df(self, out_path):
    '''
    Description:
        This function is used to save the FancyParser object to a dataframe.Ex: parser.save_to_df(out_path='/home/user/out_file.txt')
    Parameters:
        out_path: str
            path to save the dataframe.
    
    '''      
    self.df.to_csv(out_path ,sep='\t', index=None)

  def capture_files(self, grouped_by=None):
    '''
        Description:
            This function is used to capture the files from the dataframe.
        Parameters:
            grouped_by: str
                column to be used to group the files.
        return:
            A groupby object contaning a key representing the group and a list of files grouped by the selected column.
    '''
    out_list = []
    for k,v in self.df.groupby(grouped_by):
      out_list.append([k,v['file_path'].values.tolist()])
    return out_list
