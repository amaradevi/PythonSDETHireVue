#!/usr/bin/env python
import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def get_all_widgets(url,headers):
    print("url is "+url)
    response=requests.get(url,headers=at_headers,verify=False,timeout=60)
    if response.status_code==200:
        print(response.json())
        return response.json()
    elif response.status_code==400:
        print("get all widgets call failed ")
        return 400


def create_widget(url,headers,payload):
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code==201:
        print(response.json())
        widgetid = response.json()["widget_id"]
        print("Created widget with id: " + widgetid)
        return widgetid
        
    elif response.status_code==400:
        print("create widget operation failed")
        return 400


def getwidget(url,widgetid,at_headers):
    if widgetid=="":
        print("widget id is not sepcified.please specify the widget id")
        return
    else:
        get_url=url+widgetid
        print(get_url) 
    response=requests.get(get_url,headers=at_headers,verify=False)

    if response.status_code==200:
        print(response.json())
    elif response.status_code==400:
        print("specified widget is not exists")

    return response


def updatewidget(url,widgetid,at_headers,payload):
    if widgetid=="":
        print("widget id is not sepcified.please specify the widgetid")
        return
    else:
        update_url=url+str(widgetid)
        print(update_url)


    response=requests.patch(update_url,headers=at_headers,data=json.dumps(payload),verify=False)
    print(response.status_code)
    print(response.json())

    if response.status_code == 201:
        print("widget updation is successful")
        return 0
    elif response.status_code == 400:
        print("specified widget is not updated ")
        return 1




def delete_widget(url,widgetid,at_headers):
    delete_url=url+str(widgetid)
    print(delete_url)
    response=requests.delete(get_url,headers=at_headers,verify=False)
    if response.status_code == 204:
        print("widget deletion is successful")
        return 0
    elif response.status_code == 400:
        print("specified widget is not exists in rackspace")
        return 1



def main():
    
    url="https://dev.rackspace.example.com/widgets"

    token="xxxxxxxx"
    at_headers = {
                    "Content-Type": "application/json",
                    "X-Auth-Token": token
                 }

    payload = {
        
                 "widget_name": "Test Widget1",
                 "description": "This is Testwidget"
              }

    update_payload={
                "description": "A new description"
            }
    ###creation of new widget
    widgetid_or_code=create_widget(url,at_headers,payload)
    widget_id=""
    if widgetid_or_code != "400":
         print("created wiget id is:"+widgetid_or_code)
         widget_id=widgetid_or_code
         
    ###updation of widget with widegt_id got from POST response  
    update_code=updatewidget(url,widget_id,at_headers,updatepayload)
    
        
    ####Validation of updated widget in list of all widgets
    if update_code == "0":
        if ( get_all_widgets(url,at_headers) != "400" ):
            response_json=get_all_widgets(url,at_headers)
            if  any(x['widget_id'] == widget_id for x in response_json):
                print("widget with"+ widget_id  +"is updated and exists in list of widgets")
            else:
                print("widget with"+ widget_id  +"is not exists or timesout")
    
    ####deletion of widget
    if delete_widget(url,widget_id,at_headers) ==0:
        print("deletion of widegt is success")
    else :
        print("widegt is not exists to delete ")



if __name__=='__main__':
    main()

    
