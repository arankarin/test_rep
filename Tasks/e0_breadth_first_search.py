from typing import Hashable, List
import networkx as nx
from collections import  deque


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	print(g, start_node)
	return list(g.nodes)


def bfs_find(graph, src, dst):
	visited = {node: False for node in graph.nodes()}
	parents = {src: src}

	deque_node = deque()
	deque_node.appendleft(src)
	#visited[src] = True

	while True:
		try:
			src = deque_node.pop()
			visited[src] = True
			for node in graph.adj[src]:
				if not visited[node]:
					deque_node.appendleft(node)
					parents[node] = parents[src] + node
				if node == dst:
					return parents[node]

		except IndexError:
			return  None



if __name__ == "__main__":
	graph = nx.Graph()
	graph.add_nodes_from("ABCDEFG")
	graph.add_edges_from(

		[
			("A", "B"),
			("A", "C"),
			("B", "D"),
			("B", "E"),
			("C", "F"),
			("E", "G"),
			("Q", "W"),

		]
	)

	src = "B"
	dst = "W"

	print(bfs_find(graph, src,dst))