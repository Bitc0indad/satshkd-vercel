import pandas as pd
import json

def get_data_from_file(datafile):
    with open(datafile, '+r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    datafile = "hkd_historical"
    df = get_data_from_file(datafile)

    # Check for duplicates
    duplicates = df.duplicated(keep="first")
    
    # Remove duplicate rows
    df = df[~duplicates]
    
    # Print the updated DataFrame
    print(df)

    print(df.duplicated().any())   #Output: False