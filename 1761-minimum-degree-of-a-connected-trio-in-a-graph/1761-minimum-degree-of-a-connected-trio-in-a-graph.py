class Solution:
	def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
		graph = defaultdict(set)
		degree = defaultdict(int)
		result = sys.maxsize

		for u,v in edges:
			graph[min(u,v)].add(max(u,v))
			degree[u] += 1
			degree[v] += 1

		for n1 in range(1,n+1):
			for n2 in graph[n1]:
				for n3 in graph[n1]:
					if n3 in graph[n2]:
						result = min(result, degree[n1]+degree[n2]+degree[n3]-6)

		return result if result < sys.maxsize else -1