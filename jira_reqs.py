import requests
import csv

def create_csv():
    # Тестовый автоматический запрос для последнего бага :
    #URL_REQ = "https://jira.atlassian.com/rest/api/2/search?maxResults=1&startAt=0&jql=project = JRASERVER AND resolution = Unresolved and type = Bug ORDER BY createdDate DESC"
    
    
    #Запрос с вводом пользавателя
    url = "https://jira.atlassian.com/rest/api/2/search?"
    maxResults = int(input("Max results = "))
    startAt = int(input("Start at = "))
    jql = "jql=project = JRASERVER AND resolution = Unresolved and type = Bug ORDER BY createdDate DESC"
    
    URL_REQ = url + "maxResults="+str(maxResults) + "&" + "startAt="+str(startAt) + "&" + jql
    
    r = requests.get(URL_REQ)
    
    # Status code :
    #print(r)
    
    data_json = r.json()
    header = ["key", "component", "reporter", "creation_date", "update_date"]
    rows = []
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
    
        row = [key, component, reporter, creation_date, update_date]
        rows.append(row) 
    
    with open(r"C:\Users\danil\Documents\Work\jira_reqs\data_csv.csv","w", encoding='UTF8', newline='') as f:
        write = csv.writer(f)
        write.writerow(header)
        write.writerows(rows)

    data_graph = {
        "key" : l_key,
        "component" : l_com,
        "reporter" : l_rep,
        "creation date" : l_cd,
        "update date" : l_up
    }

    return data_graph