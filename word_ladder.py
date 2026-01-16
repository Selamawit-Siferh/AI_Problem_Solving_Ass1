from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        print("End word not in dictionary!")
        return 0

    queue = deque([(beginWord, [beginWord])])  # store path instead of steps

    while queue:
        word, path = queue.popleft()

        # print the current word and path
        print(f"Current word: {word}, Path so far: {path}")

        if word == endWord:
            print(f"\nShortest transformation sequence found: {' -> '.join(path)}")
            return len(path)

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    queue.append((new_word, path + [new_word]))

    print("No transformation sequence found!")
    return 0

# Call the function and print the number of steps
steps = word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(f"\nNumber of steps: {steps}")