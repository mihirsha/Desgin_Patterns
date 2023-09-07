class Singleton:
    
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("method already created")
        else:
            Singleton.__instance = self

S1 = Singleton.getInstance()
S2 = Singleton.getInstance()
S3 = Singleton.getInstance()
print(S1, S2, S3)