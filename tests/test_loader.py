import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from data.data_loader import load_dataset

features, labels = load_dataset("data/features.tsv", "data/labels.tsv")

print("Number of samples:", len(features))
print("First feature:", features[0])
print("First label:", labels[0])
