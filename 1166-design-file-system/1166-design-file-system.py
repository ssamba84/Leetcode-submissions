class FileSystem:

    def __init__(self):
        self.fs = {}

    def createPath(self, path: str, value: int) -> bool:
        path = path.split('/')[1:]
        curr = self.fs
        
        for files in path[:-1]:
            if files not in curr:
                return False
            curr = curr[files]
        if path[-1] in curr:
            return False
        curr[path[-1]] = {}
        curr[path[-1]]['#'] = value
        return True

    def get(self, path: str) -> int:
        path = path.split('/')[1:]
        curr = self.fs

        for files in path:
            if files in curr:
                curr = curr[files]
            else:
                return -1
        
        return curr.get('#',-1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)