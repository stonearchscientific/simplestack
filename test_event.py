from event import Reference
import java
import jpype.imports

guava = './guava-31.0.1-jre.jar'
fca = './ngs-fca-1.9-SNAPSHOT.jar'
tinkerpop = './blueprints-core-2.6.0.jar'
jpype.startJVM(classpath=[fca, guava, tinkerpop, 'classes'], convertStrings=False)
def test_reference():
    ref = Reference('test1', java.int(1), java.int(2))
    assert ref.name == 'test1'
    assert ref.interval.toRange().lowerEndpoint() == 1
    assert ref.interval.toRange().upperEndpoint() == 2
    assert ref.type == Reference.Type.DAY

    ref = Reference('test2', java.int(1), java.int(2), Reference.Type.MONTH)
    assert ref.name == 'test2'
    assert ref.type == Reference.Type.MONTH