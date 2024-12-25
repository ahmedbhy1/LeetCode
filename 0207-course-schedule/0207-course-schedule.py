class Solution:
    def __init__(self):
        self.vis = [0]*2001

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        mapp = defaultdict(list)

        for i in prerequisites:
            mapp[i[0]].append(i[1])

        def dfs(x,firstInt,nb,rec_vis):
            if rec_vis[x] == 1:
                return False
            if self.vis[x] == 1:
                return True
            rec_vis[x] = 1
            self.vis[x] = 1
            test = True
            for i in mapp[x]:
                test2= dfs(i,firstInt,nb+1,rec_vis.copy())
                test = test and test2
            return test


        test = True
        self.vis = [0]*2001
        for i in range(numCourses):
            if (i in mapp):
                if (self.vis[i] == 0 and dfs(i,i,0,rec_vis = [0]*2001) == False):
                    test = False
                    break
            
        return(test)
