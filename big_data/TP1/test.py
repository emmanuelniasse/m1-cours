## Lancer le fichier test.py
# `> python test.py`

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Créez une session Spark
spark = SparkSession.builder.appName("Exemple PySpark").getOrCreate()

# Chargez le fichier CSV fictif dans un DataFrame
df = spark.read.option("header", "true").csv("data.csv")

# Affichez le schéma du DataFrame
df.printSchema()

# Affichez les premières lignes du DataFrame
df.show()

# Filtrez les personnes dont l'âge est supérieur à 25 ans
filtered_df = df.filter(col("Âge") > 25)

# Calculez la moyenne des scores des personnes restantes
average_score = filtered_df.select("Score").agg({"Score": "avg"}).collect()[0][0]

# Affichez la moyenne des scores
print("Moyenne des scores des personnes de plus de 25 ans :", average_score)

# Enregistrez le DataFrame filtré dans un nouveau fichier CSV
filtered_df.write.csv("filtered_data.csv", header=True)

# Fermez la session Spark
spark.stop()
