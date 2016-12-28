import networkx as nx
import logging
import threading
import time

# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',filename='mycalc.log',filemode='w')
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)
# logging.warning('This is warning message')
# logging.info('This is info message')
# logging.debug('This is debug message')

ISOTIMEFORMAT = '%Y-%m-%d %X'

print time.strftime(ISOTIMEFORMAT, time.localtime())

with open("/home/sysadmin/Documents/ndwww/www.dat", "rb") as f:
    www = f.readlines()
G = nx.DiGraph()
for i in www:
    start = i.split(" ")[0]
    end = i.split(" ")[1].split("\n")[0]
    G.add_edge(start, end)

print ('The graph has been built!')
print (nx.info(G))

nG = G.to_undirected()
K = len(nG.edges())
N = len(nG.nodes())

print ('K = %d' % K)
print ('N = %d' % N)

avg = 0.0
num = 0

if not nx.is_connected(nG):
    raise nx.NetworkXError("Graph nG is not connected.")

for node in nG:
    print ('%s, node = %s, number = %d, sum = %f' % (time.strftime(ISOTIMEFORMAT, time.localtime()),node, num, avg))
    num += 1
    path_length=nx.single_source_shortest_path_length(G, node)
    avg += sum(path_length.values())

n=len(nG)

print ('Calc finished!')
print ('The sum is %f' % avg)
print ('The n is %d' % n)
print ('The avg is %f' % avg/(n*(n-1)))

print time.strftime(ISOTIMEFORMAT, time.localtime())