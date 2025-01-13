#my_functions.py

def pad_column_values(data, column_name, target_length, pad_char='0'):
    """
    Pads the values in the specified column of a DataFrame to a desired character count.

    Parameters:
    - data (pd.DataFrame): The input DataFrame.
    - column_name (str): The name of the column to process.
    - target_length (int): The desired character count after padding.
    - pad_char (str): The character to use for padding (default: '0').

    Returns:
    - pd.DataFrame: The updated DataFrame with padded column values.
    """
    if column_name in data.columns:
        # Ensure the column is in string format
        data[column_name] = data[column_name].astype(str)
        print(f"Ensuring '{column_name}' values are treated as strings.")

        # Count occurrences of each length
        length_counts = data[column_name].str.len().value_counts().sort_index()
        print(f"Character counts for '{column_name}' before padding:\n{length_counts}")

        # Apply padding to ensure all values meet the target length
        data[column_name] = data[column_name].apply(lambda x: x.rjust(target_length, pad_char))
        print(f"Applied padding to '{column_name}' using '{pad_char}' to reach {target_length} characters.")

        # Validate results
        invalid_rows = data[data[column_name].str.len() != target_length]
        if not invalid_rows.empty:
            print(f"Warning: The following rows have '{column_name}' values that are not {target_length} characters long:\n{invalid_rows}")
        else:
            print(f"All '{column_name}' values are now exactly {target_length} characters long.")
    else:
        print(f"The column '{column_name}' does not exist in the data.")

    return data