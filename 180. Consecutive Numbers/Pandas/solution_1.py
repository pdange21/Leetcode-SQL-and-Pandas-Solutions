import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['diff1'] = logs['num'].diff()
    logs['diff2'] = logs['num'].diff().diff()
    return logs[(logs['diff1'] == 0) & (logs['diff2'] == 0)][['num']].drop_duplicates().rename(columns={'num': 'ConsecutiveNums'})