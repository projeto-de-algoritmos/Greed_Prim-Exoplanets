import csv
import math
import heapq


class Graph(dict):
    def __init__(self):
        self.vertices = []
        self.edges = {}

    def add_vertex(self, distance, v, origin):
        heapq.heappush(self.vertices, [distance, v, origin])

    def add_edge(self, v1, v2, distance):
        self.edges.setdefault(v1, []).append([v2, distance])


def csv_read():
    graph = Graph()
    line_count = 0
    with open('../pre-processing/planets_xyz_values.csv') as csv_file, open('../pre-processing/planets_xyz_values.csv') as csv_aux:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_repeater = csv.reader(csv_aux, delimiter=',')
        for row in csv_reader:
            if line_count == 0:
                graph.add_vertex(0, row[0], '')
                for repeater in csv_repeater:
                    graph.add_edge(row[0], repeater[0], repeater[3])
                line_count += 1
            else:
                csv_aux.seek(0)
                graph.add_vertex(99999, row[0], '')
                for repeater in csv_repeater:
                    graph.add_edge(row[0], repeater[0], math.sqrt(math.pow(float(row[4]) - float(repeater[4]), 2) + math.pow(float(row[5]) - float(repeater[5]), 2) + math.pow(float(row[6]) - float(repeater[6]), 2)))
                line_count += 1
    return graph
