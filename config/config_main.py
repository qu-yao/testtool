import configparser


class Config(object):
    def __init__(self, path):
        self.path = path
        self.cf = configparser.ConfigParser()
        self.cf.read(path, encoding='UTF-8')
        self.rd = self.cf
        self.wt = self.cf

    def configread(self, key):
        data = self.rd.get("data", key)
        return data

    def configwrite(self, key, value):
        self.wt.set("data", key, value)

    def configwritesave(self):
        with open(self.path, 'w', encoding="UTF-8") as f:
            self.wt.write(f)
