class FileSystem:

    def __init__(self):
        self.fs = {}
    
    def createPath(self, path: str, value: int) -> bool:
        path = [p for p in path.split('/') if p != '']
        curr = self.fs
        for f in path[:-1]:
            if f not in curr:
                return False
            curr = curr[f]
        lastdir = path[-1]
        if lastdir not in curr:
            curr[lastdir] = {}
            curr[lastdir]['$'] = value
            return True
        else:
            return False
    def get(self, path: str) -> int:
        path = [p for p in path.split('/') if p != '']
        curr = self.fs
        for f in path[:-1]:
            if f not in curr:
                return -1
            curr = curr[f]
        lastdir = path[-1]
        if lastdir not in curr:
            return -1
        return curr[path[-1]].get('$',-1)
         


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)