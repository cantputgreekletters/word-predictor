"""
D = {
    SingleWords: {
        word : {
            other_word : n,
            __Total__ : n
        },
    },
    ComboWords : {
        wordprev_word : {
            other_word : n
            __Total__ : n
        },
    }
    }
}
"""
_SingleWords = "SingleWords"
_ComboWords = "ComboWords"
_Tots = "__Total__"
_TheRaven_path : str = "data/TheRaven.txt"

def _my_filter(word : str) -> str:
    new_word : str = ""
    for i in word:
        if i in ('"', "'", ",", "!", ".", ";", "`", '“', '’', '?'):
            continue
        new_word += i
    return new_word.lower()

def _counter_to_probs(D : dict[dict[set]]) -> dict:
    new_d = {}
    for instance_key in D.keys():
        new_d[instance_key] = {}
        instance = D[instance_key]
        for key in instance.keys():
            new_d[key] = {}
            for word in instance[key].keys():
                if str(key) == _Tots: continue
                new_d[key][word] = instance[key][word] / instance[key][_Tots]
    return new_d

def _IncrementWord(key_word : str, other_word : str, D : dict) -> None:
    try:
        D[key_word]
    except KeyError:
        D[key_word] = {}
        D[key_word][_Tots] = 0
    try:
        D[key_word][other_word]
    except KeyError:
        D[key_word][other_word] = 1
    else:
        D[key_word][other_word] += 1
    D[key_word][_Tots] += 1

def _SplitWords(text : str) -> list[str]:
    Words = text.split()
    Words = list(map(_my_filter, Words))
    return Words

def GetText() -> str:
    with open(_TheRaven_path, "r", encoding="utf-8") as f:
        contents : str = f.read()
    return contents

def GetProbabilitiesDict(words : str) -> dict:
    Words : list[str] = _SplitWords(words)
    Probs : dict[dict] = {
        _SingleWords : {},
        _ComboWords : {}
    }
    #scanning
    for i in range(0, len(Words) - 2):
        current_word = Words[i]
        next_word = Words[i + 1]
        _IncrementWord(current_word, next_word, Probs[_SingleWords])
        #combo words
        if(i == 0): continue
        previous_word = Words[i - 1]
        _IncrementWord(previous_word + current_word, next_word, Probs[_ComboWords])
    return _counter_to_probs(Probs)

def Predict(word1 : str, word2 : str, D : dict[dict[dict]]) -> str:
    cand_words : list[str] = D[word2].keys()
    shared_words : list[str] = []
    for word in cand_words:
        try:
            D[word1 + word2][word]
        except KeyError:
            pass
        else:
            if(word == _Tots): continue
            shared_words.append(word)
    if len(shared_words) == 0:
        return "Could not predict"
    #calculate probabilities
    probs : list[float] = []
    for word in shared_words:
        probs.append(D[word2][word] * D[word1 + word2][word])
    return shared_words[probs.index(max(probs))]

if __name__ == "__main__":
    from pprint import pprint
    text = GetText()
    D = GetProbabilitiesDict(text)
    re = Predict("the", "raven", D)
    print(f"Result is = {re}")