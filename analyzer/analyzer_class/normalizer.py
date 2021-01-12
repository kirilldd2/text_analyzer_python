import maru
import pymorphy2


class Normalizer(object):
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
        self.analyzer = maru.get_analyzer(tagger='crf', lemmatizer='pymorphy')

    def get_norm_pymorphy(self, word):
        return self.morph.parse(word)[0].normal_form

    def pymorphy2(self, words):
        return [self.morph.parse(word)[0].normal_form for word in words]


    def maru(self, words):
        return [word.lemma for word in self.analyzer.analyze(words)]

    def normalize_ner(self, words):
        return [word.lemma for word in self.analyzer.analyze(words)]