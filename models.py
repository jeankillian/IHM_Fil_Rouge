import datetime
from peewee import *
import os
import json
# -------------------------------Sauvegarde des données-----------------------


mysql_db = MySQLDatabase('filrouge', user='Dodo', password='Dorian26000.',
                         host='localhost', port=3306)


class BaseModel(Model):
    class Meta:
        database = mysql_db


class GameServers(BaseModel):

    nom = CharField(unique=True)
    adresse_ip = CharField(unique=True)
    jeu = CharField()

    def __str__(self):
        return self.nom

    def record_data(self, Data_obj):
        pass

    @classmethod
    def liste_serveur(cls):
        """
            :parameter: class
            :return: une liste, contenant un objet python par enregistrement dans la table (correspond a l'enregistrement).
        """

        return cls.select()


class ReceivedMessage(BaseModel):

    msg_id = IntegerField()
    machine = ForeignKeyField(GameServers, backref='machin_id')
    created_date = DateTimeField(default=datetime.datetime.now)
    message = TextField()

    def __str__(self):
        return self.machine.nom + " " + str(self.msg_id) + " "+ self.message

    @classmethod
    def liste_msg_per_marchine(cls, machine_name):
        """
            :parameter: class + str(Le nom de la machine)
            :return: une liste, contenant un objet python par enregistrement lié a la machine "server_name"
            dans la table ReceivedMessage.
        """
        return cls.select().join(GameServers).order_by(cls.created_date).where(GameServers.nom == machine_name)

    @classmethod
    def record_data(cls, data_obj):
        """
            :parameter: (type: Class/Objet) class + Data_obj (instance de la class Data)
            Fait un "get or create" des attributs ciblés de Data_obj (créer un enregistrement dans la base
            :returns:   (type : Objet) retourne objet Query avec les attributs présents dans les param de get_or_create
                        (type : boolean) retourne Vrai si enregistrement, sinon Faux
         """
        gs, created = cls.get_or_create(msg_id=data_obj.msg_id, machine=data_obj.machine,
                                        message=data_obj.msgsaved)
        return gs, created


class StatsPerMatch(BaseModel):

    machine = ForeignKeyField(GameServers, backref='machin_id')
    start_time = DateTimeField()
    game_time = IntegerField()
    winner = CharField()

    @classmethod
    def record_data(cls, data_obj):

        """
            :parameter: (type: Class/Objet) class + Data_obj (instance de la class Data)
            Fait un "get or create" des attributs ciblés de Data_obj (créer un enregistrement dans la base
            :returns:   (type : Objet) retourne objet Query avec les attributs présents dans les param de get_or_create
                        (type : boolean) retourne Vrai si enregistrement, sinon Faux
        """

        gs, created = cls.get_or_create(machine=data_obj.machine, start_time=data_obj.start_time,
                                        game_time=data_obj.get_game_duration(), winner=data_obj.get_winner())
        return gs, created


class StatsPerDay(BaseModel):

    machine = ForeignKeyField(GameServers, backref='machin_id')
    date = DateField()
    nb_partie = IntegerField()
    moyenne_partie = IntegerField()
    win_count_joueur1 = IntegerField()
    win_count_joueur2 = IntegerField()
    draw_count = IntegerField()

    @classmethod
    def liste_stat_per_marchine(cls):
        pass


# ----------------------------------------Traitement des données-------------------------------


class Data:
    """Récupère les données en format json et les transforme en objet"""

    def __init__(self, json_formatted_string):
        """
            :parameter: String de donnée formater en json (!!!!contenant un dict!!!)
            :return : (type: objet) un objet avec comme attribut chaque "key/value" du "dict" extrait des données
        """

        data = json.loads(json_formatted_string)
        self.msg_type = data["Msg type"]                                                    # str
        self.msg_id = data["Msg ID"]                                                        # int
        self.machine = GameServers.get(GameServers.nom == data["Machine name"])             # Obj
        self.jeu = data["Game type"]                                                        # int or str
        self.start_time = datetime.datetime.strptime(data["Start time"], "%d/%m/%y %H:%M")  # datetime
        self.end_time = datetime.datetime.strptime(data["End time"], "%d/%m/%y %H:%M")      # datetime
        self.winner = data["Winner"]                                                        # str
        self.msgsaved = json_formatted_string                                               # str

    def get_day(self):
        """
            :return:(type: datetime) la valeur de l'attribut start_time tronqué avec uniquement la date
        """

        return self.start_time.date()

    def get_game_duration(self):
        """
            :return: (type: datetime) le resultat de la soustraction de l'attrbut "end_time" par "start_time" en seconde
        """

        return (self.end_time - self.start_time).total_seconds()

    def get_winner(self):
        """
            :return: (type: str)la valeur de l'attribut "winner" habillé avec une phrase
        """

        return "And the winner is " + self.winner

# A FINIR-------------------------------------------------------------------------------------------------------

    def get_stat_per_day(self):

        try:

            stat = StatsPerDay.get(StatsPerDay.machine_id == self.machine,
                                   StatsPerDay.msg_id == datetime.datetime.now.date())
# FAIRE TRAITEMENT ET REMPOLACEMENT DE LA LIGNE EXISTANTE"""
        except IndexError:

            if self.winner == "joueur1":
                StatsPerDay.create(machine_id=self.machine, date=self.get_day(), nb_partie=1,
                                   moyenne_partie=self.get_game_duration, win_count_joueur1=1)
            elif self.winner == "joueur2":
                StatsPerDay.create(machine_id=self.machine, date=self.get_day(), nb_partie=1,
                                   moyenne_partie=self.get_game_duration, win_count_joueur2=1)
            else:
                StatsPerDay.create(machine_id=self.machine, date=self.get_day(), nb_partie=1,
                                   moyenne_partie=self.get_game_duration, draw_count=1)

# ------------------------------------------------------------------------------------------------------------------
