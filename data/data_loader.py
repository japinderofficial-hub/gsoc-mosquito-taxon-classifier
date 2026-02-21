from typing import List, Tuple
import pandas as pd


def load_features(path: str) -> List[str]:
    """
    Load feature file paths from features.tsv.
    """
    df = pd.read_csv(path, sep='\t', header=None)
    return df[0].tolist()


def load_labels(path: str) -> List[str]:
    """
    Load labels from labels.tsv.

    """
    df = pd.read_csv(path, sep='\t', header=None)
    return df[0].tolist()


def validate_data(features: List[str], labels: List[str]) -> None:
    """
    Validate that features and labels have same length.

    """
    if len(features) != len(labels):
        raise ValueError(
            f"Mismatch: {len(features)} features but {len(labels)} labels"
        )


def load_dataset(
    features_path: str,
    labels_path: str
) -> Tuple[List[str], List[str]]:
    """
    Load and validate dataset.


    """
    features = load_features(features_path)
    labels = load_labels(labels_path)
    validate_data(features, labels)
    return features, labels