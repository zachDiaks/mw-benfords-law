'''
WebpageProcessor: Utility class to handle processing of the HTML of certain webpages.
                  Contains untilities like:
                    1) Find all text in a page that should be visible to a user
                    2) Find all numbers in a page that should be visible to a user
'''
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

class WebpageProcessor:
    #----------- Setup -----------
    # Constructor 
    def __init__(self):
        self.Webpage = None
        self.Browser = None
    # Set up class
    async def setup(self, url):
        p = await async_playwright().start()
        self.Browser = await p.webkit.launch()
        page = await self.Browser.new_page()
        page.on("load", lambda: print("Loaded page: " + url))
        await page.goto(url)
        self.Webpage = page
    
    # Clean up webpage
    def __exit__(self):
        self.Browser.close()

    #----------- Processing Methods  -----------
    async def getVisibleText(self):
        soup = BeautifulSoup(await self.Webpage.content())
        pageText = soup.findAll(text=True)
        print('------------------------------------------')
        print(pageText)
        print('------------------------------------------')
