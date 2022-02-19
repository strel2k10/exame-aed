from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from functools import partial
import os



window = Tk()
window.geometry("1000x500")
window.title("EXAME AED")

trails_file = "ficheiros/trails.txt"
ultratrails_file = "ficheiros/ultratrails.txt"
favorites_file = "ficheiros/favorites.txt"

Checkbutton1 = IntVar()  
Checkbutton2 = IntVar()

def data_treeview(tree):  # Remove TODAS as linhas da Treeview
    tree.delete(*tree.get_children())
    # activity_type = l_activities.get(l_activities.curselection())
    # formatted_activity_type = activity_type.rstrip("\n")
    # num_laps = entry_num_laps.get()  
    #messagebox.showinfo("test1", activity_type)

    f = open(trails_file, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()

    f1 = open(ultratrails_file, "r", encoding="utf-8")
    lista1 = f1.readlines()
    f1.close()
    num_laps = 0
    if Checkbutton1.get() == 1 and Checkbutton2.get() == 0:
        for linha in lista:
            campos = linha.split(";")
            #messagebox.showinfo("test2", user_type)            
            tree.insert("", "end", values = (campos[0],campos[1], campos[2]))
            num_laps = num_laps + 1

    if Checkbutton2.get() == 1 and Checkbutton1.get() == 0:
        for linha in lista1:
            campos = linha.split(";")
            #messagebox.showinfo("test2", user_type)            
            tree.insert("", "end", values = (campos[0],campos[1], campos[2]))
            num_laps = num_laps + 1

    if Checkbutton1.get() == 1 and Checkbutton2.get() == 1:
        for linha in lista:
            campos = linha.split(";")
            #messagebox.showinfo("test2", user_type)            
            tree.insert("", "end", values = (campos[0],campos[1], campos[2]))
            num_laps = num_laps + 1
        for linha in lista1:
            campos = linha.split(";")
            #messagebox.showinfo("test2", user_type)            
            tree.insert("", "end", values = (campos[0],campos[1], campos[2]))
            num_laps = num_laps + 1

    entry_num_laps.configure(state="normal")
    entry_num_laps.delete(0, END)
    entry_num_laps.insert(END, num_laps)
    entry_num_laps.configure(state="disabled")   

def a_z_order(tree):    

    rows = [(tree.set(item, 'Prova').lower(), item) for item in tree.get_children('')]
    rows.sort()

    for index, (values, item) in enumerate(rows):
        tree.move(item, '', index)

    
   

def z_a_order(tree):
    rows = [(tree.set(item, 'Prova').lower(), item) for item in tree.get_children('')]
    rows.sort(reverse=True)

    for index, (values, item) in enumerate(rows):
        tree.move(item, '', index)
 
def add_favorites(tree):
    indice = tree.selection() # Indice da linha selecionada
    prova = tree.item(indice)["values"][0]
    l_favorites.insert("end",prova )
    # tree_select = tree.focus()
    # messagebox.showinfo("test", tree_select.item)

    # f = open(favorites_file, "a")
    
    # linha = tree_select + "\n"
    # f.write(linha)
    # f.close()

def remove_favorites(l_favorites):
    sel_fav_index = l_favorites.curselection()  #Indice da linha selecionada
    
    if len(sel_fav_index) == 0:
        messagebox.showinfo("WARNING", "PFV ESCOLHE UMA LINHA")

    else:
        sel_fav = l_favorites.get(l_favorites.curselection())
        formatted_sel_fav = sel_fav.rstrip("\n")
        l_favorites.delete(sel_fav_index,sel_fav_index)

        f = open(favorites_file, "r", encoding="utf-8")
        lista = f.readlines()
        f.close()

        f = open(favorites_file, "w", encoding="utf-8")        
        for linha in lista:           
            formatted_linha = linha.rstrip("\n")
            if formatted_linha != formatted_sel_fav:
                f.write(linha)
        f.close()

        l_favorites.delete(0,END)

        f = open(favorites_file, "r", encoding="utf-8")
        lista = f.readlines()
        for favorite in lista:
            l_favorites.insert(END, favorite)
        f.close()
      

# def remove_favorites(l_favorites):
#     fav = l_favorites.get(l_favorites.curselection())   

#     f = open(favorites_file, "r", encoding="utf-8")
#     lista = f.readlines()
#     f.close()

#     f = open(favorites_file, "w", encoding="utf-8")
    
#     for linha in lista:
#         #messagebox.showinfo("test", mov)
#         formatted_linha = linha.rstrip("\n")
#         if formatted_linha != fav:
#             f.write(linha)

#     l_favorites.delete(0,END)
    
#     f = open(favorites_file, "r", encoding="utf-8")
#     lista = f.readlines()
#     f.close()

#     for favorite in lista:
#         l_favorites.insert(END, favorite)
    
def save_favs(l_favorites):

    f = open(favorites_file, "w", encoding="utf-8")

    listbox_lines = l_favorites.get(0, END)

    for line in listbox_lines:
        f.write(line + '\n')
    f.close()
   
 



def chose_image():
    filepath = filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files", "*.png"), ("all files","*.*")))
    # # adiciona à listBox
    # lboxImg.insert("end", filename)
    # lista_imagens()

    # image = Image.open(filepath)
    img = PhotoImage(file = filepath)
    canvas_image.create_image(64,64, image=img)
    canvas_image_resize = canvas_image.resize((300,130), Image.ANTIALIAS) # ESPERO QUE FUNCIONE N CONSIGO TESTAR
    new_img = PhotoImage(canvas_image_resize)
    canvas_image.image = new_img

    # f = open(setup_file, "a")
    # linha = os.path.basename(filepath) + ";" + filepath + "\n"
    # f.write(linha)
    # f.close()
    
            

check_short = Checkbutton(window, text = "Trail Curto", variable = Checkbutton1, onvalue = 1, offvalue = 0, height = 2, width = 10)
check_short.place(x=20, y = 40)
check_short.select()

check_ultra = Checkbutton(window, text = "Ultra trail", variable = Checkbutton2, onvalue = 1, offvalue = 0, height = 2, width = 10)
check_ultra.place(x=140, y = 40)


tree = ttk.Treeview(window, selectmode = "browse", columns = ("Prova", "Data", "Local"), show = "headings")

tree.column("Prova", width = 170,   anchor="w")
tree.column("Data", width = 170,  anchor="c") 
tree.column("Local", width = 170,  anchor="c")    # c- center, e - direita, w- esquerda
tree.heading("Prova", text = "Prova")
tree.heading("Data", text = "Data")
tree.heading("Local", text = "Local")
tree.place(x=20, y=100)

search_image = PhotoImage(file = "imagens/pesquisar_GIF.gif")
a_z_image =  PhotoImage(file = "imagens/asc_GIF.gif")
z_a_image =  PhotoImage(file = "imagens/desc_GIF.gif")



label_num_laps = Label(window, text="Nº de provas: ", fg="black", font=("Helvética",11))
label_num_laps.place(x=50, y=360)

entry_num_laps = Entry(window, width= 8, font=("Helvética",11))
entry_num_laps.configure(state="disabled")
entry_num_laps.place(x=160, y=360)

btn3 = Button(window, text="Selecionar Imagem", width=15, height=1 , font=("Helvética",11), command = partial(chose_image))
btn3.place(x=180,y=420)

btn4 = Button(window, width=35, height=35 ,image=search_image, command = partial(data_treeview,tree))
btn4.place(x=250,y=40)

btn5 = Button(window,image=a_z_image, command = partial(a_z_order,tree))
btn5.place(x=320,y=20)

btn6 = Button(window,image=z_a_image, command = partial(z_a_order,tree))
btn6.place(x=400,y=20)


panel1 = PanedWindow(window,width=250, height=150, bd=2, relief="sunken")
panel1.place(x= 330, y= 340 )


canvas_image = Canvas(panel1, width=300, height=130)
canvas_image.place(x=0, y=0)

panel2 = PanedWindow(window,width=250, height=480, bd=2, relief="sunken")
panel2.place(x= 700, y= 0 )

label_favs = Label(panel2, text="Favoritos ", fg="black", font=("Helvética",11))
label_favs.place(x=100, y=50)

l_favorites = Listbox(panel2, width = 25, height = 15, relief = "sunken", font = ("Helvetica", "11"))
l_favorites.place (x=20,y=80)

f = open(favorites_file, "r")

lista = f.readlines()
f.close()
for favorite in lista:
    formatted_favorite = favorite.rstrip("\n")
    #re.sub('\s+','',user_type)
    l_favorites.insert(END, formatted_favorite)

btn1 = Button(window, text="Adicionar Favoritos", width=15, height=2 , font=("Helvética",11), command = partial(add_favorites,tree))
btn1.place(x=550,y=130)

btn2 = Button(window, text="Remover Favoritos", width=15, height=2 , font=("Helvética",11),  command = partial(remove_favorites,l_favorites))
btn2.place(x=550,y=200)

btn7 = Button(panel2,text="guardar favoritos", command = partial(save_favs,l_favorites), font=("Helvética",11))
btn7.place(x=100,y=400)



# label_my_laps = Label(panel1, text="As Minhas Provas", fg="black", font=("Rubik Bold",12))
# label_my_laps.place(x=80, y=50)

# label_select_logo = Label(panel1, text="Logotipo da prova:", fg="black", font=("Rubik",10))
# label_select_logo.place(x=15, y=120)

# btn1 = Button(panel1, text="Selecionar", width=10, height=1 , font=("Rubik",12),  bg="light gray", command = partial(chose_image))
# btn1.place(x=130,y=110)

# btn2 = Button(panel1, text="Guardar", width=25, height=1 , font=("Rubik",12),  bg="light gray", command = "")
# btn2.place(x=30,y=440)

# panel2 = PanedWindow(window,width=200, height=200, bd=2, relief="sunken")
# panel2.place(x= 90, y= 210)
# canvas_logo = Canvas(panel2, width=200, height=200)
# canvas_logo.place(x=0, y=0)



# panel3 = PanedWindow(window,width=430, height=500, bd=2, relief="sunken")
# panel3.place(x= 350, y= 20 )

# label_my_notifications = Label(panel3, text="As Minhas Notificações", fg="black", font=("Rubik Bold",12))
# label_my_notifications.place(x=80, y=50)

# label_my_notifications_type = Label(panel3, text="Ver Notificações de:", fg="black", font=("Rubik Bold",12))
# label_my_notifications_type.place(x=60, y=100)






# btn2 = Button(panel3, text="Ver", width=25, height=1 , font=("Rubik",12),  bg="light gray", command = "")
# btn2.place(x=30,y=200)

# l_notifications = Listbox(panel3, width = 50, height = 10, relief = "sunken", font = ("Helvetica", "10"))
# l_notifications.place (x=30,y=250)

# f = open(activities_file, "r")

# lista = f.readlines()
# f.close()
# for activity in lista:
#     formatted_activity = activity.rstrip("\n")
#     #re.sub('\s+','',user_type)
#     l_activities.insert(END, formatted_activity)




# btn2 = Button(window, text="+", width=2, height=1 ,bg="gray",  fg="white", font=("Rubik",12), command = "")
# btn2.place(x=235,y=120)

# btn3 = Button(panel5, text="Filtrar", width=8, height=3 ,bg="gray",  fg="white", font=("Rubik",12), command = "")
# btn3.place(x=250,y=10)


window.mainloop()