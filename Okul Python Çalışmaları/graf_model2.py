# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:31:37 2023

@author: Hasan Emre
"""

import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random

# Belirlenen 10 noktanın koordinatları
noktalar = {
    "Hastane": (41.008236, 28.973454),
    "Okul": (41.006919, 28.968986),
    "Belediye": (41.003942, 28.970025),
    "Spor Salonu": (41.009324, 28.967496),
    "Market": (41.009861, 28.972123),
    "Park": (41.003658, 28.973859),
    "Cami": (41.006293, 28.972932),
    "Kütüphane": (41.007840, 28.971327),
    "Stadyum": (41.007512, 28.966402),
    "İtfaiye": (41.004833, 28.971137)
}

# Stok bilgileri

stoklar = {
    "sağlık malzemesi": 100,
    "temel gıda": 100,
    "ısınma gereci": 70,
    "giyecek": 70
}


# Öncelik sırası belirleme
oncelik_sirasi = {
    "sağlık malzemesi": 1,
    "temel gıda": 2,
    "ısınma gereci": 3,
    "giyecek": 4
}
# İhtiyaç malzemelerinin stokları
ihtiyac_stoklari = {
    "Hastane": {"sağlık malzemesi": 25, "temel gıda": 20, "ısınma gereci": 10, "giyecek": 16},
    "Okul": {"sağlık malzemesi": 10, "temel gıda": 20, "ısınma gereci": 12, "giyecek": 13},
    "Belediye": {"sağlık malzemesi": 13, "temel gıda": 15, "ısınma gereci":8, "giyecek": 11},
    "Spor Salonu": {"sağlık malzemesi": 7, "temel gıda": 5, "ısınma gereci": 6, "giyecek": 2},
    "Market": {"sağlık malzemesi": 11, "temel gıda": 10, "ısınma gereci": 0, "giyecek": 4},
    "Park": {"sağlık malzemesi": 4, "temel gıda": 0, "ısınma gereci": 10, "giyecek": 8},
    "Cami": {"sağlık malzemesi": 10, "temel gıda": 6, "ısınma gereci": 4, "giyecek": 6},
    "Kütüphane": {"sağlık malzemesi": 0, "temel gıda": 10, "ısınma gereci": 10, "giyecek": 1},
    "Stadyum": {"sağlık malzemesi": 8, "temel gıda": 0, "ısınma gereci": 3, "giyecek": 0},
    "İtfaiye": {"sağlık malzemesi": 12, "temel gıda": 14, "ısınma gereci": 7, "giyecek": 9},
}



# Boş bir graf oluştur
graf = nx.Graph()

# Noktaları düğümler olarak ekle
for nokta, koordinat in noktalar.items():
    graf.add_node(nokta, pos=koordinat)

# Kenarları ekle ve ağırlıklarını belirle
for nokta, ihtiyaclar in ihtiyac_stoklari.items():
    for diger_nokta, diger_ihtiyaclar in ihtiyac_stoklari.items():
        if nokta != diger_nokta:
            agırlık = 0
            for ihtiyac, miktar in ihtiyaclar.items():
                if miktar > 0:
                    oncelik = oncelik_sirasi[ihtiyac.lower()]
                    agırlık += (miktar / stoklar[ihtiyac]) * oncelik
            graf.add_edge(nokta, diger_nokta, weight=agırlık)

# Kenarların ağırlıklarını düzenle
agırlıklar = nx.get_edge_attributes(graf, 'weight')
nx.set_edge_attributes(graf, agırlıklar, 'weight')
                        

# Grafı çizdirme
pos = nx.spring_layout(graf)
nx.draw_networkx_nodes(graf, pos, node_size=500)
nx.draw_networkx_labels(graf, pos, font_size=10, font_family="sans-serif")
nx.draw_networkx_edges(graf, pos, width=2, edge_color="blue")
nx.draw_networkx_edge_labels(graf, pos, font_size=8)
plt.axis("off")
plt.show()



# En kısa yol algoritması
def dijkstra(graf, baslangic):
    distances = {node: float('inf') for node in graf}  # Tüm noktalara sonsuz mesafe atanır.
    distances[baslangic] = 0  # Başlangıç noktasının mesafesi 0 olarak atanır.
    heap = [(0, baslangic)]  # Heap sırası, mesafeleri saklamak için kullanılır.
    while heap:
        (current_distance, current_node) = heapq.heappop(heap)  # Heap sırasından en küçük mesafeli düğüm seçilir.
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graf[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))  # Heap sırasına eklenir.
    return distances



# Dağıtım planı oluşturma
dagitim_plani = []
# Öncelik sırasına göre dağıtım yap
for oncelik in oncelik_sirasi.values():
    for nokta in noktalar:
        ihtiyaclar = noktalar[nokta]
        if ihtiyaclar[oncelik] > 0:
            en_kisa_yollar = []
            for hedef in stoklar:
                print(type(hedef))
                for ihtiyaclar2 in stoklar[hedef]:
                    if ihtiyaclar2[oncelik] > 0:
                        # En kısa yolu bul
                        yol = dijkstra(nokta, hedef)
                        if yol is not None:
                            en_kisa_yollar.append((hedef, yol))

            # En kısa yolu seç
            en_kisa_yollar = sorted(en_kisa_yollar, key=lambda x: x[1])
            if len(en_kisa_yollar) > 0:
                en_kisa_yol = en_kisa_yollar[0][1]
                hedef = en_kisa_yollar[0][0]

                # İhtiyaçları karşıla
                for ihtiyac in oncelik_sirasi[oncelik]:
                    if ihtiyaclar[ihtiyac] > 0 and stoklar[hedef][ihtiyac] > 0:
                        ihtiyac_miktari = min(ihtiyaclar[ihtiyac], stoklar[hedef][ihtiyac])
                        dagitim_plani[ihtiyac] += ihtiyac_miktari
                        ihtiyaclar[ihtiyac] -= ihtiyac_miktari
                        stoklar[hedef][ihtiyac] -= ihtiyac_miktari

                            
# Dağıtım planı yazdırma
print("Dağıtım Planı:")
for ihtiyac, miktar in dagitim_plani.items():
    print(f"{ihtiyac.capitalize()}: {miktar}")

# Kalan stokları yazdırma
print("\nKalan Stoklar:")
for nokta, stoklar in stoklar.items():
    print(f"{nokta.capitalize()}: {stoklar}")                         
                            
                            
                            
                            
                            
       
                            
       
# # Adım 6: Kalan stokları güncelleme ve yeniden malzeme taşıma planı yapma
# def update_stock(stocks, needs):
#     for i in range(len(stocks)):
#         stocks[i] -= needs[i]
#         if stocks[i] < 0:
#             stocks[i] = 0
#     return stocks
 
# def create_new_plan(graph, stocks, needs, current_plan):
#     new_plan = []
#     for i in range(len(current_plan)):
#         start_node = current_plan[i]
#         end_node = current_plan[i+1] if i < len(current_plan)-1 else current_plan[0]
#         edge_weight = graph[start_node][end_node]
#         if stocks[needs.index(max(needs))] == 0:
#             break
#         if needs[start_node] > 0:
#             transfer_amount = min(needs[start_node], stocks[needs.index(max(needs))])
#             new_plan.append((start_node, end_node, transfer_amount))
#             stocks[needs.index(max(needs))] -= transfer_amount
#             needs[start_node] -= transfer_amount
#             needs[end_node] += transfer_amount
#     return new_plan

# # Adım 7: Acil müdahale ekipleri
# def call_for_help():
#     print("Acil müdahale ekipleri çağrıldı.")

# # Adım 8: Verileri kullanarak daha etkili bir dağıtım planı yapma
def generate_optimal_plan(graph, stocks, needs, current_plan):
    new_plan = create_new_plan(graph, stocks, needs, current_plan)
    while len(new_plan) > 0:
        current_plan += new_plan
        stocks = update_stock(stocks, needs)
        needs = [max(0, needs[i]-stocks[i]) for i in range(len(needs))]
        new_plan = create_new_plan(graph, stocks, needs, current_plan)
    return current_plan

# Test verileri
priority = [1, 2, 3, 4, 2, 3, 4, 1, 2, 3]
types = ["Sağlık Malzemesi", "Temel Gıda", "Isınma Gereci", "Giyecek", "Sağlık Malzemesi", "Isınma Gereci", "Giyecek", "Sağlık Malzemesi", "Temel Gıda", "Isınma Gereci"]
stocks = [100, 100, 70, 70]
needs = [20, 30, 10, 50, 40, 20, 30, 20, 40, 10]
locations = [(0, 0), (1, 2), (2, 1), (3, 3), (4, 2), (5, 0), (6, 1), (7, 3), (8, 2), (9, 0)]
graph = create_graph(locations)
plan = generate_plan(graph, priority, types, stocks, needs)
print(plan)
                            
                            
                            
                            
                            
                            
                        
                        
                        
# -En az 10 noktadan oluşan lokasyona, aşağıdaki listedeki öncelik sırası ve stoğu gözeterek, bu 10 noktadakisizin belirleyeceğiniz ihtiyaç miktarlarını dikkate alan ve graf algoritması kullanan bir dağıtım planı oluşturulması.
# Aşağıdaki tabloya göre;
# Öncelik                     Çeşidi                         Elinizdeki Stok        
#     1                       Sağlık Malzemesi                 100                 
#     2                      Temel Gıda                              100
#     3                        Isınma Gereci                        70 
#     4                            Giyecek                                70

# -Dağıtım planı koşulu en çok ihtiyacın duyulacağı yere en kısa zamanda, harita üzerinde belirlenen drone rotası belirleme şeklinde olacaktır.

# Adım 1: Alanın haritasını inceleriz ve 10 adet nokta belirleriz. Bu noktalar, ihtiyaç malzemelerinin dağıtımını yapacağımız yerler olacaktır.

# Adım 2: Bu noktalar arasında bir graf oluştururuz ve ihtiyaç malzemelerinin stoklarına göre ağırlıklandırırız. Grafın düğümleri, belirlediğimiz 10 nokta olacaktır ve kenarlar, bu noktalar arasındaki rota olacaktır.

# Adım 3: Graf teorisindeki en kısa yol algoritması kullanarak, ihtiyaç malzemelerinin dağıtımını yapacağımız rotayı belirleriz. Bu, ihtiyaç malzemelerinin en çok ihtiyaç duyulan noktalara en kısa sürede ulaşmasını sağlayacaktır.

# Adım 4: Belirlediğimiz rotayı takip ederek, her noktaya ihtiyaç malzemelerini dağıtırız. Dağıtım, belirlenen öncelik sırasına göre yapılmalıdır. Yani öncelik sırasında sağlık malzemeleri, temel gıda, ısınma gereci ve giyecek sırasıyla dağıtılmalıdır.

# Adım 5: Dağıtım sırasında, belirlediğimiz rotayı takip ederek, en kısa sürede ve en az miktarda malzeme kullanarak dağıtım yapmak için drone veya araç gibi araçları kullanabiliriz.

# Adım 6: Dağıtım sonrası, kalan stokları güncellemeli ve ihtiyaç duyulan noktalara yeniden malzeme taşıma planı yapmalıyız. Bu planı yaparken de öncelik sırasına ve stok miktarına göre hareket etmeliyiz.

# Adım 7: Dağıtım sırasında ve sonrasında herhangi bir sorun veya aksaklık durumunda acil müdahale ekiplerini çağırmalı ve yardım istemeliyiz.

# Adım 8: Daha sonraki dağıtımlarda, önceki dağıtımların verilerini kullanarak daha etkili bir dağıtım planı yapabilir ve süreci daha verimli hale getirebiliriz.

# Bu şekilde, belirlenen önceliklere ve stok durumuna göre, en kısa sürede ve en az miktarda malzeme kullanarak ihtiyaç duyulan noktalara malzeme taşıma planı yapabiliriz. Bu, acil durumlarda veya ihtiyaç duyulan noktalara ulaşmanın zor olduğu bölgelerde büyük bir fark yaratabilir ve hayat kurtarabilir.

                            
                            
           
                            
           
#             Örnek Senaryo:

# Lokasyon Belirleme: 10 noktadan oluşan bir bölgede ihtiyaç malzemelerinin dağıtımı yapılacak. Bu noktalar, harita üzerinde belirli koordinatlara sahip olan ve ihtiyaç malzemelerinin teslim edileceği noktalardır.

# Graf Oluşturma: Belirlenen noktalar arasında bir graf oluşturulur ve ihtiyaç malzemelerinin stoklarına göre ağırlıklandırılır. Grafın düğümleri, belirlediğimiz 10 nokta olacaktır ve kenarlar, bu noktalar arasındaki rota olacaktır.

# En Kısa Yol Belirleme: Graf teorisindeki en kısa yol algoritması kullanılarak, ihtiyaç malzemelerinin dağıtımını yapacağımız rotayı belirleriz. Bu, ihtiyaç malzemelerinin en çok ihtiyaç duyulan noktalara en kısa sürede ulaşmasını sağlayacaktır.

# Öncelik Sırasına Göre Dağıtım: Belirlediğimiz rotayı takip ederek, her noktaya ihtiyaç malzemelerini dağıtırız. Dağıtım, belirlenen öncelik sırasına göre yapılmalıdır. Yani öncelik sırasında sağlık malzemeleri, temel gıda, ısınma gereci ve giyecek sırasıyla dağıtılmalıdır.

# Araç Kullanımı: Dağıtım sırasında, belirlediğimiz rotayı takip ederek, en kısa sürede ve en az miktarda malzeme kullanarak dağıtım yapmak için drone veya araç gibi araçları kullanabiliriz.

# Stok Güncelleme: Dağıtım sonrası, kalan stokları güncellemeli ve ihtiyaç duyulan noktalara yeniden malzeme taşıma planı yapmalıyız. Bu planı yaparken de öncelik sırasına ve stok miktarına göre hareket etmeliyiz.

# Acil Müdahale: Dağıtım sırasında ve sonrasında herhangi bir sorun veya aksaklık durumunda acil müdahale ekiplerini çağırmalı ve yardım istemeliyiz.

# Veri Analizi: Daha sonraki dağıtımlarda, önceki dağıtımların verilerini kullanarak daha etkili bir dağıtım planı yapabilir ve süreci daha verimli hale getirebiliriz.
                            
                            
                            
                            
                            
                            
                            
                            
                            