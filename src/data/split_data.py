


def split_data(data):
    """
    Front function to split the data into train/test/validation/others
    
    Args:
        data (pd.DataFrame): a pandas dataframe with the data filtered to split
        whatever

    Returns:
        splits (list): a list of pandas dataframe with elements such as:
                        element [0]: train set
                        element [1]: validation set
                        element [2]: test set
                        element [3]: others sets
    """

    return [data]