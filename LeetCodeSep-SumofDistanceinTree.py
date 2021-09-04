class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        G = defaultdict(set)
        for i, j in edges:
            G[i].add(j)
            G[j].add(i)
        
        def dfs(node, parent, depth):
            ans = 1
            for neib in G[node]:
                if neib != parent:
                    ans += dfs(neib, node, depth + 1)
            weights[node] = ans
            depths[node] = depth
            return ans
        
        def dfs2(node, parent, w):
            ans[node] = w
            for neib in G[node]:
                if neib != parent:
                    dfs2(neib, node, w + N - 2*weights[neib])
        
        weights, depths, ans = [0]*N, [0]*N, [0]*N
        dfs(0, -1, 0)
        dfs2(0, -1, sum(depths))
        
        return ans
