# Gale-Shapley CLI Visualizer

This project implements the Gale-Shapley algorithm to find stable matches between two groups (men and women) based on their preferences. It includes a command-line interface (CLI) that allows users to input preferences and visualize the matching process.

## Project Structure

```
gale_shapley_cli
├── src
│   ├── gale_shapley.py       # Implementation of the Gale-Shapley algorithm
│   ├── cli.py                # Command-line interface for user interaction
│   └── __init__.py           # Marks the directory as a Python package
├── requirements.txt           # Lists project dependencies
└── README.md                  # Project documentation
```

## Installation

To get started, clone the repository and navigate to the project directory. Then, install the required dependencies using:

```
pip install -r requirements.txt
```

## Usage

To run the CLI visualizer, execute the following command:

```
python src/cli.py
```

You will be prompted to enter the preferences for men and women in the following format:

- Men preferences: `{"man1": ["woman1", "woman2"], "man2": ["woman2", "woman1"]}`
- Women preferences: `{"woman1": ["man1", "man2"], "woman2": ["man2", "man1"]}`

After entering the preferences, the program will display the matching process and the final engagements.

## Example

Here is an example of how to input preferences:

```
Men Preferences: {"A": ["X", "Y"], "B": ["Y", "X"]}
Women Preferences: {"X": ["B", "A"], "Y": ["A", "B"]}
```

The output will show the step-by-step matching process and the final engagements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.