## Lab 1: Text Preprocessing and Laws Analysis

### Tasks Completed
1. **Text Preprocessing Pipeline**
   - Tokenization: Extract words using regex `\w+`
   - Case folding: Convert all text to lowercase
   - Stop word removal: Filter common English words
   - Normalization: Apply simple stemming algorithm

2. **Text Laws Analysis**
   - **Zipf's Law**: Frequency-rank distribution analysis
   - **Benford's Law**: First digit distribution of frequencies
   - **Vocabulary Growth**: Unique terms vs total terms relationship

### Collections Analyzed

#### Bible (pg10.txt)
- **Total tokens**: 422,089
- **Unique tokens**: 10,110
- **Vocabulary ratio**: 0.024
- **Top terms**: shall (9,840), unto (8,997), lord (8,007)
- **Zipf analysis**: Good adherence at high ranks, deviation increases with lower ranks
- **Benford's Law**: First digit '1' over-represented (43.8% vs expected 30.1%)
- **Vocabulary growth**: Shows sub-linear growth pattern

#### Quran (quran.txt)
- **Total tokens**: 72,975
- **Unique tokens**: 4,264
- **Vocabulary ratio**: 0.058
- **Top terms**: allah (2,739), who (1,695), shall (1,281)
- **Zipf analysis**: Moderate adherence with increasing deviation at lower ranks
- **Benford's Law**: Similar pattern to Bible with digit '1' over-represented (46.1%)
- **Vocabulary growth**: Higher vocabulary ratio than Bible

#### Wikipedia Abstracts (abstracts.wiki.txt)
- **Total tokens**: 726,170 (50,000 lines processed)
- **Unique tokens**: 62,712
- **Vocabulary ratio**: 0.086
- **Top terms**: quot (12,235), county (5,389), may (5,018)
- **Zipf analysis**: Best Zipf adherence among the three collections
- **Benford's Law**: Strongest deviation from expected distribution (digit '1' at 59.8%)
- **Vocabulary growth**: Highest vocabulary diversity

### Key Observations

#### Zipf's Law Analysis
- All collections show approximate Zipf distribution for high-frequency terms
- Deviation from ideal Zipf increases at lower frequency ranks
- Wikipedia shows best adherence to Zipf's law
- Religious texts (Bible, Quran) show greater deviation due to specialized vocabulary

#### Benford's Law Analysis
- All collections deviate significantly from Benford's expected distribution
- Consistent over-representation of digit '1' as first digit
- This suggests the text collections don't follow typical naturally occurring numerical patterns
- Wikipedia shows strongest deviation, likely due to technical/specialized content

#### Vocabulary Growth Patterns
- All collections exhibit sub-linear vocabulary growth (consistent with Heap's Law)
- Wikipedia has highest vocabulary diversity (8.64% unique terms)
- Bible has lowest vocabulary diversity (2.40% unique terms)
- Quran shows intermediate diversity (5.84% unique terms)

### Technical Implementation

#### Preprocessing Pipeline
```python
def preprocess_text(text):
    # 1. Tokenization & case folding
    tokens = re.findall(r'\w+', text.lower())

    # 2. Stop word removal
    tokens = [token for token in tokens if token not in STOP_WORDS]

    # 3. Simple stemming
    tokens = [simple_stem(token) for token in tokens]

    return tokens
```

#### Analysis Methods
- **Frequency Analysis**: Counter-based frequency counting
- **Zipf Verification**: Rank-frequency plotting and ratio analysis
- **Benford Testing**: First digit extraction and distribution comparison
- **Growth Tracking**: Incremental vocabulary size measurement

### Files Generated
- `lab1_preprocessing.py`: Full Porter stemmer implementation
- `lab1_analysis.py`: Efficient analysis script
- `lab1_instructions.md`: Complete lab requirements
- `bible_preprocessed.txt`: Processed Bible tokens sample
- `quran_preprocessed.txt`: Processed Quran tokens sample
- `wikipedia_abstracts_preprocessed.txt`: Processed Wikipedia sample

---

## Comparative Analysis Summary

| Collection | Total Tokens | Unique Tokens | Vocab Ratio | Zipf Adherence | Benford Deviation |
|------------|--------------|---------------|-------------|----------------|-------------------|
| Bible      | 422,089      | 10,110        | 0.024       | Moderate       | High (43.8% vs 30.1%) |
| Quran      | 72,975       | 4,264         | 0.058       | Moderate       | High (46.1% vs 30.1%) |
| Wikipedia  | 726,170      | 62,712        | 0.086       | Good           | Very High (59.8% vs 30.1%) |

