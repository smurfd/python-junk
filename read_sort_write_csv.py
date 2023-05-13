import pandas

df = pandas.read_csv('sample.csv',  index_col='Bug ID', parse_dates=['Updated'], header=0, names=['Bug ID','Type','Summary',
  'Product','Component','Assignee','Status','Resolution','Updated'])
df.sort_values(['Bug ID'], axis=0, ascending=[True],  inplace=True)
df.to_csv('sorted.csv')
