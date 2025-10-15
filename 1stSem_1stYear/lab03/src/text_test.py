from text import *

print('normilize')
print(r'ПрИвЕт\nМИр\t  Out: ', normalize('ПрИвЕт\nМИр\t'))
print(r'ёжик, Ёлка  Out: ', normalize('ёжик, Ёлка', yo2e=True))
print(r'Hello\r\nWorld  Out: ', normalize('Hello\r\nWorld'))
print(r' двойные пробелы   Out: ', normalize(' двойные пробелы '))

print('tokenize')
print(r'привет мир Out:', tokenize('привет мир'))
print(r'hello,world!!! Out:', tokenize('hello,world!!!'))
print(r'по-настоящему круто Out:', tokenize('по-настоящему круто'))
print(r'2025 год Out:', tokenize('2025 год'))
print(r'emoji 😀 не слово Out:', tokenize('emoji 😀 не слово'))

print('count_freq & top_n')
print(f'["a","b","a","c","b","a"] Out counter: {count_freq(["a","b","a","c","b","a"])} Out top_n {top_n(count_freq(["a","b","a","c","b","a"]))}')
print(f'["bb","aa","bb","aa","cc"] Out counter: {count_freq(["bb","aa","bb","aa","cc"])} Out top_n {top_n(count_freq(["bb","aa","bb","aa","cc"]), 2)}')
