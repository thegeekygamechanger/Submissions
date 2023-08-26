# -*- coding: utf-8 -*-
"""2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oOWsVCNwdmEeY5wqZzcEQT555P5jDZa8
"""

import requests
from bs4 import BeautifulSoup
import re

def get_social_links(soup):
    social_links = []
    social_patterns = ['facebook.com', 'twitter.com', 'instagram.com', 'linkedin.com']
    for pattern in social_patterns:
        links = soup.find_all(href=re.compile(pattern, re.IGNORECASE))
        social_links.extend(links)
    return social_links

def get_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails = re.findall(email_pattern, text)
    return emails

def get_phone_numbers(text):
    phone_pattern = r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'
    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers

def main():
    url = input("Enter the URL of the website: ")

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        social_links = get_social_links(soup)
        emails = get_emails(response.text)
        phone_numbers = get_phone_numbers(response.text)

        print("Social Links:")
        for link in social_links:
            print(link.get('href'))

        print("\nEmail/s:")
        for email in emails:
            print(email)

        print("\nPhone Numbers:")
        for phone in phone_numbers:
            print(phone)

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()