import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    #More readable query
    result = pd.merge(person, address, on='personId', how='left')

    return result[['firstName', 'lastName', 'city', 'state']]