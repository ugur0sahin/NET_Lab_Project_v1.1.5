import os
import pandas as pd
import networkx as nx
from graph_generator.create_graph_from_db_implemented import generate_db_name_csv_for_edge_files,assign_wire, Wire

if __name__ == '__main__':
    #This is the part of Graph is Generated with diminished database

    wire_database = pd.read_csv(str(os.getcwd()) + '/actual_databases/HIPPIE-confidence-075.csv')
    print(wire_database)

    # This is the diminished actual databased no any differentiation (randirect is not executed)
    Graph_HIPPIE_confidence_075 = nx.Graph()
    for index, row in wire_database.iterrows():
        assign_wire(Graph_HIPPIE_confidence_075,
                    Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'], True))

    nx.write_adjlist(Graph_HIPPIE_confidence_075,os.getcwd()+"/actual_databases/Actual_graph.adj")
    print(Graph_HIPPIE_confidence_075)
    print("Graph is constructed\n")
    print("Stock Graph (that obtained from the database) is recorded as .adj format")

    #generate_db_name_csv_for_edge_files(Graph_HIPPIE_confidence_075, target_path_and_name=os.getcwd()+"/actual_databases/HIPPIE-node-075.csv")

    #How exported graph can be import again:
    #nx.read_adjlist(os.getcwd()+"/actual_databases/1000_diminished_graph.adj")
    #plot_generated_graph(Graph_HIPPIE_confidence_075_diminished)
    #nx.draw(Graph_HIPPIE_confidence_075_diminished, with_labels=True)
    #plt.show()
