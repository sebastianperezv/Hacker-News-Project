# 📰 Hacker News Scraper

A simple Python script that scrapes the most popular stories from [Hacker News](https://news.ycombinator.com/) using `requests` and `BeautifulSoup`.

## 🚀 Overview

This script fetches data from the first two pages of Hacker News, extracts story titles, URLs, and vote counts, and displays only those stories with more than 99 points. The results are sorted by popularity (highest votes first).

## 📌 Features

- Retrieves story titles and links from Hacker News (pages 1 and 2).
- Extracts vote counts and filters stories with more than 99 points.
- Sorts stories by vote count in descending order.
- Displays the results in a clean and readable format using `pprint`.

## 🛠 Technologies

- Python 3
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- pprint (Python standard library)
