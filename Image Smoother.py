class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        ans = []
        for i in range(len(img)):
            t = []
            for j in range(len(img[0])):
                ele = 0
                cnt = 0
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        if 0<=y<len(img[0]) and 0<=x<len(img):
                            ele += img[x][y]
                            cnt += 1

                t.append(ele//cnt)
            ans.append(t)
        return ans

