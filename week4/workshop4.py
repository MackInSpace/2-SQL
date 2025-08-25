"""!sudo apt-get -y -qq update
!sudo apt-get -y -qq install postgresql
!sudo service postgresql start"""

"""!sudo -u postgres psql -c 'DROP DATABASE IF EXISTS moma;'"""

"""!sudo -u postgres psql -c 'CREATE DATABASE moma;'"""

"""!sudo -u postgres psql moma < momaviz.sql"""

"""!sudo -u postgres psql -U postgres -c "ALTER USER postgres PASSWORD 'postgres';" """

"""import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

conn = psycopg2.connect("dbname=moma user=postgres password=postgres host=localhost port=5432")
conn.set_session(autocommit=True)

cur = conn.cursor()"""

"""def sql_to_df(sql_query: str):
    #Get result set of sql_query as a pandas DataFrame.
    return pd.read_sql(sql_query, conn)"""

# Task 1: Part 2 - Test your query

cur.execute(
    """
    SELECT department, COUNT(*)
    FROM moma_works
    GROUP BY department
    ORDER BY count DESC;
    """
)

works = cur.fetchall()
for w in works:
  print(w)

# Task 1: Part 3 - Data visualization

title = "Artworks by Department"
query = """
        SELECT department, COUNT(*)
        FROM moma_works
        GROUP BY department
        ORDER BY count DESC;
        """

dataframe = sql_to_df(query)
_fig, axes = plt.subplots(figsize=(10, 5))
axes.set_title(title, fontsize=14)

# get evenly spaced x-axis positions
xpos = np.arange(len(dataframe))
# at each x, add bar (height based on count data)
axes.bar(xpos, dataframe["count"], width=0.50)
# at each x, add tick mark
axes.set_xticks(xpos)
# at each x, add label based on dept data
axes.set_xticklabels(dataframe["department"])
# label y-axis
axes.set_ylabel("Count", fontsize=12)
# rotate x-axis labels to prevent overlap
plt.setp(axes.get_xticklabels(), rotation=30, horizontalalignment='right')

plt.show()

# Task 2: Part 2 - Test your query

cur.execute(
    """
    SELECT classification, COUNT(*)
    FROM moma_works
    GROUP BY classification
    ORDER BY count DESC;
    """
)

works = cur.fetchall()
for w in works:
  print(w)

  # Task 2: Part 3 - Data visualization

title = "Artworks by Classification"
query = """
        SELECT classification, COUNT(*)
        FROM moma_works
        GROUP BY classification
        ORDER BY count DESC;
        """

dataframe = sql_to_df(query)
_fig, axes = plt.subplots(figsize=(10, 5))
axes.set_title(title, fontsize=14)

xpos = np.arange(len(dataframe))
axes.bar(xpos, dataframe["count"], width=0.50)
axes.set_xticks(xpos)
axes.set_xticklabels(dataframe["classification"])
axes.set_ylabel("Count", fontsize=12)
plt.setp(axes.get_xticklabels(), rotation=30, horizontalalignment='right')

plt.show()

# Task 3: Part 2 - Test your query

cur.execute(
    """
    SELECT
      info -> 'nationality' AS nationality,
      COUNT(*) AS count
    FROM moma_artists
    WHERE info ->> 'nationality' IS NOT NULL
      AND info ->> 'nationality' <> ''
    GROUP BY nationality
    ORDER BY count DESC
    LIMIT 10;
    """
)

artists = cur.fetchall()
for a in artists:
  print(a)

  # Task 3: Part 3 - Data visualization

title = "Artists by Nationality"
query = """
        SELECT
          info -> 'nationality' AS nationality,
          COUNT(*) AS count
        FROM moma_artists
        WHERE info ->> 'nationality' IS NOT NULL
          AND info ->> 'nationality' <> ''
        GROUP BY nationality
        ORDER BY count DESC
        LIMIT 10;
        """

dataframe = sql_to_df(query)
_fig, axes = plt.subplots(figsize=(10, 5))
axes.set_title(title, fontsize=14)

xpos = np.arange(len(dataframe))
axes.bar(xpos, dataframe["count"], width=0.50)
axes.set_xticks(xpos)
axes.set_xticklabels(dataframe["nationality"])
axes.set_ylabel("Count", fontsize=12)

plt.show()

# Task 4: Part 2 - Test your query

cur.execute(
    """
    SELECT
      UPPER(info ->> 'gender') AS gender,
      COUNT(*) AS count
    FROM moma_artists
    WHERE info ->> 'gender' IS NOT NULL
      AND info ->> 'gender' <> ''
    GROUP BY UPPER(info ->> 'gender')
    ORDER BY gender;
    """
)

artists = cur.fetchall()
for a in artists:
  print(a)

  # Task 4: Part 3 - Data visualization

title = "Artists by Gender"
query = """
        SELECT
          UPPER(info ->> 'gender') AS gender,
          COUNT(*) AS count
        FROM moma_artists
        WHERE info ->> 'gender' IS NOT NULL
          AND info ->> 'gender' <> ''
        GROUP BY UPPER(info ->> 'gender')
        ORDER BY gender;
        """

dataframe = sql_to_df(query)
fig, axes = plt.subplots(figsize=(10, 5))
axes.set_title(title, fontsize=14)

fig.set_facecolor('white')
axes.pie(
    x=dataframe["count"],
    labels=dataframe["gender"],
    autopct='%1.1f%%',
    colors=['lightcoral', 'skyblue', 'lavender']
)
# Equal aspect ratio ensures that pie is drawn as a circle.
axes.axis('equal')

plt.show()

# BONUS TASK 5

title = "Cumulative Count of Acquired Artwork"
query = """
        WITH daily_acquisition_count AS (
            SELECT date_acquired, COUNT(*) FROM moma_works 
            WHERE date_acquired IS NOT NULL 
            GROUP BY date_acquired
        )
        SELECT date_acquired, SUM(count) 
        OVER (ORDER BY date_acquired) FROM daily_acquisition_count;
        """
dataframe = sql_to_df(query)
_fig, axes = plt.subplots(figsize=(10, 5))
axes.set_title(title, fontsize=14)

xpos = np.arange(len(dataframe))
axes.bar(xpos, dataframe["sum"], width=0.50)
axes.set_xticks([
    0,
    len(dataframe) // 2,
    len(dataframe)
])
axes.set_xticklabels(dataframe.iloc[[
    0,
    len(dataframe) // 2,
    -1
]]["date_acquired"])
axes.set_ylabel("Count", fontsize=12)

plt.show()