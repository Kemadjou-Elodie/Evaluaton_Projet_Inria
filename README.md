# Evaluaton_Projet_Inria

Ce fichier décrit les différents fichiers de mon repertoire.
Il comporte 4 fichiers, 2 fichiers de jupyter notebook et 2 programmes python (detect_duplicates_func.py et test_detect_duplicate.py)


### Description des programmes python 

1- La fonction Python "detect_duplicates" qui prend en parametère le dataframe "df_patient" et qui renvoit un nouveau dataframe 
après suppression des doublons. En faisant attention, aux données dupliquées qui ne sont pas identiques. Il comporte aussi 
des problèmes de saisies de données (typos, information manquante etc.)

Et j'estimere aussi le pourcentage de données dupliquées. En faisant toujours attention, aux données dupliquées qui ne sont pas identiques. 
Par exemple les problèmes de saisies de données (typos, information manquante etc.).

2- La fonction "test_detect_duplicate.py" qui teste la véricité de ma fonction précédente en se basant sur le pourcentage de données publiquées.


### Description des fichiers jupyter notebook

1- Le premier fichier met en exergue les problèmes d'incohérences sur le jeu de données, les données manquantes, etc...

2- Dans le second fichier, je fais la visualisation des données en faisant la jointure des deux tables du jeu de données, 
et je répresente la prévalence de la maladie dans la population en fonction des tranches d'age.

### La sortie des courbes 

###### Le nombre de test pcr effectué

![newplot(1)](https://user-images.githubusercontent.com/58962159/91657439-3232d000-eac1-11ea-946e-056fd580539b.png)

Cette courbe représente le nombre de test positif et négatif effectué dans toute la population.

###### Le nombre de personnes testées par ville

![newplot(2)](https://user-images.githubusercontent.com/58962159/91657553-21cf2500-eac2-11ea-8692-5896b93a0f28.png)

Ce graphe montre le nombre de personnes testées par état, l'état où on a effectué plus de test est "nsw" , nous allons voir s'il y a plus de personnes positif dans cette état.


##### L'état des tests effectués par ville 

![newplot(3)](https://user-images.githubusercontent.com/58962159/91657710-58f20600-eac3-11ea-817a-b041b1e81bd0.png)

On constate que l'état où on a effectué plus de tests pcr, les gens sont plus atteints du covid. Donc plus on effectue les tests, plus on a la possibilité de detecter les gens qui ont la maladie.

##### Le nombre de personnes testées par tranche d'âge

![newplot(4)](https://user-images.githubusercontent.com/58962159/91658070-68bf1980-eac6-11ea-937c-4e42ba8193d7.png)

On constate sur ce graphe que les gens de plus de 30 ans sont les plus contaminés et ont effectué beaucoup le test pcr
