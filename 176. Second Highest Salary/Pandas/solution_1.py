import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    #adding a rank column which contains rank based on salary and the dense function handles the duplicate values
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)

    #getting the list of all the employees with rank 2
    second = employee[employee['rank'] == 2]

    #dataframe with the column name and if it is empty then return None else return the second highest salary
    return pd.DataFrame({'SecondHighestSalary': [None if len(second) == 0 else second['salary'].iloc[0]]})
