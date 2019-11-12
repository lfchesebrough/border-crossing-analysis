# border-crossing-analysis

This is my submission for the Insight Data Engineering Coding Challenge. It uses only built-ins and the Python standard library.

The goal is to extract border crossing data, transform the data so that it is grouped by Border, Date, and Measure with total sum of crossings for that group as well as the running total average for that group.

The 'Value' column is the total number of crossings for that group of Border/Date/Measure. From the original data, this is spread out across multiple ports.

The 'Average' column is the running average of total crossings for that Border/Measure for the prior months of the year. For example, pedestrians at the US-Mexico border for March (03/01/2019) would average the sum values from February and January. For January the Average will always be 0 because there are no prior months.

The code aggregates the Value totals and Averages by running through the Date-Value pairs for each Border-Measure group, and keeping track of the running sum until it moves onto the next set of Date-Value pairs or the next Border-Measure group.

The output is sorted by date, then value, then measure, then border in descending order.

