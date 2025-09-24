#!/usr/bin/env python3
"""
Lab 1: Text Preprocessing and Laws Analysis
Implements tokenization, case folding, stopping, and Porter stemming.
Analyzes Zipf's Law, Benford's Law, and vocabulary growth.
"""

import re
import math
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import numpy as np
from scipy.optimize import curve_fit

class PorterStemmer:
    """Implementation of Porter Stemmer algorithm."""

    def __init__(self):
        self.consonant = "[^aeiouAEIOU]"
        self.vowel = "[aeiouAEIOU]"

    def _is_consonant(self, word, i):
        """Check if character at position i is a consonant."""
        if word[i] in 'aeiou':
            return False
        if word[i] == 'y':
            return i == 0 or not self._is_consonant(word, i-1)
        return True

    def _measure(self, word):
        """Calculate the measure of a word."""
        n = 0
        i = 0
        while i < len(word):
            # Skip consonants at start
            while i < len(word) and self._is_consonant(word, i):
                i += 1
            if i >= len(word):
                break
            # Skip vowels
            while i < len(word) and not self._is_consonant(word, i):
                i += 1
            n += 1
        return n

    def _contains_vowel(self, word):
        """Check if word contains a vowel."""
        return any(not self._is_consonant(word, i) for i in range(len(word)))

    def _ends_with_double_consonant(self, word):
        """Check if word ends with double consonant."""
        return (len(word) >= 2 and
                word[-1] == word[-2] and
                self._is_consonant(word, len(word)-1))

    def _cvc(self, word):
        """Check if word ends with consonant-vowel-consonant pattern."""
        return (len(word) >= 3 and
                self._is_consonant(word, len(word)-3) and
                not self._is_consonant(word, len(word)-2) and
                self._is_consonant(word, len(word)-1) and
                word[-1] not in 'wxy')

    def stem(self, word):
        """Apply Porter stemming algorithm."""
        word = word.lower()
        if len(word) <= 2:
            return word

        # Step 1a
        if word.endswith('sses'):
            word = word[:-2]
        elif word.endswith('ies'):
            word = word[:-2]
        elif word.endswith('ss'):
            pass
        elif word.endswith('s'):
            word = word[:-1]

        # Step 1b
        if word.endswith('eed'):
            if self._measure(word[:-3]) > 0:
                word = word[:-1]
        elif word.endswith('ed'):
            if self._contains_vowel(word[:-2]):
                word = word[:-2]
                if word.endswith(('at', 'bl', 'iz')):
                    word += 'e'
                elif self._ends_with_double_consonant(word) and word[-1] not in 'lsz':
                    word = word[:-1]
                elif self._measure(word) == 1 and self._cvc(word):
                    word += 'e'
        elif word.endswith('ing'):
            if self._contains_vowel(word[:-3]):
                word = word[:-3]
                if word.endswith(('at', 'bl', 'iz')):
                    word += 'e'
                elif self._ends_with_double_consonant(word) and word[-1] not in 'lsz':
                    word = word[:-1]
                elif self._measure(word) == 1 and self._cvc(word):
                    word += 'e'

        # Step 2
        if self._measure(word[:-1]) > 0:
            if word.endswith('ational'):
                word = word[:-7] + 'ate'
            elif word.endswith('tional'):
                word = word[:-6] + 'tion'
            elif word.endswith('enci'):
                word = word[:-4] + 'ence'
            elif word.endswith('anci'):
                word = word[:-4] + 'ance'
            elif word.endswith('izer'):
                word = word[:-4] + 'ize'
            elif word.endswith('abli'):
                word = word[:-4] + 'able'
            elif word.endswith('alli'):
                word = word[:-4] + 'al'
            elif word.endswith('entli'):
                word = word[:-6] + 'ent'
            elif word.endswith('eli'):
                word = word[:-3] + 'e'
            elif word.endswith('ousli'):
                word = word[:-5] + 'ous'
            elif word.endswith('ization'):
                word = word[:-7] + 'ize'
            elif word.endswith('ation'):
                word = word[:-5] + 'ate'
            elif word.endswith('ator'):
                word = word[:-4] + 'ate'
            elif word.endswith('alism'):
                word = word[:-6] + 'al'
            elif word.endswith('iveness'):
                word = word[:-7] + 'ive'
            elif word.endswith('fulness'):
                word = word[:-7] + 'ful'
            elif word.endswith('ousness'):
                word = word[:-7] + 'ous'
            elif word.endswith('aliti'):
                word = word[:-5] + 'al'
            elif word.endswith('iviti'):
                word = word[:-5] + 'ive'
            elif word.endswith('biliti'):
                word = word[:-6] + 'ble'

        # Step 3
        if self._measure(word[:-1]) > 0:
            if word.endswith('icate'):
                word = word[:-3]
            elif word.endswith('ative'):
                word = word[:-5]
            elif word.endswith('alize'):
                word = word[:-3]
            elif word.endswith('iciti'):
                word = word[:-5] + 'ic'
            elif word.endswith('ical'):
                word = word[:-2]
            elif word.endswith('ful'):
                word = word[:-3]
            elif word.endswith('ness'):
                word = word[:-4]

        # Step 4
        if self._measure(word[:-1]) > 1:
            if word.endswith(('al', 'ance', 'ence', 'er', 'ic', 'able', 'ible', 'ant', 'ement', 'ment', 'ent')):
                if word.endswith('ement'):
                    word = word[:-6]
                elif word.endswith(('ment', 'able', 'ible')):
                    word = word[:-4]
                elif word.endswith(('ance', 'ence')):
                    word = word[:-4]
                else:
                    word = word[:-2]
            elif word.endswith('ion'):
                if len(word) >= 4 and word[-4] in 'st':
                    word = word[:-3]
            elif word.endswith('ou'):
                word = word[:-2]
            elif word.endswith('ism'):
                word = word[:-3]
            elif word.endswith('ate'):
                word = word[:-3]
            elif word.endswith('iti'):
                word = word[:-3]
            elif word.endswith('ous'):
                word = word[:-3]
            elif word.endswith('ive'):
                word = word[:-3]
            elif word.endswith('ize'):
                word = word[:-3]

        # Step 5a
        if word.endswith('e'):
            if self._measure(word[:-1]) > 1:
                word = word[:-1]
            elif (self._measure(word[:-1]) == 1 and
                  not self._cvc(word[:-1])):
                word = word[:-1]

        # Step 5b
        if (self._measure(word) > 1 and
            self._ends_with_double_consonant(word) and
            word.endswith('l')):
            word = word[:-1]

        return word

class TextPreprocessor:
    """Text preprocessing pipeline for TTDS Lab 1."""

    def __init__(self):
        self.stemmer = PorterStemmer()
        self.stop_words = {
            'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
            'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
            'to', 'was', 'will', 'with', 'i', 'you', 'we', 'they', 'she', 'her',
            'his', 'him', 'but', 'or', 'not', 'this', 'these', 'those', 'there',
            'their', 'them', 'have', 'had', 'been', 'being', 'do', 'does', 'did',
            'can', 'could', 'should', 'would', 'may', 'might', 'must', 'shall',
            'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
            'such', 'no', 'nor', 'only', 'own', 'same', 'so', 'than', 'too',
            'very', 's', 't', 'can', 'will', 'just', 'don', 'now', 'd', 'll',
            'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn',
            'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn',
            'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn'
        }

    def tokenize(self, text):
        """Tokenize text into words, removing punctuation."""
        # Use regex to extract word characters only
        tokens = re.findall(r'\w+', text.lower())
        return tokens

    def remove_stop_words(self, tokens):
        """Remove stop words from token list."""
        return [token for token in tokens if token not in self.stop_words]

    def stem_tokens(self, tokens):
        """Apply Porter stemming to tokens."""
        return [self.stemmer.stem(token) for token in tokens]

    def preprocess_text(self, text):
        """Complete preprocessing pipeline."""
        # Step 1: Tokenization and case folding
        tokens = self.tokenize(text)

        # Step 2: Stop word removal
        tokens = self.remove_stop_words(tokens)

        # Step 3: Stemming
        tokens = self.stem_tokens(tokens)

        return tokens

def analyze_zipf_law(token_counts):
    """Analyze Zipf's law distribution."""
    # Sort by frequency (descending)
    sorted_counts = sorted(token_counts.values(), reverse=True)
    ranks = list(range(1, len(sorted_counts) + 1))

    # Create log-log plot
    log_ranks = [math.log10(r) for r in ranks]
    log_freqs = [math.log10(f) for f in sorted_counts if f > 0]

    # Fit power law: log(f) = log(k) - alpha * log(r)
    if len(log_ranks) == len(log_freqs):
        coeffs = np.polyfit(log_ranks, log_freqs, 1)
        alpha = -coeffs[0]  # Zipf exponent
        k = 10**coeffs[1]   # Zipf constant

        return {
            'ranks': ranks,
            'frequencies': sorted_counts,
            'log_ranks': log_ranks,
            'log_frequencies': log_freqs,
            'alpha': alpha,
            'k': k
        }
    return None

def analyze_benford_law(frequencies):
    """Analyze first digit distribution (Benford's law)."""
    first_digits = []
    filtered_first_digits = []  # For frequencies >= 10

    for freq in frequencies:
        if freq > 0:
            first_digit = int(str(freq)[0])
            first_digits.append(first_digit)

            if freq >= 10:
                filtered_first_digits.append(first_digit)

    # Count distribution
    digit_counts = Counter(first_digits)
    filtered_digit_counts = Counter(filtered_first_digits)

    # Benford's law expected probabilities
    benford_expected = {d: math.log10(1 + 1/d) for d in range(1, 10)}

    return {
        'all_digits': digit_counts,
        'filtered_digits': filtered_digit_counts,
        'benford_expected': benford_expected
    }

def analyze_vocabulary_growth(text):
    """Analyze vocabulary growth following Heap's law."""
    preprocessor = TextPreprocessor()

    # Process text incrementally
    tokens = preprocessor.tokenize(text)
    unique_terms = set()
    growth_data = []

    for i, token in enumerate(tokens, 1):
        unique_terms.add(token)
        if i % 1000 == 0 or i == len(tokens):  # Sample every 1000 tokens
            growth_data.append((i, len(unique_terms)))

    # Fit Heap's law: V = k * N^b
    n_values = [point[0] for point in growth_data]
    v_values = [point[1] for point in growth_data]

    # Fit power law in log space
    log_n = [math.log(n) for n in n_values]
    log_v = [math.log(v) for v in v_values]

    coeffs = np.polyfit(log_n, log_v, 1)
    b = coeffs[0]  # Heap's exponent
    k = math.exp(coeffs[1])  # Heap's constant

    return {
        'growth_data': growth_data,
        'k': k,
        'b': b,
        'n_values': n_values,
        'v_values': v_values
    }

def process_collection(filename, collection_name):
    """Process a single text collection through complete analysis pipeline."""
    print(f"\nProcessing {collection_name}...")

    # Read text
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except UnicodeDecodeError:
        with open(filename, 'r', encoding='latin1') as f:
            text = f.read()

    print(f"Loaded {len(text):,} characters")

    # Preprocess text
    preprocessor = TextPreprocessor()
    tokens = preprocessor.preprocess_text(text)

    print(f"Generated {len(tokens):,} tokens after preprocessing")

    # Count frequencies
    token_counts = Counter(tokens)
    print(f"Unique terms: {len(token_counts):,}")

    # Analyze Zipf's law
    zipf_results = analyze_zipf_law(token_counts)
    print(f"Zipf analysis: alpha = {zipf_results['alpha']:.3f}, k = {zipf_results['k']:.1f}")

    # Analyze Benford's law
    benford_results = analyze_benford_law(list(token_counts.values()))
    print(f"Benford analysis: {len(benford_results['all_digits'])} digit categories")

    # Analyze vocabulary growth
    growth_results = analyze_vocabulary_growth(text)
    print(f"Heap's law: k = {growth_results['k']:.1f}, b = {growth_results['b']:.3f}")

    return {
        'tokens': tokens,
        'token_counts': token_counts,
        'zipf': zipf_results,
        'benford': benford_results,
        'growth': growth_results
    }

def create_plots(results, collection_name):
    """Create visualization plots for analysis results."""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(f'{collection_name} - Text Analysis Results')

    # Zipf's law plot
    zipf = results['zipf']
    ax1.loglog(zipf['ranks'], zipf['frequencies'])
    ax1.set_xlabel('Rank')
    ax1.set_ylabel('Frequency')
    ax1.set_title(f"Zipf's Law (α = {zipf['alpha']:.3f})")
    ax1.grid(True)

    # Benford's law plot
    benford = results['benford']
    digits = list(range(1, 10))
    all_counts = [benford['all_digits'].get(d, 0) for d in digits]
    filtered_counts = [benford['filtered_digits'].get(d, 0) for d in digits]
    expected = [benford['benford_expected'][d] * sum(all_counts) for d in digits]

    x = np.arange(len(digits))
    width = 0.25

    ax2.bar(x - width, all_counts, width, label='All frequencies')
    ax2.bar(x, filtered_counts, width, label='Frequencies ≥ 10')
    ax2.bar(x + width, expected, width, label='Benford expected')
    ax2.set_xlabel('First Digit')
    ax2.set_ylabel('Count')
    ax2.set_title("Benford's Law Distribution")
    ax2.set_xticks(x)
    ax2.set_xticklabels(digits)
    ax2.legend()

    # Vocabulary growth plot
    growth = results['growth']
    ax3.plot(growth['n_values'], growth['v_values'], 'b-', label='Observed')

    # Plot fitted curve
    fitted_v = [growth['k'] * (n ** growth['b']) for n in growth['n_values']]
    ax3.plot(growth['n_values'], fitted_v, 'r--', label=f"Fitted: V = {growth['k']:.1f} × N^{growth['b']:.3f}")

    ax3.set_xlabel('Total Terms (N)')
    ax3.set_ylabel('Unique Terms (V)')
    ax3.set_title("Vocabulary Growth (Heap's Law)")
    ax3.legend()
    ax3.grid(True)

    # Distribution of term frequencies
    freq_dist = Counter(results['token_counts'].values())
    frequencies = sorted(freq_dist.keys())
    counts = [freq_dist[f] for f in frequencies]

    ax4.loglog(frequencies, counts)
    ax4.set_xlabel('Term Frequency')
    ax4.set_ylabel('Number of Terms')
    ax4.set_title('Term Frequency Distribution')
    ax4.grid(True)

    plt.tight_layout()
    plt.savefig(f'{collection_name.lower().replace(" ", "_")}_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Main analysis function."""
    collections = [
        ('pg10.txt', 'Bible'),
        ('quran.txt', 'Quran'),
        ('abstracts.wiki.txt', 'Wikipedia')
    ]

    all_results = {}

    for filename, name in collections:
        try:
            results = process_collection(filename, name)
            all_results[name] = results
            create_plots(results, name)

            # Save preprocessed tokens
            output_filename = f'{name.lower()}_preprocessed.txt'
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(' '.join(results['tokens']))
            print(f"Saved preprocessed text to {output_filename}")

        except Exception as e:
            print(f"Error processing {name}: {e}")

    # Create comparison summary
    print("\n" + "="*60)
    print("COMPARATIVE SUMMARY")
    print("="*60)

    print(f"{'Collection':<12} {'Tokens':<10} {'Unique':<8} {'Zipf α':<8} {'Heap k':<8} {'Heap b':<8}")
    print("-"*60)

    for name, results in all_results.items():
        tokens = len(results['tokens'])
        unique = len(results['token_counts'])
        zipf_alpha = results['zipf']['alpha']
        heap_k = results['growth']['k']
        heap_b = results['growth']['b']

        print(f"{name:<12} {tokens:<10,} {unique:<8,} {zipf_alpha:<8.3f} {heap_k:<8.1f} {heap_b:<8.3f}")

if __name__ == "__main__":
    main()