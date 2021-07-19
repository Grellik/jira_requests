from jira_reqs import *
import pandas as pd
import matplotlib.pyplot as plt


def graph_time(df):

    choice = int(input("1 - bugs in month, 2 - bugs in quarter. \n" \
        "? = "))

    # Отображение кол-ва багов каждый день в течении указанного месяца
    if choice == 1:

        month = int(input("month (as number) = "))
        year = int(input("year (as 4 digit number) ="))
        
        bug_num = []
        day_num = []
        bugs = 0
        
        # Поиск нужной даты начиная с самой поздней
        for index, row in df.iterrows():
            bugs = 0
            cd = row["creation date"].split("T")
            cd = cd[0].split("-")

            # Конец цикла как только он вышел за предел искомой даты, дабы не терять время при работе-
            #- с файлом большого обьема
            if year > int(cd[0]) or month > int(cd[1]):
                break

            # Сохранение каждого полученого бага и даты его получения в списки
            if year == int(cd[0]) and month == int(cd[1]):
                bugs += 1
            bug_num.append(bugs)
            day_num.append(str(cd[2]))
        
        # Реверс списков для отображения "прошлое" -> "будущее" по оси х
        day_num.reverse()
        bug_num.reverse()
        
        graph_data = {
            "bugs" : bug_num,
            "day" : day_num
        }
        
        # Создание датафрейма для графика
        gdf = pd.DataFrame(graph_data, columns=["bugs", "day"])
        # Если на один день приходится несколько багов, одни объеденяются в одну строку
        gdf = gdf.groupby("day").agg({"bugs":'sum'}).reset_index()
        
        gdf.plot(x ="day", y="bugs", kind = 'bar')
        plt.show()

    # Отображение кол-ва багов каждый день в течении указанного квартала
    else:

        quarter = int(input("quarter (1-4) = "))
        year = int(input("year (as 4 digit number) = "))
        if quarter == 1:
            month = [1,2,3]
        elif quarter == 2:
            month = [4,5,6]
        elif quarter == 3:
            month = [7,8,9]
        else:
            month = [10,11,12]
        
        bug_num = []
        day_num = []
        bugs = 0
        
        for index, row in df.iterrows():
            bugs = 0
            cd = row["creation date"].split("T")
            cd = cd[0].split("-")
            if year > int(cd[0]) and int(cd[1] not in month):
                break
            if year == int(cd[0]) and int(cd[1]) in month:
                bugs += 1
            bug_num.append(bugs)
            day_num.append(str(cd[1] + "-" + cd[2]))
        
        day_num.reverse()
        bug_num.reverse()
        
        graph_data = {
            "bugs" : bug_num,
            "day" : day_num
        }
        
        gdf = pd.DataFrame(graph_data, columns=["bugs", "day"])
        gdf = gdf.groupby("day").agg({"bugs":'sum'}).reset_index()
        
        gdf.plot(x ="day", y="bugs", kind = 'bar')
        plt.show()



# Последующие функции для создания графиков имеют схожую структуру
    
def graph_testers(df):

    names = {}

    quarter = int(input("quarter (1-4) = "))
    year = int(input("year (as 4 digit number) = "))
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
    
    gdf.plot(x ="name", y="bugs", kind = 'bar')
    plt.show()          

def graph_analytics(df):

    components = {}

    quarter = int(input("quarter (1-4) = "))
    year = int(input("year (as 4 digit number) = "))
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
    
    gdf.plot(x ="components", y="bugs", kind = 'bar')
    plt.show()

  
choice = None
# Не забудьте поменять путь к сейву здесь (строка 191 и 204) и на строке 65 в jira_reqs)
df = pd.read_csv(r"C:\Users\danil\Documents\Work\jira_reqs\data_csv.csv",engine="python")


# Меню выбора действий
while choice !=0:
    if choice == 1:
        graph_time(df)
    elif choice == 2:
        graph_testers(df)
    elif choice == 3:
        graph_analytics(df)
    elif choice == 4:
        create_csv()
        df = pd.read_csv(r"C:\Users\danil\Documents\Work\jira_reqs\data_csv.csv",engine="python")
        print("new data ", df)

    choice = int(input("1 - graph showing amount of bugs in month/quarter \n" \
    "2 - graph showing amount of bugs found by reporters in quarter \n" \
    "3 - graph showing most problematic component in chosen quarter \n" \
    "4 - update and load data \n" \
    "0 - exit \n" \
    "? = "))
