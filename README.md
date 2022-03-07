# FancyParser
Create and access your analyses files on the fly using a simple dataframe metadata estructure .  

__How to install__:  
```
!pip uninstall FancyParser -y
!pip install git+https://github.com/diegotsouza/fancy_parser.git

```



__Example__  


```python3
# Case in the jupyter notebook
!find .| grep bam  
files = experiment  = FancyParser(files)

experiment.show_df()
experiment.df['file_name'] =   experiment.add_col_parse( column_to_parse='file_path', split_string='/', position_split=-1, remove_end = '')
experiment.df['replicate'] =     experiment.add_col_parse('file_name', '-', 1,'.bam')
#Create a function to treate this cases
experiment.df['mark'] = experiment.df['file_name'].apply(lambda x : x.split('_')[1].split('-')[0]) # create a function for this situation

experiment.df['is_TF']     =     experiment.add_flag('mark', 'CTC', ['TF', 'HISTONE_MARK'])


```
