from playwright.async_api import async_playwright, Playwright
import asyncio

async def fetchAllURLS(playwright: Playwright, mainPage):
    # Load up main page, wait for it to load
    webkit = playwright.webkit
    browser = await webkit.launch()
    context = await browser.new_context()
    page = await context.new_page()
    page.on("load", lambda: print("Page loaded!"))
    await page.goto(mainPage)

    # Fetch all links
    links = await page.locator("a").all()
    urls = [await link.get_attribute("href") for link in links if await link.get_attribute("href")]
    
    # Find the valid URLs
    print(urls)
    refPages = [extractBefore(mainPage, "referencelist") + url for url in urls if "ref/" in url and not endsWith(url, "#refsect-extended-capabilities")]

    # Close browser
    await browser.close()

    return refPages

def extractBefore(str, targetStr):
    idx = str.find(targetStr)
    return str[:idx]

def endsWith(str, targetStr):
    return str.find(targetStr) + len(targetStr) == len(str)

async def main():
    async with async_playwright() as playwright:
        return await fetchAllURLS(playwright, "https://www.mathworks.com/help/fusion/referencelist.html?type=function")
#------------------------------------------------------------------------------------------------------------------------
refPages = asyncio.run(main())
with open('refPages.txt', 'w') as f:
    for page in refPages:
        f.write(f"{page}\n")