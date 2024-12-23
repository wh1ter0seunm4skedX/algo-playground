# Gale-Shapley Algorithm Visualizer

Interactive CLI visualization of the Gale-Shapley stable matching algorithm.

## Features

- 🎯 Step-by-step algorithm visualization
- 🎨 Colored terminal output
- ⚡ Interactive progression
- 📊 Clear state representation
- 💾 Example data included

## Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Edit preferences in `data.py` (optional)
2. Run the visualizer:
```bash
python src/cli.py
```

## Data Format

Example format in `data.py`:
```python
men_preferences = {
    "1": ["A", "B", "C", "D"],
    "2": ["A", "D", "B", "C"],
}

women_preferences = {
    "A": ["1", "3", "4", "2"],
    "B": ["2", "1", "3", "4"],
}
```

## Dependencies

- Python 3.6+
- colorama

## License
MIT