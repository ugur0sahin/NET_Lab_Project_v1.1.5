import os
import pickle
if __name__ == '__main__':
    import compare_two_graphs_based_on_graphlets

    #Import Graphlet Databases
    G1 = open(os.getcwd()+"/clustered_graphlet_folder/<way_main_db_5D_G1>.pkl", "rb")
    toy_G2_graph4_4D_graphs4_4_Clique_db=pickle.load(G1)

    G2 = open(os.getcwd()+"/clustered_graphlet_folder/<way_main_db_5D_G2>.pkl", "rb")
    toy_G2_graph_4D_graphs4_4_Clique_db=pickle.load(G2)

    print(len(toy_G2_graph4_4D_graphs4_4_Clique_db))
    print("\n")
    for i in list(set(toy_G2_graph4_4D_graphs4_4_Clique_db.keys()) - set(toy_G2_graph_4D_graphs4_4_Clique_db.keys())) + list(set(toy_G2_graph_4D_graphs4_4_Clique_db.keys()) - set(toy_G2_graph4_4D_graphs4_4_Clique_db.keys())):
        print(i)
    print("\n")
    print(len(toy_G2_graph_4D_graphs4_4_Clique_db.keys()))
    #print(len(set(list(toy_G2_graph_4D_graphs4_4_Clique_db.keys()))))

    #print(toy_G2_graph4_4D_graphs4_4_Clique_db[('ERG6', 'FAA4', 'FAS2', 'TGL3')].items())