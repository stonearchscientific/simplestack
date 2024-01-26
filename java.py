from jpype import JClass
import datetime

def date(dt):
    return JClass('java.util.Date')(dt.year - 1900, dt.month - 1, dt.day)
def python_date(jd):
    return datetime.date(jd.getYear() + 1900, jd.getMonth() + 1, jd.getDate())
def int(x):
    return JClass('java.lang.Integer')(x)
def interval(start, end, dimension=1, left="closed", right="closed"):
    Range = JClass('com.google.common.collect.Range')
    Interval = JClass('org.nmdp.ngs.fca.Interval')
    if left == "open" and right == "open":
        return Interval(dimension, Range.open(start, end))
    elif left == "open" and right == "closed":
        return Interval(dimension, Range.openClosed(start, end))
    elif left == "closed" and right == "open":
        return Interval(dimension, Range.closedOpen(start, end))
    else:
        return Interval(dimension, Range.closed(start, end))