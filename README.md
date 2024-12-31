# FP-Growth Algorithm Implementation

This repository contains a Python implementation of the FP-Growth algorithm for mining frequent itemsets and generating association rules.

## Overview

The FP-Growth (Frequent Pattern Growth) algorithm is an efficient method for mining frequent itemsets without generating candidate sets. It uses a compact data structure called FP-tree (Frequent Pattern tree) to store compressed information about frequent patterns.

## Features

- Builds FP-tree from transaction data
- Mines frequent patterns from FP-tree
- Generates association rules with configurable minimum support and confidence
- Supports both file-based and direct list-based inputs
- Interactive suggestion system based on association rules

## Installation

```bash
pip install fpgrowth_py
```

## Usage

### Command Line Interface

```bash
python fpgrowth.py -f input.csv -s 0.5 -c 0.5
```

Parameters:

- `-f, --inputFile`: Path to the CSV file containing transactions
- `-s, --minSupport`: Minimum support threshold (default: 0.5)
- `-c, --minConfidence`: Minimum confidence threshold (default: 0.5)

### Python API

```python
from fpgrowth_py import fpgrowth

# Using direct itemset list
itemSetList = [['A', 'B', 'C'], ['B', 'C', 'D'], ['A', 'C', 'D']]
minSupRatio = 0.5
minConf = 0.5
freqItems, rules = fpgrowth(itemSetList, minSupRatio, minConf)

# Using file input
freqItems, rules = fpgrowthFromFile("input.csv", minSupRatio, minConf)
```

## Input Format

The input CSV file should contain transactions with items separated by commas. Each line represents a single transaction.

Example:

```
A,B,C
B,C,D
A,C,D
```

## Output

The algorithm outputs:

1. Frequent itemsets that meet the minimum support threshold
2. Association rules that meet both minimum support and confidence thresholds
3. Interactive suggestions based on input items

## Project Structure

- `fpgrowth.py`: Main implementation file with CLI interface
- `utils.py`: Utility functions and data structures (Node class, tree construction)
- `__init__.py`: Package initialization

## Implementation Details

- Uses a Node class to represent FP-tree structure
- Implements header table for efficient pattern mining
- Supports conditional pattern base generation
- Includes pattern growth and association rule mining

## Contributing

Feel free to open issues or submit pull requests for improvements.
