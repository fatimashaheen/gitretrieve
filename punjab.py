import urllib2
import csv
import os
from datetime import datetime
from bs4 import BeautifulSoup

print("\n thanks for selecting punjab,please select the district:")
dis = ''
while dis != 'q':
       print("\n[1] Enter 1 for Amritsar")
       print("[2] Enter 2 for Barnala")
       print("[3] Enter 3 for Bhantida")
       print("[4] Enter 4 for Faridkot")
       print("[5] Enter 5 for Fatehgarh")
       print("[6] Enter 6 for Fazilka")
       print("[7] Enter 7 for Ferozpur")
       print("[8] Enter 8 for Gurdaspur")
       print("[9] Enter 9 for Hoshiarpur")
       print("[10] Enter 10 for jhalandar")
       print("[11] Enter 11 for Kapurthala")
       print("[12] Enter 12 for Ludhiana")
       print("[13] Enter 13 for Mansa")
       print("[14] Enter 14 for Moga")
       print("[15] Enter 15 for Mohali")
       print("[16] Enter 16 for Muktsar")
       print("[17] Enter 17 for Nawanshahr")
       print("[18] Enter 18 for Pathankot")
       print("[19] Enter 19 for Patiala")
       print("[20] Enter 20 for Ropar(Rupnagar)")
       print("[21] Enter 21 for Sangrur")
       print("[22] Enter 22 for Tarntaran")
       print("[q] Enter q to quit")

       dis = raw_input("Enter the district: ")
       if dis == '1':
          print("\n thanks for selecting Amritsar,please select the market")
          mar =''
          while mar !='q':
                print("\n [1]Enter 1 for Ajnala")
                print("\n[2] Enter 2 for Ajnala(Sudhar) ")
                print("[3] Enter 3 for Amritsar")
                print("[4] Enter 4 for Amritsar(Amritsar Mewa Mandi)")
                print("[5] Enter 5 for Amritsar(Chehreta)")
                print("[6] Enter 6 for Amritsar(Takharpura)")
                print("[7] Enter 7 for Attari")
                print("[8] Enter 8 for Chogawan")
                print("[9] Enter 9 for Gehri")
                print("[10] Enter 10 for Gehri(Jandiala Mandi")
                print("[11] Enter 11 for Majitha")
                print("[12]Enter 12 for Rayya")
                print("[13]Enter 13 for Rayya(Sathiala)")
            
                mar = raw_input("Enter the Market: ")
                if mar =='1':
                   print("the data will be retrieved soon: ")
                   frdate = raw_input("from which date do you want the data, dd-Mmm-yyyy")
                   todate = raw_input("till which date do you want the data, dd-Mmm-yyyy")
                   fdate = raw_input("enter again from which date do you want the data, dd-Mmm-yyyy")
                   tdate = raw_input("enter again till which date do you want the data, dd-Mmm-yyyy ")
                   myurl = "http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=PB&Tx_District=1&Tx_Market=623&DateFrom="+str(frdate)+"&DateTo="+str(todate)+"&Fr_Date="+str(fdate)+"&To_Date="+str(tdate)+"&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Punjab&Tx_DistrictHead=Amritsar&Tx_MarketHead=Ajnala"
                   print(myurl)

                   page = urllib2.urlopen(myurl)

                   soup = BeautifulSoup(page, 'html.parser')
                   potatodatasaved=""
                   for record in soup.findAll('tr'):
                       potatodata=""
                       for data in record.findAll('td'):
                           potatodata=potatodata+","+data.text.strip()
                       potatodatasaved = potatodatasaved + "\n" +potatodata[1:]
                   header="number,place,district,iteam,other,FAQ,minimum,maximum,modal,date"+"\n"
                   fi = open(os.path.expanduser("potato.csv"),"wb")
                   fi.write(header)
                   fi.write(potatodatasaved)
                   print "---------------------"
                   print potatodatasaved


                elif mar == '2':
                   print("The data will be retrieved soon: ")
                   frdate = raw_input("from which date do you want the data, dd-Mmm-yyyy")
                   todate = raw_input("till which date do you want the data, dd-Mmm-yyyy")
                   fdate = raw_input("enter again from which date do you want the data, dd-Mmm-yyyy")
                   tdate = raw_input("enter again till which date do you want the data, dd-Mmm-yyyy ")
                   myurl = "http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=PB&Tx_District=1&Tx_Market=4416&DateFrom="+frdate+"&DateTo="+todate+"&Fr_Date="+fdate+"&To_Date="+tdate+"&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Punjab&Tx_DistrictHead=Amritsar&Tx_MarketHead=Ajnala+(Sudhar)"
                   print(myurl)

                   page = urllib2.urlopen(myurl)

                   soup = BeautifulSoup(page, 'html.parser')
                   potatodatasaved=""
                   for record in soup.findAll('tr'):
                       potatodata=""
                       for data in record.findAll('td'):
                           potatodata=potatodata+","+data.text.strip()
                       potatodatasaved = potatodatasaved + "\n" +potatodata[1:]
                   header="number,place,district,iteam,other,FAQ,minimum,maximum,modal,date"+"\n"
                   fi = open(os.path.expanduser("potato.csv"),"wb")
                   fi.write(header)
                   fi.write(potatodatasaved)
                   print "---------------------"
                   print potatodatasaved


                elif mar == '3':
                   print("The will be retrieved soon: ")
                   frdate = raw_input("from which date do you want the data, dd-Mmm-yyyy")
                   todate = raw_input("till which date do you want the data, dd-Mmm-yyyy")
                   fdate = raw_input("enter again from which date do you want the data, dd-Mmm-yyyy")
                   tdate = raw_input("enter again till which date do you want the data, dd-Mmm-yyyy ")
                   myurl =' http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=PB&Tx_District=1&Tx_Market=226&DateFrom='+frdate+"&DateTo="+todate+"&Fr_Date="+fdate+"&To_Date="+tdate+"&Tx_Trend=2&Tx_CommodityHead=Potato&Tx_StateHead=Punjab&Tx_DistrictHead=Amritsar&Tx_MarketHead=Amritsar"
                   print(myurl)

                   page = urllib2.urlopen(myurl)

                   soup = BeautifulSoup(page, 'html.parser')
                   potatodatasaved=""
                   for record in soup.findAll('tr'):
                       potatodata=""
                       for data in record.findAll('td'):
                           potatodata=potatodata+","+data.text.strip()
                       potatodatasaved = potatodatasaved + "\n" +potatodata[1:]
                   header="number,place,district,iteam,other,FAQ,minimum,maximum,modal,date"+"\n"
                   fi = open(os.path.expanduser("potato.csv"),"wb")
                   fi.write(header)
                   fi.write(potatodatasaved)
                   print "---------------------"
                   print potatodatasaved
       

   
       elif dis == '2':
            print("\nthanks for selecting Barnala, please select the market")
            
       elif dis == '3':
            print("\n thanks for selecting Bhatinda, please select the market")
       elif dis == '4':
            print("\n thanks for selecting Faridkot, please select the market")
       elif dis == '5':
            print("\n thanks for selecting Fatehgarh, please select the market")
       elif dis == '6':
            print("\n thanks for selecting Fazilka, please select the market")
       elif dis == '7':
            print("\n thanks for selecting Ferozpur, please select the market")
       elif dis == '8':
            print("\n thanks for selecting Gurdaspur, please select the market")
       elif dis == '9':
            print("\n thanks for selecting Hoshiarpur, please select the market")
       elif dis == '10':
            print("\n thanks for selecting Jalandhar, please select the market")
       elif dis == '11':
            print("\n thanks for selecting Kapurthala, please select the market")
       elif dis == '12':
            print("\n thanks for selecting Ludhiana, please select the market")
       elif dis == '13':
            print("\n thanks for selecting Mansa, please select the market")
       elif dis == '14':
            print("\n thanks for selecting Moga, please select the market")
       elif dis == '15':
            print("\n thanks for selecting Mohali, please select the market")
       elif dis == '16':
            print("\n thanks for selecting Muktsar, please select the market")
       elif dis == '17':
            print("\n thanks for selecting Nawanshahr, please select the market")
       elif dis == '18':
            print("\n thanks for selecting Pathankot, please select the market")
       elif dis == '19':
            print("\n thanks for selecting Patiala, please select the market")
       elif dis == '20':
            print("\n thanks for selecting Ropar(Rupnagar), please select the market")
       elif dis == '21':
            print("\n thanks for selecting Sangrur, please select the market")
       elif dis == '22':
            print("\n thanks for selecting Tarntaran, please select the market")
       elif dis == 'q':
            print("\n thanks for visiting")
       else:
            print("\n You can only choose the districts above")
    
     
    
