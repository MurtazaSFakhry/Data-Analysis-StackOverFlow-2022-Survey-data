import pandas
import pandas as pd

data = pd.read_csv("survey_results_public.csv")
schema_data = pd.read_csv("survey_results_schema.csv")

#df = data[["LanguageHaveWorkedWith", "YearsCode", "Country", "Age"]]
#print(df)

#young = data.loc[data['Age'] == "18-24 years old"]
#print(young)

#print(data[["Age", "Gender"]].value_counts())

#Age = data['Age']

#data.set_index("Age")

#print(data['LanguageHaveWorkedWith'].notnull().sum())

# filt = (data["Age"] == 'Under 18 years old') & \
#        (data["Country"] == 'United States of America')
# print(filt)

#result = data["Age", "Country", "Gender", "LanguageHaveWorkedWith"]

#youngest = data.loc[(data['WorkExp'].isnull()) &
                    #(data['Country'] == 'United States of America') &
                    #(data['Age'] == "18-24 years old")]



#languages = data['LanguageHaveWorkedWith'].str.split(';', expand = True)
#print(languages)
#print(languages.stack().value_counts())

#print(data['Country'].value_counts())

#youngest.to_csv('filetered.csv')


#print(data.ResponseId)

#filt = (data["Age"] == 'Under 18 years old') & (data["Country"] == 'United States of America')
#data[filt]

#women = data[data["Gender"] == "Women"]

#print(women)
#Filt returns Only respondents Under 18 and their country being USA.

#fil = data[data['Age'] == 'Under 18 years old' &
           #data['LanguageHaveWorkedWith'].str.contains('Python')]


#print(fil)

languages = data["LanguageHaveWorkedWith"].str.split(';', expand = True)
languages.stack().value_counts()
print(languages.stack().value_counts())

