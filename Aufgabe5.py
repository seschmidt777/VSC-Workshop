#%%
import matplotlib.pyplot as plt

# Frage 1: Natürlich! Hier ist eine Frage: Welcher britische Mathematiker veröffentlichte 1936 eine Arbeit, die als Grundlage der modernen Informatik gilt und in der das Problem der Berechenbarkeit untersucht wurde?
# Die Quersumme wird benötigt!
x_links = 

# Frage 2: Wie viele Zeilen zählen wir im Namen eines digitalen Kommunikationsmittels, das 1971 entstand und heute noch weit verbreitet ist?
y_start =   

# Frage 3: Wie lange wurd der erste vollelektronische Computer entwickelt?

y_ende =   

# Frage 4: Welche beiden Ziffern markieren das Jahr, in dem der Grundstein für das weltweite Netz gelegt wurde?

x_rechts =   

# Frage 5: Wie viele Jahre dauerte es vom Bau des ersten vollelektronischen Computers bis zur Einführung der Programmiersprache FORTRAN?

x_diag_start =   

y_diag_start = y_start  
x_diag_end = x_rechts  
y_diag_end = y_ende  


x_left_line = [x_links, x_links]
y_left_line = [y_start, y_ende]


x_right_line = [x_rechts, x_rechts]
y_right_line = [y_start, y_ende]


x_diag_line = [x_diag_start, x_diag_end]
y_diag_line = [y_diag_start, y_diag_end]


plt.figure(figsize=(4, 8))
plt.plot(x_left_line, y_left_line, color='blue', linewidth=5)     
plt.plot(x_right_line, y_right_line, color='blue', linewidth=5)   
plt.plot(x_diag_line, y_diag_line, color='blue', linewidth=5)     


plt.title("Das Geheimnis")
plt.axis('off')


plt.show()
# %%
