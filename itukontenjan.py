 # coding=utf8
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import sys,time

url = "https://www.sis.itu.edu.tr/EN/student/course-schedules/course-schedules.php?seviye=LS&derskodu=EHB"
crns = sys.argv[1:]
print("[*]İzleme başlıyor...\n")
class donguKir(Exception): pass
try:
    while(True):
        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')
        liste = [el.text for el in soup.find_all('td')]
        for crn in crns:
            print("Ders adi: {0}\nDers hocasi: {1}\nAnlik kontenjan:{2}\n\n".format(liste[liste.index(str(crn))+2],liste[liste.index(str(crn))+3],85-int(liste[liste.index(str(crn))+9])))
            if(( 85 - int( liste[liste.index(crn)+9] )) != 0 ):
                print("bosluk var!")
                kontenjan = liste[liste.index(str(crn))+9]
                toaster = ToastNotifier()
                notification = "{0} Crn'li derste boşluk var. \n Anlık kontenjan: {1}".format(crn, 85-int(kontenjan))
                raise donguKir
            else:
                pass
    
        time.sleep(20)
except donguKir:
    pass


toaster.show_toast("Guncelleme:", notification)
