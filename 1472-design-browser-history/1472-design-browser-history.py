class Page:
    def __init__(self,pageName):
        self.value=pageName
        self.next=None
        self.prev=None

        # google -> linked -> 
        #        <- 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Page(homepage)
        
    def visit(self, url: str) -> None:
        
        self.current.next = Page(url)
        self.current.next.prev = self.current
        self.current=self.current.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.prev:
                self.current=self.current.prev
        return self.current.value

            


    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next:
                self.current=self.current.next
        return self.current.value
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)