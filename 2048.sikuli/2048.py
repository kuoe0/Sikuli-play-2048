import random
import datetime
action = [Key.UP, Key.DOWN, Key.LEFT, Key.RIGHT]
game_ret_region= Region(487,574,469,13)
game_title_region = Region(474,176,189,61)
try_again_region = Region(608,674,114,35)

openApp("Safari")
switchApp("Safari")

wait(2);
type("l", KeyModifier.CMD)
type("http://gabrielecirulli.github.io/2048/")
type(Key.ENTER)
game_title_region.wait("1394957412539.png", 10)

start_time = datetime.datetime.now()
play_cnt = 0

while True:
   
    key_cnt = 0;
    game_ret = None
    while True:
        if not game_title_region.exists("1394957412539.png", 0.001):
            game_ret = "Exit"
            break
        if try_again_region.exists("1394958980132.png", 0.001):
            game_ret = "Over"
            break
        for i in xrange(10):       
            type(action[random.randint(0,3)])
            key_cnt = key_cnt + 1


    if game_ret == "Exit":
        break
    else:
        play_cnt = play_cnt + 1
          
        if game_ret_region.exists("1394957657032.png", 0.001):
            game_ret = "Lose" 
        # if game_ret_region.exists("1394926064512.png", 0.001):
        else:
            game_ret = "Win"
       
    
    if game_ret == "Lose":
        click("1394958980132.png")
    if game_ret == "Win":
        break
           
    wait(0.1)

end_time = datetime.datetime.now()

print "From: ", start_time
print "To:   ", end_time
print "Play ", play_cnt, " times."
if game_ret == "Win":
    print "Win finally!"