# Building A Twitch Streamer Recommender System From Scratch

### Twitch Recommender Using Item-Based Collaborative Filtering & Twitter Scraped Data

###### By: Aurelio Barrios

This repository stores the implementation of a Twitch streamer recommender system that is deployed using Flask and can be found 
[here](https://aureliobarrios.pythonanywhere.com/). A recommender system aims at suggesting items to users based on their interests. These machine learning systems 
found on websites like Netlix, Amazon and Twitter are often overlooked but provide great relevent suggestions to users on a particular site. This implementation 
aims to recommend Twitch streamers to a user based on other Twitch streamers that user already follows. This implementation works great for those that are new to 
the livestreaming space and even those already in the space that are looking for smaller streamers they are missing out on. 

### What Is Shown In This Project

* Domain of Project
  * Data science
  * Machine Learning
  * Flask web deployment
  * API Web Scraping
* Machine Learning Task
  * Item based recommender using user data like streamers that user follows
  
### How to Use This Project

This project is deployed on a [recommender](https://aureliobarrios.pythonanywhere.com/) website deployed using Flask. In this website you will find an input box
where you can input either a streamers twitch channel or twitter handle that you are already interested in. Input as many streamers as you want and when ready you
can select to Recommend Streamer which will redirect you to a page holding 5 streamers that you may be interested in.

### Contents
* **data/**: Subdirectory holding all the necessary data for the implementation of the recommender
* **recommenderSystem.ipynb**: A notebook that walks through three recommender system implementations from scratch 
* **twitter_scraping.ipynb**: A notebook that was used to scrape data off of Twitter using the tweepy Twitter API
