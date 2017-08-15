#!/usr/bin/python3

import psycopg2

DB_NAME = "news"

queryInfo_1 = "What are the most popular three articles of all time?"
query_1 = """select title, count(title) as views
from NEWS_STATS_VIEW
where status like '%200%'
group by title
order by views desc limit 3;"""

queryInfo_2 = "Who are the most popular article authors of all time?"
query_2 = """select name,count(name) as views from NEWS_STATS_VIEW
group by name
order by views desc;"""

queryInfo_3 = "On which days did more than 1% of requests lead to errors ?"
query_3 = """select total.day as date,ROUND(cast(error.totalError as decimal)  /
cast(total.total as decimal) * 100,2) as perc from
(select date(log.time) as day, count(*) as total
from log
group by day) as total
left join
(select date(log.time) as day, count(*) as totalError
from log
where status like '%404%'
group by day) as error
on total.day = error.day
where (error.totalError * 100) / total.total >= 1
order by total.day;"""


def connect_to_db():
    try:
        db = psycopg2.connect(database=DB_NAME)
        c = db.cursor()
    except Exception, e:
        print 'couldnt connect to DB'


def query_result(query):
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_view_results(queryinfo, query):
    print ('\n'+queryinfo+'\n')
    i = 0
    for item in query:
        i = i+1
        print (
            '\t' + str(i) + '. ' + str(item[0]) +
            ' ---> ' + str(item[1]) + ' views')


def print_err_perc_results(queryinfo, query):
    print '\n' + queryinfo + '\n'
    i = 0
    for item in query:
        i = i+1
        print (
            '\t' + str(i) + '. ' + str(item[0]) +
            ' ---> ' + str(item[1]) + ' % error')

connect_to_db()
print_view_results(queryInfo_1, query_result(query_1))
print_view_results(queryInfo_2, query_result(query_2))
print_err_perc_results(queryInfo_3, query_result(query_3))
