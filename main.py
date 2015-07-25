# -*- coding: utf-8 -*-

from synset_graph import SynsetGraph
from wordnet import WordnetUtilities as WNUtils


def evaluate(test_graph, gold_graph):
    gold_nodes = gold_graph.synset_nodes.values()
    test_nodes = test_graph.synset_nodes.values()

    total = sum([node.total_probability() for node in gold_nodes])
    success = sum([node.total_probability() for node in test_nodes
                   if node in gold_nodes])

    return (success / total)


def main():
    # print("Please write an Hebrew word")
    # word = input()
    # print("Enter number of wanted Synsets")
    # synsets_number = int(input())
    word = "מזגן"
    number_of_synsets = 2

    # word2vec definitions
    vector_file_path = "vectors-g.bin"
    topn = 500

    word2vec_synsets = WNUtils.get_word2vec_similar_synsets(word,
                                                            number_of_synsets,
                                                            vector_file_path,
                                                            topn)
    if word2vec_synsets is None:
        return None
    test_graph = SynsetGraph(word2vec_synsets)

    gold_synsets = WNUtils.get_gold_synsets(word)
    if gold_synsets is not None:
        gold_graph = SynsetGraph(gold_synsets)
        result = evaluate(test_graph, gold_graph)
        print("{0:.3f}".format(result))
        print("")
        gold_graph.print_tree()

    print("")
    test_graph.print_tree()

    #test_graph.print_leaves()
    #gold_graph.print_leaves()

if __name__ == '__main__':
    main()
