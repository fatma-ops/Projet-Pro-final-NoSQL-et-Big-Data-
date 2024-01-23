# Projet-Pro-final-NoSQL-et-Big-Data-

# OBJECTIF

Ce projet manipule les données en utlisant la base de données mongoDB via Atlas , ce projet a pour objectif d'effectuer une analyse détaillée des différentes performances des compagnies aériennes : 
- Quelles compagnies aériennes sont les plus ponctuelles ?
- Quelles sont les principales causes de retards pour chaque compagnie ?
- 
donc nous avons choisi la dataset "flights" qui contient des informations relatives aux vols, avec des colonnes décrivant divers aspects de chaque vol ainsi que le csv des compagnies.

# DATASET 

## Lien pour télécharger le dataset: 
https://www.kaggle.com/code/fabiendaniel/predicting-flight-delays-tutorial/input?select=flights.csv

## Clean DATASET
- On commence de charger le fichier 'flights.csv'  dans un dataframe pandas
- Ensuite on établit une connexion avec la base de données , Notre dataset est caractérisé par sa taille massive . Lorsque nous travaillons avec des ensembles de données aussi importants, il est essentiel de tenir compte de la capacité de notre base de données MongoDB à absorber ces données de manière efficace. Afin d'optimiser le processus d'insertion des données dans MongoDB, nous avons ajusté le paramètre connectTimeoutMS lors de l'établissement de la connexion avec la base de données. En augmentant la durée du délai de connexion à 60 secondes, nous nous assurons que le client MongoDB dispose du temps nécessaire pour établir une connexion stable, même lorsque nous manipulons des quantités massives de données.
  
- Pour récupére chaque ligne sous forme de documents on transformer le dataframe en dictionnaire.
-  Ensuite on a Créez un connecteur vers une base de données que l'on appellera 'IPSSI' et une collection nommée 'Flights'
Listes  des colonnes utiles pour notre probléme ( Après avoir supprimé ce dont on n'a pas besoin et fusionner les colonnes YEAR , MONTH et DAY dans la colonne DATES) 

retrait des des valeurs abérentes ainsi que les NaN et autres valeurs non exploitable(avec le notebook)



DATES: la date du vol 
DAY_OF_WEEK: Jour de la semaine du vol (en chiffre).
AIRLINE: Code de l'entreprise aérienne.
FLIGHT_NUMBER: Numéro de vol.
TAIL_NUMBER: Numéro d'immatriculation de l'avion.
ORIGIN_AIRPORT: Code de l'aéroport de départ.
DESTINATION_AIRPORT: Code de l'aéroport de destination.
SCHEDULED_DEPARTURE: Heure de départ prévue.
DEPARTURE_TIME: Heure effective de départ.
DEPARTURE_DELAY: Retard au départ.
SCHEDULED_TIME: Temps de vol prévu.
ELAPSED_TIME: Temps de vol écoulé.
AIR_TIME: Temps de vol dans les airs.
DISTANCE: Distance du vol.
SCHEDULED_ARRIVAL: Heure d'arrivée prévue.
ARRIVAL_TIME: Heure d'arrivée effective.
ARRIVAL_DELAY: Retard à l'arrivée.
DIVERTED: Indicateur de déviation du vol.
CANCELLED: Indicateur d'annulation du vol.
CANCELLATION_REASON: Raison de l'annulation du vol.
AIR_SYSTEM_DELAY: Retard dû au système aérien.
SECURITY_DELAY: Retard dû à la sécurité.
AIRLINE_DELAY: Retard dû à l'entreprise aérienne.
LATE_AIRCRAFT_DELAY: Retard dû à l'avion.
WEATHER_DELAY: Retard dû aux conditions météorologiques.





# Guide pour utliser le script 



