1. L’approche distribué (micro services) n’a pas été si bénéfique dans leur cas, donc le chemin inverse a été pris : passer des micro-services à du monolithique.

2. Une réduction de coût de plus de 90%, avec une possibilité d’évolution du service et l’hébergement de milliers de stream

3. Video Quality Analysis (VQA) => L’équipe qui utilise de l’outil

4. Principalement pour une question financière, les micro services mis en place réduisaient la possibilité d’évolution de certains services et le coût de ces services à grande échelle aurait été trop important pour mettre en place cette solution.

5. Le management de l’orchestration et le « media converter »

6. Il a fallu d’abord régler le problème séparément les problèmes en réglant le problème de coût et d’augment leur capacités, puis une plus grosse décision qui a été de changer l’infrastructure.

7. 1 : Media converter : Converti les entrées audio / vidéo en drames et les envoie au Defect detectors
   2 : Defect detectors : Analyse et contrôle les anomalies des drames reçues
   3 : Orchestration : Contrôle les flux du service

8. Ce sont des applications utilisables sans avoir à gérer des serveurs, parfois des applications crées par d’autres entreprises qui les mettent à disposition

—

AWS

1. AWS Step functions : inspection de la qualité audio / vidéo (défect detectors ?)
2. EC2 : Permet de mettre en place autant de servers virutuels souhaités, configurer la sécurité et gérer le stockage.
3. ECS : Permet de déployer, faire évolution les applications conteneurisées
4. AWS Lambda : Suivre l’activité des streams en temps réel, analyse des cliques sur le contenu, analyse des réseaux sociaux
5. S3 : Permet de stocker les données de manières sécurisées, pouvant les optimiser, organiser, configurer les accès

Conclusion

Les architectures, (monolithiques ou micro services) ne conviennent pas à tous les projets, selon la taille et surtout l’utilisation.
Les micro services peuvent coûter beaucoup plus cher que le bénéfice qu’ils apportent
