from flask import Flask

class Application:
    def __init__(self):
        self.app = Flask(__name__)
        self.db = {}

    def routes(self):
        pass

    def loadJson(self):
        pass

    def saveJson(self):
        pass

if __name__ == '__main__':
    app = Application()
    app.loadJson()
    app.routes()
    
    app.app.run()