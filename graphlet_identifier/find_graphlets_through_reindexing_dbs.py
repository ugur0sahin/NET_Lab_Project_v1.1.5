import pickle
import networkx as nx
from graphlet_identifier.building_graphlet_library import N4_graphlet_library, N3_graphlet_library, N5_graphlet_library

"""
This module contain the functions that is responsible to:
1) Generating a list that include 1st degree relevancy nodes as a format of dict, like{A:[B,C,D], B:[A,R,E,D] .... }
2) Formation of 5Dimensional dictionary to index everything as egoistic structure, like Dictionart Structure is {A:{B:[...], C:[...], D:[...]},  T:{B:[...], Y:[...], P:[...]}________'
#      '___Node_Init:{Node_in_1st_dist:[..2nd_sit_nodes..], Another_node_in_1st_dist:[..2nd_sit_nodes..]}}')
3) And this module include a different dimensional graphlet searching functions like 3Node, 4Node, 5Node contain subgraphs, searching method is walking on the egoistic database.
 
"""


path_of_main_dir = "/Users/ugursahin/PycharmProjects/NETLabProject_v1.1.5"

def find_another_node_in_edge(edge,node):
    for node_in_edge in edge:
        if node != node_in_edge:
            return node_in_edge


def generate_2D_relevant_nodes_database(Graph, save=True, folder_file_name=""):
    node_2D_dict=dict()
    for node in Graph.nodes:
        node_belonged_ls=list()
        for edge in Graph.edges:
            if node in edge:
                interacted_node = find_another_node_in_edge(edge,node)
                node_belonged_ls.append(interacted_node)
        node_2D_dict[node]=node_belonged_ls
    if save:
        D2_relevant_file = open(path_of_main_dir + folder_file_name +".pkl","wb")
        pickle.dump(node_2D_dict, D2_relevant_file)
        print("2D relevant database is saved to the"+ str(folder_file_name) +".pkl ")
        D2_relevant_file.close()

    return node_2D_dict

def optimized_reindex_dataset_as_ego_structure_5D(node_2Dict, save=True, folder_path_file=""):
    main_5D_dict_as_db=dict()
    for interest_node in node_2Dict.keys():
        dict_2ndDim = dict()
        for primary_node in node_2Dict[interest_node]:
            if isinstance(primary_node, str):
                dict_3rdDim=dict()
                for secondary_node in node_2Dict[primary_node]:
                    if isinstance(secondary_node, str):
                        dict_4thDim=dict()
                        for tertiary_node in node_2Dict[secondary_node]:
                            if isinstance(tertiary_node,str):
                                dict_4thDim[tertiary_node] = node_2Dict[tertiary_node]
                        dict_3rdDim[secondary_node]=dict_4thDim
                dict_2ndDim[primary_node]=dict_3rdDim
        #print(dict_2ndDim)
        print("----------------------------------"+str(interest_node)+"---------------------------------")
        main_5D_dict_as_db[interest_node]=dict_2ndDim

    if save:
        D5_relevant_file = open(path_of_main_dir +str(folder_path_file)+".pkl", "wb")
        pickle.dump(main_5D_dict_as_db, D5_relevant_file)
        print("5D relevant database is saved to the "+str(folder_path_file)+".pkl")
        D5_relevant_file.close()
    return main_5D_dict_as_db

def search_Graphlets_in_egoistic_database_5D_load_todict(egoistic_db_dict, Graph, Graph_ID):
    span_dict_5D = dict()
    for target_graphlet in N5_graphlet_library:
        print(target_graphlet.pattern)
        print('\n-------------------' + str(target_graphlet.name) + '-------------------\n')
        for node_key in egoistic_db_dict.keys():
            for primary_dist_node in egoistic_db_dict[node_key].keys():
                for secondary_dist_node in egoistic_db_dict[node_key][primary_dist_node].keys():
                    for tertiary_dist_node in egoistic_db_dict[node_key][primary_dist_node][secondary_dist_node].keys():
                        for quaternary_dist_node in egoistic_db_dict[node_key][primary_dist_node][secondary_dist_node][tertiary_dist_node]:
                            try:
                                sorted_name_list = sorted(
                                    [node_key, primary_dist_node, secondary_dist_node, tertiary_dist_node, quaternary_dist_node])
                                sorted_name = (str(sorted_name_list[0]), str(sorted_name_list[1]), str(sorted_name_list[2]),
                                               str(sorted_name_list[3]), sorted_name_list[4])
                                if sorted_name not in span_dict_5D.keys():
                                    #print(sorted_name)
                                    if (node_key not in [primary_dist_node, secondary_dist_node, tertiary_dist_node, quaternary_dist_node] and primary_dist_node not in [
                                            node_key, secondary_dist_node, tertiary_dist_node, quaternary_dist_node] and secondary_dist_node not in [
                                                node_key, primary_dist_node,tertiary_dist_node, quaternary_dist_node] and tertiary_dist_node not in [node_key, primary_dist_node ,secondary_dist_node, quaternary_dist_node]
                                        and quaternary_dist_node not in [node_key, primary_dist_node ,secondary_dist_node, tertiary_dist_node ])and (
                                                None not in [node_key, primary_dist_node, secondary_dist_node, tertiary_dist_node, quaternary_dist_node]):
                                        defined_subgraph = Graph.subgraph(
                                                [node_key, primary_dist_node, secondary_dist_node, tertiary_dist_node, quaternary_dist_node])
                                        if nx.is_connected(defined_subgraph) and nx.is_isomorphic(defined_subgraph,target_graphlet.pattern):
                                            span_dict_5D[sorted_name] = {"type":target_graphlet, "dimension":5,
                                                                      "node_content":sorted_name_list,
                                                                      "edge_structure":defined_subgraph.edges ,
                                                                      "defined_subgraph": defined_subgraph}
                                            print(str(sorted_name)+ " denotes for the pattern of " + str(defined_subgraph.edges))

                            except:
                                pass
        target_graphlet_file = open(path_of_main_dir + "/clustered_graphlet_folder/" + Graph_ID + "5_"+str(target_graphlet.name)+".pkl","wb")
        pickle.dump(span_dict_5D, target_graphlet_file)
        print(str(target_graphlet) + "is saved to the folder name" + str(Graph_ID))
        target_graphlet_file.close()

        return span_dict_5D

def search_Graphlets_in_egoistic_database_4D_load_todict(egoistic_db_dict, Graph, Graph_ID):
    for target_graphlet in N4_graphlet_library:
        span_dict_4D = dict()
        print(target_graphlet.pattern)
        print('\n-------------------' + str(target_graphlet.name) + '-------------------\n')
        for node_key in egoistic_db_dict.keys():
            for primary_dist_node in egoistic_db_dict[node_key].keys():
                for secondary_dist_node in egoistic_db_dict[node_key][primary_dist_node].keys():
                    for tertiary_dist_node in egoistic_db_dict[node_key][primary_dist_node][secondary_dist_node].keys():
                        try:
                            sorted_name_list = sorted([node_key, primary_dist_node, secondary_dist_node, tertiary_dist_node])
                            sorted_name = (str(sorted_name_list[0]),str(sorted_name_list[1]), str(sorted_name_list[2]), str(sorted_name_list[3]))
                            if sorted_name not in span_dict_4D.keys():
                                if (node_key not in [primary_dist_node, secondary_dist_node, tertiary_dist_node] and primary_dist_node not in [
                                        node_key, secondary_dist_node, tertiary_dist_node] and secondary_dist_node not in [
                                        node_key, primary_dist_node, tertiary_dist_node] and tertiary_dist_node not in [node_key, primary_dist_node,secondary_dist_node] and (None not in [node_key, primary_dist_node, secondary_dist_node, tertiary_dist_node])):
                                    defined_subgraph = Graph.subgraph([node_key, primary_dist_node, secondary_dist_node, tertiary_dist_node])

                                    if nx.is_connected(defined_subgraph) and nx.is_isomorphic(defined_subgraph,
                                                                                              target_graphlet.pattern):
                                        print(str(sorted_name)+ " denotes for the pattern of " + str(defined_subgraph.edges))
                                        span_dict_4D[sorted_name] = {"type": target_graphlet, "dimension": 4,
                                                                  "node_content": sorted_name_list,
                                                                  "edge_structure": defined_subgraph.edges,
                                                                  "defined_subgraph": defined_subgraph}
                        except:
                            pass
        target_graphlet_file = open(path_of_main_dir+"/clustered_graphlet_folder/"+Graph_ID+"4_"+str(target_graphlet.name)+".pkl","wb")
        pickle.dump(span_dict_4D, target_graphlet_file)
        print(str(target_graphlet)+ "is saved to the folder name" + str(Graph_ID) )
        target_graphlet_file.close()

    return span_dict_4D

def search_Graphlets_in_egoistic_database_3D_load_todict(egoistic_db_dict, Graph, Graph_ID):
    for target_graphlet in N3_graphlet_library:
        span_dict_3D = dict()
        print(target_graphlet.pattern)
        print('\n-------------------' + str(target_graphlet.name) + '-------------------\n')
        for node_key in egoistic_db_dict.keys():
            for primary_dist_node in egoistic_db_dict[node_key].keys():
                for secondary_dist_node in egoistic_db_dict[node_key][primary_dist_node].keys():
                    try:
                        sorted_name_list = sorted([node_key, primary_dist_node, secondary_dist_node])
                        sorted_name = (str(sorted_name_list[0]),str(sorted_name_list[1]), str(sorted_name_list[2]))
                        if sorted_name not in span_dict_3D.keys():
                            if (node_key not in [primary_dist_node, secondary_dist_node] and primary_dist_node not in [
                                    node_key, secondary_dist_node] and secondary_dist_node not in [
                                    node_key, primary_dist_node] and (None not in [node_key, primary_dist_node, secondary_dist_node])):
                                defined_subgraph = Graph.subgraph([node_key, primary_dist_node, secondary_dist_node])

                                if nx.is_connected(defined_subgraph) and nx.is_isomorphic(defined_subgraph,
                                                                                          target_graphlet.pattern):
                                    print(
                                        str(sorted_name) + " denotes for the pattern of " + str(defined_subgraph.edges))
                                    span_dict_3D[sorted_name] = {"type": target_graphlet, "dimension": 3,
                                                              "node_content": sorted_name_list,
                                                              "edge_structure": defined_subgraph.edges,
                                                              "defined_subgraph": defined_subgraph}
                    except:
                        pass
        target_graphlet_file = open(path_of_main_dir+"/clustered_graphlet_folder/"+Graph_ID+"3_"+str(target_graphlet.name)+".pkl","wb")
        pickle.dump(span_dict_3D, target_graphlet_file)
        print(str(target_graphlet)+ "is saved to the folder name" + str(Graph_ID) )
        target_graphlet_file.close()

    return span_dict_3D



