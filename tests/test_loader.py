from pathlib import Path
import importlib.util

project_root = Path(__file__).parent.parent
data_loader_path = project_root / "data" / "data_loader.py"

spec = importlib.util.spec_from_file_location("data.data_loader", data_loader_path)
data_loader = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(data_loader)
load_dataset = data_loader.load_dataset

features, labels = load_dataset("data/features.tsv", "data/labels.tsv")

print("Number of samples:", len(features))
print("First feature:", features[0])
print("First label:", labels[0])
