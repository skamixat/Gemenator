from faker import Faker
import tkinter as tk
import customtkinter as ctk
import random
import kishbase
from PIL import Image

def generate_menu(knopka):
	global twoframe
	def generations():
		skolka = int(vvod.get())
		poletexta.delete("1.0", "250.25")

		fake = Faker (locale = 'ru_RU')
		if knopka == "Name":
			for _ in range(skolka):
				poletexta.insert("1.0", (str(fake.first_name()) + "\n"))
		elif knopka == "Familia":
			for _ in range(skolka):
				poletexta.insert("1.0", (str(fake.last_name()) + "\n"))				
		elif knopka == "FIO":
			for _ in range(skolka):
				poletexta.insert("1.0", (str(fake.name()) + "\n"))		
		elif knopka == "index":
			for _ in range(skolka):
				poletexta.insert("1.0", (str(fake.postcode()) + "\n"))
		elif knopka == "street":
			for _ in range(skolka):
				poletexta.insert("1.0", (str(fake.street_name()) + "\n"))		
		elif knopka == "city":
			for _ in range(skolka):
				poletexta.insert("1.0", (str(fake.city()) + "\n"))	
		elif knopka == "adresok":
			for _ in range(skolka):
				poletexta.insert("1.0", (str(fake.street_address()) + "\n"))	
		elif knopka == "Nomer":
			for _ in range(skolka):
				poletexta.insert("1.0", (str("+7 (" + (str(''.join(map(str, (random.sample(range (1,9), 3))))) + ") "
					+ (str(''.join(map(str, (random.sample(range (0,9), 3))))) + " "
						+ (str(''.join(map(str, (random.sample(range (0,9), 2))))) + "-"
							+ (str(''.join(map(str, (random.sample(range (0,9), 2)))))+ "\n")))))))								
	value = str(knopka)
	oneframe.pack_forget()
	if 'numberframe' in globals():
		numberframe.pack_forget()
	if 'adressframe' in globals():
		adressframe.pack_forget()	


	twoframe = ctk.CTkFrame(okno, width=500, height=800)
	twoframe.pack(expand=True)

	if value == "Name":
		nadpis = ctk.CTkLabel(twoframe, text = "Сколько нужно имен?", font=("bahnschrift Bold",35))
		nadpis.place(x=10,y=2)
	elif value == "Familia":
		nadpis = ctk.CTkLabel(twoframe, text = "Сколько нужно фимилий?", font=("bahnschrift Bold",35))
		nadpis.place(x=10,y=2)
	elif value == "FIO":
		nadpis = ctk.CTkLabel(twoframe, text = "Сколько нужно ФИО?", font=("bahnschrift Bold",35))
		nadpis.place(x=10,y=2)
	elif value == "index":
		nadpis = ctk.CTkLabel(twoframe, text = "Сколько нужно индексов?", font=("bahnschrift Bold",35))
		nadpis.place(x=10,y=2)
	elif value == "street":
		nadpis = ctk.CTkLabel(twoframe, text = "Сколько нужно улиц?", font=("bahnschrift Bold",35))
		nadpis.place(x=10,y=2)
	elif value == "city":
		nadpis = ctk.CTkLabel(twoframe, text = "Сколько нужно городов?", font=("bahnschrift Bold",35))
		nadpis.place(x=10,y=2)
	elif value == "adresok":
		nadpis = ctk.CTkLabel(twoframe, text = "Сколько нужно адресов?", font=("bahnschrift Bold",35))
		nadpis.place(x=10,y=2)
	elif value == "Nomer":
		nadpis = ctk.CTkLabel(twoframe, text = "Сколько нужно телефонов?", font=("bahnschrift Bold",35))
		nadpis.place(x=10,y=2)
	vvod = ctk.CTkEntry(twoframe, width=90, height=50, font=("bahnshrift Bold", 45), justify=("left"))
	vvod.place(x=10, y=50)

	poletexta = ctk.CTkTextbox(twoframe, width = 480, height = 600,  font=("Bahnschrift SemiBold",25))
	poletexta.place(x=10, y=120)

	knopka_generate = ctk.CTkButton(twoframe, text = "Генерировать", width=90, height=57,
		font=("bahnschrift Bold",35), fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", command=generations)
	knopka_generate.place(x=110, y=50)

	knopka_nazad = ctk.CTkButton(twoframe, text = "Домой", width=90, height=57,
		font=("bahnschrift Bold",35), fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", command=vozvrat)
	knopka_nazad.place(x=10, y=730)

def fio_menu():
	global numberframe
	oneframe.pack_forget()
	numberframe = ctk.CTkFrame(okno, width = 500, height=800)
	numberframe.pack(expand=True)

	name_btn = ctk.CTkButton(master = numberframe, text = "Фамилия", font=("bahnschrift Bold",45),
		width=384, height=100, fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", text_color_disabled="#DEB887", command=lambda: generate_menu('Familia'))
	name_btn.place(x=58, y=220)

	name_btn2 = ctk.CTkButton(master = numberframe, text = "Имя", font=("bahnschrift Bold",45),
		width=384, height=100, fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", text_color_disabled="#DEB887", command=lambda: generate_menu('Name'))
	name_btn2.place(x=58, y=350)

	name_btn3 = ctk.CTkButton(master = numberframe, text = "ФИО", font=("bahnschrift Bold",45),
		width=384, height=100, fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", text_color_disabled="#DEB887", command=lambda: generate_menu('FIO'))
	name_btn3.place(x=58, y=480)

	knopka_nazad = ctk.CTkButton(numberframe, text = "Домой", width=90, height=57,
		font=("bahnschrift Bold",35), fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", command=vozvrat)
	knopka_nazad.place(x=10, y=730)

def adress_menu():
	global adressframe
	oneframe.pack_forget()
	adressframe = ctk.CTkFrame(okno, width = 500, height=800)
	adressframe.pack(expand=True)

	adress_btn = ctk.CTkButton(master = adressframe, text = "Индекс", font=("bahnschrift Bold",45),
		width=384, height=100, fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", text_color_disabled="#DEB887", command=lambda: generate_menu('index'))
	adress_btn.place(x=58, y=120)

	adress_btn2 = ctk.CTkButton(master = adressframe, text = "Улица", font=("bahnschrift Bold",45),
		width=384, height=100, fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", text_color_disabled="#DEB887", command=lambda: generate_menu('street'))
	adress_btn2.place(x=58, y=250)

	adress_btn3 = ctk.CTkButton(master = adressframe, text = "Город", font=("bahnschrift Bold",45),
		width=384, height=100, fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", text_color_disabled="#DEB887", command=lambda: generate_menu('city'))
	adress_btn3.place(x=58, y=380)

	adress_btn4 = ctk.CTkButton(master = adressframe, text = "Адрес", font=("bahnschrift Bold",45),
		width=384, height=100, fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", text_color_disabled="#DEB887", command=lambda: generate_menu('adresok'))
	adress_btn4.place(x=58, y=510)	

	knopka_nazad = ctk.CTkButton(adressframe, text = "Домой", width=90, height=57,
		font=("bahnschrift Bold",35), fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", command=vozvrat)
	knopka_nazad.place(x=10, y=730)

def kish():
	def song_generate():
		songtext.delete("1.0", "250.25")
		gabase = kishbase.gorshokbase
		songtext.insert("1.0", gabase[random.randrange(len(gabase))])
	global kishframe
	oneframe.pack_forget()
	pictures = ctk.CTkImage(light_image = Image.open("2k.jpg"), size = (400,400))
	kishframe = ctk.CTkFrame(okno, width = 500, height=800)
	kishframe.pack(expand=True)
	knizz = ctk.CTkLabel(kishframe, text = "", image=pictures)
	knizz.place(x=50, y=16)
	songtext = ctk.CTkTextbox(kishframe, width = 400, height = 140,  font=("Bahnschrift SemiBold",33))
	songtext.place(x=50, y=430)
	song_btn = ctk.CTkButton(master = kishframe, text = "Ща спою", font=("bahnschrift Bold",45),
		width=400, height=100, fg_color="#B22222", text_color="#fffafa",
		hover_color="#CD5C5C", text_color_disabled="#DEB887", command=song_generate)
	song_btn.place(x=50, y=585)
	knopka_nazad = ctk.CTkButton(kishframe, text = "Домой", width=90, height=57,
		font=("bahnschrift Bold",35), fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", command=vozvrat)
	knopka_nazad.place(x=10, y=730)

def vozvrat():
		if 'numberframe' in globals():
			numberframe.pack_forget()
			oneframe.pack()
		if 'adressframe' in globals():
			adressframe.pack_forget()
			oneframe.pack()			
		if 'kishframe' in globals():
			kishframe.pack_forget()
			oneframe.pack()			
		twoframe.pack_forget()
		oneframe.pack()

def menu():
	global oneframe
	global okno
	okno = ctk.CTk()
	okno.geometry("500x800+700+130")
	okno.resizable(False, False)
	okno.title("Генератор случайных данных")
	#okno.bind('<Key>', enter)

	oneframe = ctk.CTkFrame(okno, width=500, height=800)
	oneframe.pack(expand=True)

	title = ctk.CTkLabel(oneframe, text="Генератор случайных\nданных", font=("bahnschrift Bold",45),
		justify="center")
	title.place(x=23, y=50)

	btn1 = ctk.CTkButton(master = oneframe, text = "Случайный номер", font=("bahnschrift Bold",45),
		width=250, height=100, fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", text_color_disabled="#DEB887", command=lambda: generate_menu('Nomer'))
	btn1.place(x=58, y=220)

	btn2 = ctk.CTkButton(master = oneframe, text = "Случайное ФИО", font=("bahnschrift Bold",45),
		width=386, height=100, fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED",text_color_disabled="#DEB887", command=fio_menu)
	btn2.place(x=58, y=350)

	btn3 = ctk.CTkButton(master = oneframe, text = "Случайный адрес", font=("bahnschrift Bold",45),
		width=386, height=100, fg_color="#4169E1", text_color="#E0FFFF",
		hover_color="#6495ED", text_color_disabled="#DEB887", command=adress_menu)
	btn3.place(x=58, y=480)

	btn4 = ctk.CTkButton(master = oneframe, text = "Король и шут", font=("bahnschrift Bold",45),
		width=386, height=100, fg_color="#B22222", text_color="#fffafa",
		hover_color="#CD5C5C", text_color_disabled="#DEB887", command=kish)
	btn4.place(x=58, y=610)


	okno.mainloop()
menu()