from subprocess import call

start = 26
to = 3*60+17
num_frames = (to-start)*2
call('ffmpeg -ss 00:00:26.0 -i "evo2014 gf.mp4" -an -filter:v "setpts=PTS/29.97, crop=280:50:360:60" -frames:v '+str(num_frames)+' -f image2 "Mango Hbox Evo 2014 game 1\\time\\output_%05d.png"',shell=True)

# crop=out_w:out_h:x:y
# Seeking:
# -ss hh:mm:ss.0 BEFORE -i OR IT WILL BE REALLY SLOW
# -to 00:03:17.0 after -i "file" for end time
# -t hh:mm:ss.0 for length after -i "file"

# ffmpeg -i "input.mp4" -ss 00:00:30.0 -t 00:00:10.0 -filter:v "setpts=PTS/30, crop=out_w:out_h:x:y" -an -f image2 "output_%05.png"

# Grab n frames : -frames:v n
# put after -i "file"

# 4:3 --> 720p = 960 x 720

# Smash crops (for a 720p video with the 4:3 Smash screen flush with the left side)
# crop=230:90:30:615 P1 percents
# crop=280:50:360:60 Timer
