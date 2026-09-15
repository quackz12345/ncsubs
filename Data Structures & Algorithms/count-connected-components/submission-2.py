class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen = set()
        ans = 0
        for start in range(n):
            if start in seen:
                continue
            
            ans += 1
            queue = deque([start])
            seen.add(start)
            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)

        return ans