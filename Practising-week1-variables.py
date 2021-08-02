




class Sequence(object):

    def __init__(self, identifier, comment, seq):
        self.id = identifier
        self.comment = comment
        self.seq = self._clean(seq)


    def _clean(self, seq):
        """
        remove newline from the string representing the sequence
        :param seq: the string to clean
        :return: the string without '\n'
        :rtype: string
        """
        return seq.replace('\n')


    def gc_percent(self):
        """
        :return: the gc ratio
        :rtype: float
        """
        seq = self.seq.upper()
        return float(seq.count('G') + seq.count('C')) / len(seq)




dna1 = Sequence('gi214', 'the first sequence', 'tcgcgcaacgtcgcctacatctcaagattca')
dna2 = Sequence('gi3421', 'the second sequence', 'gagcatgagcggaattctgcatagcgcaagaatgcggc')
class MyClass(object):

    class_attr = 'foo'

    def __init__(self, val):
        self.inst_attr = val


a = MyClass(1)
b = MyClass(2)

print(a.inst_attr)
1
print(b.inst_attr)
2

print(a.class_attr == b.class_attr)
True
print(a.class_attr is b.class_attr)
True

b.class_attr = 4

print(a.class_attr)
4
del a.class_attr

MyClass.class_attr = 4