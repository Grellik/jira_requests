import requests
import pandas as pd


# Метод для api запрос с jira и сохранения полученного файла в csv формате
def create_csv():
    # Тестовый автоматический запрос для последнего бага :
    #URL_REQ = "https://jira.atlassian.com/rest/api/2/search?maxResults=1&startAt=0&jql=project = JRASERVER AND resolution = Unresolved and type = Bug ORDER BY createdDate DESC"
    
    
    # Запрос с вводом пользавателя
    url = "https://jira.atlassian.com/rest/api/2/search?"
    maxResults = int(input("Max results = "))
    startAt = int(input("Start at = "))
    jql = "jql=project = JRASERVER AND resolution = Unresolved and type = Bug ORDER BY createdDate DESC"
    
    URL_REQ = url + "maxResults="+str(maxResults) + "&" + "startAt="+str(startAt) + "&" + jql
    
    r = requests.get(URL_REQ)
    
    # Status code :
    #print(r)
    


    # Создание датафрейма из нужных параметров
    data_json = r.json()

    l_key = []
    l_com = []
    l_rep = []
    l_cd = []
    l_up = []    
    
    for issue in data_json["issues"]:
        key = issue["key"]    
        #print(key)
        l_key.append(key)
    
        component = issue["fields"]["components"][0]["name"]
        #print(component)
        l_com.append(component)
    
        reporter = issue["fields"]["reporter"]["displayName"]
        #print(reporter)
        l_rep.append(reporter)
    
        creation_date = issue["fields"]["created"]
        #print(creation_date)
        l_cd.append(creation_date)
    
        update_date = issue["fields"]["updated"]
        #print(update_date)
        l_up.append(update_date)    

    data_graph = {
        "key" : l_key,
        "component" : l_com,
        "reporter" : l_rep,
        "creation date" : l_cd,
        "update date" : l_up
    }

    # Не забудьте поменять расположение файла для сохранение здесь и в graph.py (строки 191 и 204)!
    df = pd.DataFrame(data_graph,columns=["key", "component", "reporter", "creation date", "update date"])
    df.to_csv(r"C:\Users\danil\Documents\Work\jira_reqs\data_csv.csv",index=False)
