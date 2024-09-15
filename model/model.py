import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._states = DAO.getAllStates()
        self._idMap = {}
        for s in self._states:
            self._idMap[s.id] = s

    def buildGraph(self, s, y):

        self._grafo.add_nodes_from(self._states)

        neight = DAO.getAllEdges(s, y, self._idMap)
        for n in neight:
            self._grafo.add_edge(n.state1, n.state2, weight=n.tot)

    def getWeight(self):
        lista = []
        for v in self._grafo.nodes:
            somma = 0
            for n in list(self._grafo.neighbors(v)):
                somma += self._grafo[v][n]["weight"]
            lista.append((v, somma))
        return lista



    def getAllYears(self):
        years = list(set([date.year for date in DAO.getAllYears()]))
        return years

    def getAllShapes(self):
        return DAO.getAllShapes()

    def getNodes(self):
        return len(self._grafo.nodes)

    def getEdges(self):
        return len(self._grafo.edges)

