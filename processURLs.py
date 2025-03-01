from WebpageProcessor import WebpageProcessor
import asyncio

async def main():
    sampleURL = "https://www.mathworks.com/help/fusion/ref/trackospametric-system-object.html"
    processor = WebpageProcessor()
    await processor.setup(sampleURL)
    await processor.getVisibleText()
    print("++++++++++ Exiting main ++++++++++++++++")

if __name__ == "__main__":
    asyncio.run(main())