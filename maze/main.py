from do import do_maze

# do_maze("labyrinth_00.json")

# do it for 00 to 99
for i in range(99):
    try:
        do_maze("labyrinth_{:02d}.json".format(i))
    except:
         print("failed on {}".format(i))
         continue
