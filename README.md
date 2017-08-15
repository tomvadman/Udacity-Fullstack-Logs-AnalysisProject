# Udacity-Fullstack-Project 3 - Logs Analysis Project

This project is about creating a reporting tool that parse a database containing data about news articles. You can download the database and VM in the prereq section. This repo only containing the reporting tool.

# Overview 

## So what are we reporting, anyway?
## Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

### 1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.


### 2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.


### 3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)


# How to use this solution

### prereq
* Setup this environment : https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0
* Create a SQL view on Vagrant Machine (news_reporting.py uses NEWS_STATS_VIEW).

``` CREATE VIEW NEWS_STATS_VIEW AS
    SELECT articles.title,log.path,authors.name,log.status,log.time,date(log.time) as day
    FROM articles
    LEFT JOIN log ON log.path LIKE CONCAT('%', articles.slug ,'%')
    JOIN authors ON authors.id = articles.author;
 ```
### Run reporting Tool
* Download news_reporting.py and copy it to Vagrant Machine. Then run the news_reporting.py and wait for the result.

