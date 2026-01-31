# Using power laws as an excuse to learn web scraping
When my wife and I go on a walk to Coolidge Corner, we ususally stop in at our favorite bookstore: Brookline Booksmith. When I'm there, I have a bad habit of
buying Math books from the discount non-fiction table which I typically stop reading after I hit 100 pages. This time around, for $8, I picked up [Grapes of Math](https://www.goodreads.com/book/show/13547287-the-grapes-of-math).

The book outlines some interesting patterns in nature and the math that describes them. One night, the author reminded me of two empirical laws which seem too bizzarre to be real: [Zipf's Law](https://www.wikiwand.com/en/articles/Zipf%27s_law) and [Benford's Law](https://www.wikiwand.com/en/articles/Benford%27s_law). I first encountered these laws in this [Vsauce video](https://www.youtube.com/watch?v=fCn8zs912OE) from 2015, around the same time when I started my undergraduate degree in Physics and began learning about power laws. I won't go into great detail to explain these laws here - for that, I recommend watching that video. However, revisiting this topic got me thinking...

>Are there naturally occurring datasets that *I* interact with often, which are Zipfian? 

I'm currently a Quality Engineer at MathWorks, supporting the [Sensor Fusion and Tracking Toolbox](https://www.mathworks.com/help/fusion/index.html). I've been meaning to learn how do web scraping so I set off to investigate just how Zipfian and Benfordian the documentation for our toolbox is!

## The Experiment
After a little bit of reading, it became clear that the most popular tool for this job is [Playwright](https://playwright.dev/python/). Now technically Playwright is advertised as a tool for automated testing for web applications. However, you can also use it to read in contents of web pages and understand the hierarchical structure of a website.

So the setup is simple:
1. Start with the landing page for our documentation
2. Iterate over all subpages, extracting the contents of each page
3. Save off the contents into a series of text files
4. Analyze the text in those files!

## The Results
### Adherance to Benford's Law
Benford's law tells us that the leading digit of a number in a naturally occurring dataset is likely to be small. The distribution of digits 1-9 in our dataset should be distributed according to:
$$P(d) = log10(1 + \frac{1}{d})$$

Where $P(d)$ is the probability of the leading digit of a number in the dataset being some digit $d$ (bounded from 0-9). In a table:
| d | P(d)|
|:---|:---|
|1| 30.10%|
|2| 17.61%|
|3| 12.49%|
|4| 9.69%|
|5| 7.92%|
|6| 6.69%|
|7| 5.80%|
|8| 5.12%|
|9| 4.58%|
![Benford Result](./BenfordResult.png)

### Adherance to Zipf's law
1. Analysis using a simple slope comparison
2. Using the Mandlebrot Refinement to explain the initial curve in the dataset. This is apparently a common thing.
3. A more naiive approach to (2) is zooming in on the first section and showing that it follows a different linear curve in the beginning, then is consistent for the tail - Probably leave this out
4. Show some of the top words. Notice that most of the top ones agree with the same top words the video!
![Zipf Result](./ZipfResult.png)
