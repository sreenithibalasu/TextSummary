# TextSummary

## The task given in the first project was:
1. Extract the links from the RSS feeds of 3 major Indian Finance Newspapers: The Hindu Business Line, The Financial Express and Economic Times
2. Extract the articles from each link using newskaper3k module
3. Put the article content through the TextRank Algorithm - based on PageRank Algorithm - and generate a summary
4. Store the summarized text in a Database

## The work I've done:
- For the time being, there are three copies of the code, modified for each of the three webpage RSS feeds
- since the extracted links and its content varies for each webpage, there were slight modifications made for each of the webpages and hence there are three copies. In the future, I hope to generalize the code for any given webpage
- Using Python and the BeautifulSoup module, I was able to extract the links from the RSS feeds of each newspaper franchise
- After extracting the links and storing them in a list, I used the newspaper3k module to download, parse and extract the article from each link in the list.
- The issue I ran into while extracting an article, is that sometimes the webpage displays a pop up alert which is usually for asking people to sign up for alerts. What newspaper3k is doing, is instead of extracting the article content, the content of the pop up notification is extracted instead. Since the solution for this is complicated, I chose to ignore the content of this link. The probability of this problem occuring was pretty small too.
- After extracting the article content, I stored the content and title in two seperate lists
- I ran the contents of the article through the TextRank algorithm and got an okayish summary. Although, I was not happy with some of the results. I wish to do further research and run this content through another approach to get a better output.
- After getting the summary, I used SQLAlchemy to create a Database which has the following columns: ID, NewsPaper Name, ArticleTitle and ArticleSummary. The summary content and all other information was stored in the Database.
- Since there are 3 copies of the code, there are 3 seperate databases for each newspaper franchise. I wish to eliminate this as well and use a single DB for all the summaries, once the code for summarization has been generalized.
