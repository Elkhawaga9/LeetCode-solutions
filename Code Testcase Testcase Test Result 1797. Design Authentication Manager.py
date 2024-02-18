from collections import defaultdict
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tockens = defaultdict(int)
        self.t = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tockens[tokenId] = (currentTime + self.t)


    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tockens[tokenId] > currentTime:
            self.tockens[tokenId] = currentTime + self.t

        else:
            del self.tockens[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans = 0
        for key in self.tockens:
            if self.tockens[key]>currentTime:
                ans+=1
        return ans
        

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
