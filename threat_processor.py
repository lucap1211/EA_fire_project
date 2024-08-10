
import os
import pandas as pd

def process_threat_data(df, collist, output_path):
    """
    Process and consolidate threat reporting data across multiple time frames, 
    generating a narrative.

    This function takes a DataFrame with multiple columns representing threat 
    levels at different time frames and processes the data to create a 
    consolidated narrative. The narrative tracks how the threat level changes 
    over time and appends the information into a new column 
    (`CURRENT_THREAT_NARR2`). 
    The processed DataFrame is then saved to a CSV file.

    Parameters:
    -----------
    df : pandas.DataFrame
        The input DataFrame containing the threat level data to be processed. 
        Must contain columns specified in `collist`.

    collist : list of str
        A list of column names in `df` that represent the threat levels at 
        different time frames('CURRENT_THREAT_12', 'CURRENT_THREAT_24', etc.).

    output_path : str
        The file path where the processed DataFrame will be saved as CSV file.

    Returns:
    --------
    None
        The function saves the processed DataFrame to specified `output_path`.
    
    Example:
    --------
    >>> process_threat_data(
               dfsub, 
               ['CURRENT_THREAT_12', 'CURRENT_THREAT_24', 'CURRENT_THREAT_48'],
                'output.csv')
    
    Notes:
    ------
    The function assumes that the columns specified in `collist` contain string
    data and that missing values have been filled with empty strings ('').
    """
               
    # Make a copy of the DataFrame to avoid modifying the original data                      
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
