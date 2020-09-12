# surfs_up

## Module Project Overview

W. Avy wants to open up a Surf and Ice Cream store in Oahu, Hawaii. This analysis is to analyze the weather data to see if Oahu is a good fit or not for this business.

W. Avy is concerned about the amount of precipitation on Oahu. There needs to be enough rain to keep everything green, but not so much that you lose out on that ideal surfing and ice cream weather.

## Resources:
  - Data Source: hawaii.sqlite
  - Software: anaconda3, python 3.7.7, jupyter notebook, flask
  - Library: matplotlib, pandas, numpy, datetime, sqlalchemy, and flask

## Module Project Analysis

Based on the weather data provided by W. Avy in sqlite file, analysis was done to find the amount of precipitation on each day for a year between Aug - 2016 to Aug - 2017. The data is then plotted in the chart shown below.

plot:

!["precipitation plot"](./Resources/precipitation_2016_2017_aug.png "Precipitation for yr 2016-2017")

Statistics for the year length on precipitation data is as follows:

!["precipitation stats"](./Resources/precipitation_2016_2017_aug_stat.png "Precipitation stats yr 2016-2017")

## Challenge Overview

W. Avy liked the above analysis, and he wanted more information about temperature trends before opening the surf shop. Specifically, he wanted temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

## Challenge Analysis

Analysis was done by extracting all of June temperature data and December temperature data. The statistics are displayed below.

June:

!["June stats"](./Resources/challenge_june_temps.png "June stats")
 
December:

!["December stats"](./Resources/challenge_december_temps.png "December stats")

### Differences
  - Average temperatures in June and December are 75 and 72 degs F, which indicates more people will surf in June than in December.
  - Max temperatures in June and December are 85 and 83 degs F, which indicates there will be days in December, when icecream sales will be high.
  - Min temperatures in June and December are 64 and 56 degs F, which indicates there will be days in June, when icecream sales will go down.

### Summary

Based on the information we can recommend that opening surf and icecream shops in Oahu is a sound investment. With temperatures @70+ deg F, Oahu is a good place to surf and have icecreams after surfing.

#### Additional Queries:
  - To have a better idea about the weather, following queries would help out more:
    - a query to get the max, min, avg precipitations recorded by station for months of June and December.
      - select station, strftime('%m', date) date, max(prcp), min(prcp), avg(prcp) from measurement 
        where strftime('%m', date) in ('07', '12') group by station, strftime('%m', date)
    - a query to get the max, min, avg temperatures recorded by station for months of June and December.
      - select station, strftime('%m', date) date, max(tobs), min(tobs), avg(tobs) from measurement 
        where strftime('%m', date) in ('07', '12') group by station, strftime('%m', date)
    
