from db_helper import COLUMN_NAMES


class Citation:
    def __init__(self, data):
        # the code below filter the data from the db.
        # it deletes all the key that have no value assosiated with them
        self.data = {}
        for i, value in enumerate(data):
            if value:
                self.data[COLUMN_NAMES[i]] = value

    def __str__(self):
        return str(self.data)

    def get_entrys(self):
        return self.data.keys()
