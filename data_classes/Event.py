
class Event():
    def __init__(self, id, name, type, tags=None, time=False, duration= False, daily=False):
        self.id = id
        self.name = name
        self.type = type
        self.tags = tags
        self.time = time
        self.duration = duration
        self.daily = daily



    def serialize(self):
        """prepare to put in database"""
        pass

    def deserialize(self):
        pass

    def save(self):
        """jobs:
        save new events
        alert user of problems doing so. IE. duplicate data_classes or other error"""
        pass

    def update(self, table, data):
        """jobs:
        update info for even on given table
        alert user of issue
        update ui if neccesary
        """
        pass

    def basic_display_info(self):
        """get info for display in minimum form. ie. from calendar view"""
        pass

    def full_display_info(self):
        """get info for detailed view"""
        pass


    def get_id(self):
        pass
    def get_name(self):
        pass
    def get_type(self):
        pass
    def get_tags(self):
        pass
    def get_time(self):
        pass
    def get_time(self):
        pass
    def get_duration(self):
        pass
    def get_daily(self):
        pass