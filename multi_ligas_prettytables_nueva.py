import urllib2, re
from bs4 import BeautifulSoup
import re
from prettytable import PrettyTable

# url that we are scraping
urls = ["http://www.espnfc.us/english-premier-league/23/table" , "http://www.espnfc.us/spanish-primera-division/15/table" , "http://www.espnfc.us/german-bundesliga/10/table" , "http://www.espnfc.us/italian-serie-a/12/table"]
hh = 0
for url in urls:
  page = urllib2.urlopen(url)

  soup = BeautifulSoup(page, "lxml")


  table = soup.find('table')

  rows = table.find_all('tr')

  results = []

  for row in rows:
        table_headers = row.find_all('th')
        if table_headers:
            results.append([headers.get_text() for headers in table_headers])

        table_data = row.find_all('td')
        if table_data:
	    results.append([data.get_text() for data in table_data])


  tabla_formateada = []

  
  equipo_nombre = []
  posicion_eq = []
  #Listas para totales
]
  Goles_Diferencia = []
  Puntos_tot = []


  i = 0
  for datos  in results:
  
    if i >= 2:
        while ( u'\xa0'  or u'\n' or u'' )  in datos:
            if (u'')  in datos :
                datos.remove(u'')
            elif  u'\n'  in datos:
	       datos.remove(u'\n')
	    elif  u'\xa0'  in datos:
	       datos.remove(u'\xa0')
	       
        
        
        
        tabla_formateada.append(datos)

    i += 1        


  
  for h in tabla_formateada:
   
      posicion = h[0]
      posicion_eq.append(posicion)
        
    
      equipo_nom = h[1]
      equipo_nom = equipo_nom.strip()
      equipo_nombre.append(equipo_nom)
        

      
  numero_items = len(posicion_eq)
   


  table = PrettyTable(["Posicion", "Equipo", "Puntos", "Dif_Gol"])
  i = 0
  
  for i in range(0,numero_items):
    
    table.add_row([posicion_eq[i], equipo_nombre[i], Goles_Diferencia[i] , Puntos_tot[i]])
    
    i += 1
  if hh == 0:
    print " "
    print " "

    print "                     Liga Premier"
  elif hh == 1:
    print "                     Liga BBVA"

  elif hh == 2:
    print "                     Bundesliga"

    
  elif hh == 3:
    print "                     Seie A"
    
  print table
  hh += 1
  print " "
  print " "



  
  
  