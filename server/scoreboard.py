import json


class Scoreboard:
    def __init__(self, file) -> None:
        self.file = file
        self.scores = json.load(file)

    def addScore(self, username, score):
        self.scores[username] = score

    def toJSON(self):
        return json.dumps(self.scores)

    def save(self, data):
        self.file.seek(0)
        self.file.write(data)
        self.file.truncate()
