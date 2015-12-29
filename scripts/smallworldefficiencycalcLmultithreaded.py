import networkx as nx
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',filename='mycalc.log',filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

#logging.warning('This is warning message')
#logging.info('This is info message')
#logging.debug('This is debug message')

with open("/home/sysadmin/Documents/ndwww/www.dat", "rb") as f:
    www = f.readlines()
G = nx.DiGraph()
for i in www:
    start = i.split(" ")[0]
    end = i.split(" ")[1].split("\n")[0]
    G.add_edge(start, end)

logging.info('The graph has been built!')
logging.debug(nx.info(G))

nG = G.to_undirected()
K = len(G.edges())
N = len(G.nodes())

logging.info('K = %d' % K)
logging.info('N = %d' % N)

sum = 0
lock = threading.Lock()

def calc(start, end):
    global sum
    D = 0
    logging.info('thread %s is running...' % threading.current_thread().name)
    for i in range(start, end):
        for j in range(N):
            D += nx.shortest_path_length(nG,source=str(i),target=str(j))
        lock.acquire()
        try:
            logging.debug('thread %s, i = %d' % (threading.current_thread().name, i))
            logging.debug('thread %s, D = %d' % (threading.current_thread().name, D))
            logging.debug('thread %s, sum = %d' % (threading.current_thread().name, sum))
            sum += D
        except BaseException as e:
	        logging.exception(e)
        finally:
            lock.release()

t = threading.Thread(target=calc, args=(0,66000))
t1 = threading.Thread(target=calc, args=(66000,132000))
t2 = threading.Thread(target=calc, args=(132000,198000))
t3 = threading.Thread(target=calc, args=(198000,264000))
t4 = threading.Thread(target=calc, args=(264000,325729))

t.start()
t1.start()
t2.start()
t3.start()
t4.start()

t.join()
t1.join()
t2.join()
t3.join()
t4.join()

logging.info('Calc finished!')
logging.info('The sum is %d', sum)
