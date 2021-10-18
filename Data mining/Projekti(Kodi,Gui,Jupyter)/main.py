import os
import pandas as pd
import tkinter as tk
import tkinter.scrolledtext as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


r""" #clusterim
#marrja e datasetit per vitin 2016 4 tremujort
tre1=pd.read_csv('tremujori1_2016.csv', encoding='ISO-8859-1')
tre2=pd.read_csv('tremujori2_2016.csv', encoding='ISO-8859-1')
tre3=pd.read_csv('tremujori3_2016.csv', encoding='ISO-8859-1')
tre4=pd.read_csv('tremujori4_2016.csv', encoding='ISO-8859-1')
tre1["tremujori"] = tre1["Viti"]-2015
tre2["tremujori"] = tre2["Viti"]-2014
tre3["tremujori"] = tre3["Viti"]-2013
tre4["tremujori"] = tre4["Viti"]-2012

#marrja e datasetit per vitin 2017 4 tremujort
ttre1=pd.read_csv('tremujori1_2017.csv', encoding='ISO-8859-1')
ttre2=pd.read_csv('tremujori2_2017.csv', encoding='ISO-8859-1')
ttre3=pd.read_csv('tremujori3_2017.csv', encoding='ISO-8859-1')
ttre4=pd.read_csv('tremujori4_2017.csv', encoding='ISO-8859-1')
ttre1["tremujori"] = ttre1["Viti"]-2016
ttre2["tremujori"] = ttre2["Viti"]-2015
ttre3["tremujori"] = ttre3["Viti"]-2014
ttre4["tremujori"] = ttre4["Viti"]-2013

shpenzimet1=tre1.append(tre2)
shpenzimet2=tre3.append(tre4)
files = [file for file in os.listdir(r"C:\Users\beny shop\Desktop\projekti")]
for file in files:
    shpenzimet2016=shpenzimet1.append(shpenzimet2)
shpenzimet2016.to_csv("shpenzimet2016.csv", index=False)

shpenzimett1=ttre1.append(ttre2)
shpenzimett2=ttre3.append(ttre4)
files = [file for file in os.listdir(r"C:\Users\beny shop\Desktop\projekti")]
for file in files:
    shpenzimet2017=shpenzimett1.append(shpenzimett2)
shpenzimet2017.to_csv("shpenzimet2017.csv", index=False)

## total shpenzimet
sh1=pd.read_csv('shpenzimet2016.csv')
sh2=pd.read_csv('shpenzimet2017.csv')
files = [file for file in os.listdir(r"C:\Users\beny shop\Desktop\projekti")]
for file in files:
    shpenzimet_tot1=sh1.append(sh2)
shpenzimet_tot1.to_csv("shpenzimet_tot1.csv", index=False)

#marrja e datasetit per vitin 2018 4 tremujort
tre1=pd.read_csv('tremujori1_2018.csv', encoding='ISO-8859-1')
tre2=pd.read_csv('tremujori2_2018.csv', encoding='ISO-8859-1')
tre3=pd.read_csv('tremujori3_2018.csv', encoding='ISO-8859-1')
tre4=pd.read_csv('tremujori4_2018.csv', encoding='ISO-8859-1')
tre1["tremujori"] = tre1["Viti"]-2017
tre2["tremujori"] = tre2["Viti"]-2016
tre3["tremujori"] = tre3["Viti"]-2015
tre4["tremujori"] = tre4["Viti"]-2014
shpenzimet1=tre1.append(tre2)
shpenzimet2=tre3.append(tre4)
files = [file for file in os.listdir(r"C:\Users\beny shop\Desktop\projekti")]
for file in files:
    shpenzimet2018=shpenzimet1.append(shpenzimet2)
shpenzimet2018.to_csv("shpenzimet2018.csv", index=False)


#marrja e datasetit per vitin 2019 4 tremujort
tre1=pd.read_csv('tremujori1_2019.csv', encoding='ISO-8859-1')
tre2=pd.read_csv('tremujori2_2019.csv', encoding='ISO-8859-1')
tre3=pd.read_csv('tremujori3_2019.csv', encoding='ISO-8859-1')
tre4=pd.read_csv('tremujori4_2019.csv', encoding='ISO-8859-1')
tre1["tremujori"] = tre1["Viti"]-2018
tre2["tremujori"] = tre2["Viti"]-2017
tre3["tremujori"] = tre3["Viti"]-2016
tre4["tremujori"] = tre4["Viti"]-2015
shpenzimet1=tre1.append(tre2)
shpenzimet2=tre3.append(tre4)
files = [file for file in os.listdir(r"C:\Users\beny shop\Desktop\projekti")]
for file in files:
    shpenzimet2019=shpenzimet1.append(shpenzimet2)
shpenzimet2019.to_csv("shpenzimet2019.csv", index=False)

#marrja e datasetit per vitin 2020 4 tremujort
tre1=pd.read_csv('tremujori1_2020.csv', encoding='ISO-8859-1')
tre2=pd.read_csv('tremujori2_2020.csv', encoding='ISO-8859-1')
tre3=pd.read_csv('tremujori3_2020.csv', encoding='ISO-8859-1')
tre4=pd.read_csv('tremujori4_2020.csv', encoding='ISO-8859-1')
tre1["tremujori"] = tre1["Viti"]-2019
tre2["tremujori"] = tre2["Viti"]-2018
tre3["tremujori"] = tre3["Viti"]-2017
tre4["tremujori"] = tre4["Viti"]-2016
shpenzimet1=tre1.append(tre2)
shpenzimet2=tre3.append(tre4)
files = [file for file in os.listdir(r"C:\Users\beny shop\Desktop\projekti")]
for file in files:
    shpenzimet2020=shpenzimet1.append(shpenzimet2)
shpenzimet2020.to_csv("shpenzimet2020.csv", index=False)


## total shpenzimet2
sh1=pd.read_csv('shpenzimet2018.csv')
sh2=pd.read_csv('shpenzimet2019.csv')
files = [file for file in os.listdir(r"C:\Users\beny shop\Desktop\projekti")]
for file in files:
    shpenzimet_tot2=sh1.append(sh2)
shpenzimet_tot2.to_csv("shpenzimet_tot2.csv", index=False)

## total shpenzimet4
sh1=pd.read_csv('shpenzimet_tot3.csv')
sh2=pd.read_csv('shpenzimet2020.csv')
files = [file for file in os.listdir(r"C:\Users\beny shop\Desktop\projekti")]
for file in files:
    shpenzimet_tot4=sh1.append(sh2)
shpenzimet_tot4.to_csv("shpenzimet_tot4.csv", index=False)

Te hyrat sipas viteve
t1 = pd.read_csv('TeHyrat2014.csv', encoding='ISO-8859-1')
t2 = pd.read_csv('TeHyrat2015.csv', encoding='ISO-8859-1')
t3 = pd.read_csv('TeHyrat2016.csv', encoding='ISO-8859-1')
t4 = pd.read_csv('TeHyrat2017.csv', encoding='ISO-8859-1')
t5 = pd.read_csv('TeHyrat2018.csv', encoding='ISO-8859-1')
t6 = pd.read_csv('TeHyrat2019.csv', encoding='ISO-8859-1')
t7 = pd.read_csv('TeHyrat2020.csv', encoding='ISO-8859-1')
t1["tremujori"] = t1["Viti"] - 2013
t2["tremujori"] = t2["Viti"] - 2014
t3["tremujori"] = t3["Viti"] - 2015
t4["tremujori"] = t4["Viti"] - 2016
t5["tremujori"] = t5["Viti"] - 2017
t6["tremujori"] = t6["Viti"] - 2018
t7["tremujori"] = t7["Viti"] - 2019

tehyrat1=t1.append(t2)
tehyrat2=t3.append(t4)
tehyrat3=t5.append(t6)
files = [file for file in os.listdir(r"C:\Users\Kobit PC\PycharmProjects\pythonProject1")]
for file in files:
    Tehyratt1 = tehyrat1.append(tehyrat2)
    Tehyratt2 = tehyrat3.append(t7)
    tehyrat = Tehyratt1.append(Tehyratt2)
tehyrat.to_csv("tehyrat.csv", index=False)
df = pd.read_csv('tehyrat.csv')

Te hyrat per cdo muaj te viteve
th1 = pd.read_csv('te-hyrat-sipas-muajve-2018.csv', encoding='ISO-8859-1')
th2 = pd.read_csv('te-hyrat-sipas-muajve-2019.csv', encoding='ISO-8859-1')
th3 = pd.read_csv('te-hyrat-sipas-muajve-2020.csv', encoding='ISO-8859-1')
th4 = pd.read_csv('te-hyrat-sipas-muajve-2021.csv', encoding='ISO-8859-1')
th1["tremujori"] = th1["Viti"] - 2017
th2["tremujori"] = th2["Viti"] - 2016
th3["tremujori"] = th3["Viti"] - 2015
th4["tremujori"] = th4["Viti"] - 2014

tehyratsipasmuajve1 = th1.append(th2)
tehyratsipasmuajve2 = th3.append(th4)
files = [file for file in os.listdir(r"C:\Users\Kobit PC\PycharmProjects\pythonProject1")]
for file in files:
   tehyratsipasmuajve = tehyratsipasmuajve1.append(tehyratsipasmuajve2)
tehyratsipasmuajve.to_csv("tehyratsipasmuajve.csv", index=False)
df = pd.read_csv('tehyratsipasmuajve.csv')
"""

df = pd.read_csv('shpenzimet_tot4.csv')
df.columns = [col.strip() for col in list(df.columns)]
df['Shuma'] = df['Shuma'].astype(int)

df1 = pd.read_csv('tehyratsipasmuajve.csv')
df1.columns = [col.strip() for col in list(df1.columns)]
df1['Janar'] = df1['Janar'].astype(int)

df2 = pd.read_csv('tehyratsipasmuajve.csv')
df2.columns = [col.strip() for col in list(df2.columns)]
df2['Shkurt'] = df2['Shkurt'].astype(int)

df3 = pd.read_csv('tehyratsipasmuajve.csv')
df3.columns = [col.strip() for col in list(df3.columns)]
df3['Mars'] = df3['Mars'].astype(int)

df4 = pd.read_csv('tehyrat.csv')
df4.columns = [col.strip() for col in list(df4.columns)]
df4['Përqindja'] = df4['Përqindja'].astype(int)

df5 = pd.read_csv('tehyrat.csv')
df5.columns = [col.strip() for col in list(df4.columns)]
df5['Realizimi'] = df5['Realizimi'].astype(int)

# GUI
window = tk.Tk()
window.title("Data Mining")
TLabel5 = tk.Label(window)
TLabel5.place(relx=0.03, rely=0.22, height=19, width=42)
TLabel5.configure(background="#EDF2F3")
TLabel5.configure(foreground="#000000")
TLabel5.configure(text='''Output''')


def ShpenzimetClick():
    # query
    # gjej cila drejtori ne kategorin ekonomike subvencionet ka me shumti shpenzime ne tremujorin1
    # the number of rows
    if (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 1) & (var4.get() == 1) & (var5.get() == 1):
        b = df.groupby('Drejtoria', as_index=False).agg({"Shuma": "sum"})
        b1 = b['Shuma'].max()
        b2 = b.loc[b['Shuma'].idxmax()]
        output.insert(tk.INSERT, "Drejtoria me me se shumti shpenzime ne te gjitha vitet eshte:\n")
        output.insert(tk.INSERT, b2)


    if (var5.get() == 1):
        output.insert(tk.INSERT, " ------------------------------------------------\n")
        data2020 = df.query("Viti == 2020 ")
        l = data2020.groupby('Drejtoria', as_index=False).agg({"Shuma": "sum"})
        l1 = l['Shuma'].max()
        l2 = l.loc[l['Shuma'].idxmax()]
        output.insert(tk.INSERT, "Drejtoria me me se shumti shpenzime ne vitin 2020 eshte:\n")
        output.insert(tk.INSERT, l2)

        output.insert(tk.INSERT, " ------------------------------------------------\n")
        data2010_1 = df.query("Viti=='2020' & tremujori == 1")
        l = data2010_1.groupby(['Drejtoria', 'Viti'], as_index=False).agg({"Shuma": "sum"})
        l1 = l['Shuma'].max()
        l2 = l.loc[l['Shuma'].idxmax()]
        output.insert(tk.INSERT, "Drejtoria me me se shumti shpenzime ne tremujorin 1 te vitit 2020 ka:\n")
        output.insert(tk.INSERT, l2)

        output.insert(tk.INSERT, " ------------------------------------------------\n")
        data2010_1 = df.query("Viti=='2020' & tremujori == 2")
        v = data2010_1.groupby(['Drejtoria', 'Viti'], as_index=False).agg({"Shuma": "sum"})
        v1 = v['Shuma'].max()
        v2 = v.loc[v['Shuma'].idxmax()]
        output.insert(tk.INSERT, "Drejtoria me me se shumti shpenzime ne tremujorin 2 te vitit 2020 ka:\n")
        output.insert(tk.INSERT, v2)

        output.insert(tk.INSERT, " ------------------------------------------------\n")
        data2010_1 = df.query("Viti=='2020' & tremujori == 3")
        m = data2010_1.groupby(['Drejtoria', 'Viti'], as_index=False).agg({"Shuma": "sum"})
        m1 = m['Shuma'].max()
        m2 = m.loc[m['Shuma'].idxmax()]
        output.insert(tk.INSERT, "Drejtoria me me se shumti shpenzime ne tremujorin 3 te vitit 2020 ka:\n")
        output.insert(tk.INSERT, m2)

        output.insert(tk.INSERT, " ------------------------------------------------\n")
        data2010_1 = df.query("Viti=='2020' & tremujori == 4")
        n = data2010_1.groupby(['Drejtoria', 'Viti'], as_index=False).agg({"Shuma": "sum"})
        n1 = n['Shuma'].max()
        n2 = n.loc[n['Shuma'].idxmax()]
        output.insert(tk.INSERT, "Drejtoria me me se shumti shpenzime ne tremujorin 4 te vitit 2020 ka:\n")
        output.insert(tk.INSERT, n2)

        output.insert(tk.INSERT, " ------------------------------------------------\n")
        l3 = [l1, l2]
        v3 = [v1, v2]
        m3 = [m1, m2]
        n3 = [n1, n2]
        list = [l3, v3, m3, n3]
        k = max(list)
        output.insert(tk.INSERT, "Drejtoria me shpenzimet me se shumti ne kuader te tremujorve te vitit 2020:\n")
        output.insert(tk.INSERT, k[1:])

    if (var4.get() == 1):
        output.insert(tk.INSERT, " ------------------------------------------------\n")
        data2019 = df.query("Viti == 2019 ")
        c = data2019.groupby('Drejtoria', as_index=False).agg({"Shuma": "sum"})
        c1 = c['Shuma'].max()
        c2 = c.loc[c['Shuma'].idxmax()]
        output.insert(tk.INSERT, "Drejtoria me me se shumti shpenzime ne vitin 2019 eshte:\n")
        output.insert(tk.INSERT, c2)
    if (var3.get() == 1):
        output.insert(tk.INSERT, " ------------------------------------------------\n")
        data2019 = df.query("Viti == 2018 ")
        d = data2019.groupby('Drejtoria', as_index=False).agg({"Shuma": "sum"})
        d1 = d['Shuma'].max()
        d2 = d.loc[d['Shuma'].idxmax()]
        output.insert(tk.INSERT, "Drejtoria me me se shumti shpenzime ne vitin 2018 eshte:\n")
        output.insert(tk.INSERT, d2)
    if (var2.get() == 1):
        output.insert(tk.INSERT, " ------------------------------------------------\n")
        data2019 = df.query("Viti == 2017 ")
        e = data2019.groupby('Drejtoria', as_index=False).agg({"Shuma": "sum"})
        e1 = e['Shuma'].max()
        e2 = e.loc[e['Shuma'].idxmax()]
        output.insert(tk.INSERT, "Drejtoria me me se shumti shpenzime ne vitin 2017 eshte:\n")
        output.insert(tk.INSERT, e2)
    if (var1.get() == 1):
        output.insert(tk.INSERT, " ------------------------------------------------\n")
        data2019 = df.query("Viti == 2016 ")
        f = data2019.groupby('Drejtoria', as_index=False).agg({"Shuma": "sum"})
        f1 = f['Shuma'].max()
        f2 = f.loc[f['Shuma'].idxmax()]
        output.insert(tk.INSERT, "Drejtoria me me se shumti shpenzime ne vitin 2016 eshte:\n")
        output.insert(tk.INSERT, f2)
    

def TeHyratClick():
    if (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 1) & (var4.get() == 1) & (var5.get() == 1):
        g = df1.groupby('Viti', as_index=False).agg({"Janar": "sum"})
        g1 = g['Janar'].max()
        g2 = g.loc[g['Janar'].idxmax()]
        output.insert(tk.INSERT, "Shuma e te hyrave ne muajin janar::\n")
        output.insert(tk.INSERT, g2)

        output.insert(tk.INSERT, " ------------------------------------------------\n ")
        h = df2.groupby('Viti', as_index=False).agg({"Shkurt": "sum"})
        h1 = h['Shkurt'].max()
        h2 = h.loc[h['Shkurt'].idxmax()]
        output.insert(tk.INSERT, "Shuma e te hyrave me te larta ne muajin shkurt:\n")
        output.insert(tk.INSERT, h2)

        output.insert(tk.INSERT, " ------------------------------------------------\n ")
        i = df3.groupby('Viti', as_index=False).agg({"Mars": "sum"})
        i1 = i['Mars'].max()
        i2 = i.loc[i['Mars'].idxmax()]
        output.insert(tk.INSERT, "Shuma e te hyrave me te larta ne muajin mars:\n")
        output.insert(tk.INSERT, i2)

        output.insert(tk.INSERT, " ------------------------------------------------\n ")
        o = df4.groupby('Viti', as_index=False).agg({"Përqindja": "max"})
        o1 = o['Përqindja'].max()
        o2 = o.loc[o['Përqindja'].idxmax()]
        output.insert(tk.INSERT, "Perqindja me e larte e te hyrave:\n")
        output.insert(tk.INSERT, o2)

        output.insert(tk.INSERT, " ------------------------------------------------\n ")
        j = df4.groupby('Viti', as_index=False).agg({"Përqindja": "min"})
        j1 = j['Përqindja'].min()
        j2 = j.loc[j['Përqindja'].idxmin()]
        output.insert(tk.INSERT, "Perqindja me e ulet e te hyrave:\n")
        output.insert(tk.INSERT, j2)

    if (var4.get() == 1):
        output.insert(tk.INSERT, " ------------------------------------------------\n")
        data2019 = df5.query("Viti == 2019 ")
        x = data2019.groupby('Përshkrimi', as_index=False).agg({"Realizimi": "sum"})
        x1 = x['Realizimi'].max()
        x2 = x.loc[x['Realizimi'].idxmax()]
        output.insert(tk.INSERT, "Drejtoria me me se shumti te hyra ne vitin 2019 eshte:\n")
        output.insert(tk.INSERT, x2)

        output.insert(tk.INSERT, " ------------------------------------------------\n")
        data2019 = df5.query("Viti == 2019 ")
        y = data2019.groupby('Përshkrimi', as_index=False).agg({"Realizimi": "min"})
        y1 = y['Realizimi'].min()
        y2 = y.loc[y['Realizimi'].idxmin()]
        output.insert(tk.INSERT, "Drejtoria me me se paku te hyra ne vitin 2019 eshte:\n")
        output.insert(tk.INSERT, y2)


def GrafiClick():
    import tkinter 
    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg, NavigationToolbar2Tk)
    # Implement the default Matplotlib key bindings.
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    df=pd.read_csv('shpenzimet_tot4.csv')
    df.columns = [col.strip() for col in list(df.columns)]
    df['Shuma'] = df['Shuma'].astype(int)
    root = tkinter.Tk()
    root.wm_title("Paraqitja grafike")
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/3 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))
    fig = Figure(figsize=(6, 5), dpi=100)
    ax = fig.add_subplot(111)
    b=df.groupby('Drejtoria', as_index=False).agg({"Shuma": "sum"})
    #paraqitja grafike
    b.plot(kind="bar", x="Drejtoria", y="Shuma",label = 'Shpenzimet_totale',  color ='coral', ax=ax,fontsize=5)
    
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



    def _quit1():
        root = tkinter.Tk()
        root.wm_title("Paraqitja grafike ")
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        positionRight = int(root.winfo_screenwidth()/3 - windowWidth/2)
        positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
        root.geometry("+{}+{}".format(positionRight, positionDown))
        fig = Figure(figsize=(6, 5), dpi=100)
        ax = fig.add_subplot(111)
        data2020 = df.query("Viti == 2020 ")
        l=data2020.groupby('Drejtoria', as_index=False).agg({"Shuma": "sum"})
        #paraqitja grafike
        l.plot(kind="bar", x="Drejtoria", y="Shuma",label = 'Shpenzimet_2020',  color ='blue', ax=ax,fontsize=5)
       
        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        def _quit2():
            root = tkinter.Tk()
            root.wm_title("Paraqitja grafike")
            windowWidth = root.winfo_reqwidth()
            windowHeight = root.winfo_reqheight()
            positionRight = int(root.winfo_screenwidth()/3 - windowWidth/2)
            positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
            root.geometry("+{}+{}".format(positionRight, positionDown))
            fig = Figure(figsize=(6, 5), dpi=100)
            ax = fig.add_subplot(111)
            data2020 = df.query("Viti == 2019 ")
            l=data2020.groupby('Drejtoria', as_index=False).agg({"Shuma": "sum"})
            #paraqitja grafike
            l.plot(kind="bar", x="Drejtoria", y="Shuma",label = 'Shpenzimet_2020',  color ='red', ax=ax,fontsize=5)
           
            canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
            def _quit3():
                    root= tk.Tk() 
                    root.wm_title("Paraqitja grafike ")
                    windowWidth = root.winfo_reqwidth()
                    windowHeight = root.winfo_reqheight()
                    positionRight = int(root.winfo_screenwidth()/3 - windowWidth/2)
                    positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
                    root.geometry("+{}+{}".format(positionRight, positionDown))
                    df=pd.read_csv('shpenzimet_tot4.csv')
                    df.columns = [col.strip() for col in list(df.columns)]
                    figure1 = plt.Figure(figsize=(6,5), dpi=100)
                    ax1 = figure1.add_subplot(111)
                    bar1 = FigureCanvasTkAgg(figure1, root)
                    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                    df=sns.stripplot(y= "Drejtoria", x = "Shuma", hue = "Viti", data = df,ax=ax1)
                    ax1.set_title(label = "shpenzimet ne baze te tremujorve")
                    ax1.set_xlabel(xlabel = " Total shpenzimet")
                    ax1.set_ylabel(ylabel = "Drejtorite perkatese")
                    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
                            
                    button = tk.Button(root, width=10, command=root.destroy)
                    button.place(x=505, y=470)
                    button.configure(foreground="white")
                    button.configure(background="gray")
                    button.configure(activebackground="#FFFFFF")
                    button.configure(text='''Exit''')
                    button.configure(padx=0, pady=0, font=("Courier", 10))
            
                
                          
            button = tkinter.Button(master=root, text="Next",command=_quit3)
            button.pack(side=tkinter.BOTTOM)
        button = tkinter.Button(master=root, text="Next",command=_quit2)
        button.pack(side=tkinter.BOTTOM)
    button = tkinter.Button(master=root, text="Next", command=_quit1)
    button.pack(side=tkinter.BOTTOM)
    tkinter.mainloop()     
          




def clear():
    output.delete('1.0', tk.END)
    a1.deselect()
    a2.deselect()
    a3.deselect()
    a4.deselect()
    a5.deselect()

button = tk.Button(window, width=15, activebackground='#FFFFFF', command=ShpenzimetClick)
button.configure(padx=0, pady=0, font=("Courier", 10))
button.place(x=50, y=50)
button.configure(foreground="white")
button.configure(background="gray")
button.configure(activebackground="#FFFFFF")
button.configure(text='Shpenzimet')

button = tk.Button(window, width=15, activebackground='#FFFFFF', command=TeHyratClick)
button.configure(padx=0, pady=0, font=("Courier", 10))
button.place(x=225, y=50)
button.configure(foreground="white")
button.configure(background="gray")
button.configure(activebackground="#FFFFFF")
button.configure(text='Te hyrat')

button = tk.Button(window, width=15, activebackground='#FFFFFF', command=GrafiClick)
button.configure(padx=0, pady=0, font=("Courier", 10))
button.place(x=400, y=50)
button.configure(foreground="white")
button.configure(background="gray")
button.configure(activebackground="#FFFFFF")
button.configure(text='Grafi')

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
a1 = tk.Checkbutton(window, text='2016', variable=var1, onvalue=1, offvalue=0)
# a1.place(x=400, y=470)
a1.grid(row=10, column=1)
a1.configure(background="#EDF2F3")
a1.place(x=45, y=80)

a2 = tk.Checkbutton(window, text='2017', variable=var2, onvalue=1, offvalue=0)
a2.grid(row=10, column=2)
a2.configure(background="#EDF2F3")
a2.place(x=100, y=80)

a3 = tk.Checkbutton(window, text='2018', variable=var3, onvalue=1, offvalue=0)
a3.grid(row=10, column=3)
a3.configure(background="#EDF2F3")
a3.place(x=150, y=80)

a4 = tk.Checkbutton(window, text='2019', variable=var4, onvalue=1, offvalue=0)
a4.grid(row=10, column=4)
a4.configure(background="#EDF2F3")
a4.place(x=200, y=80)

a5 = tk.Checkbutton(window, text='2020', variable=var5, onvalue=1, offvalue=0)
a5.grid(row=10, column=5)
a5.configure(background="#EDF2F3")
a5.place(x=250, y=80)


output = st.ScrolledText(window, wrap=tk.WORD)
output.place(relx=0.07, rely=0.27, relheight=0.40, relwidth=0.84)
output.configure(background="white")
output.configure(font="TkTextFont")
output.configure(foreground="black")
output.configure(highlightbackground="#d9d9d9")
output.configure(insertborderwidth="3")
output.configure(width=10)
output.configure(state=tk.NORMAL)

# Clear button
button = tk.Button(window, width=12, activebackground='#FFFFFF', command=clear)
button.configure(padx=0, pady=0, font=("Courier", 10))
button.place(x=400, y=470)
button.configure(foreground="white")
button.configure(background="gray")
button.configure(activebackground="#FFFFFF")
button.configure(text='''Clear''')

# Exit Button
button = tk.Button(window, width=10, command=window.destroy)
button.place(x=505, y=470)
button.configure(foreground="white")
button.configure(background="gray")
button.configure(activebackground="#FFFFFF")
button.configure(text='''Exit''')
button.configure(padx=0, pady=0, font=("Courier", 10))

window.geometry("600x500+200+200")
window['background'] = '#EDF2F3'
window.mainloop()