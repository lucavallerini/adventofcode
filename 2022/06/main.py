#!/bin/env python3

filename = 'input'
with open('input', 'r') as f:
    content = f.readlines()


buffer = content[0].replace("\n", '')


def all_different_characters(marker):
    return len(set(marker)) == len(marker)


def first_occurence_of_different_chars(window_size):
    for c in range(0, len(buffer) - window_size):
        if all_different_characters(buffer[c:c+window_size]):
            return c + window_size


print("First start-of-packet marker: " + str(first_occurence_of_different_chars(4)))
print("First start-of-message marker: " + str(first_occurence_of_different_chars(14)))
