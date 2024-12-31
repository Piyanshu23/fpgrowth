from collections import defaultdict, OrderedDict
from csv import reader
from itertools import chain, combinations
from optparse import OptionParser
from fpgrowth_py.utils import *

def fpgrowth(itemSetList, minSupRatio, minConf):
    frequency = getFrequencyFromList(itemSetList)
    minSup = len(itemSetList) * minSupRatio
    fpTree, headerTable = constructTree(itemSetList, frequency, minSup)
    if(fpTree == None):
        print('No frequent item set')
    else:
        freqItems = []
        mineTree(headerTable, minSup, set(), freqItems)
        rules = associationRule(freqItems, itemSetList, minConf)
        return freqItems, rules

def fpgrowthFromFile(fname, minSupRatio, minConf):
    itemSetList, frequency = getFromFile(fname)
    minSup = len(itemSetList) * minSupRatio
    fpTree, headerTable = constructTree(itemSetList, frequency, minSup)
    if(fpTree == None):
        print('No frequent item set')
        return "", ""
    else:
        freqItems = []
        mineTree(headerTable, minSup, set(), freqItems)
        rules = associationRule(freqItems, itemSetList, minConf)
        return freqItems, rules

if __name__ == "__main__":
    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='inputFile',
                         help='CSV filename',
                         default=None)
    optparser.add_option('-s', '--minSupport',
                         dest='minSup',
                         help='Min support (float)',
                         default=0.5,
                         type='float')
    optparser.add_option('-c', '--minConfidence',
                         dest='minConf',
                         help='Min confidence (float)',
                         default=0.5,
                         type='float')

    (options, args) = optparser.parse_args()

    freqItemSet, rules = fpgrowthFromFile(
        options.inputFile, options.minSup, options.minConf)

    print(freqItemSet)
    print()
    print(rules)
    print()
    
    user_input = input("Input an Items (comma-separated): ")
    input_set = set(user_input.replace(" ", "").split(","))
    # input_set = set(list(filter(None, input_list.replace(" ",""))))
    print(user_input, input_set)
    suggestionSet = []
    for item in rules:
        first_set, second_set, decimal = item
        if first_set == input_set:
            suggestionSet.append((second_set, decimal))
    # for s in freqItemSet:
    #     if len(s) > 1:
    #         if item in s:
    #             for i in s:
    #                 suggestionSet.add(i)
    if len(suggestionSet) == 0:
        print("No suggestion as such.")
    else:
        suggestionSet.sort(key=lambda s:s[1], reverse=True)
        print(suggestionSet)
            
    