class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.authManager = dict()
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.authManager[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.authManager:
            return
        elif self.authManager[tokenId] <= currentTime:
            del self.authManager[tokenId]
        else:
            self.authManager[tokenId] = currentTime + self.timeToLive
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count, expired = 0, []
        for key, val in self.authManager.items():
            if val <= currentTime:
                expired.append(key)
            else:
                count += 1
        
        for key in expired:
            del self.authManager[key]
        return count
            


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
