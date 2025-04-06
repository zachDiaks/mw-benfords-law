from WebpageProcessor import WebpageProcessor
import asyncio
import os

async def main():
    # Fetch URLs that were previously saved
    with open("refPages.txt", "r") as f:
        urls = f.readlines()
    urls = [url[:-1] for url in urls] # Trim newline character in each URL
    
    # Set up processor which will be used for fetching all text from a URL
    processor = WebpageProcessor()
    processedFiles = os.listdir("RawTextContents")
    print(f"{processedFiles}")
    for url in urls:
        # Skip if we've already processed this file
        name = makeName(url)
        if name in processedFiles:
            print(f"URL {url} already processed. Skipping")
            continue

        print(f"Processing URL: {url}")
        await processor.setup()
        pageText = await processor.getVisibleText(url)
        with open("RawTextContents/" + name, "w") as f:
            f.writelines(pageText)
    
    # Close the processor
    await processor.Playwright.stop()

def makeName(url):
    return url.split("/")[-1].replace(".html", "") + ".txt"

if __name__ == "__main__":
    asyncio.run(main())