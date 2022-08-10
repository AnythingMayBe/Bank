from flask import Flask
import json
import shutil
import time
import threading

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
        while True:
            shutil.copyfile("db.json", "backups/" + str(time.time()))
            with open("db.json", "w") as file:
                file.write(json.dumps(self.db))
                file.close()
            time.sleep(360)

if __name__ == '__main__':
    app = Application()
    app.loadJson()
    app.routes()
    threading.Thread(target=app.saveJson).start()
    app.app.run()