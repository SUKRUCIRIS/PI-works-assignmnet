SELECT country_vaccination_stats.country, country_vaccination_stats.date, country_vaccination_stats.vaccines,
case when country_vaccination_stats.daily_vaccinations IS NULL then COALESCE(Y.daily_vaccinations,0) else country_vaccination_stats.daily_vaccinations end 
as daily_vaccinations FROM (SELECT X.country,AVG(X.daily_vaccinations) AS daily_vaccinations FROM (SELECT MAX(X.number) as number, X.country 
FROM (SELECT country_vaccination_stats.daily_vaccinations, COUNT(country_vaccination_stats.daily_vaccinations) AS number, country_vaccination_stats.country 
FROM country_vaccination_stats GROUP BY country_vaccination_stats.daily_vaccinations, country_vaccination_stats.country) AS X GROUP BY X.country) AS K 
LEFT JOIN X ON X.country=K.country AND X.number=K.number GROUP BY X.country) AS Y RIGHT JOIN country_vaccination_stats ON Y.country=country_vaccination_stats.country