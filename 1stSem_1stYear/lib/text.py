def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if type(text) is not str:
        raise TypeError('Нужна строка')
    if text=='':
        return ''
    if casefold:
        text=text.casefold()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
    text=' '.join(text.split())
    return text
    
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

def tokenize(text: str) -> list[str]:
    if type(text) is not str:
        raise TypeError('Нужна строка')
    text=normalize(text)
    result=[]
    token=[]
    for character in text:
        if character.isalnum() or character=='_':
            token.append(character)
        elif character=='-' and token and token[-1].isalnum():
            token.append(character)
        else:
            if token and token[-1]!='-':
                result.append(''.join(token))
                token=[]
    result.append(''.join(token))
    return result

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    if type(tokens) is not list:
        raise TypeError('Нужен список')
    return {word: tokens.count(word) for word in set(tokens)}

print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if type(freq) is not dict:
        raise TypeError('Нужен словари')
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]

print(top_n(count_freq(["a","b","a","c","b","a"])))
print(top_n(count_freq(["bb","aa","bb","aa","cc"])))