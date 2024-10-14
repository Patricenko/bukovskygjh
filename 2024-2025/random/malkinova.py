import keyboard, time
f = open("malkinova.csv", "r")
lines = f.readlines()
f.close()
for i in range(len(lines)):
    lines[i] = lines[i].strip().split(";")
time.sleep(5)
for i in range(len(lines)):
    entry = lines[i][0]
    slot = lines[i][1]
    item = lines[i][2]
    price = lines[i][3]
    keyboard.write(f"insert into npc_vendor (entry, slot, item, ExtendedCost) values ({entry},{slot},{item},5016);\n")
    #keyboard.write(f"delete from npc_vendor where entry={entry} and slot={slot} and item={item};\n")
    time.sleep(0.1)
    keyboard.write(f"update item_template set BuyPrice = {price} where entry = {item};\n")
    time.sleep(0.1)