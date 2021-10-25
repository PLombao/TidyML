


def filter_data(data):
    """
    Front function to filter data to perform a train
    
    Args:
         data (pd.DataFrame): a pandas dataframe with the non-filtered data
        
    Returns:
        filtered_data (pd.DataFrame): a pandas dataframe with the filtered data
    """
    filtered_data = data.copy()
    return data