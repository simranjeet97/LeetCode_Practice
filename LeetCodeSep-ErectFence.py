class Solution:
    def outerTrees(self, points):
        def cross(p1, p2, p3):
            return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

        start = min(points)
        points.pop(points.index(start))
        points.sort(key=lambda p: (atan2(p[1]-start[1], p[0]-start[0]), -p[1], p[0]))
        
        last = len(points) - 1
        while last > 0 and cross(start, points[-1], points[last - 1]) == 0:
            last -= 1
            
        points[last:] = sorted(points[last:], key = lambda p: (-p[0]))

        ans = [start]
        for p in points:
            ans.append(p)
            while len(ans) > 2 and cross(*ans[-3:]) < 0:
                ans.pop(-2)
        return ans
