
import logging as log
from time import gmtime, strftime
import module.movies_api_consumption as apirequest
import json
from sys import argv, exit
import flask




ts = gmtime()
datetime=strftime("%Y%m%d_%H%M%S", ts)

log.basicConfig(filename='logs/moviesapiconsumption_' + datetime + '.log',format='%(asctime)s %(levelname)-8s %(message)s',level=log.DEBUG,datefmt='%Y-%m-%d %H:%M:%S')




log.info("Mounting request string")
key='3a759be71aa9bae9de1e0621d0ef7f14'



#TODO: Receive parameter with sys.argv
# path = argv[1]
path='now_playing'


# In[4]:


response = apirequest.getapidata(path,key,log)
log.info("Executing API request")


# In[5]:


api_results = ""


# In[6]:


try:
    api_results = response.json()['results']
    if len(api_results) <= 0:
        system.exit(2) #dados não encontrados
except Exception as e:
    log.error("e")
    exit(99)


# In[7]:


api_results[0]


# In[ ]:




