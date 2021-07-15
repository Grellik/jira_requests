from jira_reqs import *
import pandas as pd
import matplotlib.pyplot as plt

data = create_csv()

df = pd.DataFrame(data,columns=["key", "component", "reporter", "creation date", "update date"])
print(df)

def graph_time(df):

    month = int(input("month (as number) = "))
    year = int(input("year (as 4 digit number) ="))
    
    bug_num = []
    day_num = []
    bugs = 0
    
    for index, row in df.iterrows():
        cd = row["creation date"].split("T")
        cd = cd[0].split("-")
        if year > int(cd[0]) or month > int(cd[1]):
            break
        if year == int(cd[0]) and month == int(cd[1]):
            bugs += 1
        bug_num.append(bugs)
        day_num.append(str(cd[2]))
    
    day_num.reverse()
    bug_num.reverse()
    
    graph_data = {
        "bugs" : bug_num,
        "day" : day_num
    }
    
    gdf = pd.DataFrame(graph_data, columns=["bugs", "day"])
    gdf = gdf.groupby("day").agg({"bugs":'sum'}).reset_index()
    
    print(gdf)
    gdf.plot(x ="day", y="bugs", kind = 'bar')
    plt.show()
    
def graph_testers(df):

    names = {}

    quarter = int(input("quarter (1-4) ="))
    year = int(input("year (as 4 digit number) ="))
    if quarter == 1:
        month = [1,2,3]
    elif quarter == 2:
        month = [4,5,6]
    elif quarter == 3:
        month = [7,8,9]
    else:
        month = [10,11,12]

    for index, row in df.iterrows():
        cd = row["creation date"].split("T")
        cd = cd[0].split("-")
        if year > int(cd[0]) and int(cd[1] not in month):
            break
        if year == int(cd[0]) and int(cd[1]) in month:
            if row["reporter"] not in names:
                names[row["reporter"]] = 1
            else:
                names[row["reporter"]] += 1

    name = []
    bugs = []
    for k, v in names.items():
        name.append(k)
        bugs.append(v)

    graph_data = {
        "name" : name,
        "bugs" : bugs
    }

    gdf = pd.DataFrame(graph_data, columns=["bugs", "name"])
    
    print(gdf)
    gdf.plot(x ="name", y="bugs", kind = 'bar')
    plt.show()          

def graph_analytics(df):

    components = {}

    quarter = int(input("quarter (1-4) ="))
    year = int(input("year (as 4 digit number) ="))
    if quarter == 1:
        month = [1,2,3]
    elif quarter == 2:
        month = [4,5,6]
    elif quarter == 3:
        month = [7,8,9]
    else:
        month = [10,11,12]
    
    for index, row in df.iterrows():
        cd = row["creation date"].split("T")
        cd = cd[0].split("-")
        if year > int(cd[0]) and int(cd[1] not in month):
            break
        if year == int(cd[0]) and int(cd[1]) in month:
            if row["component"] not in components:
                components[row["component"]] = 1
            else:
                components[row["component"]] += 1

    component = []
    bugs = []
    for k, v in components.items():
        component.append(k)
        bugs.append(v)
    
    graph_data = {
        "components" : component,
        "bugs" : bugs
    }

    print(graph_data)

    gdf = pd.DataFrame(graph_data, columns=["bugs", "components"])
    
    print(gdf)
    gdf.plot(x ="components", y="bugs", kind = 'bar')
    plt.show()



choice = int(input("1 - bugs per monyh; 2 - testers; 3 - analytics. = "))

if choice == 1:
    graph_time(df)
elif choice ==2:
    graph_testers(df)
else:
    graph_analytics(df)