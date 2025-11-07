t1 = int(input("VVedite olimp: "))*4*365
t2 = int(input("vvedite god ot olimp: "))*365


date = -776*365 -181 + t1 + t2#начало осение приблизительно

print(date//365, date%365//30 +1)