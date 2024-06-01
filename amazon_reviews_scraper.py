import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

def get_amazon_reviews(url, num_pages):
    """
    Collects reviews from the specified Amazon product URL.

    Args:
        url (str): The URL of the Amazon product reviews page.
        num_pages (int): The number of pages to scrape.

    Returns:
        pd.DataFrame: A DataFrame containing the collected reviews.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    reviews = []
    
    for page in range(1, num_pages + 1):
        page_url = f"{url}&pageNumber={page}"
        response = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        review_blocks = soup.find_all('div', {'data-hook': 'review'})
        
        for review in review_blocks:
            title = review.find('a', {'data-hook': 'review-title'}).text.strip()
            rating = review.find('i', {'data-hook': 'review-star-rating'}).text.strip().split(' ')[0]
            body = review.find('span', {'data-hook': 'review-body'}).text.strip()
            reviews.append({"Title": title, "Rating": float(rating), "Review": body})
    
    return pd.DataFrame(reviews)

def save_reviews_to_csv(reviews_df, filename='amazon_reviews.csv'):
    """
    Saves the reviews to a CSV file.

    Args:
        reviews_df (pd.DataFrame): A DataFrame containing the reviews.
        filename (str): The name of the file to save the reviews to.
    """
    reviews_df.to_csv(filename, index=False)

def plot_review_statistics(reviews_df):
    """
    Visualizes the review statistics and saves the plots.

    Args:
        reviews_df (pd.DataFrame): A DataFrame containing the reviews.
    """
    # Average rating
    average_rating = reviews_df['Rating'].mean()
    print(f"Average Rating: {average_rating}")

    # Rating distribution
    reviews_df['Rating'].value_counts().sort_index().plot(kind='bar', title='Rating Distribution')
    plt.xlabel('Ratings')
    plt.ylabel('Frequency')
    plt.savefig('rating_distribution.png')
    plt.show()

    # Review length distribution
    reviews_df['Review Length'] = reviews_df['Review'].apply(len)
    reviews_df['Review Length'].plot(kind='hist', bins=20, title='Review Length Distribution')
    plt.xlabel('Review Length')
    plt.ylabel('Frequency')
    plt.savefig('review_length_distribution.png')
    plt.show()

    with open('summary.txt', 'w') as f:
        f.write(f"Average Rating: {average_rating}\n")

def main():
    url = 'https://www.amazon.com/Purina-Friskies-Gravy-Swirlers-Adult/dp/B07CWV479K/ref=sr_1_2?content-id=amzn1.sym.3e23f907-b859-4094-8b45-cf96f8c9286b%3Aamzn1.sym.3e23f907-b859-4094-8b45-cf96f8c9286b&dib=eyJ2IjoiMSJ9.VNM8MRdDrg3isywwx603qMbqmQ7KQCl5UckHOh9tcFZN5osUvJpPU8Qn09e9HF63FdfN-70bIXoUoxFRiBUU_vYKfUEH2f4rMpio9gB6Ma52saZEqYJOtnRatnpIxD5wHX4MjS8q5nif1LlLMnX4HhhY80FJud6ze8sWZu6ido5ca_cniqMB0RLjdNS-uJY8bUshWTC_qpR9tL0zCCJvNdQgRvH5kIIAoEJJpPeuF4QXpkK-q3sGCkFSdO9zIfPKMx_kYhKhFSwSE8F40QV8V34s7mQbq9Stwa3h5VdnitI._3b5VCZTl_h0MBcRu9GhKiLpaIY9cd3etkDDBp2Hh0A&dib_tag=se&keywords=cat%2Bfood&pd_rd_r=c46fb69f-1d10-47e0-8c36-6905fcc971d5&pd_rd_w=0M8Mu&pd_rd_wg=zUsJG&pf_rd_p=3e23f907-b859-4094-8b45-cf96f8c9286b&pf_rd_r=S4KQ1YW50F1WPCWCA70D&qid=1717236522&sr=8-2&th=1'

    reviews_df = get_amazon_reviews(url, 5)
    print(reviews_df.head())

    save_reviews_to_csv(reviews_df)

    plot_review_statistics(reviews_df)

if __name__ == "__main__":
    main()