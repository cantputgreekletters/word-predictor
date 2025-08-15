from FetchData import *
from Choice import Choose

from enum import IntEnum

def _Main(argc : int, argv : list[str]) -> None:
    training_text : str = Choose()
    D = GetProbabilitiesDict(training_text)
    if(argc == 3):
        re = Predict(argv[1], argv[2], D)
    else:
        word1 = input("Give the first word\n").lower()
        word2 = input("Give the second word\n").lower()
        re = Predict(word1, word2, D)
    print(f"The prediction is = {re}")

if __name__ == "__main__":
    from sys import argv
    _Main(len(argv), argv)