class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        n = len(bookings)
        ans = [0 for i in range(bookings[n-1][1]+2)]
        for f,l,s in bookings:
            ans[f]+=s
            ans[l+1]-=s
        for i in range(1,len(ans)):
            ans[i]+=ans[i-1]
        return ans[1:len(ans)-1]
        