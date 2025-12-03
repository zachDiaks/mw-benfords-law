# Using power laws as an excuse to learn web scraping
In undergrad I studied physics, where power laws are everywhere! Power laws dictate the motion of planets, sound intensity at different distances from a source, the relationship between kinetic energy and speed, and countless other laws named after some ancient dudes.

While they may sound complicated, power laws are actually quite simple. They dictate that 

 Newton's law of gravitation was probably the first one I encountered:
$$ F_g = \frac{Gm_1m_2}{r^2} $$

This equation tells us that the farther away two objects are from eachother, not only does the gravitational force between the two objects gets weaker, the *rate* at which it gets weaker increases. This can be simply shown like so:

TODO: Add figure showing inverse square law

Since undergrad I've strayed away from physics and now work as a software engineer, but sometimes I like to reconnect with my past and paruse some cheap math books that I can find at a bookstore. I've been reading through the Grapes of Math by Alex Bellos, and one of the first chapters brought me right back to power laws! 

This section of the book discussed how these power laws appear in everyday life, likely in places that you wouldn't expect. It goes on to introduce [Benford's Law](https://www.wikiwand.com/en/articles/Benford%27s_law) which illustrates a strange fact about the distribution of the first digit of numbers in naturally ocurring data sets (e.g. a company's balance sheet or all known [physical constants](https://www.wikiwand.com/en/articles/Physical_constant) of the universe). It also introduces a very similar observation about the distribution of words in a naturally occurring dataset of words (e.g. all articles in some 1964 newspaper, or Tolstoy's *War and Peace*): [Zipf's Law](https://www.wikiwand.com/en/articles/Zipf's_law).

I find these naturally ocurring distributions fascinating - almost as if they were crafted by some higher being. I was curious to see how closely a dataset that I work with often adheres to these distributions. I also have been wanting to learn web scraping and to brush up on my Python skills (I work for MathWorks and primarily write code in MATLAB and sometimes JavaScript). The result is this blog post! Here, I'll discuss how closely the documentation for [Sensor Fusion and Tracking Toolbox](https://www.mathworks.com/help/fusion/index.html), the primary MATLAB toolbox that I work for, adheres to both Benford's and Zipf's Law.

## Setting up the experiment
Like any good experiment, we'll start with a hypothesis and some priors. The hypothesis here is simple: **The Sensor Fusion and Tracking Toolbox documentation adheres to Benford's and Zipf's Law**.

Easy-peasy! Now for the more formal piece. If you aren't terribly interested in the underlying math of these laws, I'd recommend skipping this section.

### Benford's Law

### Zipf's Law

## Results
