# 12/08/2026
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pvt = weather.pivot(index = 'month', columns = 'city', values = 'temperature')
    return pvt