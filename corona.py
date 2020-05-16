import pandas as pd
import matplotlib.pyplot as plt 


confirmed = pd.read_csv('covid19_confirmed.csv')
deaths = pd.read_csv('covid19_deaths.csv')
recovered = pd.read_csv('covid19_recovered.csv')

confirmed = confirmed.drop(['Province/State','Lat','Long'],axis=1)
deaths = deaths.drop(['Province/State','Lat','Long'],axis=1)
recovered = recovered.drop(['Province/State','Lat','Long'],axis=1)


confirmed = confirmed.groupby(confirmed['Country/Region']).aggregate('sum')
deaths = deaths.groupby(deaths['Country/Region']).aggregate('sum')
recovered = recovered.groupby(recovered['Country/Region']).aggregate('sum')

confirmed = confirmed.T
deaths = deaths.T
recovered = recovered.T

new_cases = confirmed.copy()
for day in range(1,len(confirmed)):
    new_cases.iloc[day] = confirmed.iloc[day] = confirmed.iloc[day-1]


growth_rate = confirmed.copy()
for day in range(1,len(confirmed)):
    growth_rate.iloc[day] = (new_cases.iloc[day] / confirmed.iloc[day-1])*100

active_cases = confirmed.copy()

for day in range(0,len(confirmed)):
    active_cases.iloc[day] = confirmed.iloc[day] - deaths.iloc[day] - recovered.iloc[day]


overall_groth_rate = confirmed.copy()
for day in range(1,len(confirmed)):
    overall_groth_rate.iloc[day] = ((active_cases.iloc[day] - active_cases.iloc[day-1]) / active_cases.iloc[day-1]) * 100

# print(overall_groth_rate['South Africa'].tail(10))

death_rate = confirmed.copy()
for day in range (0,len(confirmed)):
    death_rate.iloc[day] = (deaths.iloc[day] / confirmed.iloc[day])* 100


hospitalization_rete_estimate = 0.05

hospitalization_needed = confirmed.copy()
for day in range(0,len(confirmed)):
    hospitalization_needed.iloc[day] = active_cases.iloc[day] * hospitalization_rete_estimate



countries = ['South Africa','China','Spain','US']
for country in countries:
    confirmed[country].plot(label = country)

ax = plt.Subplot()
ax.Set_faceColor('black')
ax.figure.Set_facecolor('#121212')
ax.tick_params(axis='x',colors='white')
ax.tick_params(axis='y',colors='white')
ax.set_title('covid-19 Total confimed cases by county ',color='white')    
    
plt.legend(loc='upper left')
plt.show()