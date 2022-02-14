import json 

class http():
    def __init__(self, client):
        self.client = client 

        self.datas = {}
    
    async def get_file(self, path : str):
        if path not in self.datas:
            with open(path) as f:
                self.datas[path] = json.load(f)

        return self.datas[path]
    
    async def save_to_file(self, path : str, data : json):
        self.datas[path] = data
        with open(path, "w") as f:
            json.dump(self.datas[path], f, indent=4)
        return self.datas[path]
    
    def get_file_sync(self, path : str):
        if path not in self.datas:
            with open(path) as f:
                self.datas[path] = json.load(f)

        return self.datas[path]