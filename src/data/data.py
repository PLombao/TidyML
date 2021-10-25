from import_data import import_data
from filter_data import filter_data
from split_data import split_data

class Data():
    """
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

