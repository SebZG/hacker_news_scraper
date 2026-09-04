# Hacker News Scraper

A simple Python program that collects popular stories from Hacker News.

## What it does

The script:

- downloads one or more Hacker News pages
- reads each story's title, link, and points
- keeps stories with more than 99 points
- sorts the results from highest to lowest score
- prints the results in the terminal

The program waits briefly between requests to avoid sending requests too quickly.

## Requirements

Install the required packages:

```bash
pip3 install requests beautifulsoup4
```

## Usage

Run the script with the number of pages to scrape:

```bash
python3 news.py 1
```

For example, to scrape the first three pages:

```bash
python3 news.py 3
```

The results will look similar to:

```text
[{'link': 'https://example.com',
  'points': 250,
  'title': 'Example story'}]
```

## Notes

- A value less than `2` is treated as one page.
- The page count must be an integer.
- Hacker News may temporarily limit requests if the script is run repeatedly in a short period.