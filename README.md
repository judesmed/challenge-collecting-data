# challenge-collecting-data
Team project BeCode

## Get_urls_function permet d'extraire toutes les urls assez rapidement (17000 en 15 minutes)
> Mettre en commentaire la 66ème ligne et uncomment la 65ème.

##
README immoweb :

1/ Extraction of the URLs. 

	- We used Selenium because URL was hidden in Java + in order to pass the cookie (RGPD).
	- To accelerate the extract, we used the command pool / starmap, which allows to run the scraping on several browsers at the same time.
	- We saved the extract of all pages URL on a Json file.

2/ Extraction of the data
	- We used requests for the speed
	- We used two sources (because some info are not classes). One from the URL (e.g. :  sub-type) and one from the page itself
	- we speed up the process with the map function
