#!/usr/bin/env python3
"""
Lab 0: Programming Skills Assessment
Count occurrences of specific words in the Bible text.
"""

import re
import os

def count_words(filename, target_words):
    """
    Count occurrences of specific words in a text file.

    Args:
        filename (str): Path to the text file
        target_words (list): List of words to count (will be converted to lowercase)

    Returns:
        dict: Dictionary with word counts
    """
    # Initialize counters
    word_counts = {word.lower(): 0 for word in target_words}

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Convert line to lowercase and extract words using regex
                # \w+ matches word characters (letters, digits, underscores)
                words = re.findall(r'\w+', line.lower())

                # Count target words
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    return word_counts

def main():
    """Main function to run the word counting task."""
    # Check if bible.txt exists
    filename = "bible.txt"
    if not os.path.exists(filename):
        print(f"Error: {filename} not found in current directory.")
        print("Please ensure the Bible text file is downloaded and named 'bible.txt'")
        return

    # Target words to count
    target_words = ["lord", "to", "36"]

    print("Lab 0: Word Counting in Bible Text")
    print("=" * 40)
    print(f"Analyzing file: {filename}")
    print(f"Target words: {target_words}")
    print()

    # Count the words
    results = count_words(filename, target_words)

    if results:
        print("Results:")
        print("-" * 20)
        for word, count in results.items():
            print(f"'{word}': {count:,} occurrences")

        # Calculate total words processed
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                total_words = 0
                for line in file:
                    words = re.findall(r'\w+', line.lower())
                    total_words += len(words)

            print(f"\nTotal words in text: {total_words:,}")
            print(f"Target words found: {sum(results.values()):,}")
            print(f"Percentage of target words: {sum(results.values())/total_words*100:.2f}%")

        except Exception as e:
            print(f"Error calculating statistics: {e}")

if __name__ == "__main__":
    main()