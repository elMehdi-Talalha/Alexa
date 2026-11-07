    # ALEXA – ASSISTANT VOCAL POUR ORDINATEUR

    **Rapport de projet technique**

    **Réalisé par :** Mehdi Talalha  
    **Établissement :** Lycée Mehdi Ben Berka  
    **Année scolaire :** 2026–2027  
    **Date :** Novembre 2026

    ---

    # Table des matières

    1. Introduction
    2. Présentation du projet et objectifs
    3. Besoins fonctionnels et techniques
    4. Technologies utilisées
    5. Architecture et conception du système
    6. Réalisation et développement
    7. Tests et évaluation
    8. Conclusion
    9. Références

    ---

    # 1. Introduction

    Aujourd'hui, l'informatique occupe une place importante dans notre vie quotidienne. Pour utiliser un ordinateur, nous avons généralement besoin d'un clavier et d'une souris. Mais il existe aussi une autre façon de communiquer avec un ordinateur : utiliser la voix.

    C'est à partir de cette idée que j'ai décidé de développer **Alexa**, un assistant vocal pour ordinateur, en utilisant le langage de programmation Python.

    Le principe du projet est assez simple : l'utilisateur donne une commande vocale, le programme reconnaît les mots prononcés, puis il exécute l'action demandée. Par exemple, au lieu d'ouvrir un navigateur et de chercher YouTube manuellement, il suffit de dire : « Alexa, ouvre YouTube ».

    Pour réaliser ce projet, j'ai utilisé plusieurs bibliothèques Python. Chacune a un rôle précis, comme la reconnaissance vocale, la réponse avec une voix, l'ouverture des applications et le contrôle du clavier.

    Ce projet m'a aussi permis de mettre en pratique plusieurs notions de programmation que j'ai étudiées, notamment la programmation orientée objet, les conditions, les boucles et l'utilisation des bibliothèques externes.

    # 2. Présentation du projet et objectifs

    ## 2.1. Présentation générale

    **Alexa** est un assistant vocal pour ordinateur. Il permet d'effectuer certaines opérations sur un ordinateur simplement en utilisant la voix.

    Pour communiquer avec l'assistant, l'utilisateur doit commencer sa commande par le mot **« Alexa »**, puis donner une instruction.

    Voici quelques exemples de commandes :

    - « Alexa, ouvre YouTube. »
    - « Alexa, ouvre Visual Studio Code. »
    - « Alexa, ferme Chrome. »
    - « Alexa, lance la vidéo. »
    - « Alexa, mets la vidéo en pause. »
    - « Alexa, au revoir. »

    Après avoir reçu une commande, le programme analyse la phrase pour comprendre ce que l'utilisateur veut faire. Ensuite, il appelle la fonction correspondante et donne une réponse vocale pour informer l'utilisateur.

    ## 2.2. Objectifs du projet

    Au début du projet, je voulais créer une application pratique qui permet de faire certaines opérations sur un ordinateur sans utiliser constamment le clavier et la souris.

    J'ai donc choisi plusieurs objectifs :

    - **Commande vocale :** Permettre à l'utilisateur de communiquer avec son ordinateur grâce à la voix.
    - **Ouverture des sites web :** Accéder facilement à plusieurs sites Internet.
    - **Gestion des applications :** Ouvrir et fermer certaines applications.
    - **Contrôle des vidéos :** Lancer ou mettre en pause une vidéo avec une commande vocale.
    - **Réponses vocales :** Permettre à Alexa de répondre avec une voix au lieu d'afficher uniquement des messages.
    - **Gain de temps :** Réduire les étapes nécessaires pour effectuer certaines opérations.
    - **Amélioration future :** Garder une structure qui permet d'ajouter de nouvelles fonctionnalités.

    # 3. Besoins fonctionnels et techniques

    Avant de commencer le développement, j'ai identifié les principales opérations que l'assistant devait pouvoir effectuer.

    ## 3.1. Besoins fonctionnels

    Le tableau suivant présente les principales fonctionnalités de l'application.

    | FCT | Fonctionnalité | Description |
    |---|---|---|
    | F01 | Reconnaissance vocale | Capturer la voix de l'utilisateur et la convertir en texte. |
    | F02 | Mot d'activation | Vérifier que la commande commence par « Alexa ». |
    | F03 | Ouverture des sites web | Ouvrir des sites web dans le navigateur par défaut. |
    | F04 | Ouverture des applications | Lancer des applications à partir du menu Démarrer de Windows. |
    | F05 | Fermeture des applications | Trouver et arrêter certains processus en cours. |
    | F06 | Contrôle des vidéos | Lancer ou mettre en pause une vidéo avec le clavier. |
    | F07 | Réponses vocales | Répondre à l'utilisateur avec une voix générée par ordinateur. |
    | F08 | Aide | Présenter les commandes disponibles. |
    | F09 | Fermeture du programme | Arrêter l'assistant après une commande de sortie. |

    ## 3.2. Matériel nécessaire

    Pour utiliser l'application, il faut disposer du matériel suivant :

    - **Ordinateur :** Un ordinateur fonctionnant sous Windows.
    - **Microphone :** Pour enregistrer les commandes vocales.
    - **Haut-parleurs ou écouteurs :** Pour entendre les réponses d'Alexa.
    - **Connexion Internet :** Nécessaire pour la reconnaissance vocale en ligne.

    ## 3.3. Logiciels nécessaires

    Les logiciels nécessaires sont :

    - **Système d'exploitation :** Microsoft Windows.
    - **Langage de programmation :** Python 3.
    - **Bibliothèques :** SpeechRecognition, PyAutoGUI, pyttsx3 et psutil.
    - **Environnement de développement :** Un éditeur de code ou un IDE compatible avec Python.

    # 4. Technologies utilisées

    J'ai choisi Python pour réaliser ce projet, principalement parce qu'il est facile à utiliser et possède beaucoup de bibliothèques utiles pour l'automatisation et la communication avec le système.

    Au lieu de programmer toutes les fonctionnalités depuis le début, j'ai utilisé plusieurs bibliothèques. Chacune permet de réaliser une tâche particulière.

    ## 4.1. Pourquoi Python ?

    J'ai choisi Python pour plusieurs raisons :

    - **Syntaxe simple :** Le code est facile à lire et à comprendre.
    - **Plusieurs bibliothèques :** Python propose beaucoup d'outils pour la reconnaissance vocale et l'automatisation.
    - **Flexibilité :** Il permet d'utiliser différentes méthodes de programmation, comme la programmation orientée objet.
    - **Automatisation :** Il permet de contrôler certaines fonctions de l'ordinateur.

    ## 4.2. SpeechRecognition

    La première bibliothèque utilisée est **SpeechRecognition**, car le projet dépend principalement de la reconnaissance vocale.

    Elle permet de capturer la voix à l'aide d'un microphone et de transformer les paroles en texte.

    J'ai principalement utilisé deux fonctions :

    - `recognize_google()` : Envoie l'enregistrement au service de reconnaissance vocale de Google et retourne le texte reconnu.
    - `adjust_for_ambient_noise()` : Permet d'adapter le système au bruit présent dans l'environnement avant de commencer l'enregistrement.

    Par exemple, lorsque je dis « Alexa, ouvre YouTube », cette bibliothèque transforme ma voix en texte. Le reste du programme peut ensuite analyser cette commande.

    ## 4.3. PyAutoGUI

    **PyAutoGUI** est une bibliothèque Python qui permet de contrôler automatiquement le clavier et la souris.

    Dans mon projet, je l'utilise principalement pour :

    - Ouvrir des applications à partir du menu Démarrer de Windows.
    - Simuler des touches du clavier.
    - Contrôler les vidéos avec la barre d'espace.

    Voici un exemple du code utilisé :

    ```python
    pyautogui.press('win')
    pyautogui.write(app_name, interval=0.05)
    pyautogui.press('enter')
    ```

    Le programme appuie sur la touche Windows, écrit le nom de l'application, puis appuie sur Entrée.

    ## 4.4. pyttsx3

    Je ne voulais pas qu'Alexa communique uniquement avec des messages affichés dans le terminal. Je voulais aussi qu'elle puisse répondre avec une voix.

    Pour cela, j'ai utilisé **pyttsx3**.

    Cette bibliothèque permet de transformer un texte en parole. Elle donne donc à Alexa la possibilité de répondre vocalement à l'utilisateur.

    Elle permet aussi de modifier certains paramètres :

    - **Voix :** Choisir une voix disponible sur l'ordinateur.
    - **Vitesse :** Modifier la vitesse de parole.
    - **Volume :** Régler le volume de la voix.

    ## 4.5. Webbrowser

    Le module `webbrowser` fait partie des bibliothèques intégrées de Python. Il n'est donc pas nécessaire de l'installer séparément.

    Je l'ai utilisé pour ouvrir des sites web avec le navigateur par défaut de l'ordinateur.

    Par exemple, si l'utilisateur demande à Alexa d'ouvrir YouTube, le programme cherche l'adresse du site et demande au navigateur de l'ouvrir.

    ## 4.6. psutil

    J'ai également utilisé **psutil** pour permettre à Alexa de fermer certaines applications.

    Cette bibliothèque donne des informations sur les processus qui fonctionnent sur l'ordinateur.

    Le programme cherche le processus correspondant à l'application demandée. S'il le trouve, il essaie de l'arrêter.

    Par exemple, Google Chrome utilise généralement le nom de processus `chrome.exe`.

    ## 4.7. subprocess et os

    J'ai aussi importé les modules `subprocess` et `os`.

    Ces deux modules font partie de Python. Ils permettent d'effectuer différentes opérations liées au système d'exploitation.

    Cependant, même s'ils sont importés dans le projet, ils ne sont pas directement utilisés dans la version actuelle de l'application.

    # 5. Architecture et conception du système

    Avant de commencer à écrire les différentes fonctions, je devais réfléchir à la manière dont les différentes parties de l'application allaient fonctionner ensemble.

    J'ai choisi d'organiser le projet autour d'une classe principale appelée `AlexaAssistant`. Cela permet de regrouper les différentes opérations au même endroit au lieu de mettre tout le code dans un seul bloc.

    ## 5.1. Architecture générale

    Le fonctionnement de l'application suit plusieurs étapes.

    Tout commence lorsque l'utilisateur donne une commande vocale. Le microphone capture la voix, puis SpeechRecognition transforme l'enregistrement en texte.

    Ensuite, le programme vérifie si la phrase commence par le mot « Alexa ». Après cette vérification, il analyse la commande et appelle la fonction correspondante.

    Voici les principales étapes :

    1. L'utilisateur donne une commande vocale.
    2. Le microphone capture la voix.
    3. SpeechRecognition transforme la voix en texte.
    4. Le programme vérifie la présence du mot « Alexa » au début de la commande.
    5. Le programme analyse la commande.
    6. La fonction correspondante exécute l'action demandée.
    7. Alexa répond à l'utilisateur.

    **Figure 1 : Architecture générale de l'application**

    *[Insérer ici le schéma de l'architecture générale.]*

    ## 5.2. Structure de la classe

    J'ai utilisé la **programmation orientée objet (POO)** pour organiser le code.

    La classe principale s'appelle `AlexaAssistant`. Elle contient les méthodes responsables des différentes fonctionnalités de l'assistant.

    Voici les principales méthodes :

    | Méthode | Rôle |
    |---|---|
    | `__init__()` | Initialise le système de reconnaissance vocale et les paramètres de l'assistant. |
    | `speak()` | Permet à Alexa de répondre avec une voix. |
    | `listen()` | Enregistre et reconnaît les commandes vocales. |
    | `control_video()` | Gère les commandes de lecture vidéo. |
    | `open_website()` | Ouvre un site web dans le navigateur. |
    | `open_application()` | Lance une application sur l'ordinateur. |
    | `close_application()` | Essaie de fermer une application en cours d'exécution. |
    | `process_command()` | Analyse les commandes et choisit l'action à effectuer. |
    | `run()` | Lance l'assistant et le garde en fonctionnement. |

    J'ai trouvé cette organisation pratique, car chaque méthode possède un rôle précis. Par exemple, si je veux modifier la manière dont Alexa ouvre les sites web, je peux travailler directement sur la méthode concernée sans modifier toute l'application.

    ## 5.3. Traitement des commandes

    Reconnaître la voix n'est qu'une partie du travail. Le programme doit aussi comprendre ce que l'utilisateur veut faire.

    Pour cela, j'ai utilisé des conditions comme `if`, `elif` et `else`.

    Le programme analyse la phrase reconnue et la compare avec plusieurs conditions déjà définies.

    Par exemple :

    - **Commandes de fermeture :** Si la phrase contient le mot « close », le programme cherche l'application à fermer.
    - **Commandes d'ouverture :** Si la phrase contient le mot « open », Alexa vérifie si le nom demandé existe dans le dictionnaire des sites web.
    - **Ouverture d'applications :** Si le nom n'existe pas dans le dictionnaire des sites web, le programme essaie de l'ouvrir comme une application.
    - **Autres commandes :** Le programme vérifie également les commandes liées aux vidéos, à l'aide et à la fermeture de l'assistant.

    Cette méthode est assez simple, mais elle répond aux besoins de la version actuelle du projet.

    # 6. Réalisation et développement

    Après avoir préparé la structure générale, j'ai commencé à développer les différentes fonctionnalités de l'assistant.

    J'ai travaillé sur chaque partie séparément, puis je les ai reliées avec la méthode de traitement des commandes.

    ## 6.1. Initialisation de l'assistant

    La première étape était de préparer l'assistant et de définir les paramètres de la reconnaissance vocale.

    Pour cela, j'ai utilisé la méthode `__init__()`.

    ```python
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        self.video_playing = False
    ```

    Voici le rôle des principaux paramètres :

    - **`energy_threshold` :** Définit le niveau sonore nécessaire pour détecter une voix.
    - **`dynamic_energy_threshold` :** Permet au système de s'adapter aux changements de bruit dans l'environnement.
    - **`pause_threshold` :** Définit la durée du silence avant que le programme considère que la phrase est terminée.
    - **`video_playing` :** Une variable qui permet de garder un état de lecture de la vidéo.

    Ces paramètres préparent l'assistant avant qu'il commence à écouter les commandes.

    ## 6.2. Reconnaissance vocale

    Après l'initialisation, j'ai travaillé sur la fonction d'écoute.

    Son objectif est de capturer la voix de l'utilisateur et de la transformer en texte.

    ```python
    with sr.Microphone() as source:
        self.recognizer.adjust_for_ambient_noise(
            source, duration=1
        )

        audio = self.recognizer.listen(
            source, timeout=8, phrase_time_limit=10
        )

        command = self.recognizer.recognize_google(
            audio, language='en-US'
        ).lower()
    ```

    D'abord, le programme accède au microphone et adapte le système au bruit présent dans l'environnement.

    Ensuite, il enregistre la voix de l'utilisateur. Une fois l'enregistrement terminé, la fonction `recognize_google()` envoie l'audio au service de reconnaissance de Google et récupère la phrase reconnue.

    J'ai aussi utilisé `lower()` pour transformer tous les caractères en minuscules. Cela facilite la comparaison des commandes, car le programme ne fait plus de différence entre les majuscules et les minuscules.

    J'ai également ajouté des exceptions pour gérer les problèmes possibles, par exemple lorsque le microphone ne capte pas correctement la voix ou lorsque le service ne comprend pas la phrase.

    ## 6.3. Faire parler Alexa

    Je voulais qu'Alexa puisse répondre à l'utilisateur après avoir reçu une commande.

    Par exemple, si je lui demande d'ouvrir un site web, elle doit pouvoir confirmer son action avec une réponse vocale.

    Pour réaliser cette fonctionnalité, j'ai utilisé la bibliothèque `pyttsx3` dans la méthode `speak()`.

    ```python
    def speak(self, text):
        print(f"Alexa: {text}")

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)

        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)

        engine.say(text)
        engine.runAndWait()
        engine.stop()
    ```

    La méthode reçoit un texte et le transforme en parole.

    J'ai aussi modifié quelques paramètres :

    - **Choix de la voix :** Le programme sélectionne la deuxième voix disponible si l'ordinateur en possède plusieurs.
    - **Vitesse :** La vitesse de parole est réglée sur 170.
    - **Volume :** Le volume est réglé sur 1.0.

    La réponse est également affichée dans le terminal. Cela permet de voir le message qu'Alexa prononce.

    ## 6.4. Ouverture des sites web

    L'une des premières fonctionnalités pratiques que je voulais ajouter était l'ouverture des sites web avec des commandes vocales.

    Pour cela, j'ai créé un dictionnaire qui contient les noms des sites web et leurs adresses.

    ```python
    websites = {
        "google": "google.com",
        "youtube": "youtube.com",
        "facebook": "facebook.com",
        "instagram": "instagram.com",
        "amazon": "amazon.com",
        "gmail": "gmail.com",
        "chatgpt": "chatgpt.com",
        "claude": "claude.ai",
        "spotify": "spotify.com",
        "github": "github.com"
    }
    ```

    Lorsque Alexa reçoit une commande comme « ouvre YouTube », le programme cherche le nom du site dans ce dictionnaire.

    Si le site existe, Alexa utilise la méthode `open_website()` avec le module `webbrowser` pour ouvrir la page correspondante.

    J'ai choisi cette méthode parce qu'elle permet d'ajouter facilement de nouveaux sites. Il suffit d'ajouter leur nom et leur adresse dans le dictionnaire.

    ## 6.5. Ouverture des applications

    L'ouverture d'une application est un peu différente de celle d'un site web.

    Pour cette fonctionnalité, je devais trouver une manière de faire communiquer Python avec Windows.

    J'ai donc utilisé PyAutoGUI pour simuler les actions qu'un utilisateur effectue normalement avec le menu Démarrer.

    ```python
    pyautogui.press('win')
    pyautogui.write(app_name, interval=0.05)
    pyautogui.press('enter')
    ```

    Le programme effectue trois actions :

    1. Il appuie sur la touche Windows.
    2. Il écrit le nom de l'application.
    3. Il appuie sur Entrée pour lancer l'application.

    Par exemple, lorsque je dis « Alexa, ouvre Visual Studio Code », le programme cherche l'application dans le menu Démarrer et essaie de la lancer.

    ## 6.6. Fermeture des applications

    J'ai aussi ajouté une fonctionnalité qui permet à Alexa de fermer certaines applications.

    Pour cette partie, j'ai utilisé la bibliothèque `psutil`.

    D'abord, j'ai créé un dictionnaire qui relie les noms des applications aux noms de leurs processus.

    ```python
    process_map = {
        "chrome": "chrome.exe",
        "notepad": "notepad.exe",
        "discord": "discord.exe",
        "vscode": "code.exe",
        "spotify": "spotify.exe"
    }
    ```

    Ensuite, le programme cherche dans la liste des processus en cours pour trouver l'application demandée.

    S'il trouve une correspondance, il essaie d'arrêter le processus avec la méthode `kill()`.

    Si l'application n'est pas ouverte ou si l'opération échoue, Alexa informe l'utilisateur.

    Il faut aussi noter que cette méthode peut fermer une application sans donner à l'utilisateur le temps d'enregistrer son travail.

    ## 6.7. Contrôle des vidéos

    Une autre fonctionnalité que j'ai ajoutée est le contrôle des vidéos avec des commandes vocales.

    Pour cela, j'ai utilisé PyAutoGUI afin de simuler l'appui sur la barre d'espace.

    ```python
    if action == "play" or action == "start":
        pyautogui.press('space')
        self.video_playing = True
        self.speak("Playing video")

    elif action == "pause" or action == "stop":
        pyautogui.press('space')
        self.video_playing = False
        self.speak("Video paused")
    ```

    Sur plusieurs plateformes vidéo, la barre d'espace permet de lancer ou de mettre une vidéo en pause.

    Au lieu de contrôler directement le lecteur vidéo, Alexa envoie cette commande au clavier à la fenêtre active.

    J'ai également ajouté la variable `video_playing` pour garder un état interne de la lecture.

    Cependant, cette méthode dépend de la fenêtre active. Si une autre application est sélectionnée, la barre d'espace peut avoir une autre fonction.

    ## 6.8. Traitement des commandes

    Après avoir développé les différentes fonctionnalités, je devais les relier entre elles.

    C'est le rôle de la méthode `process_command()`.

    Elle reçoit la phrase reconnue et analyse son contenu pour savoir quelle action effectuer.

    Avant de traiter la commande, le programme vérifie si elle commence par le mot d'activation.

    ```python
    if command is None:
        return True

    if not command.startswith("alexa"):
        print("Tip: Start your command with Alexa")
        return True

    command = command.replace("alexa", "").strip()
    ```

    Si aucune commande n'a été reconnue, la fonction retourne simplement une valeur.

    Si la phrase ne commence pas par « Alexa », le programme l'ignore et affiche un petit message pour rappeler à l'utilisateur d'utiliser le mot d'activation.

    Sinon, le programme supprime le mot « Alexa » et continue le traitement du reste de la phrase.

    Ensuite, il vérifie les différentes conditions pour trouver l'action demandée.

    Selon la commande reçue, Alexa peut :

    - Fermer une application.
    - Ouvrir un site web.
    - Lancer une application.
    - Lancer ou mettre en pause une vidéo.
    - Afficher les commandes disponibles.
    - Arrêter le programme.

    Si la commande ne correspond à aucune des conditions, Alexa informe l'utilisateur qu'elle n'a pas compris la demande.

    ## 6.9. Exécution principale

    La dernière partie est la méthode `run()`.

    Son rôle est de garder Alexa en fonctionnement au lieu d'exécuter une seule commande puis de s'arrêter.

    Pour cela, j'ai utilisé une boucle `while` qui permet à l'assistant d'écouter plusieurs commandes.

    Le fonctionnement est le suivant :

    1. L'assistant démarre.
    2. Il écoute une nouvelle commande.
    3. Il envoie la phrase reconnue à `process_command()`.
    4. Il exécute l'action demandée.
    5. Il recommence à écouter une nouvelle commande.

    La boucle continue jusqu'à ce que l'utilisateur donne une commande pour quitter le programme.

    Lorsque `process_command()` retourne `False`, la boucle s'arrête et Alexa termine son exécution.

    # 7. Tests et évaluation

    Après avoir développé les différentes fonctionnalités, il était nécessaire de vérifier si l'application fonctionnait comme prévu.

    J'ai préparé plusieurs cas de test pour vérifier les principales commandes d'Alexa.

    ## 7.1. Tests fonctionnels

    Le tableau suivant présente les tests prévus pour vérifier les fonctionnalités principales de l'application.

    | ID du test | Commande vocale | Résultat attendu |
    |---|---|---|
    | T01 | Alexa, ouvre YouTube | Ouvre YouTube dans le navigateur. |
    | T02 | Alexa, ouvre Google | Ouvre Google dans le navigateur. |
    | T03 | Alexa, ouvre Notepad | Lance Notepad. |
    | T04 | Alexa, ferme Chrome | Essaie de fermer Chrome. |
    | T05 | Alexa, lance la vidéo | Envoie la commande de la barre d'espace. |
    | T06 | Alexa, mets la vidéo en pause | Envoie la commande de la barre d'espace. |
    | T07 | Alexa, aide | Présente les commandes disponibles. |
    | T08 | Alexa, au revoir | Arrête l'assistant. |
    | T09 | Une commande non reconnue | Donne une réponse adaptée. |
    | T10 | Une commande sans Alexa | Ignore la commande. |

    Ces tests couvrent les principales fonctionnalités que je voulais ajouter au projet.

    Il reste à comparer les résultats attendus avec les résultats obtenus pendant l'exécution du programme. Cela permet de savoir quelles fonctionnalités fonctionnent correctement et lesquelles doivent encore être améliorées.

    ## 7.2. Gestion des erreurs

    Pendant le développement, j'ai également pensé aux problèmes qui peuvent apparaître lors de l'utilisation de l'application.

    Par exemple :

    - **Problème de reconnaissance vocale :** Le programme ne comprend pas la commande.
    - **Problème de microphone :** Le microphone n'est pas disponible ou ne fonctionne pas correctement.
    - **Application introuvable :** L'application demandée n'est pas en cours d'exécution.
    - **Erreur de fermeture :** Windows empêche l'arrêt d'un processus.

    Pour gérer ces situations, j'ai utilisé les instructions `try` et `except` de Python.

    Elles permettent de gérer certaines erreurs sans arrêter immédiatement tout le programme.

    ## 7.3. Limites du projet

    Même si l'application possède plusieurs fonctionnalités utiles, elle présente encore quelques limites.

    **1. Reconnaissance des commandes**

    Le système utilise des mots-clés déjà définis dans le code. Il ne peut donc pas comprendre toutes les façons possibles de donner une instruction.

    **2. Connexion Internet**

    La reconnaissance vocale dépend du service en ligne de Google. Une connexion Internet est donc nécessaire pour cette fonctionnalité.

    **3. Contrôle des vidéos**

    Le programme utilise la barre d'espace pour contrôler les vidéos. Son fonctionnement dépend de la fenêtre active et de la plateforme utilisée.

    **4. Fermeture des applications**

    L'utilisation de `psutil` peut arrêter une application sans laisser à l'utilisateur le temps d'enregistrer son travail.

    **5. Nombre d'applications limité**

    La version actuelle reconnaît seulement les sites web et les applications ajoutés dans les dictionnaires du programme.

    ## 7.4. Améliorations possibles

    Si je continue à développer ce projet, plusieurs améliorations pourraient être ajoutées.

    Par exemple :

    - **Interface graphique :** Ajouter une interface pour afficher l'état de l'assistant et les commandes disponibles.
    - **Reconnaissance vocale hors ligne :** Permettre à Alexa de reconnaître la voix sans connexion Internet.
    - **Plus d'applications :** Ajouter d'autres sites web et applications.
    - **Meilleure reconnaissance des commandes :** Permettre à Alexa de comprendre différentes expressions pour une même action.
    - **Plus de fonctionnalités :** Ajouter d'autres possibilités de contrôle de l'ordinateur.
    - **Interaction plus naturelle :** Améliorer la manière dont Alexa comprend les demandes de l'utilisateur.

    Ces améliorations pourraient rendre l'assistant plus complet et plus pratique à utiliser.

    # 8. Conclusion

    La réalisation de ce projet m'a permis de travailler sur une application pratique en utilisant le langage Python.

    Au départ, mon idée était simple : contrôler certaines fonctions de l'ordinateur avec ma voix. Pendant le développement, cette idée est devenue un assistant vocal capable de reconnaître des commandes, d'ouvrir des sites web, de lancer et de fermer certaines applications et de contrôler la lecture des vidéos.

    Ce que j'ai trouvé intéressant, c'est que chaque fonctionnalité demande une méthode différente. Par exemple, j'ai utilisé SpeechRecognition pour reconnaître les commandes, PyAutoGUI pour contrôler le clavier et psutil pour gérer les processus de l'ordinateur.

    Ce projet m'a également permis de mieux comprendre plusieurs notions de programmation, comme la programmation orientée objet, les conditions, les boucles et la gestion des erreurs.

    Bien sûr, l'assistant possède encore quelques limites. La reconnaissance des commandes reste simple et certaines fonctionnalités dépendent de la fenêtre active ou d'une connexion Internet. Il reste donc plusieurs améliorations possibles.

    Malgré cela, je suis satisfait du résultat obtenu. Ce travail m'a permis de mieux comprendre le fonctionnement de l'automatisation sur ordinateur et m'a donné envie d'explorer d'autres façons de communiquer avec les machines.

    # 9. Références

    Pendant la réalisation de ce projet, j'ai consulté les documentations suivantes :

    **1. Documentation Python :**

    https://docs.python.org/3/

    **2. SpeechRecognition – Bibliothèque Python :**

    https://pypi.org/project/SpeechRecognition/

    **3. Documentation PyAutoGUI :**

    https://pyautogui.readthedocs.io/

    **4. pyttsx3 – Bibliothèque Python :**

    https://pypi.org/project/pyttsx3/

    **5. Documentation psutil :**

    https://psutil.readthedocs.io/

    **6. Documentation Python Webbrowser :**

    https://docs.python.org/3/library/webbrowser.html

