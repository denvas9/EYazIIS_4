import os
import re
from nltk.corpus import wordnet

from wordcloud import WordCloud
from wiki_ru_wordnet import WikiWordnet

path = os.getcwd() + '/'


def letters_in_the_word(word):
    for i in list(word):
        if i == ' ':
            return False
    return True


def semantic_analysis(text):
    wikiwordnet = WikiWordnet()
    tree_text = re.sub('-', ',', text)
    if tree_text == '':
        return None
    if letters_in_the_word(tree_text):
        hyponyms = []
        # Кольцо синонимов или синсет - это группа элементов данных, которые считаются семантически эквивалентными
        # для целей поиска информации
        synsets2 = wikiwordnet.get_synsets(tree_text)
        text = ''
        lemmas2 = [x.lemma() for x in synsets2[0].get_words()]
        # Synset представляет группу лемм, имеющих одинаковый смысл, а лемма представляет собой отдельную словоформу.
        for lemma in lemmas2:
            text += lemma + ' '

        synset2 = synsets2[0]
        for hypernym in wikiwordnet.get_hypernyms(synset2):
            for w in hypernym.get_words():
                text += w.lemma() + ' '

        for hyponym in wikiwordnet.get_hyponyms(synset2):
            for w in hyponym.get_words():
                text += w.lemma() + ' '
        return word_cloud(text)


def word_cloud(text):
    # Облако тегов — это визуальное представление списка
    cloud = WordCloud(relative_scaling=1.0, ).generate(text)
    cloud.to_file(path + 'cloud.png')
    return open(path + 'cloud.png', 'rb')


