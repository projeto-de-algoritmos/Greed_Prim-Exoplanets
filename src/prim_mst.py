import heapq
import csv
from graph_generation import csv_read


class MST(dict):
    def __init__(self):
        self.vertices = []
        self.edges = {}

    def add_vertex(self, vertex):
        self.vertices = vertex

    def add_edge(self, v1, v2, distance):
        self.edges.setdefault(v1, []).append([v2, distance])


def prim(graph):
    mst = MST()

    while graph.vertices:
        current = heapq.heappop(graph.vertices)
        mst.vertices.append(current[1])
        if current[2]:
            mst.add_edge(current[2], current[1], current[0])

        for item in graph.edges[current[1]]:
            if item[0] not in mst.vertices:
                for sublist in graph.vertices:
                    if sublist[1] == item[0]:
                        if float(item[1]) < float(sublist[0]):
                            sublist[0] = float(item[1])
                            sublist[2] = current[1]
    return mst


def write_output(mst):
    with open('mst.csv', 'w+') as csv_output:
        csv_writer = csv.writer(csv_output, delimiter=',')
        for row in mst.edges:
            csv_writer.writerow([row, mst.edges[row]])


def main():
    graph = csv_read()
    mst = prim(graph)
    write_output(mst)


if __name__ == "__main__":
    main()
