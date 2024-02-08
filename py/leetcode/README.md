# Pandas DataFrame


### DataFrame

```
result_dataframe = pd.**DataFrame**(student_data, columns=column_names)

CREATE TABLE table (student_id, age);
```

```
[players.**shape**[0],players.**shape**[1]]

## Column Count
SELECT COUNT(COLUMN_NAME) FROM players.COLUMNS;

## Row Count
SELECT COUNT(*) FROM players;
```

```
employees.**head**(3)

SELECT TOP 3 * FROM employees;
```



### Selection

```
students.**loc**[students["student_id"] == 101, ["name","age"]] 

SELECT name,age FROM students WHERE student_id = 101;
```

employees['bonus'] = employees['salary']\*2

### Data Cleaning

customers.**drop_duplicates**(subset='email', keep='first',inplace=True)

students.**dropna**(subset=['name'], inplace=True)

employees['salary'] \*= 2

students = students.**rename**(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years"
        }
    )

students = students.**astype**({'grade':int})

products['quantity'].**fillna**(0,inplace=True)


### Reshaping

pd.**concat**([df1,df2], axis=0)

ans = weather.**pivot**(index='month',columns='city',values='temperature')

report = report.**melt**(
        id_vars=["product"],
        value_vars=["quarter_1","quarter_2","quarter_3","quarter_4"],
        var_name="quarter",
        value_name="sales"
    )

filtered_animals = animals[animals['weight'] > 100]

sorted_animals = filtered_animals.**sort_values**(by='weight', ascending=False)

names = sorted_animals[['name']]



