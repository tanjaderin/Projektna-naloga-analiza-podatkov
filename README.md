# YouTube Data Analysis Project

This project involves analyzing the **top 5,000 most popular YouTube channels**, with data sourced from [Social Blade](https://socialblade.com/youtube/top/5000). 
The main objectives of the project include web scraping, data cleaning, and conducting exploratory data analysis to gain insights into factors that influence a channel's popularity.

## **Data Collection**
The data was scraped using **Python** with a focus on utilizing regular expressions (**regex**) for extracting relevant information. The following key attributes were collected for each YouTube channel:
- **Rank**: The channel’s position in the top 5,000 list.
- **Grade**: The overall rating of the channel (e.g., A, B+).
- **Channel Name**: The name of the YouTube channel.
- **Number of Uploads**: The total count of videos uploaded by the channel.
- **Total Views**: The cumulative number of views across all videos.
- **Subscribers**: The number of subscribers to the channel.
- **Category**: The content category of the channel (e.g., Gaming, Music).

## **Data Processing**
- The data scraping and extraction were done in the **Ogrodje** module using Python and regex.
- The extracted data was cleaned and formatted into a structured table, which is saved in the **obdelani-podatki** folder.
