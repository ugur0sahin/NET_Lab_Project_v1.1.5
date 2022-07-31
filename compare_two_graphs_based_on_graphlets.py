import os
import networkx as nx
from graphlet_identifier.find_graphlets_through_reindexing_dbs import generate_2D_relevant_nodes_database, \
    optimized_reindex_dataset_as_ego_structure_5D, search_Graphlets_in_egoistic_database_3D_load_todict, \
    search_Graphlets_in_egoistic_database_4D_load_todict, search_Graphlets_in_egoistic_database_5D_load_todict

def compherensive_search(egoistic_db_dict, Graph, Graph_ID, Node5_dimension_scan_included=True):
    if Node5_dimension_scan_included:
        defined_3D_dict = search_Graphlets_in_egoistic_database_3D_load_todict(egoistic_db_dict, Graph, Graph_ID)
        defined_4D_dict = search_Graphlets_in_egoistic_database_4D_load_todict(egoistic_db_dict, Graph, Graph_ID)
        defined_5D_dict = search_Graphlets_in_egoistic_database_5D_load_todict(egoistic_db_dict, Graph, Graph_ID)
        return defined_5D_dict, defined_4D_dict, defined_3D_dict
    else:
        defined_3D_dict = search_Graphlets_in_egoistic_database_3D_load_todict(egoistic_db_dict, Graph, Graph_ID)
        defined_4D_dict = search_Graphlets_in_egoistic_database_4D_load_todict(egoistic_db_dict, Graph, Graph_ID)
        return defined_4D_dict, defined_3D_dict

if __name__ == '__main__':
    # Before everything graphs, 2D relevant_dict_db, main_5D_db_egoisticly_structured should be imported

    G1 = nx.read_adjlist(os.getcwd() + "/actual_databases/<wayG1.adj>")
    G2 = nx.read_adjlist(os.getcwd() + "/actual_databases/<wayG2.adj>")

    G1_Interaction_2D_dict = generate_2D_relevant_nodes_database(G1,
                                                                    folder_file_name="/actual_databases/<way2D_relevant_dict_db_of_G1>",
                                                                    save=True)
    G2_Interaction_2D_dict = generate_2D_relevant_nodes_database(G2, folder_file_name="/actual_databases/<way2D_relevant_dict_db_of_G2>", save=True)

    G1_5D_reindexed_dictionary_database = optimized_reindex_dataset_as_ego_structure_5D(G1_Interaction_2D_dict,
                                                                                           save=True,
                                                                                           folder_path_file="/actual_databases/<way_5D_main_db_of_G1>")
    G2_5D_reindexed_dictionary_database = optimized_reindex_dataset_as_ego_structure_5D(G2_Interaction_2D_dict, save=True, folder_path_file="/actual_databases/<way_5D_main_db_of_G2>")

    defined_5D_dict_G1, defined_4D_dict_G1, defined_3D_dict_G1 = compherensive_search(G1_5D_reindexed_dictionary_database, G1, "toy_graph_3D_G1_graphs")
    defined_5D_dict_G2, defined_4D_dict_G2, defined_3D_dict_G2 = compherensive_search(G2_5D_reindexed_dictionary_database, G2, "toy_graph_3D_G2_graphs")


    diff_3Ds = list(set(defined_3D_dict_G1.keys()) - set(defined_3D_dict_G2.keys())) + list(set(defined_3D_dict_G2.keys()) - set(defined_3D_dict_G1.keys()))

    diff_4Ds = list(set(defined_4D_dict_G1.keys()) - set(defined_4D_dict_G2.keys())) + list(set(defined_4D_dict_G2.keys()) - set(defined_4D_dict_G1.keys()))

    diff_5Ds = list(set(defined_5D_dict_G1.keys()) - set(defined_5D_dict_G2.keys())) + list(set(defined_5D_dict_G2.keys()) - set(defined_5D_dict_G1.keys()))

    overall_differences_in_all_dims = diff_3Ds + diff_4Ds + diff_5Ds

    difference_log_file = open(os.getcwd()+"/actul_databases/subgraph_differences_between_G2_and_G1.txt")
    difference_log_file.write("The graphlets differences are denoted in terms of pattern below")
    for graphlet_differ in overall_differences_in_all_dims:
        difference_log_file.write(str(graphlet_differ)+"\n")