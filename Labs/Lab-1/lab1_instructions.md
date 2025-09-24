# Lab 1: Text Preprocessing and Analysis

## Requirements

### Software Needed
- **Preferred:** Perl or Python
- **Alternative:** Any programming language you're comfortable with

### Required Files to Download
1. **Bible:** pg10.txt
2. **Quran English translation:** quran.txt
3. **Wikipedia abstracts:** abstracts.wiki.txt.gz

## Tasks

### Part 1: Preprocessing
Apply the following preprocessing steps to all three text collections:

1. **Tokenisation**
   - Convert text to tokens
   - Remove punctuation
   - Split on whitespace and punctuation marks

2. **Case Folding**
   - Convert all text to lowercase
   - Ensure consistent case across all tokens

3. **Stopping**
   - Remove English stop words
   - Use standard stop word list (articles, prepositions, common words)

4. **Normalisation**
   - Apply Porter stemmer algorithm
   - Reduce words to their root forms
   - Handle common morphological variants

### Part 2: Text Laws Analysis

For each preprocessed collection, perform the following analyses:

#### 1. Unique Terms Frequency Analysis
- Count frequency of each unique term
- Plot term frequencies on log-log graph (x=rank, y=frequency)
- Analyze adherence to Zipf's law
- Expected pattern: straight line on log-log plot

#### 2. First Digit Distribution Analysis
- Extract first digit from each frequency count
- Plot distribution of first digits (1-9)
- Observe Benford's law pattern
- Repeat analysis excluding frequencies < 10
- Compare distributions between filtered and unfiltered data

#### 3. Vocabulary Growth Analysis
- Track vocabulary size vs. total terms processed
- Plot n (total terms read) vs. v (unique terms encountered)
- Fit power law equation: v = k × n^b
- Report best-fitting constants k and b for each collection
- Compare growth patterns across different text types

## Implementation Tips

### Unix Shell Commands
For term frequency analysis, you can use:
```bash
# Basic frequency count
cat file.txt | tr ' ' '\n' | tr 'A-Z' 'a-z' | sort | uniq -c | sort -nr

# For vocabulary growth tracking
# Process file incrementally and track unique terms
```

### Expected Outcomes
- **Zipf's Law:** Frequency rank follows power law distribution
- **Benford's Law:** First digits follow logarithmic distribution
- **Vocabulary Growth:** Sub-linear growth of unique terms vs. total terms

### Deliverables
1. Preprocessed versions of all three text collections
2. Frequency analysis plots and statistics
3. First digit distribution analysis
4. Vocabulary growth curves with fitted parameters
5. Comparative analysis across the three text types

## Assessment Criteria
- Correct implementation of preprocessing pipeline
- Accurate frequency counting and statistical analysis
- Clear visualization of text law patterns
- Insightful comparison between different text collections