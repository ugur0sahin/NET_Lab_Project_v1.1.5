#Building A Library
import networkx as nx
import matplotlib.pyplot as plt

def plot(G):
    nx.draw(G)
    plt.show()

class Graphlet:
    def __init__(self, pattern, name, degree):
        self.name=name
        self.pattern=pattern
        self.degree=degree
    def __str__(self):
        return str(self.name)

#3 node motifs

#2-star
lib1 = nx.Graph()
lib1.add_edge(1,2)
lib1.add_edge(2,3)
graphlet3_2_star=Graphlet(lib1, "2-Star", 3)

#triangle
lib2=nx.Graph()
lib2.add_edge(1,2)
lib2.add_edge(2,3)
lib2.add_edge(1,3)
graphlet3_triangle=Graphlet(lib2, "Triangle", 3)

#4 node motifs

#tailed-triangle
lib3=nx.Graph()
lib3.add_edge(1,2)
lib3.add_edge(2,3)
lib3.add_edge(1,3)

lib3.add_node(4)
lib3.add_edge(3,4)
graphlet4_tailed_triangle=Graphlet(lib3, "Tailed-Triangle", 4)

#4-chordalcycle
lib4=nx.Graph()
lib4.add_edge(1,2)
lib4.add_edge(2,3)
lib4.add_edge(3,4)
lib4.add_edge(1,4)
lib4.add_edge(2,4)
graphlet4_4_chordalcycle=Graphlet(lib4, "4-Chordalcycle", 4)

#4-clique
lib5=nx.Graph()
lib5.add_edge(1,2)
lib5.add_edge(2,3)
lib5.add_edge(3,4)
lib5.add_edge(1,3)
lib5.add_edge(2,4)
lib5.add_edge(1,4)
graphlet4_4_clique=Graphlet(lib5, "4-Clique", 4)

#4 cycle
lib6=nx.Graph()
lib6.add_edge(1,2)
lib6.add_edge(2,3)
lib6.add_edge(3,4)
lib6.add_edge(1,4)
graphlet4_4_cycle=Graphlet(lib6, "4-Cycle", 4)

#3-star
lib7=nx.Graph()
lib7.add_edge(1,2)
lib7.add_edge(2,3)
lib7.add_edge(2,4)
graphlet4_3_star = Graphlet(lib7, "3-Star", 4)

#4-path
lib8=nx.Graph()
lib8.add_edge(1,2)
lib8.add_edge(2,3)
lib8.add_edge(3,4)
graphlet4_4_path=Graphlet(lib8, "4-Path", 4)


#After here there will be 5 Nodes motifs


#After here there will be 5 Nodes motifs


#
lib9 = nx.Graph()
lib9.add_edge(1,2)
lib9.add_edge(2,3)
lib9.add_edge(2,4)
lib9.add_edge(4,5)
graphlet5_lib9 = Graphlet(lib9, "lib9", 5)


lib10 = nx.Graph()
lib10.add_edge(1,5)
lib10.add_edge(1,4)
lib10.add_edge(1,3)
lib10.add_edge(1,2)
graphlet5_lib10 = Graphlet(lib10, "lib10", 5)

lib11 = nx.Graph()
lib11.add_edge(1,2)
lib11.add_edge(2,3)
lib11.add_edge(3,4)
lib11.add_edge(4,5)
graphlet5_lib11 = Graphlet(lib11, "lib11", 5)

lib12 = nx.Graph()
lib12.add_edge(1,2)
lib12.add_edge(2,3)
lib12.add_edge(1,3)
lib12.add_edge(2,4)
lib12.add_edge(3,5)
graphlet5_lib12 = Graphlet(lib12, "lib10", 5)

lib13 = nx.Graph()
lib13.add_edge(1,2)
lib13.add_edge(2,3)
lib13.add_edge(1,3)
lib13.add_edge(2,4)
lib13.add_edge(2,5)
graphlet5_lib13 = Graphlet(lib13, "lib13", 5)

lib14 = nx.Graph()
lib14.add_edge(1,2)
lib14.add_edge(2,3)
lib14.add_edge(3,4)
lib14.add_edge(4,5)
lib14.add_edge(5,1)
graphlet5_lib14 = Graphlet(lib14, "lib14", 5)

lib15 = nx.Graph()
lib15.add_edge(1,3)
lib15.add_edge(4,3)
lib15.add_edge(1,2)
lib15.add_edge(4,5)
lib15.add_edge(2,4)
graphlet5_lib15 = Graphlet(lib15, "lib15", 5)

lib16 = nx.Graph()
lib16.add_edge(1,3)
lib16.add_edge(4,3)
lib16.add_edge(1,2)
lib16.add_edge(4,5)
lib16.add_edge(2,4)
lib16.add_edge(2,3)
graphlet5_lib16 = Graphlet(lib16, "lib16", 5)

lib17 = nx.Graph()
lib17.add_edge(1,3)
lib17.add_edge(4,3)
lib17.add_edge(1,2)
lib17.add_edge(4,5)
lib17.add_edge(2,4)
lib17.add_edge(1,4)
graphlet5_lib17 = Graphlet(lib17, "lib17", 5)

lib18 = nx.Graph()
lib18.add_edge(1,2)
lib18.add_edge(2,4)
lib18.add_edge(3,4)
lib18.add_edge(1,3)
lib18.add_edge(1,5)
lib18.add_edge(4,5)
graphlet5_lib18 = Graphlet(lib18, "lib18", 5)


lib19 = nx.Graph()
lib19.add_edge(1,2)
lib19.add_edge(2,4)
lib19.add_edge(3,4)
lib19.add_edge(1,3)
lib19.add_edge(1,5)
lib19.add_edge(4,5)
graphlet5_lib19 = Graphlet(lib19, "lib19", 5)

lib20 = nx.Graph()
lib20.add_edge(1,5)
lib20.add_edge(1,2)
lib20.add_edge(2,5)
lib20.add_edge(1,3)
lib20.add_edge(2,4)
lib20.add_edge(3,4)
graphlet5_lib20 = Graphlet(lib20, "lib20", 5)

lib21 = nx.Graph()
lib21.add_edge(1,2)
lib21.add_edge(1,3)
lib21.add_edge(2,5)
lib21.add_edge(3,5)
lib21.add_edge(3,4)
lib21.add_edge(2,4)
graphlet5_lib21= Graphlet(lib21, "lib21", 5)

lib22 = nx.Graph()
lib22.add_edge(1,2)
lib22.add_edge(2,4)
lib22.add_edge(3,4)
lib22.add_edge(1,4)
lib22.add_edge(3,5)
lib22.add_edge(2,3)
lib22.add_edge(1,3)
graphlet5_lib22 = Graphlet(lib22, "lib22", 5)

lib23 = nx.Graph()
lib23.add_edge(1,3)
lib23.add_edge(3,4)
lib23.add_edge(2,4)
lib23.add_edge(1,2)
lib23.add_edge(1,5)
lib23.add_edge(4,5)
lib23.add_edge(2,5)
graphlet5_lib23 = Graphlet(lib23, "lib23", 5)

lib24=nx.Graph()
lib24.add_edge(1,2)
lib24.add_edge(2,3)
lib24.add_edge(1,3)
lib24.add_edge(2,4)
lib24.add_edge(3,4)
lib24.add_edge(4,5)
lib24.add_edge(3,5)
graphlet5_lib24 = Graphlet(lib24, "lib24", 5)

lib25 = nx.Graph()
lib25.add_edge(1,3)
lib25.add_edge(3,4)
lib25.add_edge(2,4)
lib25.add_edge(1,2)
lib25.add_edge(1,5)
lib25.add_edge(4,5)
lib25.add_edge(2,5)
graphlet5_lib25= Graphlet(lib25, "lib25", 5)

lib26 =nx.Graph()
lib26.add_edge(1,2)
lib26.add_edge(2,3)
lib26.add_edge(1,3)
lib26.add_edge(2,4)
lib26.add_edge(3,4)
lib26.add_edge(4,5)
lib26.add_edge(3,5)
graphlet5_lib26 = Graphlet(lib26, "lib26", 5)

lib27 = nx.Graph()
lib27.add_edge(1,2)
lib27.add_edge(2,4)
lib27.add_edge(3,4)
lib27.add_edge(1,3)
lib27.add_edge(2,3)
lib27.add_edge(2,5)
lib27.add_edge(3,5)
graphlet5_lib27 = Graphlet(lib27, "lib27", 5)

lib28 = nx.Graph()
lib28.add_edge(1,2)
lib28.add_edge(2,4)
lib28.add_edge(3,4)
lib28.add_edge(1,3)
lib28.add_edge(1,4)
lib28.add_edge(2,5)
lib28.add_edge(3,5)
graphlet5_lib28= Graphlet(lib28, "lib28", 5)

lib29 = nx.Graph()
lib29.add_edge(1,2)
lib29.add_edge(2,4)
lib29.add_edge(3,4)
lib29.add_edge(1,3)
lib29.add_edge(1,4)
lib29.add_edge(2,5)
lib29.add_edge(3,5)
lib29.add_edge(4,5)
graphlet5_lib29 = Graphlet(lib29, "lib29", 5)

lib30 = nx.Graph()
lib30.add_edge(1,2)
lib30.add_edge(2,4)
lib30.add_edge(3,4)
lib30.add_edge(1,3)
lib30.add_edge(2,3)
lib30.add_edge(2,5)
lib30.add_edge(3,5)
lib30.add_edge(4,5)
graphlet5_lib30= Graphlet(lib30, "lib30", 5)

lib31 = nx.Graph()
lib31.add_edge(1,2)
lib31.add_edge(2,4)
lib31.add_edge(3,4)
lib31.add_edge(1,3)
lib31.add_edge(2,3)
lib31.add_edge(2,5)
lib31.add_edge(3,5)
lib31.add_edge(4,5)
lib31.add_edge(1,4)
graphlet5_lib31= Graphlet(lib31, "lib31", 5)

lib32 = nx.Graph()
lib32.add_edge(1,2)
lib32.add_edge(2,3)
lib32.add_edge(3,4)
lib32.add_edge(4,5)
lib32.add_edge(1,5)
lib32.add_edge(1,3)
lib32.add_edge(1,4)
lib32.add_edge(2,4)
lib32.add_edge(2,5)
lib32.add_edge(3,5)
graphlet5_lib32 = Graphlet(lib32, "lib32", 5)


N5_graphlet_library = [graphlet5_lib9, graphlet5_lib10, graphlet5_lib11, graphlet5_lib12, graphlet5_lib13, graphlet5_lib14,
                       graphlet5_lib15, graphlet5_lib16, graphlet5_lib17, graphlet5_lib18, graphlet5_lib19, graphlet5_lib20,
                       graphlet5_lib21, graphlet5_lib22, graphlet5_lib23, graphlet5_lib24, graphlet5_lib25, graphlet5_lib26,
                       graphlet5_lib27, graphlet5_lib27, graphlet5_lib28, graphlet5_lib29, graphlet5_lib30, graphlet5_lib31, graphlet5_lib32]
N4_graphlet_library = [graphlet4_tailed_triangle,graphlet4_4_chordalcycle,graphlet4_4_clique,graphlet4_4_cycle,graphlet4_3_star,graphlet4_4_path]
#N4_graphlet_library = [graphlet4_4_clique] #This is the reason we only search the 4_Cliques in the Graph

N3_graphlet_library = [graphlet3_2_star, graphlet3_triangle, graphlet3_2_star, graphlet3_triangle]
graphlet_library = [ graphlet3_2_star, graphlet3_triangle, graphlet3_2_star, graphlet3_triangle,graphlet4_tailed_triangle,graphlet4_4_chordalcycle,graphlet4_4_clique,graphlet4_4_cycle,graphlet4_3_star,graphlet4_4_path]



"""
for i in graphlet_library:
    plot(nx.Graph(i.pattern))
"""
##Writing part to a text_file.

'''
f=open('graphlet_library.txt','w')
for graphlet in lib_ls:
    f.write(str(graphlet.pattern) + str(graphlet.name) + str(graphlet.degree))
f.close()
'''