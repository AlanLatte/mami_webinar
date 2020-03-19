import os

get_abs_path_folder = lambda folder_name: os.path.join(os.getcwd(),\
    str(folder_name))

INPUT_DIR_PATH = get_abs_path_folder(folder_name="input")
OUTPUT_DIR_PATH = get_abs_path_folder(folder_name="output")
print(INPUT_DIR_PATH)
print(OUTPUT_DIR_PATH)

HEADERS = {
            'content-type' : 'application/x-www-form-urlencoded',
            'x-auth-token' : '62c679c0340cd0b1aca7b34099384f54'}
ROOMS = [
            (19396587, 'W000'),
            (19396923, 'W001'),
            (19399433, 'W002'),
            (19400763, 'W003'),
            (19400927, 'W004'),
            (19401063, 'W005'),
            (19401177, 'W006'),
            (19401261, 'W007'),
            (19401371, 'W008'),
            (19401461, 'W009'),
            (19401575, 'W010'),
            (19401637, 'W011'),
            (19401779, 'W012'),
            (19401867, 'W013'),
            (19401949, 'W014'),
            (19401995, 'W015'),
            (19402063, 'W016'),
            (19402111, 'W017'),
            (19402163, 'W018'),
            (19402415, 'W019'),
            (19403759, 'W020'),
            (19403825, 'W021'),
            (19403907, 'W022'),
            (19403967, 'W023'),
            (19404011, 'W024'),
            (19404071, 'W025'),
            (19404105, 'W026'),
            (19404155, 'W027'),
            (19404225, 'W028'),
            (19404285, 'W029'),
            (19404335, 'W030'),
            (19399427, 'W031'),
            (19399937, 'W032'),
            (19400887, 'W033'),
            (19400977, 'W034'),
            (19401089, 'W035'),
            (19401173, 'W036'),
            (19401297, 'W037'),
            (19401423, 'W038'),
            (19401487, 'W039'),
            (19399731, 'W040'),
            (19401649, 'W041'),
            (19401781, 'W042'),
            (19401833, 'W043'),
            (19401873, 'W044'),
            (19401955, 'W045'),
            (19401981, 'W046'),
            (19402021, 'W047'),
            (19402079, 'W048'),
            (19402105, 'W049'),
            (19402153, 'W050'),
            (19402413, 'W051'),
            (19403377, 'W052'),
            (19403429, 'W053'),
            (19403469, 'W054'),
            (19403505, 'W055'),
            (19403541, 'W056'),
            (19403585, 'W057'),
            (19403617, 'W058'),
            (19403633, 'W059'),
            (19403669, 'W060'),
            (19403895, 'W062'),
            (19403925, 'W063'),
            (19403971, 'W064'),
            (19404007, 'W065'),
            (19404171, 'W066'),
            (19404201, 'W067'),
            (19404235, 'W068'),
            (19404263, 'W069'),
            (19404313, 'W070'),
            (19404685, 'W071'),
            (19404715, 'W072'),
            (19404753, 'W073'),
            (19404795, 'W074'),
            (19404811, 'W075'),
            (19404845, 'W076'),
            (19397643, 'W077'),
            (19398001, 'W078'),
            (19398539, 'W079'),
            (19398781, 'W080'),
            (19416453, 'W081'),
            (19416501, 'W082'),
            (19416549, 'W083'),
            (19416583, 'W084'),
            (19416619, 'W085'),
            (19416785, 'W087'),
            (19416821, 'W088'),
            (19416867, 'W089'),
            (19416911, 'W090'),
            (19416963, 'W091'),
            (19417029, 'W092'),
            (19417057, 'W093'),
            (19417083, 'W094'),
        ]
