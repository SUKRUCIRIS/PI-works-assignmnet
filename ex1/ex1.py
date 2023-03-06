import pandas as pd
import matplotlib.pyplot as plt

columns=["Area of Interest","Charles","Henry","Susan"]
rows=[["Work",8.5,9.5,7],
      ["Family",0.5,1.0,1.5],
     ["Homeworks",3,2,1],
     ["Individual",1,1.5,2.5],
     ["Socializing",1.5,0.5,2],
     ["Spare Time",3,2.5,2],
     ["Sleep",6.5,7,8]]
df=pd.DataFrame(rows,columns=columns)

fig,ax=plt.subplots(figsize=(10,10))
colors={
    df["Area of Interest"][0] : plt.rcParams['axes.prop_cycle'].by_key()['color'][0],
    df["Area of Interest"][1] : plt.rcParams['axes.prop_cycle'].by_key()['color'][1],
    df["Area of Interest"][2] : plt.rcParams['axes.prop_cycle'].by_key()['color'][2],
    df["Area of Interest"][3] : plt.rcParams['axes.prop_cycle'].by_key()['color'][3],
    df["Area of Interest"][4] : plt.rcParams['axes.prop_cycle'].by_key()['color'][4],
    df["Area of Interest"][5] : plt.rcParams['axes.prop_cycle'].by_key()['color'][5],
    df["Area of Interest"][6] : plt.rcParams['axes.prop_cycle'].by_key()['color'][6]
}

ax.pie(df["Charles"],labels=list(df["Charles"]),labeldistance=0.85, rotatelabels =True, radius=1,
	wedgeprops=dict(width=0.3, edgecolor='w'),startangle = 45,
      colors=[colors[v] for v in df['Area of Interest'].value_counts().keys()],
	textprops = dict(va='center', ha='center'))
ax.pie(df["Henry"],labels=df["Henry"],labeldistance=0.75, rotatelabels =True,radius=0.7,
	wedgeprops=dict(width=0.3, edgecolor='w'),startangle = 45,
      colors=[colors[v] for v in df['Area of Interest'].value_counts().keys()],
	textprops = dict(va='center', ha='center'))
ax.pie(df["Susan"],labels=df["Susan"],labeldistance=0.65, rotatelabels =True,radius=0.4,
	wedgeprops=dict(width=0.3, edgecolor='w'),startangle = 45,
      colors=[colors[v] for v in df['Area of Interest'].value_counts().keys()],
	textprops = dict(va='center', ha='center'))

leg=ax.legend(colors.keys(),title="Color Legend",loc='lower right')

ax.legend(["Charles : Outer Pie","Henry : Middle Pie","Susan : Inner Pie"],title="Person Legend",loc='upper right', 
	   handlelength=0)

ax.add_artist(leg)

ax.set(aspect="equal", title='Multilayered Pie Chart (Şükrü Çiriş P.I. Works Assignment)')

plt.tight_layout()

plt.show()