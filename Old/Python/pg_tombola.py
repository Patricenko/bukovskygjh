import pyautogui as pg
import time
entry = 502188
endl = ','
time.sleep(5)
pg.write(f'insert into item_template(`entry`,`name`,`displayid`,`description`) values\n')
pg.press('tab')
for i in range (79):
    if i >= 78:
        endl = ';'
    pg.write(f'({entry+i},"Listek do tomboly",3331,"cislo {i+37}"){endl}\n', interval=0.005)
