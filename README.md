# FancyParser
Create and access your analyses files on the fly using a simple dataframe metadata estructure .  

__How to install__:  
```
!pip uninstall FancyParser -y
!pip install git+https://github.com/LucasSilvaFerreira/fancy_parser.git

```



__Example__  


```python3
# Case in the jupyter notebook
!find .| grep bam  
files = experiment  = FancyParser(files)

experiment.show_df()
experiment.df['replicate'] =     experiment.add_col_parse('file_name', '-', 1,'.bam')
#Create a function to treate this cases
experiment.df['mark'] = experiment.df['file_name'].apply(lambda x : x.split('_')[1].split('-')[0]) # create a function for this situation

experiment.df['is_TF']     =     experiment.add_flag('mark', 'CTC', ['TF', 'HISTONE_MARK'])


```


```python3

The input data will be a list of  8 fastq.gz files being two treatments and two controls with a paired-end and replicates.

files_to_parse = ['/data/rnaseq/fastq/sample_0_replicate1_treatment_R1.fastq.gz',
 '/data/rnaseq/fastq/sample_1_replicate1_treatment_R2.fastq.gz',
 '/data/rnaseq/fastq/sample_2_replicate1_control_R1.fastq.gz', 
'/data/rnaseq/fastq/sample_3_replicate1_control_R2.fastq.gz',
 '/data/rnaseq/fastq/sample_4_replicate2_treatment_R1.fastq.gz',
 '/data/rnaseq/fastq/sample_5_replicate2_treatment_R2.fastq.gz',
 '/data/rnaseq/fastq/sample_6_replicate2_control_R1.fastq.gz',
 '/data/rnaseq/fastq/sample_7_replicate2_control_R2.fastq.gz'] 

files_fancy_object = FancyParser(files_to_parse)
#capture the samples id_number
files_fancy_object.add_col_parse('file_name', '_', 1, name_column='ID')
#use the id_number to create a new column with the sample category
files_fancy_object.add_flag_from_dict(column_to_parse='ID', dict_parse={'treatment':['0','2','4','6'],'control':['1','3','5','7']}, new_column='treatment_or_control')
#capturing the parired-end information R1 or R2 files
files_fancy_object.add_col_parse('file_name', '_', 4, name_column='paired_end')
# Extract the samples using the FancyParser object (flag:'treatment_or_control')
for k,v in files_fancy_object.capture_files(grouped_by='treatment_or_control'):
  print (k,v)
#I need to check if this is working


```
