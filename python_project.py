#B071 Bhavya Singhal
#B102 Pushkar Sawant
#B120 Aditi Rupvate

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
%matplotlib inline
import warnings
warnings.filterwarnings("ignore")

deliveries = pd.read_csv('archive/IPL Ball-by-Ball 2008-2020.csv')
matches = pd.read_csv('archive/IPL Matches 2008-2020.csv')

matches

x=['Sunrisers Hyderabad', 'Mumbai Indians', 'Gujarat Lions',
    'Rising Pune Supergiant', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Delhi Daredevils', 'Kings XI Punjab',
    'Chennai Super Kings', 'Rajasthan Royals', 'Deccan Chargers',
    'Kochi Tuskers Kerala', 'Pune Warriors', 'Rising Pune Supergiants', 'Delhi Capitals']

y = ['SRH','MI','GL','RPS','RCB','KKR','DC','KXIP','CSK','RR','SRH','KTK','PW','RPS','DC']

matches.replace(x,y,inplace = True)#replace x with y full name to short one
deliveries.replace(x,y,inplace = True)#replace wherever x is there to short form

deliveries

matches['season'] = matches['date'].str[:4].astype(int)#to take the year

sns.set_style("white")
sns.set_context('paper',font_scale=1.4)
plt.style.use("dark_background")
plt.xlabel('Season')
plt.ylabel('Count')
plt.title('Matches In Every Season')
plt.grid(True)
plt.hist(matches['season'],color='blue',bins=13)
plt.show()

#The year 2013 has the most matches, possibly due to super overs. Also, there are 10 teams in 2011, 9 in 2012 and 2013, this is another reason for the increase in the number of matches.

df=pd.DataFrame(matches.venue.value_counts())

plt.plot(df.index,df.venue,marker='o',linestyle='--',color='r')
plt.xticks(rotation = 90)
sns.set_style('darkgrid')
sns.set_context('paper',font_scale=1.0)
plt.grid(True)
plt.ylabel('Count')
plt.show()

matches_played=pd.concat([matches['team1'],matches['team2']])
matches_played=matches_played.value_counts().reset_index()
matches_played.columns=['Team','Total Matches']
matches_played['wins']=matches['winner'].value_counts().reset_index()['winner']

matches_played.set_index('Team',inplace=True)
totm = matches_played.reset_index().head(8)
totm

sns.set_style("white")
sns.set_context('paper',font_scale=1.1)
plt.style.use("dark_background")
plt.title('Total Matches vs Wins Per Team')
plt.xlabel('Total Matches')
plt.ylabel('Wins')
plt.grid(True)

sns.barplot(x='Total Matches',y='wins',data=totm,palette='magma',hue='Team')
plt.show()

sns.set_style('dark')
slices = [120,106,99,95,91,88,86,81]
labels = [' MI','SRH','RCB','DC','KKR','KXIP','CSK','RR']
explode=[0.2,0,0,0,0,0,0,0]
plt.pie(slices,labels=labels,explode=explode,shadow=True,startangle=90,autopct='%.1f%%')
plt.title("Wining Percentage")
plt.show()

matches_played

deliveries.head(2)

matches.toss_decision.value_counts()
sns.countplot('toss_decision',data=matches)

matches.head(2)

deliveries.head(2)

df3=pd.DataFrame(matches.season,deliveries.total_runs)

df3

batsmen = matches[['id','season']].merge(deliveries, left_on = 'id', right_on = 'id', how = 'left').drop('id', axis = 1)
season=batsmen.groupby(['season'])['total_runs'].sum().reset_index()

avgruns_each_season=matches.groupby(['season']).count().id.reset_index()
avgruns_each_season.rename(columns={'id':'matches'},inplace=1)
avgruns_each_season['total_runs']=season['total_runs']
avgruns_each_season['average_runs_per_match']=avgruns_each_season['total_runs']/avgruns_each_season['matches']

plt.plot(avgruns_each_season['season'],avgruns_each_season['average_runs_per_match'],marker='o',linestyle='--',linewidth=4,color='r',label='Average Runs')
plt.title('Total and Average run per Season')
plt.xlabel('Year')
plt.ylabel('Average Runs')
plt.legend()
plt.grid(True)

plt.show()

plt.plot(avgruns_each_season['season'],avgruns_each_season['total_runs'],marker='o',linestyle='--',linewidth=4,color='b',label='Total Runs')
plt.xlabel('Year')
plt.ylabel('Total Runs')
plt.legend()
plt.grid(True)

plt.show()

matches.head(1)

deliveries.head(2)

drt=deliveries.groupby(['inning','batting_team','bowling_team'])['total_runs'].sum().reset_index()

drt=drt[drt['total_runs']>=200]
drt = drt.nlargest(10,'total_runs')

drt

