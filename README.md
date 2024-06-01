# Amazon Reviews Scraper and Analyzer

This repository is created for the Mathematical Software class. This project is a Python script that scrapes Amazon product reviews, saves them to a CSV file, and performs basic analysis and visualization on the collected data.

## Features

- Scrapes reviews from a specified Amazon product URL.
- Saves the reviews to a CSV file.
- Calculates and prints the average rating.
- Visualizes the distribution of ratings.
- Visualizes the distribution of review lengths.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library
- `matplotlib` library

## Installation

1. Clone the repository:

   \`\`\`bash
   git clone https://github.com/svarts/amazon-web-scraping.git
   cd amazon-web-scraping
   \`\`\`

2. Create and activate a virtual environment (optional but recommended):

   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   \`\`\`

3. Install the required libraries:

   \`\`\`bash
   pip install requests beautifulsoup4 pandas matplotlib
   \`\`\`

## Usage

1. Open the `amazon_reviews_scraper.py` file and update the `url` variable with the URL of the Amazon product you want to scrape.

2. Run the script:

   \`\`\`bash
   python amazon_reviews_scraper.py
   \`\`\`

3. The script will output the first few scraped reviews and save the reviews to `amazon_reviews.csv`. It will also generate and save the following plots:
   - `rating_distribution.png`: A bar chart showing the distribution of ratings.
   - `review_length_distribution.png`: A histogram showing the distribution of review lengths.

4. A summary of the average rating will be saved in `summary.txt`.

## Functions

### `get_amazon_reviews(url, num_pages)`

Collects reviews from the specified Amazon product URL.

- **Args:**
  - `url` (str): The URL of the Amazon product reviews page.
  - `num_pages` (int): The number of pages to scrape.
- **Returns:**
  - `pd.DataFrame`: A DataFrame containing the collected reviews.

### `save_reviews_to_csv(reviews_df, filename='amazon_reviews.csv')`

Saves the reviews to a CSV file.

- **Args:**
  - `reviews_df` (pd.DataFrame): A DataFrame containing the reviews.
  - `filename` (str): The name of the file to save the reviews to.

### `plot_review_statistics(reviews_df)`

Visualizes the review statistics and saves the plots.

- **Args:**
  - `reviews_df` (pd.DataFrame): A DataFrame containing the reviews.

## Example

\`\`\`python
url = 'https://www.amazon.com/product-reviews/B08N5WRWNW?sortBy=recent'
reviews_df = get_amazon_reviews(url, 5)
print(reviews_df.head())
save_reviews_to_csv(reviews_df)
plot_review_statistics(reviews_df)
\`\`\`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.