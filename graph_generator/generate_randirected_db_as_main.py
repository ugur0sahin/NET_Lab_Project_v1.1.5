import os
import random
from graph_generator.create_graph_from_db_implemented import pd, generate_graph
path_of_main_dir = "/Users/ugursahin/PycharmProjects/NETLabProject_v1.1.5"

# Main purpose is manipulating main prototype_db to direct it (Affect similarity)
# To do that randomly impact the nodes

"There should be 3 feature to change system"#
"1)Randomly delete the node(s) or edges"
"Main part is differantiate step by step but choose the type differentiation," \
" total edge change is same but one of them belongs one node, another one independent"

def find_and_delete(pair1,pair2,df):
    for index,row in df.iterrows():
        if (row['Gene Name Interactor A'] == pair1 or row['Gene Name Interactor B'] == pair1) and (row['Gene Name Interactor A'] == pair2 or row['Gene Name Interactor B'] == pair2):
            return index
def diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def change_refer(ref,ref_nod,unit_step,node_weight,edge_weight,path_name="/actual_databases/", node_db_name="", wire_db_name="",graph_name="",database_return=False):

    import networkx as nx
    from graph_generator.create_graph_from_db_implemented import Wire,assign_wire
    # Edge weight + Node weight should be equal to 1
    database = pd.read_csv(ref)
    ref_node = pd.read_csv(ref_nod)
    unit_step_for_rand_edge, unit_step_for_node = round(edge_weight * unit_step), round(node_weight * unit_step)
    init_db, init_edge = database['Gene_Symb'].values.tolist(), [ref_node['Gene Name Interactor A'].values.tolist(),
                                                                 ref_node['Gene Name Interactor B'].values.tolist()]
    print('Initial node_count' + str(database.shape))
    print('-------------------------1--------------------------------')
    for iterator in range(unit_step_for_rand_edge):
        try:
            random_number = random.randint(0, ref_node.shape[0] - 1)
            print(ref_node.iloc[random_number])
            ref_node = ref_node.drop(random_number, axis='index')
        except:
            random_number = random.randint(0, ref_node.shape[0] - 1)
            print(ref_node.iloc[random_number])
            ref_node = ref_node.drop(random_number, axis='index')  # Dogru sayiyi buluna kadar while da dene
        print(ref_node.shape)
        print('-------------------------2--------------------------------')
    while unit_step_for_node != 0:
        random_numb = random.randint(0, len(database['Gene_Symb'].values.tolist()) - unit_step)
        chosen_node = database['Gene_Symb'].values.tolist()[random_numb]
        # Find pairs
        pair_ls_for_chosen_node = []
        # print(chosen_node)
        for index, row in ref_node.iterrows():
            if row['Gene Name Interactor A'] == chosen_node:
                pair_ls_for_chosen_node.append(row['Gene Name Interactor B'])
            if row['Gene Name Interactor B'] == chosen_node:
                pair_ls_for_chosen_node.append(row['Gene Name Interactor A'])
        # print(pair_ls_for_chosen_node)
        if len(pair_ls_for_chosen_node) < unit_step_for_node:
            '''
            try:
                ref_node=ref_node[ref_node['Gene Name Interactor A'].str.contains(chosen_node) == False]
            except:
                ref_node = ref_node[ref_node['Gene Name Interactor B'].str.contains(chosen_node) == False]
            '''
            for item in pair_ls_for_chosen_node:
                # print(item), print(chosen_node), print(ref_node)
                indice = find_and_delete(item, chosen_node, ref_node)
                print(ref_node.iloc[indice])
                ref_node = ref_node.drop(indice, axis='index')
                print(ref_node.shape)
                print('-------------------------3--------------------------------')
            unit_step_for_node = unit_step_for_node - len(pair_ls_for_chosen_node)

        else:
            pair_ls_for_chosen_node = pair_ls_for_chosen_node[:unit_step_for_node]
            for pair in pair_ls_for_chosen_node:
                indice = find_and_delete(pair, chosen_node, ref_node)
                print(ref_node.iloc[indice])
                ref_node = ref_node.drop(indice, axis='index')
                print(ref_node.shape)
                print('-------------------------4--------------------------------')
            break
    All_Term_Nodes, All_In_Nodes = ref_node['Gene Name Interactor B'].values.tolist(), ref_node[
        'Gene Name Interactor A'].values.tolist()
    for index, row in database.iterrows():
        if (row['Gene_Symb'] in All_Term_Nodes) or (row['Gene_Symb'] in All_In_Nodes):
            pass
        else:
            # database = database[database['Gene_Symb'].str.contains(row['Gene_Symb']) == False]
            drop_ls = database.index[database['Gene_Symb'] == row['Gene_Symb']].tolist()
            for drop_index in drop_ls:
                database = database.drop(drop_index, axis='index')
    if database_return:
        ref_node.to_csv(path_of_main_dir + str(path_name) + node_db_name , index=None)
        database.to_csv(path_of_main_dir + str(path_name) + wire_db_name, index=None)
    end_db, end_edge = database['Gene_Symb'].values.tolist(), [ref_node['Gene Name Interactor A'].values.tolist(),
                                                               ref_node['Gene Name Interactor B'].values.tolist()]
    print('Finished node_count' + str(database.shape))
    print('Name(s) of removed nodes' + str(diff(init_db, end_db)))
    #dif_of_edge_in = diff(init_db[0], end_edge[0])
    #dif_of_edge_term = diff(init_db[1], end_edge[1])
    #for i in range(len(dif_of_edge_in)):
    #    print(str(dif_of_edge_in[i]) + '--' + str(dif_of_edge_term[i]))


    Graph_HIPPIE_confidence_075_diminished_pruned = nx.Graph()
    for index, row in ref_node.iterrows():
        assign_wire(Graph_HIPPIE_confidence_075_diminished_pruned,
                    Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'], True))

    nx.write_adjlist(Graph_HIPPIE_confidence_075_diminished_pruned,
                     path_of_main_dir + path_name + graph_name)
    print('\n')
    print(str(path_of_main_dir + path_name)+ " is exported as graph format ")
    return Graph_HIPPIE_confidence_075_diminished_pruned

