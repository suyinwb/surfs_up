# surfs up

## Background

Jupyter notebook file: we will continue to use Jupyter Notebook for our weather analysis. The name of the file is climate_analysis.ipynb. This file will have all of the structure to help you get started on your analysis. Let's get started by downloading the notebook.

SQLite database: W. Avy has stored the weather data in a SQLite database. All SQLite databases are flat files, which means that they don't have relationships that connect the data to anything else. As a result, flat files can be stored locally, which will help us move more quickly through the analysis.

W. Avy is concerned about the amount of precipitation on Oahu. There needs to be enough rain to keep everything green, but not so much that you lose out on that ideal surfing and ice cream weather.

You know that you can set W. Avy's mind at ease by analyzing precipitation levels and showing him the cold, hard, data that backs up Oahu as the perfect place to surf. You have the last 12 months of precipitation data already loaded into your SQLite database, so you are ready to go.

W. Avy supplied you with the data he wants us to use and has asked you to look at a full year of data. When deciding how to parse the data, you remember that his favorite day is August 23, 2017 because it's the anniversary of the first time he ever went surfing and had ice cream on the same day. So, you decide to start the analysis there.

## Overview of Project
### Purpose
After executing the code and checking the results, a few folks are are appearing twice. Maybe they moved departments?

## Analysis And Challenges

## Methodology: Analytics Paradigm

#### 1. Decomposing the Ask



#### 2. Identify the Datasource
* employees.csv
* dept_manager.csv
* dept_emp.csv
* salaries.csv
* titles.csv
* departments.csv

#### 3. Define Strategy & Metrics
**Resource:** Postgres 11, pgAdmin, SQL

1. create ERD based on the 6 csv data above
1.

#### 4. Data Retrieval Plan
Import csv data into the database tables using pgAdmin import function.


#### 5. Assemble & Clean the Data

Bad data comes in three states:
* Beyond repair
Data beyond repair could be data that has been overwritten or has suffered severe data corruption during storage or transfer (such as power loss during writing, voltage spikes, or hard-drive failures). The worst-case example would be having data with every value missing. All the information is lost and unrecoverable. For data beyond repair, all we can do is delete it and move on.

* Badly damaged
Data that is badly damaged may have good data that we can recover, but it will take time and effort to repair the damaged data. This can be garbled data, with a lot of missing values, from inconsistent sources, or existing in multiple columns. Consider trade-offs to pick the best solution (even if the "best" solution isn't perfect, but rather the "best-available" solution). To repair badly damaged data, try these strategies:
Filling in missing data by
substituting data from another source,
interpolating between existing data points, or
extrapolating from existing data
Standardizing units of measure (e.g., monetary values stored in multiple currencies)
Consolidating data from multiple columns

* Wrong form
data in the wrong form should usually be fixed—that is, the data is good but can't be used in its current form. "Good" data in the wrong form can be data that is too granular or detailed, numeric data stored as strings, or data that needs to be split into multiple columns (e.g., address data). To remedy good data in the wrong form, try these strategies:
Reshape the data
Convert data types
Parse text data to the correct format
Split columns


It's important to document data cleaning assumptions as well as decisions and their motivations. Later decisions depend on earlier decisions made, which can be too much to remember. Any assumptions that were part of an earlier decision can, if forgotten, ruin later steps.
Transforming a messy dataset into a clean dataset is an iterative process. As you clean one part of the data, you may reveal something messy in another part of the data. Sometimes that means unwinding a lot of work that you've already done and having to redo it with a slight change. Documenting why a particular step is necessary will show you how to redo it without introducing more errors.

One thing to watch out for is to make nondestructive edits as much as possible while designing your pipeline. That means it's better to keep your raw data in one variable, and put the cleaned data in another variable. It takes up more memory, but it makes tracking the iterative process of data cleaning easier.


#### 6. Analyse for Trends

Results from data filter above will give us more in-depth information regarding the different departments, roles and future retirees.

#### 7. Acknowledging Limitations
pgAdmin is an old application for Postgres front end GUI. So sometimes when closing the application, the database will be corrupted and wiped out by pgAdmin. Do a full backup before closing.

#### 8. Making the Call:
The "Proper" Conclusion is indicated below on [Summary](#summary)

## Analysis


>Total Employees

![Total Employees](total_employees.png)


## Summary


## Appendix
