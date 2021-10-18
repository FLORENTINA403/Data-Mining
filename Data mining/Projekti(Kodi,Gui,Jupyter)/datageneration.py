import pymysql
import random

db= pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='datat',
)
cursor = db.cursor()
i = 1
while(i<500):
    ke = ['132 - Shpenzimet Komunale', '20 - Subvencione dhe Transfere', '30 - Shpenzimet Kapitale', '11 - Paga dhe Mëditje']
    randomke = random.choice(ke)
    kek = randomke
    dr = ['Administrata dhe Personeli', 'Infrastruktura Publike', 'Zyrja për Komunitete dhe Kthim', 'Kultura', 'Shërbimet e Shëndetësisë Primare', 'Shërbimet Sociale', 'Administrata e Arsimit', 'Arsimi Parafillor (Qerdhet)']
    randomke = random.choice(dr)
    drt = randomke
    sh = random.randint(2, 90000)
    tre=random.randint(1,4)
    query = "INSERT INTO shpenzimet2016 (Viti, Kategoria_Ekonomike, Sektori, Shuma,tremujori) VALUES (%s, %s, %s, %s,%s)"
    values = ("2016", kek, drt, sh,tre)
    cursor.execute(query, values)
    db.commit()
    i += 1
