class Solution:
    def simplifyPath(self, path: str) -> str:
        respath = []
        for d in path.split('/'):
            if d == '.' or len(d) == 0:
                continue
            if d == '..':
                if len(respath) > 0:
                    respath.pop()
            elif len(d) > 0:
                respath.append(d)
        return "/"+"/".join(respath)