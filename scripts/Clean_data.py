#Load Dataset

import pandas as pd
df = pd.read_csv("data/Hospital_raw.csv")

#Cleaning Bed_ID
df['Bed_ID'] = df['Bed_ID'].fillna('0')
df['Bed_ID'] = df['Bed_ID'].astype(int)
print(df['Bed_ID'])

#Dpt_ID looks already clean
print(df["Dpt_ID"].tail(50))

#Removing Duplicate rows
df = df.drop_duplicates()
print(df.info())

#ID column looks perfect
print(df['ID'].tail(50))


print(df['Name'].head(50))
#Name is uncleaned

#separating first and last name
df[['First_Name', 'Last_Name']] = df['Name'].str.split(',', n=1, expand=True)
print(df[['First_Name', 'Last_Name']])
df = df.drop('Name', axis=1)

#Gender columns looks clean
print(df['Gender'].head(50))
print(df['Gender'].tail(50))

#Both the City and State columns are perfect
print(df[['City', 'State']].head(50))
print(df[['City', 'State']].tail(50))

# These all three columns are also clean
print(df[['Age', 'Patient type', 'Status']])

#The Bed column has null values
print(df[['treatemencost', 'Bed', 'LOS']])
print(df['Bed'])

#Filling Null values to Not Occupied
df['Bed'] = df['Bed'].fillna('Not Occupied')
print(df['Bed'].head(50))

#Formatting ER_Time
df['ER_Time'] = df['ER_Time'].fillna("0")
print(df['ER_Time'])

#Refining ER_Time
df['ER_Time'] = df['ER_Time'].astype(int)
df['ER_Time'] = df['ER_Time'].apply(
    lambda x: f"{x//60} Hrs {x%60} mins" if x>=60 else f"{x} mins"
)
print(df['ER_Time'])

#Date format is correct for all row, lets remove the unnecessary time from it
print(df['Date'].head(50))
df[['Admit_Date', 'TimeStamp']] = df['Date'].str.split(' ', n=1, expand=True)
print(df[['Admit_Date', 'TimeStamp']])

df = df.drop('TimeStamp', axis= 1)
df = df.drop('Date', axis=1)

#Feedback and Rating Columns are perfect
print(df[['Feedback', 'Rating']].head(50))

#When we have actual Age then why we need Age bucket let's remove it
print(df['Age Bucket'])

df = df.drop('Age Bucket', axis = 1)

#FZ me column is perfect
print(df['FZ me'].tail(50))
print(df.columns)

#Changing Column Names
df = df.rename(columns= {
    'LOS' : 'Length of Stay',
    'treatemencost' : 'Treatment Cost'
})

df['Length of Stay'] = df['Length of Stay'].astype(str) + ' Days'


#Rearranging the columns
df = df[['Staff_Id', 'Bed_ID', 'Dpt_ID', 'ID', 'First_Name', 'Last_Name', 'Gender', 'City', 'State',
       'Age', 'Patient type', 'Status', 'Treatment Cost', 'Bed', 'Length of Stay',
       'ER_Time', 'Admit_Date', 'Feedback', 'Rating', 'Custom', 'FZ me']]

#Lets remove the unnecessary column which is not required for analysis
df = df.drop(['Custom', 'FZ me'], axis = 1)
print(df.head(50))
print(df.info())

df = df.reset_index()
df.to_excel("Hospital_cleaned.xlsx", index=False)
df.to_csv("Hospital_Cleaned.csv", index = False)