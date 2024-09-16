# Xoserve Scraper

This script scrapes data from the Xoserve website, specifically looking for Excel files, and saves the data into a CSV file.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python 3.x installed on your Windows machine.
- You have the following Python libraries installed:
  - `pandas`
  - `lxml`
  - `requests_html`

You can install these libraries using pip:

```sh
pip install -r requirements.txt
```

## Usage

To use this script, follow these steps:

1. Clone this repository or download the `xoserve.py` file.
2. Open a terminal and navigate to the directory containing `xoserve.py`.
3. Run the script using Python:

```sh
python xoserve.py
```

## Functions

### `scrape_data()`

This function sends a request to the Xoserve website and retrieves the HTML content.

### `save_data(response)`

This function processes the HTML content to find the URL of the Excel file, downloads it, and saves the data into a CSV file named `uig_data.csv`.

- **Parameters**:
  - `response (requests.models.Response)`: The response object containing the data.

### `run()`

This function orchestrates the scraping process by calling `scrape_data()` and `save_data(response)`
## Example

Here is an example of how to run the script:

```sh
python xoserve.py
```

After running the script, you should see a message indicating that the data has been saved successfully, and a file named `uig_data.csv` will be created in the same directory.