import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    result_df = person.merge(address[['personId', 'city', 'state']], on='personId', how='left')

    result_df = result_df[['firstName', 'lastName', 'city', 'state']]
    
    return result_df