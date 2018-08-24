# Hacker News Project

This is the
'Guided Project: Transforming data with Python', part of the course Data Scientist In Python at [dataquest.io](). I have completed 34% of the course now and this project was in the second course of 'The Command Line'.


In this project I worked with a dataset of article submissions to the webpage [Hacker News](https://news.ycombinator.com) from 2006 to 2015. In this webpage, a user can submit articles, and the articles can receive "upvotes" from other user, signifying that they like them. The more upvotes a submission gets, the more popular it was in the community. Popular articles get to the "front page" of Hacker News, where they're more likely to be seen by others.

The dataset was compiled by Arnaud Drizard using the Hacker News API, and can be found in this  [repo](https://github.com/arnauddri/hn). The dataset used takes 10000 rows from the data randomly, and it's been cleaned a bit by [dataquest.io](). There are four columns:

submission_time -- when the story was submitted.
upvotes -- number of upvotes the submission got.
url -- the base domain of the submission.
headline -- the headline of the submission. Users can edit this, and it doesn't have to match the headline of the original article.

The aim of the project is to  write python scripts that can answer these questions:

What words appear most often in the headlines?
What domains were submitted most often to Hacker News?
At what times are the most articles submitted?

The project answers these questions by writing command line scripts, instead of using IPython notebook or Jupyter notebooks.

Here is a sample of the dataset:

`2014-06-24T05:50:40.000Z	1	flux7.com	8 Ways to Use Docker in the Real World`
`2010-02-17T16:57:59Z	1	blog.jonasbandi.net	Software: Sadly we did adopt from the construction analogy`
`2014-02-04T02:36:30Z	1	blogs.wsj.com	 Google's Stock Split Means More Control for Larry and Sergey`
`2011-10-26T07:11:29Z	1	threatpost.com	SSL DOS attack tool released exploiting negotiation overhead`
`2011-04-03T15:43:44Z	67	algorithm.com.au	Immutability and Blocks Lambdas and Closures`
