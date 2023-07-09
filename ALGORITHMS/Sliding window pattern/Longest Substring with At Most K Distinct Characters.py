
def minSubArrayLen(k, string):
    char = {}
    wstart, maxlen = 0, 0
    for wend in range(len(string)):
        if string[wend] not in char:
            char[string[wend]] = 0
        char[string[wend]] += 1

        while len(list(char.keys())) > k:
            char[string[wstart]] -= 1
            if char[string[wstart]] == 0:
                del char[string[wstart]]
            wstart += 1
        maxlen = max(maxlen, wend - wstart + 1)

    return maxlen

print(minSubArrayLen(3, 'abcyzaaaa'))


