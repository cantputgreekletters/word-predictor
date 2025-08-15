from FetchData import *
from Choice import Choose

def _GenerateText(starting_word1 : str, starting_word2 : str, D : dict, word_amount : int = 250) -> str:
    final_text = f"{starting_word1} {starting_word2}"
    for _ in range(word_amount):
        seperated_text = final_text.split()
        final_text += ' ' + Predict(seperated_text[-2], seperated_text[-1], D)
    return final_text

def _Main(argc : int, argv : list[str]) -> None:
    training_text : str = Choose()
    D = GetProbabilitiesDict(training_text)
    if(argc == 3):
        result = _GenerateText(argv[1], argv[2], D)
    else:
        result = _GenerateText("while", "i", D)
    print(f"Result is:\n{result}")

if __name__ == "__main__":
    from sys import argv
    _Main(len(argv), argv)