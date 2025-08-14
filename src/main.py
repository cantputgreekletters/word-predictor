from FetchData import *
from enum import IntEnum

class _train_choice(IntEnum):
    the_raven = 1
    custom = 2

def _choose() -> int:
    print("Which text should be used for training")
    while True:
        try:
            choice = int(input("1. The Raven\n2. Custom\n"))
        except:
            pass
        else:
            if(choice in (1,2)):
                break
    return choice

def _LoadCustom(path : str) -> str:
    with open(path, "r", encoding = "utf-8") as f:
        contents = f.read()
    if(contents):
        return contents
    else:
        raise Exception("Could not load the custom training text")

def _Main(argc : int, argv : list[str]) -> None:
    choice = _choose()
    if(choice == _train_choice.the_raven):
        training_text = GetText()
    if(choice == _train_choice.custom):
        path = input("Provide a file path\n")
        training_text = _LoadCustom(path)
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