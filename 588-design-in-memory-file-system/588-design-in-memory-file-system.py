class FileSystem:

    def __init__(self):
        self.fs = {}
        '''
        fs is a hashtable
        key is file/dirname 
        value is a tuple (isdir:X)
        X is a ht if isdir is true
        X is a string if isdir is false
        '''
    def traversetoorcreate(self, path):
        curr = self.fs
        for files in path:
            if files not in curr:
                curr[files] = (True,{})
            curr = curr[files][1]
        return curr
    def ls(self, path: str) -> List[str]:
        
        path = [files for files in path.split('/') if files!='']
        curr = self.traversetoorcreate(path)
        res = list(curr.keys())
        res.sort()
        return res
    
        
    def mkdir(self, path: str) -> None:
        path = [files for files in path.split('/') if files!='']
        curr = self.traversetoorcreate(path[:-1])
        lastdir = path[-1]
        if lastdir not in curr:
            curr[lastdir] = (True,{})
    def addContentToFile(self, path: str, content: str) -> None:
        path = [files for files in path.split('/') if files!='']
        curr = self.traversetoorcreate(path)
        file = path[-1]
        if file not in curr:
            curr[file] = (False,content)
        else:
            curr[file] = (False,curr[file][1]+content)
    def readContentFromFile(self, path: str) -> str:
        path = [files for files in path.split('/') if files!='']
        curr = self.traversetoorcreate(path)
        file = path[-1]
        return curr[file][1]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)