class Codec:
    def __init__(self):
        self.ht = []
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.ht.append(longUrl)
        return str(len(self.ht))

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.ht[int(shortUrl)-1]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))