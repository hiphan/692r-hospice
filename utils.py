import pandas as pd
import os


def file_to_df(file_name):
    df = pd.read_excel(file_name)
    return df


# process dataframe for the IDHER table
def process_df(df):
    d = {}
    for _, row in df.iterrows():
        patient_id = row['PatientID']
        if 'IDEHR' in df.columns:
            idehr = row['IDEHR']
        elif 'EHRID' in df.columns:
            idehr = row['EHRID']
        if patient_id in d and idehr not in d[patient_id]:
            d[patient_id].append(idehr)
        else:
            d[patient_id] = [idehr]

    for k in d.keys():
        d[k].sort()
    return d


def get_table(files):
    big_table = {}
    for f in files:
        f_name = f.split('.')[0]
        curr_df = file_to_df(f)
        print(curr_df.columns.values)
        curr_table = process_df(curr_df)
        big_table[f_name] = curr_table

    return big_table

