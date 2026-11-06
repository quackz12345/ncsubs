class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        queue = deque([(0,-1)])
        seen = {0}
        prev = None
        ans = True
        vs = 0
        while queue:
            node, par = queue.popleft()
            vs+=1
            # do some logic
            
            print(node,"a")
            for neighbor in adj[node]:
                print(neighbor)
                if neighbor in seen and not neighbor == par:
                    return False
                if not neighbor in seen and not neighbor == par:
                    seen.add(neighbor)
                    queue.append((neighbor,node))
        
        return ans and vs == n
        