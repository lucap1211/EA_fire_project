
import os
import pandas as pd

def process_threat_data(df, collist, output_path):
    dfclean_dfclean = df.copy()
    
    for col in collist:
        clean_df[col] = df[col].str.strip()

    # Initialize appended to False and consolidated narrative to empty string
    clean_df['CURRENT_THREAT_NARR2'] = ''
    for col in collist:
        time_frame = col.split('_')[-1]
        # Strip to make sure not null
        if time_frame == '12':
            # Initialize processed content
            clean_df.loc[clean_df[col] != '', 'prev_narr'] = clean_df['CURRENT_THREAT_12']
            clean_df.loc[clean_df[col] != '', 'time_label'] = time_frame
        else:  # Later time_frame
            # Equal to previous narrative -- add time to time label
            clean_df.loc[
                (clean_df[col] != '') & (clean_df[col].str.lower() == clean_df['prev_narr']
               .str.lower()), 
                'time_label'
            ] = clean_df.time_label + '/' + time_frame
            
            # Not equal -- append and re-initialize
            clean_df.loc[
                (clean_df[col] != '') & (clean_df[col].str.lower() != clean_df['prev_narr']
               .str.lower()), 
                'CURRENT_THREAT_NARR2'
            ] = (
                clean_df.CURRENT_THREAT_NARR2 + 
                "\n" + clean_df.time_label + " Hours: " + clean_df.prev_narr
            )
            clean_df.loc[
                (clean_df[col] != '') & (clean_df[col].str.lower() != clean_df['prev_narr']
               .str.lower()), 
                'time_label'
            ] = time_frame
            clean_df.loc[
                (clean_df[col] != '') & (clean_df[col].str.lower() != clean_df['prev_narr']
               .str.lower()), 
                'prev_narr'
            ] = clean_df[col]

    # Append remaining values
    clean_df['CURRENT_THREAT_NARR2'] = (
        clean_df.CURRENT_THREAT_NARR2 + "\n" + 
        clean_df.time_label + " Hours: " + clean_df.prev_narr
    )
    clean_df['CURRENT_THREAT_NARR2'] = clean_df['CURRENT_THREAT_NARR2'].str.strip()

    # Save the resulting DataFrame to a CSV file
    clean_df.to_csv(output_path, index=False)
