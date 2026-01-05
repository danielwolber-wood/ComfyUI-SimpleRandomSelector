# ComfyUI-SimpleRandomSelector

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to select a random item from a file. This is useful for dynamic prompt generation, randomizing parameters, or picking random styles/colors from a list.

## Features

- **Supports Multiple Formats**: Works with `.txt`, `.csv`, and `.json` files.
- **Reproducible**: Uses a `seed` input to ensure consistent results when needed.
- **Simple Integration**: Returns a string that can be connected to any other node expecting text input.

## Installation

1. Navigate to your ComfyUI `custom_nodes` directory.
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ComfyUI-SimpleRandomSelector.git
   ```
3. Restart ComfyUI.

## Usage

1. Search for the node **"Random Line form File"** in the node menu (under `Utils/Random`).
2. **file_path**: Enter the path to your file. You can use absolute paths or paths relative to the ComfyUI root directory.
   - Default: `examples/colors.txt`
3. **seed**: Set a seed for the random selection. Changing the seed will select a new item.
4. Connect the **selected_item** output to a CLIP Text Encode node or any other node that accepts a string.

## Supported File Formats

### Text Files (.txt)
Reads the file line by line. Each non-empty line is treated as a separate item.

### CSV Files (.csv)
Reads the file using a CSV reader. Each row is joined by commas and treated as a single item.

### JSON Files (.json)
- **List**: Selects a random element from the list.
- **Dictionary**: Selects a random value from the dictionary.

## Example

If you have a `colors.txt`:
```text
red
blue
green
```
The node will output one of "red", "blue", or "green" based on the seed.
