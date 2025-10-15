from text import *

def main():
    text = input()
    normalized = normalize(text)
    words = tokenize(normalized)
    freq = count_freq(words)
    top = top_n(freq, 5)
    total = len(words)
    unique = len(freq.items())
    print(f"Всего слов: {total}")
    print(f"Уникальных слов: {unique}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")
if __name__ == "__main__":
    main()