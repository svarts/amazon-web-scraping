# Amazon Reviews Scraper

This repository is created for the Mathematical Software class. This repository created for a Python script that scrapes Amazon product reviews,This project scrapes reviews from a specified Amazon product URL and performs statistical analysis on the collected reviews.

# Requirements
- Python 3.6 or higher
- pip (Python package installer)

# Setup

# 1. Clone the Repository
- Clone this repository to your local machine:
```sh
git clone https://github.com/svarts/amazon-reviews-scraper.git
cd amazon-reviews-scraper
```

# 2. Create a Virtual Environment
- Create a virtual environment to isolate dependencies:
```sh
python3 -m venv myenv
```

# 3. Activate the Virtual Environment
- Activate the virtual environment:

On macOS/Linux:
```sh
source myenv/bin/activate
```
On Windows:
```sh
myenv\Scripts\activate
```

# 4. Install Dependencies
- Install the required dependencies using `requirements.txt`:
```sh
pip install -r requirements.txt
```

# 5. Run the Script
Run the script to scrape Amazon reviews and perform analysis:
```sh
python amazon_reviews_scraper.py
```
or 
```sh
python3 amazon_reviews_scraper.py
```

# Create `requirements.txt`
- To generate a `requirements.txt` file that lists all the dependencies, run the following command:
```sh
pip freeze > requirements.txt
```

# Note
Do not include the `myenv` directory in your GitHub repository. To prevent this, add `myenv/` to your `.gitignore` file.
Ensure ethical use of web scraping and comply with Amazon's terms of service.

# License
This project is licensed under the MIT License.