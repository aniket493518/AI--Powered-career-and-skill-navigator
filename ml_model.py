import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


data_set =pd.read_csv(r"C:\Users\anike\OneDrive\Desktop\final project\student_dataset_10000.csv")
# print(data_set.head)
# print(data_set.columns)
print(data_set.dtypes)
column_to_remove=['student_id','name', 'income_bracket','hindi_comfort','regional_lang_comfort', 'career_interest_1','career_interest_2' ];
dataset1 =data_set.drop(columns=column_to_remove);
# print(dataset1)
# print(dataset1.columns)
# print(dataset1.shape);
# print(dataset1.dtypes);
print("which column contain  null value")
dataset1.isnull().sum()
dataset1['internet_type']=dataset1['internet_type'].fillna("Not_internate");
print(dataset1.isnull().sum())
dataset1['english_comfort']=dataset1['english_comfort'].fillna(dataset1['english_comfort'].mode()[0])
print(dataset1.isnull().sum());
print("number of  dulpicated count: ")
print(dataset1.duplicated().sum())
print("which row are duplicated: ")
print(dataset1[dataset1.duplicated()])
dataset1=dataset1.drop_duplicates();
print("show again  number  of duplicated value")
print(dataset1.duplicated().sum())
# print (dataset1.columns)
dataset1.columns = dataset1.columns.str.replace('_',' ').str.title()
print (" new dataset")
print(dataset1.columns)
dataset1.columns = dataset1.columns.str.replace('Eligible','').str.strip()
print(dataset1.columns)
print(dataset1.isnull().sum())
print(dataset1.dtypes)
print(dataset1.head)
print(dataset1.info())
print(dataset1.describe())
# check  which  column content null  value 
print( "null  value")
print(dataset1.isnull().sum())
#  suppose numeric null value
# dataset1['column name']=dataset1['column_name'].fillna(dataset1['column_name'].median())
#  suppose  dataset content categies value
# dataset1['column_name']=dataset1['colum_name'].fillna(dataset['column_name'].mode()[0]);
print(dataset1.dtypes)
# dataset1['col'] = pd.to_numeric(dataset1['col'], errors='coerce')
# dataset1['col'] = dataset1['col'].astype('category')
#   for english comfort
print(dataset1)
print(dataset1['English Comfort'].unique())
print(dataset1['Current Education Level'].unique())

oe = OrdinalEncoder(categories=[['Basic', 'Moderate', 'Fluent']])
dataset1[['English Comfort']] = oe.fit_transform(dataset1[['English Comfort']])

#  for  physical  health
oe2 = OrdinalEncoder(categories=[['Poor', 'Moderate', 'Good', 'Excellent']])
dataset1[['Physical Health']] = oe2.fit_transform(dataset1[['Physical Health']])

# 
oe3 = OrdinalEncoder(categories=[['Class_10', 'Class_12', 'Diploma_ITI', 'Undergraduate', 'Postgraduate']])
dataset1[['Current Education Level']] = oe3.fit_transform(dataset1[['Current Education Level']])
 
#  check the  unique value 
print(dataset1['State'].nunique())
print(dataset1['District'].nunique())
print(dataset1['Father Occupation'].nunique())
print(dataset1['Mother Occupation'].nunique())
 
#   this  encoder  fro  prediction columns;
le_target = LabelEncoder()
dataset1['Recommended Career'] = le_target.fit_transform(dataset1['Recommended Career'])
#   this is  for  converted into  equal scale 
cols_to_scale = [
    'Age',
    'Family Income Annual',
    'Family Size',
    'Nearest City Km',
    'Nearest College Km',
    'Class 10 Percent',
    'Class 12 Percent'
]
scaler = StandardScaler()
dataset1[cols_to_scale] = scaler.fit_transform(dataset1[cols_to_scale]) 

