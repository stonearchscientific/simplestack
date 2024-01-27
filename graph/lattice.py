import jpype.imports
import graphviz

guava = '../guava-31.0.1-jre.jar'
fca = '../ngs-fca-1.9-SNAPSHOT.jar'
tinkerpop = '../blueprints-core-2.6.0.jar'
jpype.startJVM(classpath=[fca, guava, tinkerpop, 'classes'], convertStrings=False)

from com.tinkerpop.blueprints import Direction
def draw(lattice):
    f = open('lattice.dot', 'w', encoding='utf-8')
    f.write(str(lattice.toString()))
    f.close()

    g = graphviz.Source.from_file('lattice.dot')
    g.view()

def dfs(lattice, start, up=True, labels=True):
    visited = set()
    stack = [start]
    filter_condition = lattice.up if up else lattice.down

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            targets = [edge.getVertex(Direction.IN) for edge in vertex.getEdges(Direction.BOTH)]
            stack.extend(target for target in targets if filter_condition(vertex, target) and target not in visited)

    if labels:
        return [str(vertex.getProperty('label')) for vertex in visited]
    return visited

