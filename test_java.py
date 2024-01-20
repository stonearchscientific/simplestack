import java
import jpype.imports
from datetime import date

guava = './guava-31.0.1-jre.jar'
fca = './ngs-fca-1.9-SNAPSHOT.jar'
tinkerpop = './blueprints-core-2.6.0.jar'
jpype.startJVM(classpath=[fca, guava, tinkerpop, 'classes'], convertStrings=False)

def test_date():
    dt = java.date(date(2021, 1, 1))
    assert dt.getYear() == 121
    assert dt.getMonth() == 0
    assert dt.getDate() == 1
def test_python_date():
    dt = java.date(date(2021, 1, 1))
    assert java.python_date(dt) == date(2021, 1, 1)
def test_interval():
    int_interval = java.interval(java.int(1), java.int(2))
    assert int_interval.getDimension() == 1
    assert int_interval.toRange().lowerEndpoint() == 1
    assert int_interval.toRange().upperEndpoint() == 2



