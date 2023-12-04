import requests
from bs4 import BeautifulSoup
import urllib.parse
import pandas as pd

def scrape_linkedin_jobs(job_roles, base_url, pages_per_role=30):
    """
    Scrapes job postings from LinkedIn for specified job roles.

    Args:
    job_roles (list of str): A list of job roles to search for.
    base_url (str): The base URL for LinkedIn job postings search.
    pages_per_role (int): Number of pages to scrape for each role.

    Returns:
    pd.DataFrame: A DataFrame containing details of scraped job postings.
    """

    # Initialize list to store job posting details
    job_details = []

    # Creating URLs for each job role
    for role in job_roles:
        # Encoding the job role for URL
        encoded_role = urllib.parse.quote(role)
        url = f"{base_url}keywords={encoded_role}&start={{}}"

        # Scrape job postings for each role
        for page in range(pages_per_role):
            response = requests.get(url.format(page), headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
            })
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract job IDs from the current page
            job_ids = [job.find("div", {"class": "base-card"}).get('data-entity-urn').split(":")[3]
                       for job in soup.find_all("li")]

            # Scrape details for each job ID
            for job_id in job_ids:
                job_data = scrape_job_details(job_id)
                job_details.append(job_data)

    # Create a DataFrame from the list of job details
    return pd.DataFrame(job_details)

def scrape_job_details(job_id, target_url='https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'):
    """
    Scrapes details of a single job posting using its job ID.

    Args:
    job_id (str): The job ID for the posting.
    target_url (str): Base URL for individual job posting details.

    Returns:
    dict: A dictionary containing details of the job posting.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    response = requests.get(target_url.format(job_id), headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting job details
    job_details = {
        "company": extract_text(soup, "div", {"class": "top-card-layout__card"}, "a", "img", "alt"),
        "job-title": extract_text(soup, "div", {"class": "top-card-layout__entity-info"}, "a"),
        "level": extract_criteria(soup, "Seniority level"),
        "employment type": extract_criteria(soup, "Employment type")
    }

    return job_details

def extract_text(soup, *selectors, attr=None):
    """
    Extracts text from a BeautifulSoup object based on given selectors.

    Args:
    soup (BeautifulSoup): BeautifulSoup object to extract from.
    selectors (tuple): Sequence of selectors to navigate to the desired element.
    attr (str, optional): Attribute name to extract value from, if needed.

    Returns:
    str or None: Extracted text or attribute value, or None if not found.
    """
    element = soup
    for selector in selectors:
        element = element.find(selector) if element else None
    return element.get(attr) if attr and element else element.text.strip() if element else None

def extract_criteria(soup, criteria_name):
    """
    Extracts specific job criteria (like Seniority level, Employment type) from a BeautifulSoup object.

    Args:
    soup (BeautifulSoup): BeautifulSoup object to extract from.
    criteria_name (str): The name of the criteria to extract.

    Returns:
    str or None: Extracted criteria value, or None if not found.
    """
    criteria = soup.find("ul", {"class": "description__job-criteria-list"}).find("li", {
        "class": "description__job-criteria-item"}, string=criteria_name)
    return criteria.find("span", {"class": "description__job-criteria-text--criteria"}).text.strip() if criteria else None

job_roles = ['Software Engineer', 'Data Scientist', 'Product Manager', 'Graphic Designer', 'Marketing Manager', 'Sales']


if __name__ == "__main__":
    # Scrape job postings from LinkedIn
    df = scrape_linkedin_jobs(job_roles, "https://www.linkedin.com/jobs/search/?")

    # Save the DataFrame as a CSV file
    df.to_csv("linkedin_jobs.csv", index=False)