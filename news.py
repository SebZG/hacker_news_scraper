import sys
import time
from pprint import pprint

import requests
from bs4 import BeautifulSoup


def get_hn_pages(n_pages):
    mega_links = []
    mega_subtext = []
    headers = {"User-Agent": "hacker-news-scraper/1.0"}

    for page_number in range(1, n_pages + 1):
        res = requests.get(
            "https://news.ycombinator.com/news",
            params={"p": page_number},
            headers=headers,
            timeout=10,
        )
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        mega_links += soup.select(".titleline > a")
        mega_subtext += soup.select(".subtext")

        time.sleep(1)  # Be polite and avoid overwhelming the server

    return mega_links, mega_subtext


def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["points"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []

    for link, details in zip(links, subtext):
        title = link.getText()
        href = link.get("href")
        vote = details.select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "points": points})
    return sort_by_votes(hn)


try:
    n_pages = int(sys.argv[1])
except ValueError:
    print("The number of pages must be an integer or can ommit it to default to 1.")
    sys.exit(1)

if n_pages < 2:
    n_pages = 1

mega_links, mega_subtext = get_hn_pages(n_pages)

pprint(create_custom_hn(mega_links, mega_subtext))
