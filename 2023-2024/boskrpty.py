import keyboard, time
time.sleep(5) # You have 5 seconds to switch to the window where you want to write the text.

StartingEntry = 505148
Count = 50
StartNumber = 116

keyboard.write("insert into item_template(entry, name, displayid,  BuyCount, BuyPrice, stackable, description, ItemLimitCategory) values\n")
for i in range(Count):
    keyboard.write(f"({StartingEntry+i}, 'Lístek do tomboly', 3331, 1, 2500, 1, 'číslo {StartNumber+i}', 500),\n")