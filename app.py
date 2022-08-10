from flask import Flask, request
import json
import shutil
import time
import threading

# Token generator
from os import urandom
from struct import unpack
from hashlib import sha512

class Application:
    def __init__(self):
        self.app = Flask(__name__)
        self.db = {}

    def routes(self):
        @self.app.route("/api/gentoken")
        def gentoken():
            return self.genToken(int(request.args.get("amount")))
        
        @self.app.route("/api/redeem")
        def redeem():
            t = self.genToken(self.db["tokens"][request.args.get("token")])
            del self.db["tokens"][request.args.get("token")]
            return t
        
        @self.app.route("/api/check")
        def check():
            return str(self.db["tokens"][request.args.get("token")])
            

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
            time.sleep(5)

    def genToken(self, amount : int):
        r = urandom(4)
        u = str(unpack("i", r)[0])
        hash = sha512()
        hash.update(u.encode())
        self.db["tokens"][str(hash.hexdigest())] = amount
        return str(hash.hexdigest())

if __name__ == '__main__':
    app = Application()
    app.loadJson()
    app.routes()
    threading.Thread(target=app.saveJson).start()
    app.app.run()