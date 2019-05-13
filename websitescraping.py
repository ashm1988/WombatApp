import requests
import urllib.request
import time
import re
import sys
import logging
import datetime
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class ScrapeSportFix(object):
    def __init__(self):
        self.team_ids = ['129036', '129042', '129044', '129041', '129040', '129037', '129043', '129039', '129038']
        self.content_ids = {
            "Pos": 1,
            "Team Name": 3,
            "Points": 5,
            "played": 9,
            "Won": 11,
            "Lost": 13,
            "Byes": 15,
            "Drawn": 17,
            "Goals For": 23,
            "Goals Against": 25,
        }

    def get_page_response(self, url):
        try:
            response = requests.get(url)
        except Exception as err:
            logger.error(err)
            sys.exit(1)

        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def scrape_league_table(self):
        # URL of the league table page
        url = 'https://sportfix.net/app/competition.aspx?sportFixId=73d44dd0-e1a8-48ca-aaa2-990ba84ea886&sp=613&div=2741&sea=495'
        # Use the URL and pass to function to get the page data
        soup = self.get_page_response(url)

        # parse the date and compare it to the database update time to check if the table needs to be scraped
        lutime = soup.find(id="MainContent_lblLadderLastMod")
        lutime = lutime.text.split()
        del lutime[0:3]
        lutime[0] = lutime[0][:-2]
        lutime = ' '.join(lutime)
        lutime = datetime.datetime.strptime(lutime, "%d %b %Y %I:%M %p")
        # using now as a test example until there is data in the table
        now = datetime.datetime.now()
        if lutime < now:
            print(lutime)
            for tid in self.team_ids:
                tbl = soup.find(id=tid)
                for key, cid in self.content_ids.items():
                    print("%s: %s" % (key, tbl.contents[cid].text.strip()))
            # TODO: pump the data into the firebase table
        else:
            logger.info("No need to update the table")


def main():
    scrape = ScrapeSportFix()
    scrape.scrape_league_table()


if __name__ == '__main__':
    main()
