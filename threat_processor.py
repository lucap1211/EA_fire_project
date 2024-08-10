
import os
import pandas as pd

def process_threat_data(df, collist, output_path):
    df = df.copy()
    
    for col in collist:
        df[col] = df[col].str.strip()

    # Initialize appended to False and consolidated narrative to empty string
    df['CURRENT_THREAT_NARR2'] = ''
    for col in collist:
        time_frame = col.split('_')[-1]
        # Strip to make sure not null
        if time_frame == '12':
            # Initialize processed content
            df.loc[df[col] != '', 'prev_narr'] = df['CURRENT_THREAT_12']
            df.loc[df[col] != '', 'time_label'] = time_frame
        else:  # Later time_frame
            # Equal to previous narrative -- add time to time label
            df.loc[
                (df[col] != '') & (df[col].str.lower() == df['prev_narr']
               .str.lower()), 
                'time_label'
            ] = df.time_label + '/' + time_frame
            
            # Not equal -- append and re-initialize
            df.loc[
                (df[col] != '') & (df[col].str.lower() != df['prev_narr']
               .str.lower()), 
                'CURRENT_THREAT_NARR2'
            ] = (
                df.CURRENT_THREAT_NARR2 + 
                "\n" + df.time_label + " Hours: " + df.prev_narr
            )
            df.loc[
                (df[col] != '') & (df[col].str.lower() != df['prev_narr']
               .str.lower()), 
                'time_label'
            ] = time_frame
            df.loc[
                (df[col] != '') & (df[col].str.lower() != df['prev_narr']
               .str.lower()), 
                'prev_narr'
            ] = df[col]

    # Append remaining values
    df['CURRENT_THREAT_NARR2'] = (
        df.CURRENT_THREAT_NARR2 + "\n" + 
        df.time_label + " Hours: " + df.prev_narr
    )
    df['CURRENT_THREAT_NARR2'] = df['CURRENT_THREAT_NARR2'].str.strip()

    # Save the resulting DataFrame to a CSV file
    df.to_csv(output_path, index=False)
