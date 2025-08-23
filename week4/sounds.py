"""!unzip sounds.zip"""

"""import numpy as np
import matplotlib.pyplot as plt
import wave
import glob
import os.path
import random"""

"""soundfile_1 = wave.open('sounds/1_george_12.wav', 'r')
print(soundfile_1)"""

"""buf = soundfile_1.readframes(-1)"""

"""data_1 = np.frombuffer(buf, 'int16')"""

"""rate_1 = soundfile_1.getframerate()"""

"""xValues_1 = np.linspace(start=0,
                        stop=len(data_1)/rate_1,
                        num=len(data_1))"""

"""plt.plot(xValues_1, data_1)
plt.title('one sound file')
plt.xlabel('time')
plt.ylabel('amp')"""

"""plt.specgram(data_1, Fs=rate_1)"""

"""def getSoundData(sf):
    data = sf.readframes(-1)
    data = np.frombuffer(data, 'int16')
    rate = sf.getframerate()
    timescale = np.linspace(start=0,
                            stop=len(data)/rate,
                            num=len(data))
    return (timescale, data)"""

"""# a python list to store our collection of sound file data
sound_files_datas = []
# use glob to import all the sounds from the sounds folder
# then loop over each sound and add the data to our list
for file in glob.glob('sounds/*.wav'):
    soundfile = wave.open(file, 'r')
    sound_files_datas.append(getSoundData(soundfile))

print(len(sound_files_datas))"""

"""rows, cols = 3, 5
fig, ax = plt.subplots(rows, cols, sharex='col', sharey='row')

rowCount = 0
colCount = 0

for sf_data in sound_files_datas:
    timescale, data = sf_data
    ax[rowCount, colCount].plot(timescale, data, c=(
        random.random(), random.random(), random.random()))
    if colCount < 4:
        colCount += 1
    else:
        rowCount += 1
        colCount = 0"""

"""rows, cols = 3, 5
fig, ax = plt.subplots(rows, cols, sharex='col', sharey='row')
fig.set_size_inches(10, 10)
rowCount = 0
colCount = 0

for sf_data in sound_files_datas:
    timescale, data = sf_data
    ax[rowCount, colCount].specgram(data, Fs = 2)

    if colCount < 4:
        colCount += 1
    else:
        rowCount += 1
        colCount = 0"""

#sakila exercise

"""import sqlite3"""
"""import pandas as pd"""

"""con = sqlite3.connect('sakila.db')"""

"""def sql_to_df(sql_query):
  df = pd.read_sql(sql_query, con)
  return df"""

"""query = '''
  SELECT *
  FROM sqlite_master
  WHERE type = 'table'
'''

tables = sql_to_df(query)
tables"""

"""query = '''
  SELECT first_name, last_name
  FROM customer
'''

customer_names = sql_to_df(query)
customer_names"""

"""print(customer_names.head())"""

"""print(customer_names.tail())"""

"""print(customer_names.info())"""

"""print(customer_names.describe())"""

"""query = '''
  SELECT *
  FROM film
  WHERE description
  LIKE '%Pastry%'
'''

pastry_films = sql_to_df(query)
pastry_films"""

"""query = '''
  SELECT
    COUNT(title) AS Count,
    rating
  FROM film
  WHERE description
  LIKE '%Pastry%'
  GROUP BY rating
  ORDER BY Count DESC
'''

pastry_films_by_rating = sql_to_df(query)
pastry_films_by_rating"""

"""pastry_films_by_rating.hist(column='Count', grid=False)"""

# SQL-2

"""import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

con = sqlite3.connect('sakila.db')

def sql_to_df(sql_query):
    df = pd.read_sql(sql_query, con)
    return df"""

"""query = '''
  SELECT
    strftime('%Y-%m', payment_date) AS Date, ROUND(SUM(amount), 0) AS Sales
  FROM payment
  GROUP BY Date
  ORDER BY Date ASC;
'''

sales_per_month = sql_to_df(query)
sales_per_month"""

"""sales_per_month = sales_per_month.set_index('Date')
sales_per_month.plot()"""


"""sales_per_month = sales_per_month.iloc[0:4]
sales_per_month.plot()"""

"""fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(sales_per_month, "bo-")
ax.set_ylim(ymin=0, ymax=32000)
ax.set_title("Sales Per Month")
ax.set_ylabel("Sales")
for date, sales in sales_per_month["Sales"].items():
    ax.annotate(str("${:,.0f}".format(sales)),
        xy=(date, sales+1000),
        fontweight="semibold",
        fontsize=12)

plt.show()"""

"""query = '''
    SELECT
        cat.name category_name,
        sum( IFNULL(pay.amount, 0) ) revenue
    FROM category cat
    LEFT JOIN film_category flm_cat
    ON cat.category_id = flm_cat.category_id
    LEFT JOIN film fil
    ON flm_cat.film_id = fil.film_id
    LEFT JOIN inventory inv
    ON fil.film_id = inv.film_id
    LEFT JOIN rental ren
    ON inv.inventory_id = ren.inventory_id
    LEFT JOIN payment pay
    ON ren.rental_id = pay.rental_id
    GROUP BY cat.name
    ORDER BY revenue DESC
    limit 5;
'''

categories_by_gross = sql_to_df(query)
categories_by_gross

fig, ax = plt.subplots(figsize=(10, 5))

ypos = np.arange(len(categories_by_gross["revenue"]))
bars = ax.bar(ypos, categories_by_gross["revenue"].round(3), width=0.50)
ax.set_xticks(ypos)
ax.set_xticklabels(categories_by_gross["category_name"])
ax.set_ylim(ymin=3000, ymax=6000)
ax.set_title("gross by category", fontsize=14)
ax.set_ylabel("gross sales", fontsize=12)

for bar in bars:  # add data labels
    height = bar.get_height()
    ax.annotate(f"{height}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center", va="bottom",
                fontweight="semibold")

plt.show()"""

"""explode = np.zeros(len(categories_by_gross["category_name"]))
explode[0] = 0.1
print(explode)

fig, ax = plt.subplots()
ax.pie(categories_by_gross["revenue"].round(3), explode=explode, labels=categories_by_gross["category_name"], 
       autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()"""

"""query = '''
    SELECT
        COUNT(title) AS Count,
        rating AS Rating
    FROM film
    WHERE description
    LIKE '%Pastry%'
    GROUP BY rating
    ORDER BY Count DESC;
'''

df = sql_to_df(query)
df.set_index('Rating', inplace=True)

num_adult_pastry = df.loc['NC-17', 'Count']
total = df['Count'].sum()
labels = ['all other', 'adult pastry']
nums = np.array([total, num_adult_pastry])
nums"""

"""explode = [0, 0.2]

fig, ax = plt.subplots()
ax.pie(nums, labels=labels, explode=explode, shadow=True)
ax.axis('equal')

plt.show()"""