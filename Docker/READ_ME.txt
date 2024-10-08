pour lancer le docker:

 ----    Lancé start_kicekifeqoa.exe    ----


si le start_kicekifeqoa.exe ne fonctionne pas, merci de passé en manuelle :

- avoir docker desktop installé sur son pc
- allé dans le fichier dédier ( dans le terminal taper : cd docker)

    - LES COMANDES POUR LE DOCKER

- si pas encore construit : docker build -t Kicekifeqoa .
- pour le lancer : docker run -d -p 5000:5000 Kicekifeqoa
- pour verifier le status du docker : docker ps
- pour le stoper : docker stop Kicekifeqoa
- si il faut le supprimer (au cas ou) ; docker rm Kicekifeqoa