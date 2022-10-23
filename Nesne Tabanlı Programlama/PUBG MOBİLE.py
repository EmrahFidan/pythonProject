import random
import time

class game():
    def __init__(self,game_state="on",map_list=["erangel"],map="erangel",game_mo=["team","single","dual"],game_mode="team",game_clothes=["bot"],clothes="bot",missions=[],events= 'the BLACKPİNK dropss have been played',UC= 0,silvercoin= 0,RP="not purchased",rank="diamond_2",number_of_likes=52,friends=[],number_of_friends=0,clan="BELİEVER",graph_selection="akıcı",sensitivity="medium",cross_color="white",language="english",merit_point=85):

        self.game_state = game_state
        self.map_list = map_list
        self.map = map
        self.game_mo = game_mo
        self.game_mode = game_mode
        self.game_clothes = game_clothes
        self.clothes = clothes
        self.missions = missions
        self.events = events
        self.UC = UC
        self.silvercoin = silvercoin
        self.RP = RP
        self.rank = rank
        self.number_of_likes = number_of_likes
        self.friends = friends
        self.number_of_friends = number_of_friends
        self.clan = clan
        self.graph_selection = graph_selection
        self.sensitivity = sensitivity
        self.cross_color = cross_color
        self.language = language
        self.merit_point = merit_point

    def game_open(self):
        if(self.game_state == "on"):
            print("already on..")
        else:
            print("is closing....")
            time.sleep(1)
            self.game_state ="off"
    def map_add(self,map_name):
        print("adding map....")
        time.sleep(1)
        self.map_list.append(map_name)
        print("map added..")
    def random_map(self):
        rastgele = random.randint(0,len(self.map_list)-1)
        self.map = self.map_list[rastgele]
        print("selected map= ",self.map)
    def random_mode(self):
        rastgele = random.randint(0, len(self.game_mo)-1)
        self.game_mode = self.game_mo[rastgele]
        print("selected mode= ",self.game_mode)
    def clothes_add(self,clothes_name):
        print("adding clothes....")
        time.sleep(1)
        self.game_clothes.append(clothes_name)
        print("clothes added..")
    def add_missions(self,mission):
        print("adding missions....")
        time.sleep(1)
        self.missions.append(mission)
        print("missions added..")
    def  read_events(self):
        print(self.events)
    def info_UC(self):
        print(self.UC)
    def info_silvercoin(self):
        print(self.silvercoin)
    def add_friends(self,friend):
        print("aadding friend....")
        time.sleep(1)
        self.friends.append(friend)
        print("friend added..")
    def __len__(self):
        return len(self.map_list)
        return len(self.game_mo)
    def __str__(self):
        return "game_state= {}\nmap_list= {}\nmap= {}\ngame_mo= {}\ngame_mode= {}\ngame_clothes= {}\nclothes= {}\nmissions= {}\nevents= {}\nUC= {}\nsilvercoin= {}\nRP= {}\nrank= {}\nnumber_of_likes= {}\nfriends= {}\nnumber_of_friends= {}\nclan= {}\ngraph_selection= {}\nsensitivity= {}\ncross_color= {}\nlanguage= {}\nmerit_point= {}\n".format(self.game_state,self.map_list,self.map,self.game_mo,self.game_mode,self.game_clothes,self.clothes,self.missions,self.events,self.UC,self.silvercoin,self.RP,self.rank,self.number_of_likes,self.friends,self.number_of_friends,self.clan,self.graph_selection,self.sensitivity,self.cross_color,self.language,self.merit_point)

pubg = game()

while True:
    user_id = input("enter user id: ")
    if (user_id == "12345"):
        print("welcome")
        break
    else:
        print("Entry was denied")
        continue

print("""
Pubg
    1 = play game
    2 = add map 
    3 = game mode
    4 = add clothes 
    5 = missions 
    6 = random map
    7 = education
    8 = take UC # oyun içi para 
    9 = lucky spin # gelen sayıya göre hediye verir (50 gümüş para,10 gümüş para,100 gümüş para)
    10= create # oyun için sandık (uc ye  ve gümüş paraya alınabilecek sandık çeşitleri)
    11= Royal Pass purchase # oyun içi görev - ödül mekanizması (oyuncu görev yaptıkça 5 gümüş para ver)
    12= player name and İD # oyundaki adını gösterir
    13 = popularity # oyuncunu beğeni sayısını göster
    14 = rank #oyundaki # rütben 
    15 = arkadaşlar # arkadaş listene bakabilirsin 
    16= clan # klan özellikleri (klan adı,ödülleri,seviyesi,klandaki oyuncu isimleri)
    17 = settings # oyun içi ayarları (şifre değiştirme, grafik seçimi,hassasiyet =(düşük,orta,yüksek),nişan rengi,dil değiştirme)
    18 = merit # liyakat puanı (diğer kullanıcılara saygı durumu)

""")
while True:
    x= input("select the operation: ")
    if(x == "q"):
        print("The program is shutting down....")
        break
    else:
        x = int(x)

        if(x == 1):
            pubg.game_open()
        elif (x == 2):
            add_names = input("please enter ',' with map names:")
            map_list = add_names.split(",")
            for i in map_list:
                pubg.map_add(i)
        elif (x == 3):
            pubg.random_mode()
        elif (x == 4):
            add_name = input("please enter ',' with clothes names:")
            game_clothes = add_name.split(",")
            for i in game_clothes:
                pubg.clothes_add(i)
        elif(x == 5):
            mission = input("eklemek istediğiniz görevi yazınız:")
            pubg.add_missions(mission)
        elif (x == 6):
            pubg.random_map()
        elif(x == 7):
            print(pubg)
        elif(x == 8):
            print(""""
            15= 60uc
            150= 660 uc
            1500= 8100 uc
            """)
            a=int(input("how much UC do you want:"))










