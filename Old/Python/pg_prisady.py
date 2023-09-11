import pyautogui as pg
import time
prisady = [501245,501629,501311,501825,501246,501265,501268,501314,501315,501278,501277,501560,501849,501943,501946,501949,501977]
entry = 502273
slot = 5
endl = ','
time.sleep(5)
#pg.write(f'select * from item_template where entry in ({prisady}) order by find_in_set(entry,"{prisady}");\n')
pg.write(f'insert into npc_vendor(entry,slot,item,extendedcost) values\n')
pg.press('tab')
#for i in range :
#    pg.write(f'-- prisada = {prisady[i]}\n')
#    pg.write(f'insert into item_template(entry,`name`,quality,flags,requiredreputationrank,`description`) values ({entry+i},"Vacek s {prisady[i]}",1,4,4,"Obsahuje 5ks dane suroviny");\n')
#    pg.write(f'insert into item_loot_template(entry,item,mincount,maxcount) values ({entry+i},{prisady[i]},5,5);\n')

for i in range (len(prisady)):
    if i >= len(prisady)-1:
        endl = ';'
    pg.write(f'(5000704,{slot+i},{entry+i},5025){endl}\n')
   
