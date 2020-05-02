from MongoAPI import MongoAPI

# 3. Create fitbit api class that can
        # - get desired data without using a library
        # - figure out oauth2 without using a library 

class fitbit(MongoAPI):

    def __init__(self, user):
        self._user = user
        # should store keys 

