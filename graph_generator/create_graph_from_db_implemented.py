import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
# Locating
# This part prepare a gene class for every element that
# is obtained from the raw data file
path_of_main_dir = "/Users/ugursahin/PycharmProjects/NETLabProject_v1.1.5"


class Gene():
    def __init__(self,name,transcription_level,crispr_KO,hotpoint_mut,differentiation_rate):
        self.name=name
        self.transcription_level=transcription_level
        self.KO=crispr_KO
        self.hotpoint_mut=hotpoint_mut
        self.differentiation_rate=differentiation_rate

    def __str__(self):
        return str(self.name)
# Prepare function that assign gene to node

def assign_node(Graph,gene):
    Graph.add_node(str(gene.name),TL=gene.transcription_level,KO=gene.KO,HP=gene.hotpoint_mut)

# Wiring

#wire_database=pd.read_csv('confidence_db.csv',sep=';')
#print(wire_database.iterrows('InNode'))

class Wire():
    def __init__(self,nodeI,nodeT,confidence,state):
        self.InNode=nodeI
        self.TermNode=nodeT
        self.confidence=confidence
        self.state=state

    def __str__(self):
        return '/' + str(self.InNode)+' - '+ str(self.TermNode) + '/'

def assign_wire(Graph,Wire):
    Graph.add_edge(Wire.InNode, Wire.TermNode, weight_based_conf=Wire.confidence, S=Wire.state)


def get_trial_code_from_filename(file):
    file_direc=file.split('/')
    trial_name=file_direc[-1].split('_')[0]
    return trial_name

def generate_graph(db_wire, db_name=None, trial_ID="?"):
    G = nx.Graph()  # Define Null Graph

    if not db_name == None:
        if trial_ID == "?":
            trial_ID=get_trial_code_from_filename(db_name)
        database = pd.read_csv(db_name)
        #print(database)

        for index, row in database.iterrows():
            assign_node(G, Gene(row['Gene_Symb'], row['Transcription_Level'], row['CRISPR_KO_Effect'],
                                row['Hotpoint_Mutation'], row['Differentiation_Rate']))

    wire_database = pd.read_csv(db_wire)

    for index, row in wire_database.iterrows():
        assign_wire(G, Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'], True))
    return G, trial_ID

def plot_generated_graph(G, plot_show=True, dpi_chosen=400, name_of_map="/Map_Prototoype"):
    pos = nx.spring_layout(G)
    nx.draw(G, pos)
    nx.draw_networkx_labels(G, pos)

    labels = nx.get_edge_attributes(G, 'weight_based_conf')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    figure = plt.gcf()
    figure.set_size_inches(15, 10)
    #plt.savefig(path+name_of_map+str(trial_no)+".png", dpi=dpi_chosen)
    if plot_show:
        plt.show()
    plt.clf(); plt.cla(); plt.close()

def generate_db_name_csv_for_edge_files(Graph,target_path_and_name="/actual_databases/Not_Known.csv",headlines="Gene_Symb,Transcription_Level,Hotpoint_Mutation,CRISPR_KO_Effect,Differentiation_Rate", target_path=path_of_main_dir+"/"):
    db_headline_ls = headlines.rsplit(","); headline_count= len(db_headline_ls)
    db_file = open(path_of_main_dir+str(target_path_and_name), "w")
    db_file.write(headlines)
    db_file.write("\n")
    for node in Graph.nodes:
        line=str(node)
        for number_of_headlines in range(headline_count-1):
            line+=",None"
        line+="\n"
        db_file.write(line)
    db_file.close()



