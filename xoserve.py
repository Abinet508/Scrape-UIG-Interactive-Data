import requests
import pandas as pd
import csv
from requests_html import HTML


class XoserveScraper:
    """
    A class to scrape data from the Xoserve website.
    """

    def __init__(self):
        self.cookies = self.get_cookies()
        self.headers = self.get_headers()

    def get_cookies(self):
        """
        Get the cookies required to access the Xoserve website.

        Returns:
            dict: A dictionary containing the cookies.
        """
        return {
            "WelcomeOverlay": "y",
        }

    def get_headers(self):
        """
        Get the headers required to access the Xoserve website.

        Returns:
            dict: A dictionary containing the headers.
        """
        return {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-User": "?1",
            "Sec-GPC": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
        }

    def scrape_data(self):
        """
        Scrape the data from the Xoserve website and save it to an Excel file.
        """
        response = requests.get(
            "https://www.xoserve.com/help-centre/demand-attribution/unidentified-gas-uig/chart-uig-by-gas-day/",
            cookies=self.cookies,
            headers=self.headers,
        )
        if response.status_code == 200:
            return response
        else:
            return None

    def save_data(self, response: requests.models.Response):
        """
        Save the data to a CSV file.

        Args:
            response (requests.models.Response): The response object containing the data.
        """

        html_str = HTML(html=response.text)
        url = html_str.xpath('//a[contains(@href,".xlsx")]', first=True).attrs["href"]
        url = "https://www.xoserve.com" + url
        df = pd.read_excel(url)
        df.to_csv(
            "uig_data.csv",
            index=False,
            encoding="utf-8",
            lineterminator="\n",
            quotechar='"',
            quoting=csv.QUOTE_ALL,
        )

    def run(self):
        """
        Run the scraper.
        """
        response = self.scrape_data()
        if response:
            self.save_data(response)
            print("Data saved successfully.")


if __name__ == "__main__":
    scraper = XoserveScraper()
    scraper.run()
