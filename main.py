import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pymongo import MongoClient

# Charger les données
@st.cache_data
def load_data():
    client = MongoClient(
        "mongodb+srv://batman:jesuisbatman@bdd-cours-mongo.qbpym7c.mongodb.net/?retryWrites=true&w=majority")
    cursor = client['IPSSI']['Flights']
    # pour faire un random sur la bdd
    # data = cursor.aggregate([{'$sample': {'size': 10000}}])
    data = cursor.find().limit(100000)
    df = pd.DataFrame(data)
    return df

df = load_data()

def plot_histogram(data, title, x_label, y_label='Nombre de Vols'):
    plt.figure(figsize=(10, 6))
    sns.histplot(data, bins=30)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)


def plot_bar_chart(data, x, y, title):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x, y=y, data=data)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)


# Application Streamlit
st.title('Analyse des Données de Vols des USA sur l\'Année 2015')

# Choix de l'analyse à afficher
analysis_option = st.sidebar.selectbox(
    'Choisir un théme:',
    ('Retards de Vol', 'Performance des Compagnies Aériennes',
     'Trafic Aéroportuaire', 'Durée et Distance des Vols', 'Tendances Temporelles', 'About')
)

# Analyse des Retards de Vol
if analysis_option == 'Retards de Vol':
    st.header('Retards de Vol')
    delay_option = st.selectbox(
        'Choisissez le type de retard:',
        ('Retard au Départ', 'Retard à l\'Arrivée')
    )
    if delay_option == 'Retard au Départ':
        st.header('Retards de Départ')
        plot_histogram(df['DEPARTURE_DELAY'].dropna(),
                       'Retards au Départ', 'Retard (minutes)')
    else:
        plot_histogram(df['ARRIVAL_DELAY'].dropna(),
                       'Retards à l\'Arrivée', 'Retard (minutes)')
    st.pyplot(plt)

# Performance des Compagnies Aériennes
elif analysis_option == 'Performance des Compagnies Aériennes':
    st.header('Performance des Compagnies Aériennes')
    # Calcul de la ponctualité moyenne pour chaque compagnie aérienne
    avg_delay_by_airline = df.groupby(
        'AIRLINE')['DEPARTURE_DELAY'].mean().reset_index()
    plot_bar_chart(avg_delay_by_airline, 'AIRLINE', 'DEPARTURE_DELAY',
                   'Ponctualité Moyenne par Compagnie Aérienne')
    st.pyplot(plt)

# Trafic Aéroportuaire
elif analysis_option == 'Trafic Aéroportuaire':
    st.header('Trafic Aéroportuaire')
    # Nombre de vols par aéroport d'origine
    flights_by_origin = df['ORIGIN_AIRPORT'].value_counts().reset_index()
    flights_by_origin.columns = ['ORIGIN_AIRPORT', 'NUMBER_OF_FLIGHTS']
    plot_bar_chart(flights_by_origin.head(14), 'ORIGIN_AIRPORT',
                   'NUMBER_OF_FLIGHTS', 'Top 14 des Aéroports d\'Origine par Nombre de Vols')
    st.pyplot(plt)

    # Nombre de vols par aéroport de destination
    flights_by_destination = df['DESTINATION_AIRPORT'].value_counts(
    ).reset_index()
    flights_by_destination.columns = [
        'DESTINATION_AIRPORT', 'NUMBER_OF_FLIGHTS']
    plot_bar_chart(flights_by_destination.head(14), 'DESTINATION_AIRPORT',
                   'NUMBER_OF_FLIGHTS', 'Top 14 des Aéroports de Destination par Nombre de Vols')
    st.pyplot(plt)

# Durée et Distance des Vols
elif analysis_option == 'Durée et Distance des Vols':
    st.header('Durée et Distance des Vols')
    plt.figure(figsize=(10, 6))

    sns.scatterplot(data=df, x='DISTANCE', y='ELAPSED_TIME',
                    hue='AIRLINE', alpha=0.5)
    plt.xlabel('Distance')
    plt.ylabel('Durée Totale du Vol')
    plt.title('Relation entre la Distance et la Durée des Vols')
    plt.legend(title='Compagnie Aérienne', bbox_to_anchor=(1.05, 1),
               loc='upper left')  # Légende à droite du graphique
    st.pyplot(plt)


# Tendances Temporelles
elif analysis_option == 'Tendances Temporelles':
    st.header('Tendances Temporelles')
    # Nombre de vols par mois avec la colonnes DATES (1/01/2015)
    df['DATES'] = pd.to_datetime(df['DATES'])
    flights_by_month = df['DATES'].dt.month.value_counts().reset_index()
    flights_by_month.columns = ['MONTH', 'NUMBER_OF_FLIGHTS']
    flights_by_month = flights_by_month.sort_values('MONTH')
    plot_bar_chart(flights_by_month, 'MONTH', 'NUMBER_OF_FLIGHTS',
                   'Nombre de Vols par Mois')
    st.pyplot(plt)


# About 
elif analysis_option == 'About':
    st.header('Au sujet du projet')
    st.subheader('Objectif', divider='rainbow')
    st.markdown("""
Ce projet manipule les données en utlisant la base de données mongoDB via Atlas , ce projet a pour objectif d'effectuer une analyse détaillée des différentes performances des compagnies aériennes : 
- Quelles compagnies aériennes sont les plus ponctuelles ?
- Quelles sont les principales causes de retards pour chaque compagnie ?
- Quelles compagnies aériennes sont les plus ponctuelles ?
- Combien de vols présentant des retards?
- Quelles sont les principales causes de retards pour chaque compagnie ?
- Quel est le nombre total de vols pour chaque aéroport d'origine ?
- Quel est le nombre total de vols pour chaque aéroport de destination?
- Quelle est la durée moyenne des vols, et quelle est la distance moyenne parcourue par les avions ?
- Quel est le nombre de vols enregistrés chaque mois?   
donc nous avons choisi la dataset "flights" qui contient des informations relatives aux vols, avec des colonnes décrivant divers aspects de chaque vol ainsi que le csv des compagnies. """)
    st.subheader('Dataset', divider='rainbow')
    st.markdown(""" Lien pour télécharger la dataset : 
(https://www.kaggle.com/code/fabiendaniel/predicting-flight-delays-tutorial/input?select=flights.csv)
               
        """)

    st.subheader('Code source ', divider='rainbow')
    st.markdown(""" Github : 
(https://github.com/fatma-ops/Projet-Pro-final-NoSQL-et-Big-Data-)
               
        """)

    st.caption('Mourad SALHI , Enzo DAVAL , Fatma MOKRANI')







# Fermeture de la figure matplotlib
plt.close()
