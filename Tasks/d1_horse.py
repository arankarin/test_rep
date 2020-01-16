import networkx
import matplotlib

def calculate_paths(shape: (int, int), point: (int, int)) -> int:
	"""
	Given field with size rows*cols count available paths from (0, 0) to point

	:param shape: tuple of rows and cols (each from 1 to rows/cols)
	:param point: desired point for horse
	:return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
	"""
	print(shape, point)
	return 0

def dfs_find(graph, src, dst, visited):
	if src == dst:
		return True
	visited[src] = True


if __name__ == "__main__":
	graph = networkx.nx.Graph()
	graph.add_nodes_from("ABCDEFG")
	graph.add_edges_from(

		[
			("A", "B"),
			("A", "C"),
			("B", "D"),
			("B", "E"),
			("C", "F"),
			("E", "G"),
		]
	)

	src = "A"
	dst = "F"
	visited = {node: False for node in graph.nodes()}
	for node in graph.adj:
		print(node, graph.adj[node])