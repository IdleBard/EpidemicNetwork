#! .\venv\Scripts\python.exe

#------------------------------------------------------------
# Project : Epidemic Network
#------------------------------------------------------------
# Description : 
#------------------------------------------------------------
# Author : nrigotti
#------------------------------------------------------------
import igraph
import random

from igraph       import Graph, plot
from numpy.random import uniform

def generate_graph():
    network = Graph.Famous('Zachary')
    network.vs["is_infected"]   = False
    network.vs["recovery_time"] = 0

    my_vcount  = network.vcount()
    p_infected = 0.1

    res = random.sample(range(1, my_vcount), round(my_vcount * p_infected))
    print(res)
    network.vs[res]["is_infected"] = True
    return network


def run_simulation(network, iterations = 10):

    tx_prob = 0.5
    max_recovery_time = 2

    for t in range(0,iterations):

        infected = list()
        for p in network.vs:
            if p["is_infected"]:
                infected.append(p)

        for i in list(infected):
            i["recovery_time"] -= 1
            if i["recovery_time"] < 1:
                i["is_infected"] = False


            neighbors = network.neighbors(i)

            for n in neighbors:
                if network.vs[n]["is_infected"] == False:
                    if uniform() > tx_prob:
                        network.vs[n]["is_infected"]   = True
                        network.vs[n]["recovery_time"] = max_recovery_time
    
    return network


def plot_network(network):
    # my_vcount = network.vcount()
    print(network.vs)
    network.vs["color"] = "Red"

    network.vs["color"] = [ ("Red" if f else "Blue") for f in network.vs["is_infected"] ]

    plot(network)

# Main
if __name__ == "__main__":
    print("igraph " + igraph.__version__)

    my_n = int(1.352 * (10**3))
    my_p = 0.1**1

    # g = Graph()
    # g = Graph.Tree(127, 2)
    # g = Graph.Erdos_Renyi(my_n, p=my_p)
    # g = Graph.Famous('Zachary')
    g = generate_graph()

    plot_network(g)
    g = run_simulation(g)
    plot_network(g)
   