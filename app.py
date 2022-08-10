from flask import Flask
import json

class Application:
    def __init__(self):
        self.app = Flask(__name__)
        self.db = {}

    def routes(self):
        pass

    def loadJson(self):
        with open("db.json", "r") as file:
            self.db = json.loads(file.read())
            file.close()

    def saveJson(self):
        pass

if __name__ == '__main__':
    app = Application()
    app.loadJson()
    app.routes()
    
    app.app.run()