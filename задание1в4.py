class MedOsmotr:
    def __init__(self, namePol, adress, familiaPacienta, numberPolis,dateOsmotra,familiaVracha,doljnostVracha,diagnos):
        self.namePol = namePol
        self.adress = adress
        self.familiaPacienta = familiaPacienta
        self.numberPolis = numberPolis
        self.dateOsmotra = dateOsmotra
        self.familiaVracha = familiaVracha
        self.doljnostVracha = doljnostVracha
        self.diagnos = diagnos

    def info(self):
        print(f"Название поликлиники: {self.namePol}")
        print(f"Адрес: {self.adress}")
        print(f"Фамилия пациента: {self.familiaPacienta}")
        print(f"Номер полиса: {self.numberPolis}")
        print(f"Дата осмотра:{self.dateOsmotra}")
        print(f"Фамилия врача: {self.familiaVracha}")
        print(f"Должность врача: {self.doljnostVracha}")
        print(f"Диагнос: {self.diagnos}")

class PPO(MedOsmotr):
    def __init__(self, vid, yearProvedenia, periodDeistvia, result):
        super().__init__('Хорошая поликлиника','чикалово 11','Мишенков','32','01.01.2024','Печкин','хирург','сыпь')
        self.vid = vid
        self.yearProvedenia =yearProvedenia
        self.periodDeistvia = periodDeistvia
        self.result = result

    def info(self):
        super().info()
        print(f"Название зала: {self.vid}")
        print(f"Количество источников литературы: {self.yearProvedenia}")
        print(f"Этаж: {self.periodDeistvia}")
        print(f"Кабинет: {self.result}")
        print()

class Vakcinacia(MedOsmotr):
    def __init__(self,nameVakcini,dateVakcini,periodDeistvia):
        super().__init__('Хорошая поликлиника','чикалово 11','Мишенков','32','01.01.2024','Печкин','хирург','сыпь')
        self.nameVakcini = nameVakcini
        self.dateVakcini = dateVakcini
        self.periodDeistvia = periodDeistvia

    def info(self):
        super().info()
        print(f"Название вакцины: {self.nameVakcini}")
        print(f"Дата вакцинации: {self.dateVakcini}")
        print(f"Период действия: {self.periodDeistvia}")
        print()

class MDIP(MedOsmotr):
    def __init__(self, svidORoj, pol, year):
        super().__init__('Хорошая поликлиника','чикалово 11','Мишенков','32','01.01.2024','Печкин','хирург','сыпь')
        self.svidORoj = svidORoj
        self.pol = pol
        self.year = year

    def info(self):
        super().info()
        print(f"Возраст: {self.year}")
        print(f"Пол: {self.pol}")
        print(f"Свидетельство о рождении: {self.svidORoj}")
        print()


MedOsmotr = MedOsmotr('Хорошая поликлиника','чикалово 11','Мишенков','32','01.01.2024','Печкин','хирург','сыпь')
MedOsmotr.info()
print(' ')
PPO = PPO('амбулаторный','2016','1.5 года','сыпь')
PPO.info()
print(' ')
Vakcinacia = Vakcinacia('от вича','01.01.1999','1 год')
Vakcinacia.info()
print(' ')
MDIP = MDIP('мама свидетель','мужской','13')
MDIP.info()