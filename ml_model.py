import pandas as pd




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