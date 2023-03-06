import pandas as pd

def fillnawithmin(df):
	#get min values per country
	minrows=df.groupby("country",as_index=False).min()
	#get rows with nan value
	nanrows=df.loc[df["daily_vaccinations"].isna()].reset_index(drop=True)
	#fill nan rows
	nanrows=nanrows.merge(minrows[["country","daily_vaccinations"]],on="country",
		suffixes=('_x', '_y'),how="left").drop(columns=["daily_vaccinations_x"]).rename(
		columns={"daily_vaccinations_y":"daily_vaccinations"})
	#merge with main df as another column
	df=df.merge(nanrows[["country","daily_vaccinations","date"]],how="left",left_on=["country","date"],
		right_on=["country","date"],suffixes=('', '_y'))
	#replace nan values with the merged column
	df["daily_vaccinations"].fillna(df["daily_vaccinations_y"],inplace=True)
	#if there are still nan values, replace them with 0
	df["daily_vaccinations"].fillna(0,inplace=True)
	#drop the merged column and return the df
	return df.drop(columns=["daily_vaccinations_y"]).reset_index(drop=True)

df=pd.read_csv("country_vaccination_stats.csv")

df=fillnawithmin(df)

df2=df.groupby("date",as_index=False).sum(numeric_only=True)

print(df2.loc[df2["date"]=="1/6/2021"]["daily_vaccinations"].iloc[0])