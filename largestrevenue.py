
import requests
from bs4 import BeautifulSoup

company_rank=[]
company_name=[]
company_yearending=[]
company_revenue=[]
company_employees=[]
company_headquarter=[]

url="https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue"

response = requests.get(url)
html_soup = BeautifulSoup(response.text,'html.parser')

company_list=html_soup.find_all("table", class_="wikitable sortable plainrowheads")
#print(company_list)

table_data=company_list[0].tbody.find_all('tr')
cols=company_list[0].find_all('td')
#print(len(cols))



i=0
for j in range(len(cols)):
    if i<len(cols):
        company_rank.append(cols[i].text)
        i=i+7
#print(company_rank)
i=2
for j in range(len(cols)):
    if i<len(cols):
        company_name.append(cols[i].text.rstrip())
        i=i+7
#print(company_name)
i=3
for j in range(len(cols)):
    if i<len(cols):
        company_yearending.append(cols[i].text)
        i=i+7
#print(company_yearending)
i=4
for j in range(len(cols)):
    if i<len(cols):
        cols[i]=cols[i].text.replace("$","")
        company_revenue.append(cols[i])
        i=i+7
#print(company_revenue)
i=5
for j in range(len(cols)):
    if i<len(cols):
        cols[i]=cols[i].text.replace(",","")
        company_employees.append(cols[i])
        i=i+7
#print(company_employees)
i=6
for j in range(len(cols)):
    if i<len(cols):
        company_headquarter.append(cols[i].text)
        i=i+7
#print(company_headquarter)


for i in range(0,len(company_name)):
    data="{:<5}|{:<30}|{:^20}|{:^15}|{:^15}|{:<50}".format(company_rank[i],company_name[i],company_yearending[i],company_revenue[i],company_employees[i],company_headquarter[i])
    #print(data)


table_data=company_list[1].tbody.find_all('tr')
cols=company_list[1].find_all('td')
#print(len(cols))
i=0
for j in range(len(cols)):
    if i<len(cols):
        company_rank.append(cols[i].text)
        i=i+7
#print(company_rank)
i=2
for j in range(len(cols)):
    if i<len(cols):
        company_name.append(cols[i].text.rstrip())
        i=i+7
#print(company_name)
i=3
for j in range(len(cols)):
    if i<len(cols):
        f=""
        cols[i]=cols[i].text
        flag=cols[i]
        for m in range(len(flag)):
            if flag[m]!='[':
                f=f+flag[m]
            else:
                break
        company_yearending.append(f)
        i=i+7
#print(company_yearending)
i=4
for j in range(len(cols)):
    if i<len(cols):
        cols[i]=cols[i].text.replace("$","")
        f=""
        cols[i]=cols[i]
        flag=cols[i]
        for m in range(len(flag)):
            if flag[m]=='[' or flag[m]=='–' :
                break
            else:
                f=f+flag[m]

        company_revenue.append(f)
        i=i+7

#print(company_revenue)
i=5
for j in range(len(cols)):
    if i<len(cols):
        cols[i]=cols[i].text.replace(",","")
        f=""
        cols[i]=cols[i]
        flag=cols[i]
        for m in range(len(flag)):
            if flag[m]!='[':
                f=f+flag[m]
            else:
                break
        company_employees.append(f)
        i=i+7
#print(company_employees)
i=6
for j in range(len(cols)):
    if i<len(cols):
        company_headquarter.append(cols[i].text)
        i=i+7
#print(company_headquarter)
for i in range(len(company_name)):
    data="{:<5}|{:<30}|{:^20}|{:^15}|{:^15}|{:<50}".format(company_rank[i],company_name[i],company_yearending[i],company_revenue[i],company_employees[i],company_headquarter[i])
    print(data)
    #print(company_rank[i],company_name[i],company_yearending[i],company_revenue[i],company_employees[i],company_headquarter[i],sep="-")



import matplotlib.pyplot as plt
company_name_key=list(company_name)
company_revenue_value=list(company_revenue)
company_employees_value=list(company_employees)

data={}
for i in range((10)):
    data[company_name_key[i]]=company_revenue_value[i]

#print(data)
names = list(data.keys())
values = list(data.values())
values = [float(i) for i in values]
#print(names)
#print(values)

fig, axs = plt.subplots(1, 1, figsize=(25, 3))
axs.bar(names,values)

fig.suptitle('Company vs Revenue')

data1={}
for i in range((10)):
    data1[company_name_key[i]]=company_employees_value[i]

names = list(data1.keys())
values = list(data1.values())
values = [float(i) for i in values]
#print(names)
#print(values)

fig, axs = plt.subplots(1, 1, figsize=(25, 3))
axs.bar(names, values)

#axs[1].scatter(names, values)
#axs[2].plot(names, values)
fig.suptitle('Company vs Employees')





import matplotlib
#import matplotlib.pyplot as plt
import numpy as np


labels = list(data.keys())
revenue = list(data.values())
revenue = [float(i) for i in revenue]
employees = list(data1.values())
employees = [float(j) for j in employees]


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, revenue, width, label='revenue')
rects2 = ax.bar(x + width/2, employees, width, label='employees')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()






