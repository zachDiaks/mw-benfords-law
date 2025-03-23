from WebpageProcessor import WebpageProcessor
import asyncio

async def main():
    # Fetch URLs that were previously saved
    with open("refPages.txt", "r") as f:
        urls = f.readlines()
    urls = [url[:-1] for url in urls] # Trim newline character in each URL
    
    # Set up processor which will be used for fetching all text from a URL
    processor = WebpageProcessor()
    for url in urls:
        print(f"Processing URL: {url}")
        await processor.setup()
        pageText = await processor.getVisibleText(url)
        with open("RawTextContents" + makeName(url) + ".txt", "w") as f:
            f.writelines(pageText)
    
    # Close the processor
    await processor.Playwright.stop()

def makeName(url):
    return "foo"

def extractBetween(str, first, second):
    return str

if __name__ == "__main__":
    asyncio.run(main())