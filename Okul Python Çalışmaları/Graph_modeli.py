# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 09:45:50 2023

@author: Hasan Emre
"""

import heapq

def dijkstra(graph, start, end):
    # Başlangıç düğümünden diğer düğümlere olan minimum mesafeleri saklayacak bir sözlük oluşturuyoruz.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Her düğümün önceki düğümünü saklayacak bir sözlük oluşturuyoruz.
    previous_nodes = {node: None for node in graph}
    
    # Henüz ziyaret edilmemiş düğümleri saklayacak bir öncelik kuyruğu oluşturuyoruz.
    # (uzaklık, düğüm) çiftleri öncelik kuyruğuna eklenir, böylece öncelik küçük olan önce çıkar.
    unvisited_nodes = [(0, start)]
    heapq.heapify(unvisited_nodes)
    
    while unvisited_nodes:
        # Öncelik kuyruğundan en kısa mesafeye sahip düğümü alıyoruz.
        current_distance, current_node = heapq.heappop(unvisited_nodes)
        
        # Eğer bu düğüm hedef düğüm ise, en kısa yol bulundu demektir. Geriye yolu oluşturup döndürüyoruz.
        if current_node == end:
            path = []
            while previous_nodes[current_node] is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start)
            path.reverse()
            return path
        
        # Bu düğüme henüz daha kısa bir yolla ulaşmadıysak, uzaklığı güncelliyoruz.
        if distances[current_node] < current_distance:
            continue
        
        # Komşu düğümleri dolaşıyoruz ve mesafeleri güncelliyoruz.
        for neighbor, distance in graph[current_node].items():
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(unvisited_nodes, (new_distance, neighbor))

# Örnek kullanım:
# Önce, haritadaki düğümleri ve aralarındaki mesafeleri tanımlayalım:
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'D': 5},
    'C': {'A': 1, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3, 'F': 2},
    'F': {'E': 2}
}


# Sonra, en kısa yolu bulmak istediğimiz başlangıç ve hedef düğümlerini belirleyelim.
start_node = "A"
end_node = "F"

# Dijkstra algoritmasını kullanarak, en kısa yolu bulalım.
shortest_path = dijkstra(graph, start_node, end_node)


print(f"{start_node} ile {end_node} arasındaki en kısa yol: {shortest_path}")   
    
for i in range(4): 
    print("En kısa yol:", shortest_path[i])
    print("Maliyet:", shortest_path[i+1])

    
    
    
