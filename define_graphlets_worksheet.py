import os
import networkx as nx

from graphlet_identifier.find_graphlets_through_reindexing_dbs import generate_2D_relevant_nodes_database, \
    optimized_reindex_dataset_as_ego_structure_5D, search_Graphlets_in_egoistic_database_3D_load_todict, \
    search_Graphlets_in_egoistic_database_4D_load_todict, search_Graphlets_in_egoistic_database_5D_load_todict

if __name__ == "__main__":
    """
    #BEFORE PART REQUIRE
    from graph_generator.create_graph_from_db_implemented import assign_wire, Wire, pd

    #This is the part of Graph is Generated with diminished database

    wire_database = pd.read_csv(str(os.getcwd()) + '/actual_databases/HIPPIE-confidence-075.csv')
    print(wire_database)

    # This is the diminished actual databased no any differentiation (randirect is not executed)
    Graph_HIPPIE_confidence_075 = nx.Graph()
    for index, row in wire_database.iterrows():
        assign_wire(Graph_HIPPIE_confidence_075,
                    Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'], True))

    nx.write_adjlist(Graph_HIPPIE_confidence_075,os.getcwd()+"/actual_databases/toy_graph.adj")
    print(Graph_HIPPIE_confidence_075)
    print("Graph is constructed\n")
    print("Stock Graph (that obtained from the database) is recorded as .adj format")

    #generate_db_name_csv_for_edge_files(Graph_HIPPIE_confidence_075, target_path_and_name=os.getcwd()+"/actual_databases/HIPPIE-node-075.csv")

    #How exported graph can be import again:
    #nx.read_adjlist(os.getcwd()+"/actual_databases/1000_diminished_graph.adj")
    #plot_generated_graph(Graph_HIPPIE_confidence_075_diminished)
    #nx.draw(Graph_HIPPIE_confidence_075_diminished, with_labels=True)
    #plt.show()
    """

    #Before everything graphs, 2D relevant_dict_db, main_5D_db_egoisticly_structured should be imported

    stock_Graph = nx.read_adjlist(os.getcwd() + "/actual_databases/toy_graph.adj")

    stock_Interaction_2D_dict=generate_2D_relevant_nodes_database(stock_Graph, folder_file_name="/actual_databases/toy_HIPPIE_075_2D_relevancy", save=True)

    stock_5D_reindexed_dictionary_database = optimized_reindex_dataset_as_ego_structure_5D(stock_Interaction_2D_dict, save=True, folder_path_file="/actual_databases/toy_5D_Egoistic_DB_HIPPIE_075_dictionary_db")

    defined_3D_dict = search_Graphlets_in_egoistic_database_3D_load_todict(stock_5D_reindexed_dictionary_database,stock_Graph, "toy_graph_3D_graphs")

    defined_4D_dict = search_Graphlets_in_egoistic_database_4D_load_todict(stock_5D_reindexed_dictionary_database, stock_Graph, "toy_graph_4D_graphs")

    defined_5D_dict = search_Graphlets_in_egoistic_database_5D_load_todict(stock_5D_reindexed_dictionary_database, stock_Graph,"toy_graph_5D_graphs")
