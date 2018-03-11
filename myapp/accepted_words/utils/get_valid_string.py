import argparse
import os

def main():
    args = parse_argument()
    word = args.input_word
    get_accepted_words(word)

def get_accepted_words(word):
    word = ''.join(sorted(word.lower()))
    accepted_words = []
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'accepted_words.txt')
    with open(file_path, 'r') as fh:
        for accepted_word in fh:
            accepted_word = accepted_word.rstrip().lower()
            sorted_word = ''.join(sorted(accepted_word))
            if sorted_word in word:
                accepted_words.append(accepted_word)
    return accepted_words

def generate_word_combinations(word):
    """ This will generated a list of Combination based on the given string """
    list_of_words = []
    for word_length in range (1, len(word)+1):
        for generated_word in permutations(word, word_length):
            list_of_words.append("".join(generated_word))
    return list_of_words


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_word", help="Input String where words will be generated", type=str)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()

