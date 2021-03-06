# ClusterDuck

Disease clustering from phenotypic literature data through Document Understanding, Comprehension and Knowledge

(doi: )

## What's the problem ?

Typically, SNPs are studied in terms of a "one disease - one SNP" relationship. This results in researchers and clinicians with deep knowledge of a disease but often incomplete knowledge of all potentially relevant SNPs.

## Why should we solve it ?

Knowledge of a larger set of potentially relevant SNPs to a collection of phenotypes would allow finding a novel set of relevant publications. 

## What is ClusterDuck ?

ClusterDuck is a tool to automatically identify genetically-relevant publications and returns relevant

## How to use ClusterDuck ?

### Prerequisite

- Python 3
- [EDirect](https://dataguide.nlm.nih.gov/edirect/install.html)

### Installation

- Install python packages required: `pip3 install -r requirements.txt`

- Download the pubmed database and required data from nltk: `python3 setup.py`

### Example

1. Use easy-to-start command line tool `ClusterDuck.py`

   ``` shell
   python3 ClusterDuck.py "Autistic behavior" "Restrictive behavior" "Impaired social interactions" "Poor eye contact" "Impaired ability to form peer relationships" "No social interaction" "Impaired use of nonverbal behaviors" "Lack of peer relationships" "Stereotypy"
   ```

1. A case study

   `python3 generate_csv.py`

1. Train Topic Models

   After you have corpora, you can run the following function in `train_lda.py` to obtain topic models:

   ``` python
   lda1, lda2 = train_ldas(corpus1, corpus2, n_topics=N_TOPICS, alpha=ALPHA, eta=ETA)
   ```

   where `N_TOPICS`, `ALPHA` and `ETA` parameterize both topic models.

### Test Suite

`python3 ./dc/test_utils.py`

## ClusterDuck Workflow

![Workflow Pipeline](https://github.com/NCBI-Hackathons/DiseaseClusters/blob/master/assets/pipeline.png "Workflow Pipeline")

### Input

Set of phenotypic terms from HPO ontology.

### Workflow

- A 'phenotypic' corpus of literature is extracted from PubMed using the user-input HPO phenotypic terms.
- All SNPs mentioned in the 'phenotypic clusters are idenfified.
- PubMed is queried using the phenotypically-relevant SNPs to extract a second 'phenotypic + genetic' corpus.
- Topic modeling is run on each corpus separately.
- Topic distributions are compared to discover new genetically-inspired and relevant topics.

### Output

A list of novel genetically-related topics to the initial phenotypic input.

### Planned Features

- Synonyms search from user-input
   HPO provides a synonym list for each of their controlled vocabulary terms. This can be incorporated as a preprocessor with the user input to allow
- Make use of hierarchy
   HPO is an ontology of terms and user-input terms are likely to have sub- and super-class terms.
- Filtering different types of research articles
   Optionally add a [PT] query filter to the PubMed query to limit the [types of publications](https://www.ncbi.nlm.nih.gov/books/NBK3827/table/pubmedhelp.T.publication_types/?report=objectonly) returned.
- Use of EMR-type data to build corpus as oppose to PubMed
   An EMR-based corpus is more likely to be associated with diseases (especially to ICD terms) than a PubMed-based corpus.

## People/Team

- Jennifer Dong
- Larry Gray
- Joseph Halstead
- [Yi Hsiao](https://github.com/hsiaoyi0504/)
- Wayne Pereanu
- Neelay Trivedi
- Nathan Wan
- Donghui Wu

## Presentations

- [Day 1](https://docs.google.com/presentation/d/1OeYWhXnbjgy0pLFU8URxye0xEFQdAGDFmN038SomnbU/edit?usp=sharing)
- [Day 2](https://docs.google.com/presentation/d/1Dgd9E-IKHj1mSZOfUHR4GfukmkeYuXqyeWCGdBRG6Lg/edit?usp=sharing)
- [Day 3](https://docs.google.com/presentation/d/1SNmItG8LKNOiSrJ1Y0qmh6G3opbJRIK7yz1YaFBS6m4/edit?usp=sharing)
