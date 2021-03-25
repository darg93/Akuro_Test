import json
import requests.api
import random

def cats_facts_function ():

    fact = requests.get("https://cat-fact.herokuapp.com/facts")
    list_fact = json.loads(fact.text)

    return list_fact

    #print(list_fact[i]["text"])

def main():
    
    i=random.randint(0,4)
    list_fact=cats_facts_function()
    print(list_fact[i]["text"])
    
if __name__=="__main__":
    main()