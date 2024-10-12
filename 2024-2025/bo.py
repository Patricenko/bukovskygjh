import time
time.sleep(10)
N = 100
item = 505585
keyboard = open("insert.txt","w")
keyboard.write("@QUEST := (select max(id) from quest_template) + 1;\n")
time.sleep(0.1)
keyboard.write("@OBJECT := (select max(entry) from gameobject_template where entry<6011577) + 1;\n")

keyboard.write("insert into quest_template(id, questtype, logtitle, logdescription, rewarditem1, rewardamount1) values\n")
for i in range(N):
    time.sleep(0.1)
    if N == (99): place = ";"
    else: place = ","
    keyboard.write(f"(@QUEST+{i},0,'Truhla s odmenou','Zjisti co truhla v sobe ukryva.', 505585, 1){place}\n")

objectinsert = "insert into gameobject_template(entry, type, displayid, name, data0) values"
objectstart = "insert into gameobject_queststarter(id,quest) values"
objectend = "insert into gameobject_questender(id,quest) values"
for i in range(N):
    time.sleep(0.1)
    keyboard.write(objectinsert + f"(@OBJECT+{i},2,259,'Truhla s odmenou',57);\n")
    time.sleep(0.1)
    keyboard.write(objectstart + f"(@OBJECT+{i},@QUEST+{i});\n")
    time.sleep(0.1)
    keyboard.write(objectend + f"(@OBJECT+{i},@QUEST+{i});\n")