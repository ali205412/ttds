#!/usr/bin/env python3
"""
Lab 1: Efficient Text Analysis
Processes Bible, Quran, and Wikipedia abstracts for text laws analysis.
"""

import re
import math
from collections import Counter
import os

# Simple stop words list
STOP_WORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
    'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
    'to', 'was', 'will', 'with', 'i', 'you', 'we', 'they', 'she', 'her',
    'his', 'him', 'but', 'or', 'not', 'this', 'these', 'those', 'there',
    'their', 'them', 'have', 'had', 'been', 'being', 'do', 'does', 'did'
}

def simple_stem(word):
    """Simple stemming - remove common suffixes."""
    word = word.lower()

    # Remove plurals
    if word.endswith('ies'):
        word = word[:-3] + 'y'
    elif word.endswith('es') and len(word) > 3:
        word = word[:-2]
    elif word.endswith('s') and len(word) > 3:
        word = word[:-1]

    # Remove common suffixes
    suffixes = ['ing', 'ed', 'er', 'est', 'ly', 'ion', 'tion', 'ness']
    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            word = word[:-len(suffix)]
            break

    return word

def preprocess_text(filename, max_lines=None):
    """Preprocess text file efficiently."""
    print(f"Processing {filename}...")

    tokens = []
    line_count = 0

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if max_lines and line_count >= max_lines:
                    break

                # Tokenize: extract word characters only
                words = re.findall(r'\w+', line.lower())

                # Remove stop words and stem
                for word in words:
                    if word not in STOP_WORDS and len(word) > 2:
                        stemmed = simple_stem(word)
                        tokens.append(stemmed)

                line_count += 1

                if line_count % 10000 == 0:
                    print(f"  Processed {line_count:,} lines, {len(tokens):,} tokens")

    except UnicodeDecodeError:
        # Try different encoding
        with open(filename, 'r', encoding='latin1') as f:
            for line in f:
                if max_lines and line_count >= max_lines:
                    break

                words = re.findall(r'\w+', line.lower())
                for word in words:
                    if word not in STOP_WORDS and len(word) > 2:
                        stemmed = simple_stem(word)
                        tokens.append(stemmed)

                line_count += 1

    print(f"  Final: {len(tokens):,} tokens from {line_count:,} lines")
    return tokens

def analyze_collection(filename, name, max_lines=None):
    """Analyze a single text collection."""
    print(f"\n{'='*50}")
    print(f"ANALYZING: {name}")
    print(f"{'='*50}")

    # Preprocess
    tokens = preprocess_text(filename, max_lines)
    if not tokens:
        print(f"No tokens found in {filename}")
        return None

    # Count frequencies
    token_counts = Counter(tokens)
    total_tokens = len(tokens)
    unique_tokens = len(token_counts)

    print(f"Total tokens: {total_tokens:,}")
    print(f"Unique tokens: {unique_tokens:,}")
    print(f"Vocabulary ratio: {unique_tokens/total_tokens:.4f}")

    # Get most common words
    print(f"\nTop 10 most frequent terms:")
    for word, count in token_counts.most_common(10):
        print(f"  {word}: {count:,}")

    # Zipf's Law Analysis
    print(f"\nZIPF'S LAW ANALYSIS:")
    frequencies = sorted(token_counts.values(), reverse=True)

    # Check Zipf's law for top terms
    zipf_constant = frequencies[0] * 1  # rank 1 * frequency should be constant
    print(f"Zipf constant (f1 * r1): {zipf_constant:,}")

    for i in [0, 4, 9, 49, 99]:  # ranks 1, 5, 10, 50, 100
        if i < len(frequencies):
            rank = i + 1
            freq = frequencies[i]
            predicted = zipf_constant / rank
            print(f"  Rank {rank:3d}: observed {freq:6,}, predicted {predicted:6.0f}, ratio {freq/predicted:.2f}")

    # Benford's Law Analysis
    print(f"\nBENFORD'S LAW ANALYSIS:")
    first_digits = [int(str(f)[0]) for f in frequencies if f > 0]
    digit_counts = Counter(first_digits)

    total_freqs = len(first_digits)
    print(f"First digit distribution (from {total_freqs:,} frequencies):")

    for digit in range(1, 10):
        observed = digit_counts.get(digit, 0)
        observed_pct = observed / total_freqs * 100 if total_freqs > 0 else 0
        benford_pct = math.log10(1 + 1/digit) * 100
        print(f"  Digit {digit}: {observed:4d} ({observed_pct:5.1f}%) vs Benford {benford_pct:5.1f}%")

    # Vocabulary Growth (simple analysis)
    print(f"\nVOCABULARY GROWTH ANALYSIS:")

    # Sample vocabulary growth at different points
    sample_points = [1000, 5000, 10000, 50000, 100000, len(tokens)]
    sample_points = [p for p in sample_points if p <= len(tokens)]

    print(f"Vocabulary growth pattern:")
    unique_so_far = set()

    for point in sample_points:
        # Count unique tokens up to this point
        unique_so_far.update(tokens[:point])
        vocab_size = len(unique_so_far)
        ratio = vocab_size / point

        print(f"  At {point:6,} tokens: {vocab_size:5,} unique ({ratio:.4f})")

    # Save preprocessed file
    output_file = f"{name.lower().replace(' ', '_')}_preprocessed.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        # Save sample of processed tokens (first 10000)
        sample_tokens = tokens[:10000] if len(tokens) > 10000 else tokens
        f.write(' '.join(sample_tokens))

    print(f"Saved sample to {output_file}")

    return {
        'name': name,
        'total_tokens': total_tokens,
        'unique_tokens': unique_tokens,
        'token_counts': token_counts,
        'top_terms': token_counts.most_common(10)
    }

def main():
    """Main analysis function."""
    collections = [
        ('pg10.txt', 'Bible', None),
        ('quran.txt', 'Quran', None),
        ('abstracts.wiki.txt', 'Wikipedia Abstracts', 50000)  # Limit Wikipedia to first 50k lines
    ]

    results = []

    for filename, name, max_lines in collections:
        if os.path.exists(filename):
            result = analyze_collection(filename, name, max_lines)
            if result:
                results.append(result)
        else:
            print(f"File not found: {filename}")

    # Final comparison
    if results:
        print(f"\n{'='*70}")
        print("COMPARATIVE SUMMARY")
        print(f"{'='*70}")

        print(f"{'Collection':<20} {'Total Tokens':<15} {'Unique Tokens':<15} {'Vocab Ratio':<12}")
        print("-" * 70)

        for result in results:
            ratio = result['unique_tokens'] / result['total_tokens']
            print(f"{result['name']:<20} {result['total_tokens']:<15,} {result['unique_tokens']:<15,} {ratio:<12.4f}")

if __name__ == "__main__":
    main()