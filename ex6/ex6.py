import pandas as pd

#python-database connection is database specific, so i will write the code without the connection part
columns=["Device_Type","Stats_Access_Link"]
rows=[["AXO145","<url>https://xcd32112.smart_meter.com</url>"],
	 ["TRU151","<url>http://tXh67.dia_meter.com</url>"]]
df=pd.DataFrame(rows,columns=columns)

def extractpurl(link):
	return link.split("//")[1].split("<")[0]

df["Pure_Url"]=df["Stats_Access_Link"].apply(extractpurl)

print(df["Pure_Url"])