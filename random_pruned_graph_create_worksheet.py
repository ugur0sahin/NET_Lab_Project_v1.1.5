import os
import pandas as pd
import networkx as nx
from graph_generator.generate_randirected_db_as_main import change_refer
from graph_generator.create_graph_from_db_implemented import assign_wire, Wire

if __name__ == '__main__':
    #Randomly Prune the Graph
    wire_database = pd.read_csv(str(os.getcwd()) + '/actual_databases/HIPPIE-confidence-075.csv')

    Graph_HIPPIE_confidence_075_toy_pruned=nx.Graph()
    for index, row in wire_database.iterrows():
        assign_wire(Graph_HIPPIE_confidence_075_toy_pruned,
                    Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'], True))


    folder="/actual_databases/"
    n_weight, e_weight, s_size = 0.7, 0.3, 10
    print('node_diff_rate: ' + str(n_weight) + ' edge_diff_rate:' + str(e_weight) + ' total_step_size' + str(s_size))

    path_of_wire_db, path_of_node_db = os.getcwd()+"/actual_databases/HIPPIE-confidence-075.csv",\
                                       os.getcwd()+"/actual_databases/HIPPIE-node-075.csv"
    Graph_HIPPIE_confidence_075_toy_pruned = change_refer(path_of_node_db, path_of_wire_db, s_size, n_weight, e_weight, path_name=folder, wire_db_name= "HIPPIE-confidence-075_pruned.csv",
                                                          node_db_name="HIPPIE-node-075_pruned.csv",graph_name="toy_pruned_graph.adj",database_return=True)
    nx.write_adjlist(Graph_HIPPIE_confidence_075_toy_pruned, os.getcwd() + "/actual_databases/toy_pruned_graph.adj")


