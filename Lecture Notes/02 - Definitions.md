# Lecture 02: Information Retrieval Definitions

**Course:** INFR11145 - Text Technologies for Data Science
**Date:** 18-Sep-2024
**Instructor:** Walid Magdy
**University:** University of Edinburgh

---

## Lecture Objectives

By the end of this lecture, students will understand the main concepts in Information Retrieval:
- **Document:** The fundamental unit of retrieval
- **Information Need:** What users actually want to find
- **Query:** How users express their information needs
- **Index:** The data structure enabling fast search
- **BOW (Bag-of-Words):** The fundamental text representation model

---

## Information Retrieval System Overview

### The Complete IR Process

#### Traditional IR in a Nutshell
```
User → Query → Search Engine → Relevant Documents → User
```

**Components:**
- **User:** Person with an information need
- **Query:** Textual expression of that need
- **Search Engine:** System that processes queries and returns results
- **Documents:** Collection of information items to search through
- **Relevant Documents:** Subset of documents that satisfy the information need

#### Modern RAG (Retrieval Augmented Generation) Process
```
User → Query/Question → Search Engine → Relevant Documents → LLM → Extract & Summarize → Generated Response → User
```

**Enhanced Components:**
- **LLM (Large Language Model):** AI system that processes retrieved documents
- **Extract & Summarize:** Process of generating coherent responses from multiple sources
- **Generated Response:** Natural language answer based on retrieved information

### Core IR Challenges

#### Two Fundamental Issues

**1. Effectiveness Challenge:**
- **Problem:** Finding relevant documents among millions or billions
- **Analogy:** "Needle in a haystack" problem
- **Complexity:** Very different from relational database queries (SQL)
- **Nature:** No exact matches - relevance is probabilistic and subjective

**2. Efficiency Challenge:**
- **Scale Requirements:** Handle hundreds of billions of web pages
- **Speed Requirements:** Process thousands of queries per second (Google: ~99,000 queries/second)
- **Dynamic Content:** Data constantly changes, requiring real-time updates
- **Performance:** Compared to other NLP areas, IR must be extremely fast

**Real-World Example:**
Google search results showing "About 293,000,000 results (0.79 seconds)" demonstrates both the massive scale and speed requirements of modern IR systems.

---

## Core IR Components

### 1. Documents

**Definition:** The fundamental elements to be retrieved in an IR system.

#### Document Characteristics

**Essential Properties:**
- **Unstructured Nature:** Free-form text without rigid formatting constraints
- **Unique Identifier:** Each document has a distinct ID for system management
- **Collection Membership:** N documents together form a searchable collection

#### Document Types and Examples

**Traditional Text Documents:**
- **Web pages:** HTML documents with hyperlinks and multimedia
- **Email messages:** Personal and business communications
- **Books and articles:** Literature, academic papers, journalistic content
- **Individual pages:** Sections of larger works
- **Sentences:** Fine-grained retrieval units

**Social Media Content:**
- **Tweets:** Short-form social media posts
- **Blog posts:** Longer-form personal and professional content
- **Forum discussions:** Community-generated content

**Multimedia and Specialized Content:**
- **Photos with metadata:** Images with descriptive text
- **Videos with transcripts:** Audio-visual content with textual descriptions
- **Musical pieces with lyrics:** Audio content with textual components
- **Source code:** Programming code as textual documents

**Structured and Semi-Structured Content:**
- **Question-answer pairs:** FAQ systems and knowledge bases
- **Product descriptions:** E-commerce catalogs
- **Advertisements:** Marketing content with targeting information

**Multilingual and Non-Standard Content:**
- **Documents in different languages:** Cross-language retrieval challenges
- **Non-textual sequences:** DNA sequences, chemical formulas

### 2. Queries

**Definition:** Free text expressions of a user's information need.

#### Query Complexity and Ambiguity

**Multiple Representations of Same Need:**
The same underlying information need can be expressed in multiple ways:

**Example - Hurricane Information:**
- "Latest news on the hurricane in the US"
- "North Carolina storm"
- "Florence"

All three queries represent the same information need but use different vocabulary and specificity levels.

**Same Query, Multiple Needs:**
A single query can represent different information requirements:

**Example - "Apple":**
- **Fruit:** Nutritional information, recipes, agriculture
- **Technology Company:** Stock prices, product information, news

**Example - "Jaguar":**
- **Animal:** Wildlife information, conservation, biology
- **Automobile:** Car specifications, reviews, purchasing

#### Query Format Variations

**Web Search Queries:**
- **Keywords:** "machine learning algorithms"
- **Narrative descriptions:** "how to implement machine learning algorithms"

**Image Search Queries:**
- **Textual descriptions:** "red sports car"
- **Sample images:** Upload image to find similar ones

**Question-Answering Systems:**
- **Direct questions:** "What is the capital of France?"
- **Natural language queries:** "Tell me about French geography"

**Music Information Retrieval:**
- **Humming recognition:** Audio input for melody matching
- **Lyric search:** Text-based music discovery

**Filtering and Recommendation:**
- **User interest profiles:** Historical behavior patterns
- **Contextual preferences:** Location, time, device-based customization

**Scholarly and Structured Search:**
- **Field-specific queries:** Author, title, publication venue
- **Advanced search interfaces:** Boolean operators, date ranges

**Complex Structured Queries:**
Advanced systems support sophisticated query languages:
```
#wsyn(0.9 #field(title, #phrase(homer,simpson)) 0.7 #and(#>(pagerank,3), #ow3(homer,simpson)) 0.4 #passage(homer, simpson, dan, castellaneta))
```

This example shows weighted synonym matching, field restrictions, PageRank filtering, and passage-level retrieval.

### 3. Relevance

**Definition:** The degree to which a document satisfies a user's information need.

#### The Relevance Problem

**Abstract Level Understanding:**
Information Retrieval fundamentally addresses two related questions:
- Does item D **match** item Q?
- Is item D **relevant** to item Q?

#### Relevance as a Complex Concept

**Multi-faceted Nature:**
Relevance is not simply binary (relevant/not relevant) but involves multiple dimensions:

**User Satisfaction Factors:**
- **Utility:** Will the user like it or click on it?
- **Task Completion:** Will it help the user achieve their goal?
- **Information Need Satisfaction:** Does it provide the needed information?
- **Novelty:** Is the information new and not redundant?

**Topical Relevance:**
- **Core Definition:** Relevance equals "what is the topic about"
- **Shared Meaning:** Documents and queries should share similar "meaning"
- **Subject Alignment:** About the same topic, subject, or issue

#### Challenges in Determining Relevance

**Semantic Ambiguity:**
Queries often lack clear, unambiguous semantics:

**Example - "William Shakespeare":**
The query could seek:
- **Biographical information:** Life history, personal details
- **Bibliography:** List of plays and works authored
- **Specific work:** Text of a particular play (Hamlet, Macbeth)
- **Analysis:** Literary criticism or historical context

**Language Ambiguity:**
Natural language introduces systematic challenges:

**Synonymy (Same Meaning, Different Words):**
- "Edinburgh festival" = "The Fringe"
- Different surface forms referring to identical concepts
- System must recognize semantic equivalence

**Polysemy (Same Word, Different Meanings):**
- "Apple" (fruit vs. technology company)
- "Jaguar" (animal vs. automobile)
- Context determines intended meaning

#### Subjectivity in Relevance

**Individual Differences:**
- **Personal preferences:** Different users judge relevance differently
- **Context dependency:** Same document may be relevant in different situations
- **Expertise levels:** Domain knowledge affects relevance judgments

**Graded Relevance Scales:**
Rather than binary relevant/not relevant:
- **Binary:** Relevant vs. Not Relevant
- **Graded:** Perfect/Excellent/Good/Fair/Bad/Not Relevant

#### Web-Specific Relevance Challenges

**Search Engine Optimization (SEO):**
- **Manipulation:** Content designed to rank highly rather than be relevant
- **Spam detection:** Identifying artificially optimized content
- **Quality assessment:** Distinguishing high-quality from low-quality content

**Commercial Bias:**
- **Advertising influence:** Commercial interests affecting result ranking
- **Sponsored content:** Paid placement mixed with organic results

### 4. Similarity-Based Relevance

**Fundamental Principle:** Items with similar vocabulary likely have similar meaning.

#### Key Insights

**Vocabulary Overlap:**
- **Assumption:** Documents relevant to similar queries will share common terminology
- **Implementation:** Statistical analysis of word co-occurrence patterns
- **Validation:** Empirically successful across many domains

**Matching Approaches:**

**String Matching:**
- **Exact word overlap:** Count identical terms between query and document
- **Boolean matching:** Presence or absence of query terms
- **Limitations:** Ignores synonyms and morphological variations

**Word Overlap:**
- **Frequency-based:** Weight terms by occurrence frequency
- **Position-aware:** Consider term positions and proximity
- **Statistical measures:** TF-IDF, BM25, language models

**Probabilistic Models:**
- **Mathematical framework:** P(Document|Query) using retrieval models
- **Statistical foundation:** Estimate probability of relevance
- **Machine learning:** Training from relevance judgments

---

## IR vs. Database Systems

### Fundamental Differences

| Aspect | Database Systems | Information Retrieval |
|--------|------------------|----------------------|
| **Data Type** | Structured data with clear semantics based on formal models | Mostly unstructured free text with some metadata |
| **Query Language** | Formally-defined (relational algebra, SQL), unambiguous | Free text ("natural language"), Boolean operators |
| **Result Quality** | Exact matches (always "correct") | Imprecise results (need relevance measurement) |
| **User Interaction** | One-shot queries with deterministic results | Interactive refinement and exploration important |

#### Database System Characteristics

**Structured Data:**
- **Formal schemas:** Predefined table structures with typed columns
- **Referential integrity:** Enforced relationships between data elements
- **ACID properties:** Atomicity, Consistency, Isolation, Durability

**Query Precision:**
- **SQL specificity:** Exact specification of required data
- **Deterministic results:** Same query always returns same results
- **Boolean logic:** Clear true/false evaluation criteria

#### IR System Characteristics

**Unstructured Text:**
- **Free-form content:** No predetermined format or structure
- **Ambiguous semantics:** Meaning depends on context and interpretation
- **Evolving content:** Dynamic, frequently changing information

**Approximate Matching:**
- **Fuzzy relevance:** Degrees of relevance rather than exact matches
- **Ranking necessity:** Results ordered by estimated relevance
- **User feedback:** Interactive refinement improves results

---

## The Bag-of-Words (BOW) Model

### Conceptual Foundation

**Core Principle:** Treat documents and queries as collections ("bags") of individual words, ignoring word order and grammatical structure.

#### Demonstration of BOW Effectiveness

**Scrambled Word Examples:**

**Example 1:**
- Scrambled: "per is salary hour €25,000 Ronaldo's"
- Correct: "Ronaldo's salary per hour is €25,000"
- **Topic:** Still clearly about Ronaldo's earnings

**Example 2:**
- Scrambled: "obesity French is of full cause and fat fries"
- Variations:
  - "French fries is full of fat and cause obesity"
  - "French fries cause obesity and is full of fat"
- **Topic:** Consistently about French fries and health effects

#### Key BOW Insights

**Word Order Independence:**
- **Meaning preservation:** Core topic remains identifiable despite reordering
- **Individual words as building blocks:** Each word contributes meaning
- **Compositional semantics:** "Bag" of words creates "composition" of meanings

**Practical Implications:**
- **Retrieval tractability:** Makes statistical models computationally feasible
- **Feature extraction:** Words serve as features for machine learning
- **Similarity computation:** Enables efficient document-query comparison

### BOW in Modern Search Systems

**Widespread Adoption:**
- **Most search engines:** Google, Bing, academic systems use BOW-based approaches
- **Document representation:** Convert all text to word frequency vectors
- **Query processing:** Transform queries using same BOW representation

**Statistical Models:**
- **Feature-based algorithms:** Use words as input features
- **Relevance prediction:** Determine which documents most likely relevant
- **Ranking computation:** Score documents based on word overlap patterns

**Matching Process:**
- **Degree of overlap:** Measure similarity between document and query word bags
- **Weighting schemes:** TF-IDF, BM25 assign importance to different words
- **Normalization:** Account for document length and term frequency variations

#### BOW Model Applications

**Information Retrieval:**
- **Document ranking:** Order results by BOW-based similarity scores
- **Query expansion:** Add related terms to improve recall
- **Relevance feedback:** Learn from user interactions to improve matching

**Text Classification:**
- **Feature representation:** Documents as vectors of word frequencies
- **Category prediction:** Classify based on characteristic word patterns
- **Spam detection:** Identify suspicious word combinations

**Text Analytics:**
- **Topic modeling:** Discover latent themes in document collections
- **Sentiment analysis:** Determine emotional tone from word choices
- **Comparative analysis:** Find differences between document sets

### BOW Criticisms and Limitations

#### Context and Meaning Loss

**Word Meaning Without Context:**
- **Criticism:** Individual words lose meaning without surrounding context
- **Counter-argument:** BOW doesn't completely discard context
- **Reality:** Discards surface form and grammatical well-formedness
- **Preservation:** Maintains topical and semantic coherence

**Negation Handling:**
- **Problem example:** "climate change is real" vs. "climate change is no real"
- **BOW perspective:** Both discuss same subject (climate change, reality)
- **Solution approach:** Treat negations as compound terms ("not real")
- **Practical handling:** Domain-specific processing of negation patterns

#### Language-Specific Limitations

**Word Segmentation Issues:**
- **Chinese and Japanese:** No natural word boundaries in written text
- **Challenge:** Automatic segmentation required before BOW application
- **Solutions:** Statistical segmentation, dictionary-based approaches

**German Compound Words:**
- **Problem:** "Lebensversicherungsgesellschaftsangestellter" (life insurance company employee)
- **Need:** Compound splitting before BOW processing
- **Solution:** Decompounding algorithms for better feature extraction

**Arabic Morphological Complexity:**
- **Rich morphology:** Extensive prefixing, suffixing, and internal changes
- **Preprocessing:** Stemming and root extraction crucial
- **BOW adaptation:** Requires language-specific normalization

#### Solutions and Adaptations

**Segmentation and Feature Induction:**
- **Approach:** Break or aggregate text units until they reflect "aboutness"
- **Examples:**
  - German compound splitting
  - Chinese word segmentation
  - Arabic morphological analysis
- **Goal:** Achieve meaningful units for BOW representation

**Enhanced BOW Variants:**
- **N-grams:** Include word sequences (bigrams, trigrams) as features
- **Phrase detection:** Identify meaningful multi-word expressions
- **Syntactic features:** Incorporate limited grammatical information
- **Semantic embeddings:** Dense vector representations capturing meaning

---

## IR System Architecture

### The IR Black Box Model

#### System Components

**Input Processing:**
- **Query:** User information need expressed as text
- **Documents:** Collection of searchable content

**Internal Processing Components:**
- **Representation Function:** Converts queries to internal format
- **Transformation Function:** Converts documents to BOW and indexed form
- **Comparison Function:** Matches queries against document representations
- **Retrieval Model:** Mathematical framework for relevance scoring

**Output Generation:**
- **Hits:** Ranked list of potentially relevant documents
- **Presentation:** User-friendly display of results

#### Online vs. Offline Processing

**Offline Processing (Indexing Phase):**
- **Document acquisition:** Crawling, importing, preprocessing
- **Text transformation:** Convert to BOW representation
- **Index creation:** Build efficient lookup data structures
- **Storage optimization:** Compression, caching strategies

**Online Processing (Search Phase):**
- **Query representation:** Convert user query to internal format
- **Index lookup:** Retrieve candidate documents efficiently
- **Scoring and ranking:** Apply retrieval model to compute relevance
- **Result presentation:** Format and display results to user

### System Perspective on IR

#### Indexing Process (Offline Operations)

**Objective:** Get data into the system in searchable form.

**Document Acquisition Stage:**
- **Web crawling:** Automated discovery and downloading of web content
- **Provider feeds:** RSS, API-based content ingestion
- **Desktop/email integration:** Personal information management
- **Batch processing:** Large-scale document ingestion

**Storage Decisions:**
- **Original preservation:** Store complete documents vs. processed versions only
- **Compression strategies:** Balance storage efficiency with access speed
- **Rights management:** Handle copyright and access restrictions
- **Scalability planning:** Anticipate growth in collection size

**Text Transformation Stage:**
- **Format conversion:** Handle different document formats (PDF, HTML, DOC)
- **Encoding normalization:** Handle different character encodings and languages
- **Content extraction:** Identify meaningful text vs. boilerplate
- **Quality filtering:** Remove low-quality or duplicate content

**Processing Decisions:**
- **Word unit definition:** How to tokenize text into searchable units
- **Stop word removal:** Which high-frequency words to exclude
- **Stemming application:** Morphological normalization strategies
- **Language detection:** Handle multilingual collections appropriately

**Index Creation:**
- **Data structure design:** Inverted indexes for fast term lookup
- **Compression techniques:** Reduce storage requirements
- **Update mechanisms:** Handle dynamic content changes
- **Distribution strategies:** Scale across multiple machines

#### Search Process (Online Operations)

**Objective:** Satisfy users' information requests efficiently and effectively.

**User Interaction Stage:**
- **Query formulation assistance:** Auto-completion, suggestions
- **Spelling correction:** Handle misspelled queries
- **Query expansion:** Add related terms automatically
- **Interface design:** Support different search modalities

**Retrieval Stage:**
- **Index lookup:** Find documents containing query terms
- **Candidate generation:** Identify potentially relevant documents
- **Scoring computation:** Apply retrieval models for relevance estimation
- **Ranking determination:** Order results by estimated relevance

**Result Presentation:**
- **Snippet generation:** Create informative document summaries
- **Highlighting:** Emphasize query terms in results
- **Categorization:** Group results by topic or source
- **Pagination:** Handle large result sets efficiently

**System Learning:**
- **User behavior logging:** Track clicks, dwell time, reformulations
- **Relevance feedback:** Learn from user interactions
- **Query analysis:** Identify common patterns and needs
- **System optimization:** Adjust algorithms based on usage data

#### Performance and Scalability Considerations

**Effectiveness Requirements:**
- **Precision:** High proportion of relevant documents in top results
- **Recall:** Find most relevant documents in collection
- **User satisfaction:** Meet information needs efficiently
- **Personalization:** Adapt to individual user preferences

**Efficiency Requirements:**
- **Response time:** Sub-second query processing for most queries
- **Throughput:** Handle thousands of simultaneous queries
- **Scalability:** Support billions of documents and millions of users
- **Resource management:** Efficient use of computational resources

**System Reliability:**
- **Availability:** 99.9%+ uptime requirements
- **Fault tolerance:** Graceful handling of component failures
- **Load balancing:** Distribute processing across multiple servers
- **Data backup:** Protect against data loss and corruption

---

## Summary

Information Retrieval represents a core technology for managing and accessing textual information at scale. The fundamental challenge lies in bridging the gap between human information needs and computational text processing capabilities.

### Key Takeaways

**IR as Core Technology:**
- **Beyond web search:** IR powers diverse applications from digital libraries to recommendation systems
- **Selling point:** Extremely fast processing with contextual understanding
- **Foundation:** Enables modern AI applications through RAG systems

**Main Technical Challenges:**
- **Effectiveness:** Finding relevant information in vast collections
- **Efficiency:** Processing queries and maintaining indexes at massive scale
- **Relevance:** Understanding and satisfying complex human information needs

**Fundamental Components:**
- **Documents:** Varied, unstructured content requiring flexible processing
- **Queries:** Ambiguous natural language expressions of information needs
- **Relevance:** Complex, subjective relationship between information and need
- **BOW Model:** Practical approach enabling computational text processing

**System Architecture:**
- **Two-phase design:** Offline indexing enables online search efficiency
- **Component integration:** Multiple specialized modules working together
- **Scalability focus:** Designed for massive scale from the ground up

### Looking Forward

The concepts introduced in this lecture form the foundation for understanding more advanced IR techniques. Subsequent lectures will explore:

**Text Laws and Statistics:** Understanding the mathematical properties of natural language that enable IR systems to work effectively.

**Preprocessing Techniques:** Transforming raw text into forms suitable for computational processing while preserving semantic content.

**Retrieval Models:** Mathematical frameworks for computing document-query similarity and predicting relevance.

**Evaluation Methods:** Measuring and comparing the effectiveness of different IR approaches.

**Modern Applications:** Integration with machine learning and AI systems for enhanced capabilities.

This comprehensive understanding of IR definitions and concepts provides the necessary foundation for building and evaluating practical text technologies for data science applications.