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
        self.Browser = None
        self.Playwright = None
    
    # Set up class
    async def setup(self):
        self.Playwright = await async_playwright().start()
        self.Browser = await self.Playwright.webkit.launch()
        

    #----------- Processing Methods  -----------
    async def getVisibleText(self, url):
        page = await self.connectToPage(url)
        soup = BeautifulSoup(await page.content(), "html.parser")
        pageText = soup.get_text()
        return pageText
    
    #---------- Helper Methods -----------------
    async def connectToPage(self, url):
        page = await self.Browser.new_page()
        page.on("load", lambda: print("Loaded page: " + url))
        await page.goto(url)
        return page
