from import_data import import_data
from filter_data import filter_data
from split_data import split_data

class Data():
    """
    Abstract class representing the origin data to perform a ML train.

    Methods:
        import_data:    import the data from the source/s
        filter_data:    select the instances of the data to train and pre-clean it (clean inference-input wise)
        split_data:     perform the split of the data in [train, test, validation, others]

    Attrs:
        
    """

    def __init__(self):
        pass

    def import_data(self):
        data = import_data()

        return data

    
    def filter_data(self, data):
        data = filter_data(data)
        return data

    
    def split_data(self, data):
        train_split = split_data(data)
        return train_split

