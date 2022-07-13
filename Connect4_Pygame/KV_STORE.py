import requests
import urllib
 
 
class KVScore:
    BASE_URL = "https://keyvalue.immanuel.co/api/KeyVal/"
 
    def __init__(self, app_key=None):
        if app_key:
            self.app_key = app_key
        else:
            self.get_app_key()
 
    def get_app_key(self):
        resp = requests.get(f"{self.BASE_URL}/GetAppKey")
        self.app_key = resp.text[1:-1]
 
    def set_value(self, key, value):
        encoded_value = urllib.parse.quote(value)
        resp = requests.post(
            f"{self.BASE_URL}/UpdateValue/{self.app_key}/{key}/{encoded_value}"
        )
        return resp
 
    def get_value(self, key):
        resp = requests.get(
            f"{self.BASE_URL}/GetValue/{self.app_key}/{key}"
        )
        return resp.text[1:-1]
 
    def encode_data(self, grid, playersign):
        s = ""
        for x in range(0, 6):
            s += "".join(grid[f"row{x}"])
        s += playersign
        return s
 
    def decode_data(self, data):
        grid = {}
        for x in range(0, 6):
            grid[f"row{x}"] = list(data[x*7:(x+1)*7])
 
        playersign = data[-1]
        return grid, playersign
 
    def store_game(self, game_id, grid, playersign):
        self.set_value(game_id, self.encode_data(grid, playersign))
 
    def get_game(self, game_id):
        return self.decode_data(self.get_value(game_id))