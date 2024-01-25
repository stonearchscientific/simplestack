import pytest
import java
from lattice import dfs

from org.nmdp.ngs.fca import IntervalLattice

@pytest.fixture()
def lattice():
    lattice = IntervalLattice()
    for x in range(1, 4):
        lattice.insert(java.interval(java.int(x), java.int(x + 3)))
    yield lattice
@pytest.fixture()
def interval():
    def _args(x, y):
        return java.interval(java.int(x), java.int(y))
    return _args
def test_find(lattice, interval):
    found = lattice.findVertex(interval(3, 5))
    assert str(found.getProperty('label')) == '1:[3..5]'

    found = lattice.findVertex(interval(4, 5))
    assert str(found.getProperty('label')) == '1:[3..5]'

    found = lattice.findVertex(interval(3, 4))
    assert str(found.getProperty('label')) == '1:[3..4]'

def test_dfs(lattice, interval):
    start = lattice.findVertex(interval(3, 5))
    assert dfs(lattice, start, up=False) == ['1:[3..4]', '1:[3..5]']
    assert dfs(lattice, start, up=True) == ['(-∞..+∞)', '1:[3..5]', '1:[3..6]', '1:[2..5]']
