import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',filename='mycalc.log',filemode='w')
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This is debug message')

import networkx as nx
import copy
import random
import matplotlib.pyplot as plt

def random_0k_with_p(G0, p=1):
    G = copy.deepcopy(G0)      
    if p<0 or p>1:
            raise nx.NetworkXError("Invalid p!.")
    K = len(G.edges())
    N = len(G.nodes())
    max_tries = K *p
    rewiring_tries = 0
    while rewiring_tries < max_tries:
        u,v = random.choice(G.edges())
        x,y = random.sample(G.nodes(),2)
        if (x,y) not in G.edges() and (y,x) not in G.edges():
            G.remove_edge(u,v)
            G.add_edge(x,y)
            rewiring_tries+=1
    return G

def calculate_e_global(G):
    avg = 0.0
    for node in G:
        path_length_list=nx.single_source_shortest_path_length(G, node)
        for e in path_length_list.values():
            if e != 0:
                avg += 1.0/e
            else:
                avg += 0
    n=len(G)
    avg = avg/(n*(n-1))
    return avg
    
def calculate_e_local(G):
    avg = 0.0
    for node in G:
        avg += calculate_e_global(G.subgraph(nx.bfs_successors(G,node)[node]))
    avg = avg/len(G)
    return avg

def calculate_e(G):
    eg = []
    el = []
    p = 0.0
    while p < 1:
        tempG = random_0k_with_p(G, p)
        logging.debug('p = %f' % p)
        e_glob = calculate_e_global(tempG)
        e_loc = calculate_e_local(tempG)
        logging.debug('e_glob = %f, e_loc = %f' % (e_glob, e_loc))
        eg.append(e_glob)
        el.append(e_loc)
        p += 0.01
    logging.info(eg)
    logging.info(el)

logging.info("Calculation Started...")
G = nx.random_graphs.gnm_random_graph(1000, 10000)
logging.info(nx.info(G))
calculate_e(G)
logging.info("Calculation Ended...")