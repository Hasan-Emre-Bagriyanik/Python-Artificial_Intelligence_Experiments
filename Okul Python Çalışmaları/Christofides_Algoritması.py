
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

# Grafigi tanımlama yapiyoruz
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]


    # En kisa yol uzunluklarini yazdiriyoruz
    def print_solution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])



    # En kisa yol uzunluklarini algoritmayla hesapliyoruz
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        parent = [-1] * self.V
        parent[src] = -1

        for cout in range(self.V - 1):
            u = self.min_distance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                    parent[v] = u


        # Minimum kesim agacinin hesaplanmasi
        tree = self.create_mst(parent)

        # Cift dereceli dugumlerin hesaplanmasi
        odd_vertices = self.find_odd_degrees(tree)

        # Minimum esleme algoritmasinin kullanilmasi
        matching = self.perfect_matching(odd_vertices, tree)

        # Eslestirme sonucunda olusan grafigin Euler turuna donusturulmesi
        euler_circuit = self.create_euler_circuit(matching, tree)

        # Euler turunun Hamilton dongusune donusturulmesi
        return self.create_hamiltonian_circuit(euler_circuit)



    # En kisa mesafeli dugumun indisini dondurme
    def min_distance(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index



    # Minimum kesim agacinin hesaplanmasi
    def create_mst(self, parent):
        tree = [[0 for column in range(self.V)]
                for row in range(self.V)]
        for i in range(1, self.V):
            tree[parent[i]][i] = self.graph[i][parent[i]]
            tree[i][parent[i]] = self.graph[i][parent[i]]
        return tree



    # Cift dereceli dugumlerin bulunmasi
    def find_odd_degrees(self, tree):
        odd_vertices = []
        for i in range(self.V):
            if sum(tree[i]) % 2 != 0:
                odd_vertices.append(i)
        return odd_vertices



    # Minimum esleme algoritmasi
    def perfect_matching(self, odd_vertices, tree):
        pairs = {}
        min_distance = sys.maxsize
        for i in range(len(odd_vertices) - 1):
            for j in range(i + 1, len(odd_vertices)):
                distance = self.graph[odd_vertices[i]][odd_vertices[j]]
                if distance < min_distance:
                    min_distance = distance
                    pairs = {odd_vertices[i]: odd_vertices[j]}
        return pairs
    
    
    
    # Euler turunun hesaplanmasi
    def create_euler_circuit(self, matching, tree):
        for key in matching.keys():
            tree[key][matching[key]] = tree[matching[key]][key] = \
                self.graph[key][matching[key]]
        graph = tree
        stack = [0]
        circuit = []
        while stack:
            vertex = stack[-1]
            if any(graph[vertex]):
                for v in range(self.V):
                    if graph[vertex][v] != 0:
                        graph[vertex][v] = graph[v][vertex] = 0
                        stack.append(v)
                        break
            else:
                circuit.append(stack.pop())
        return circuit[::-1]
    
    
    
    # Euler turunun Hamilton dongusune donusturulmesi
    def create_hamiltonian_circuit(self, euler_circuit):
        visited = [False] * self.V
        hamiltonian_circuit = []
        for vertex in euler_circuit:
            if not visited[vertex]:
                hamiltonian_circuit.append(vertex)
                visited[vertex] = True
        return hamiltonian_circuit + [euler_circuit[0]]
    

# Burada da sinifin cagrilmasi ve bir ornek ile calistirilmasi
graph = Graph(5)
graph.graph = [[0, 5, 8, 3, 1],[5, 0, 6, 7, 2],[8, 6, 0, 1, 4],[3, 7, 1, 0, 6],[1, 2, 4, 6, 0]]
print(graph.dijkstra(0))




