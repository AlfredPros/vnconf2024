
## Part #0: Testing #################################################################################################################################
label start:
    
    scene black
    
    pause

    play music crystal_blue fadein 1

    show text "{color=[cblue]}Audio Test{/color}" as text1:
        align(0.5, 0.2)
    show screen line_align(0.5, 0.05, 500, color=cblue, grad=True)
    show text "Use Headphones for better experience" as text2:
        align(0.5, 0.8)
    show screen pan_oscillation_sin
    with diss_diag
        
    pause
    
    hide text1
    hide text2
    hide screen line_align
    hide screen pan_oscillation_sin
    with diss_diag
    
    $ renpy.music.set_pan(0, 0, channel='music')
    
    stop music fadeout 1

    jump part1
    

## Part #1: Introduction ############################################################################################################################
label part1:
    
    show text "Hello !" with diss_diag:
        align(0.5, 0.5)
    
    pause
    
    hide text with diss_diag
    
    pause
    
    show text "{size=[size_h1]}AlfredPros{/size}" as text1:
        align(0.186, 0.24)
    show alfred:
        size(512, 512)
        align(0.15, 0.625)
    with diss_diag
        
    pause
    
    show text "{size=[size_h4]}- Ren'Py programmer for over 6 years{/size}" as text2 with diss_diag:
        anchor(0, 0) pos(800, 400)
    pause
    show text "{size=[size_h4]}- Lead programmer in Mycorrhiza{/size}" as text3 with diss_diag:
        anchor(0, 0) pos(800, 510)
    pause
    show text "{size=[size_h4]}- First time as a speaker here >.<{/size}" as text4 with diss_diag:
        anchor(0, 0) pos(800, 620)
    pause
    show text "{size=[size_h4]}- Made this entire presentation in Ren'Py!{/size}" as text5 with diss_diag:
        anchor(0, 0) pos(800, 730)
    pause
    
    scene black with diss_diag
    
    pause
    
    show text "{size=[size_h1]}Tim Reichert{/size}":
        align(0.173, 0.24)
    show tim_video:
        size(512, 512)
        align(0.15, 0.625)
    with diss_diag
    
    pause
    
    show text "{size=[size_h4]}- Composer, sound designer, audio director{/size}" as text2 with diss_diag:
        anchor(0, 0) pos(800, 400)
    pause
    show text "{size=[size_h4]}- Project lead and writer in Mycorrhiza{/size}" as text3 with diss_diag:
        anchor(0, 0) pos(800, 510)
    pause
    show text "{size=[size_h4]}- Talked about dynamic audio last year{/size}" as text4 with diss_diag:
        anchor(0, 0) pos(800, 620)
    pause
    show text "{size=[size_h4]}- He is good at singing! (gasp){/size}" as text5 with diss_diag:
        anchor(0, 0) pos(800, 730)
    pause
    
    scene black with diss_diag
        
    pause
    
    show text "{size=[size_h1]}{color=[cyellow]}Disclaimer!{/color}{/size}" as text1:
        align(0.5, 0.25)
    show screen line_align(0.5, 0.15, 500, color=cyellow, grad=True)
    show text "{size=[size_h3]}- Contains Ren'Py and Python code{/size}" as text2:
        anchor(0, 0) pos(500, 450)
    show text "{size=[size_h3]}- Some math is involved{/size}" as text3:
        anchor(0, 0) pos(500, 600)
    show text "{size=[size_h3]}- Source code is available in GitHub{/size}" as text4:
        anchor(0, 0) pos(500, 750)
    with diss_diag
        
    pause
    
    hide screen line_align
    scene black 
    with diss_diag
        
    pause
    
    jump part2
    
    # Skipped this part because it's not as useful
    show text "{size=[size_h1]}{color=[cblue]}Outline{/color}{/size}" as text1:
        align(0.5, 0.2)
    show screen line_align(0.5, 0.13, 400, color=cblue, grad=True)
    show text "{size=[size_h3]}1. What is Dynamic Audio?{/size}" as text2:
        anchor(0, 0) pos(500, 400)
    with diss_diag
    pause
    show text "{size=[size_h3]}2. Player's Action{/size}" as text3 with diss_diag:
        anchor(0, 0) pos(500, 525)
    pause
    show text "{size=[size_h3]}3. Randomization{/size}" as text4 with diss_diag:
        anchor(0, 0) pos(500, 650)
    pause
    show text "{size=[size_h3]}4. Closing{/size}" as text5 with diss_diag:
        anchor(0, 0) pos(500, 775)
    
    pause
    
    hide screen line_align
    scene black 
    with diss_diag
    
    pause
    
    jump part2
    

## Part #2: What is Dynamic Audio? ##################################################################################################################
label part2:
    
    show text "“ Dynamic audio is audio that is {color=[cyellow]}modified{/color}, or which's \nsequence is modified \
{color=[cyellow]}during gameplay{/color}. The change \ncan be a result of a {color=[cyellow]}player's actions{/color}, conscious \nor \
unconscious, or variables being {color=[cyellow]}randomized{/color} independent of a player's actions. ”" as text1:
        align(0.5, 0.4)
    show text "— Tim Reichert" as text2:
        align(0.5, 0.8)
    with diss_diag
    
    pause
    
    scene black with diss_diag
    
    pause
    
    show text "{size=[size_h1]}{color=[cyellow]}Key Points{/color}{/size}" as text1:
        align(0.5, 0.3)
    show screen line_align(0.5, 0.24, 540, color=cyellow, grad=True)
    with diss_diag
    pause
    show text "#1: Player's actions" as text2 with diss_diag:
        anchor(0, 0) pos(650, 500) zoom 1.0
    pause
    show text "#2: Randomization" as text3 with diss_diag:
        anchor(0, 0) pos(650, 665)
        
    pause 
    
    show text "#1: Player's actions" as text2:
        anchor(0, 0) pos(650, 500) zoom 1.0
        ease_quad 0.4 zoom 1.05
        ease_quad 0.4 zoom 1.0
    
    pause
    
    hide screen line_align
    scene black 
    with diss_diag
    
    pause
    
    jump part3a
    

## Part #3: Common Use Case #########################################################################################################################
label part3a:
    
    scene i_hubhousehallwayday with Dissolve(1)  # He is enjoying surfing through the internet; and suddenly-
    
    play music gentleness
    
    show dialogue1 "What a productive day so far... Surfing the internet."
    
    pause
    
    scene i_hubhousehallwaynight  # He realises that he had to go outside and touch some grass
    play music splatters
    
    show dialogue1 "Oh no! I forgot to do my groceries!"
    
    pause
    
    scene black4k with Dissolve(1):
        pos(0,0)
    stop music fadeout 2
    
    pause
    
    show i_hubhousehallwayday with Dissolve(1)  # He is enjoying surfing through the internet; and suddenly-
    
    play music gentleness
    
    show dialogue1 "What a productive day so far... Surfing the internet."
    
    pause
    
    camera:
        zoom 1.0
        ease 1.5 zoom 0.4
    
    pause 1.0
    
    $ code_text = ["{color=[cyellow]}scene{/color} house_light",
        "{color=[cyellow]}play{/color} music gentleness",
        "\"{color=[cgreen]}What a productive day ...{/color}\"",
        "{color=[cyellow]}pause{/color}", 
        ""]
    
    show screen show_code(900, 175) with diss_diag
    
    pause
    
    show i_hubhousehallwaynight as i_hubhousehallwayday  # He realises that he had to go outside and touch some grass
    
    play music splatters
    
    show dialogue1 "Oh no! I forgot to do my groceries!"
    
    $ code_text += ["{color=[cyellow]}scene{/color} house_dark",
        "{color=[cyellow]}play{/color} music splatters",
        "\"{color=[cgreen]}Oh no! I forgot ...{/color}\"",
        "{color=[cyellow]}pause{/color}"]
    
    pause
    
    show screen border_pos_morph(875, 250, 665, 85,  875, 250, 665, 85,  border_color=cblue) with diss_diag
    
    pause
    
    show screen border_pos_morph(875, 250, 665, 85,  875, 665, 635, 85,  border_color=cblue)
    
    pause
    
    stop music fadeout 2
    camera:
        zoom 1.0
    scene black
    hide screen show_code
    hide screen border_pos_morph
    with diss_diag
    
    pause
    
    
    show text "{size=[size_h1]}{color=[cblue]}Audio Channels{/color}{/size}" as text1:
        align(0.5, 0.25)
    show screen line_align(0.5, -0.3, 840, color=cblue, grad=True)
    show text "{size=[size_h3]}- Default audio channels are {color=[cblue]}music{/color}, {color=[cgreen]}sound{/color}, and {color=[cred]}voice{/color}{/size}" as text2:
        anchor(0, 0) pos(300, 450)
    show text "{size=[size_h3]}- Each audio channels can only play {color=[cyellow]}one{/color} audio at a time{/size}" as text3:
        anchor(0, 0) pos(300, 600)
    show text "{size=[size_h3]}- You can {color=[cyellow]}queue{/color} multiple audios in a channel{/size}" as text4:
        anchor(0, 0) pos(300, 750)
    with diss_diag
        
    pause
    
    scene black4k:
        pos(0,0)
    hide screen line_align
    with diss_diag
    
    pause
        
    
    show text "{size=[size_h1]}{color=[cblue]}Crossfade{/color}{/size}":
        align(0.5, 0.5)
    
    play music tendra_fi_inst_intro
    queue music tendra_fi_inst
    
    pause
    
    show text "{size=[size_h1]}{color=[cblue]}Crossfade{/color}{/size}":
        ease_quad 0.75 align(0.5, 0.2)
        
    pause 0.01
    
    $ renpy.show_screen("crossfade_channel1", 400, 450, _layer="master")
    with diss_diag
    
    pause
    pause
    
    jump switch_crossfade
    
label switch_crossfade:  # Jankness - Note: This doesn't sound seamless in Ren'Py 7.6/8.1 due to audio fadein/fadeout behavior change.
    if crossfade_switched:
        if renpy.music.is_playing(channel="music"):
            play sound "<sync music loop 0.0>" + tendra_fi loop fadein 2
            stop music fadeout 2
    else:
        if renpy.music.is_playing(channel="sound"):
            play music "<sync sound loop 0.0>" + tendra_fi_inst fadein 2
            stop sound fadeout 2
    
    pause
    pause
        
    jump part3b
    
label part3b:
    
    camera:
        zoom 1.0
        ease_quad 2.0 zoom 0.4
    
    pause 1.0
    
    $ passed_switch_crossfade = True
    
    $ code_text = ["{color=[cyellow]}if{/color} switch_to_music:",
        "    {color=[cyellow]}play{/color} {color=[cblue]}music{/color} \"<sync {color=[cgreen]}sound{/color} loop 0.0>\" + {color=[cpurple]}tendra_fi_inst{/color} fadein 2",
        "    {color=[cyellow]}stop{/color} {color=[cgreen]}sound{/color} fadeout 2",
        "{color=[cyellow]}else{/color}:", 
        "    {color=[cyellow]}play{/color} {color=[cgreen]}sound{/color} \"<sync {color=[cblue]}music{/color} loop 0.0>\" + {color=[cpurple]}tendra_fi{/color} loop fadein 2 ",
        "    {color=[cyellow]}stop{/color} {color=[cblue]}music{/color} fadeout 2"]
    
    show screen show_code(150, 500, size_h4) with diss_diag
    
    pause
    
    show screen border_pos_morph(140, 490, 500, 80,  140, 490, 500, 80,  border_color=cblue) with diss_diag  # If
    
    pause
    
    show screen border_pos_morph(140, 490, 500, 80,  230, 560, 1560, 150,  border_color=cblue)  # 2 lines
    
    pause
    
    show screen border_pos_morph(230, 560, 1560, 150,  230, 560, 1560, 80,  border_color=cblue) # First 2 lines
    
    pause
    
    show screen border_pos_morph(230, 560, 1560, 80,  230, 632, 550, 80,  border_color=cblue) # Second 2 lines
    
    pause
    
    show screen border_pos_morph(230, 632, 550, 80,  560, 560, 290, 80,  border_color=cblue)  # Sync sound
    
    pause
    
    show screen border_pos_morph(560, 560, 290, 80,  840, 560, 240, 80,  border_color=cblue)  # loop 0.0
    
    pause
    
    show screen border_pos_morph(840, 560, 240, 80,  230, 780, 1560, 150,  border_color=cblue) # First 2 lines
    
    pause
    
    camera:
        zoom 1.0
    stop music fadeout 2
    stop sound fadeout 2
    scene black
    hide screen crossfade_channel1
    hide screen show_code
    hide screen border_pos_morph
    with diss_diag
    
    pause
    
    show text "{color=[cred]}Issue: Audio Loading Time{/color}" as text1 with diss_diag
    
    pause
    
    show text "{color=[cred]}Issue: Audio Loading Time{/color}" as text1:
        ease_quad 0.5 align(0.5, 0.3)
        
    pause 0.01
    
    show screen arrow_align(0.5, 0.5, 180, angle=90)
    
    show text "{color=[cpurple]}Audio Channels Desync{/color}" as text2:
        align(0.5, 0.7)
    with diss_diag
        
    pause
    
    scene black
    hide screen arrow_align
    with diss_diag
    
    pause
    
    show text "Load and play both at the same time!\na.k.a {color=[cyellow]}Synchronous Start{/color}" with diss_diag
    
    pause
    
    hide text with diss_diag
    
    pause
    
    show screen crossfade_channel2(950, 50) with diss_diag
    
    pause
    
    show a1_ruralstreet with Dissolve(1)
    
    python:
        renpy.music.play("audio/hanging_in_town.opus", synchro_start=True)
        renpy.music.play("audio/hanging_in_town_bitcrush.opus", channel='sound', loop=True, synchro_start=True)
        renpy.sound.set_volume(0.0, delay=0.0)
        
    show dialogue1 "I hope it's not too late for doing grocery."
        
    pause
    
    show a1_ruralstreetnight as a1_ruralstreet with Dissolve(1)
    
    python:
        renpy.music.set_volume(0.0, delay=2.0)
        renpy.sound.set_volume(1.0, delay=2.0)
        
    show dialogue1 "Wait. Why is the sky suddenly turn darker?"
        
    pause
    
    scene black with Dissolve(2)
    
    python:
        renpy.music.set_volume(1.0, delay=2.0)
        renpy.sound.set_volume(0.0, delay=2.0)
    
    $ code_text = ["{color=[cyellow]}scene{/color} street_light",
        "{color=[cyellow]}${/color} renpy.{color=[cblue]}music{/color}.play(\"{color=[cgreen]}norm.ogg{/color}\", {color=[cred]}synchro_start{/color}=True)", 
        "{color=[cyellow]}${/color} renpy.music.play(\"{color=[cgreen]}scry.ogg{/color}\", {color=[cred]}synchro_start{/color}=True, channel='{color=[cgreen]}sound{/color}', loop=True)",
        "{color=[cyellow]}${/color} renpy.{color=[cgreen]}sound{/color}.set_volume(0.0, delay=0.0)",
        "\"{color=[cgreen]}I hope it's not too late for doing grocery.{/color}\"",
        "{color=[cyellow]}pause{/color}",
        ""]
    
    show screen show_code(100, 250, size_h5) with diss_diag
    
    pause
    
    show screen border_pos_morph(85, 300, 1750, 145,  85, 300, 1750, 145,  border_color=cblue) with diss_diag 
    
    pause
    
    show screen border_pos_morph(85, 300, 1750, 145,  770, 300, 430, 145,  border_color=cblue)
    
    pause
    
    show screen border_pos_morph(770, 300, 430, 145,  85, 430, 915, 75,  border_color=cblue)
    
    pause
    
    python:
        renpy.music.set_volume(0.0, delay=2.0, channel='music')
        renpy.music.set_volume(1.0, delay=2.0, channel='sound')
    
    $ code_text += ["{color=[cyellow]}scene{/color} street_dark",
        "{color=[cyellow]}${/color} renpy.{color=[cblue]}music{/color}.set_volume(0.0, delay=2.0)", 
        "{color=[cyellow]}${/color} renpy.{color=[cgreen]}sound{/color}.set_volume(1.0, delay=2.0)",
        "\"{color=[cgreen]}Wait. Why is the sky suddenly turn darker?{/color}\"",
        "{color=[cyellow]}pause{/color}",
        ""]
    
    show screen border_pos_morph(85, 430, 915, 75,  85, 740, 915, 145,  border_color=cblue)
    
    pause
    
    stop music fadeout 2
    stop sound fadeout 2
    hide screen crossfade_channel2
    hide screen show_code
    hide screen border_pos_morph
    with diss_diag
    
    pause
    
    show text "{color=[cblue]}Vertical Rearrangement{/color}" with diss_diag
    
    pause
    
    hide text with diss_diag
    
    pause
    
    show screen character_config with diss_diag
    
    pause
    
    hide screen character_config with diss_diag
    
    pause
    
    python:
        renpy.music.set_volume(1.0, channel='music')  # Revert back to normal
        renpy.music.set_volume(1.0, channel='back')
        renpy.music.set_volume(1.0, channel='drums')
        renpy.music.set_volume(1.0, channel='pattern')
        renpy.music.play("<sync drums loop 0>audio/chill_back1.ogg", channel='back', loop=True, synchro_start=True)
        renpy.music.play("<sync pattern loop 0>audio/chill_drums1.ogg", channel='drums', loop=True, synchro_start=True)
        renpy.music.play("<sync back loop 0>audio/chill_pattern0.ogg", channel='pattern', loop=True, synchro_start=True)
    
    show screen music_config with diss_diag
    
    pause
    
    $ renpy.music.set_volume(1.0, channel='back')
    $ renpy.music.set_volume(1.0, channel='drums')
    $ renpy.music.set_volume(0.0, channel='pattern')
    hide screen music_config 
    show screen music_config_bars
    scene a1_ruralstreetnight
    with Dissolve(1)
    
    pause
    
    show may3 with dissolve:
        xalign 1.0
    $ renpy.music.set_volume(1.0, delay=1.0, channel='pattern')
    
    pause
    
    stop back fadeout 2
    stop drums fadeout 2
    stop pattern fadeout 2
    hide screen music_config_bars
    scene black
    with Dissolve(1)
    
    pause
    
    show text "{color=[cblue]}Interactivity: Mouse Position{/color}" with diss_diag
    
    pause
    
    play music crystal_blue fadein 1

    show text "{color=[cblue]}Interactivity: Mouse Position{/color}":
        ease_quad 1.0 align(0.5, 0.2)
    pause 0.01
    show screen pan_oscillation_sin(y=660)
    with diss_diag
    
    pause
    
    hide screen pan_oscillation_sin
    show screen pan_oscillation_mouse(y=660, type="Linear", volume_change=False)
    with diss_diag
    
    pause
    
    hide screen pan_oscillation_mouse
    show screen pan_oscillation_mouse_morph(from_y=660, to_x=600, to_radius=250, volume_change=False)
    
    pause
    
    show screen pan_oscillation_mouse_morph(from_x=600, to_x=1200, from_radius=250, to_radius=150, volume_change=False)
    
    pause
    
    stop music fadeout 2
    hide screen pan_oscillation_mouse_morph
    scene black
    with diss_diag
    
    pause
    
    jump part4
    

## Part #4: Ren'Py Screen Trick #####################################################################################################################
label part4:
    
    show text "{color=[cyellow]}Screen{/color}" with diss_diag
    
    pause
    
    show text "{color=[cyellow]}Screen{/color}":
        ease_quad 1.0 yalign 0.2
    
    show screen screen_demo(1) with diss_diag
    
    pause
    
    show screen screen_demo(2)  # NANAHIRA!!!
        
    pause
    
    show screen screen_demo(3)  # Movable Nanahira!!
        
    pause
    
    show screen screen_demo(4)  # 1 Second Nanahira
        
    pause
    
    show screen screen_demo(5)  # 0.5 Second Nanahira
        
    pause
    
    show screen screen_demo(6)  # 0.1 Second Nanahira
        
    pause
    
    show screen screen_demo(7)  # 0.05 Second Nanahira
        
    pause
    
    show screen screen_demo(8)  # Mouse check
        
    pause
    
    show screen screen_demo(9)  # Mouse check (simple)
    scene black
    with diss_diag
    
    pause 0.01
    
    $ code_text = ["{color=[cblue]}default{/color} {color=[cred]}mouse_x{/color} = 0",
        "{color=[cblue]}default{/color} {color=[cpurple]}mouse_y{/color} = 0",
        "",
        "{color=[cyellow]}screen{/color} cursor_position():",
        "    {color=[cyellow]}python{/color}:", 
        "        {color=[cred]}mouse_x{/color}, {color=[cpurple]}mouse_y{/color} = renpy.get_mouse_pos()",
        "",
        "    {color=[cyellow]}text{/color} \"{color=[cgreen]}Mouse is at: ([[{color=[cred]}mouse_x{/color}], [[{color=[cpurple]}mouse_y{/color}]){/color}\"",
        "",
        "    {color=[cyellow]}timer{/color} 0.05 {color=[cblue]}action{/color} renpy.restart_interaction {color=[cyellow]}repeat{/color} True"]
    
    show screen show_code(175, 250, size_h4) with diss_diag
    
    pause
    
    show screen border_pos_morph(150, 240, 530, 150,  150, 240, 530, 150,  border_color=cblue) with diss_diag  # Defaults
    
    pause
    
    show screen border_pos_morph(150, 240, 530, 150,  150, 455, 675, 80,  border_color=cblue)  # Screen definition
    
    pause
    
    show screen border_pos_morph(150, 455, 675, 80,  260, 740, 1090, 80,  border_color=cblue)  # Text
    
    pause
    
    show screen border_pos_morph(260, 740, 1090, 80,  260, 530, 1140, 150,  border_color=cblue)  # Python
    
    pause
    
    show screen border_pos_morph(260, 530, 1140, 150,  260, 885, 1425, 80,  border_color=cblue)  # Timer
    
    pause
    
    hide screen screen_demo
    hide screen show_code
    hide screen border_pos_morph
    scene black 
    with diss_diag
    
    pause
    
    show text "{size=[size_h1]}{color=[cgreen]}Pros:{/color}{/size}" as text1:
        align(0.5, 0.25)
    show screen line_align(0.5, 0.25, 280, color=cgreen, grad=True)
    show text "{size=[size_h3]}- Allows complex screen uses{/size}" as text2:
        anchor(0, 0) pos(500, 450)
    show text "{size=[size_h3]}- Adjustable refresh time{/size}" as text3:
        anchor(0, 0) pos(500, 600)
    show text "{size=[size_h3]}- Less knowledge barrier for entry{/size}" as text4:
        anchor(0, 0) pos(500, 750)
    with diss_diag
    
    pause
    
    hide screen line_align
    scene black
    with diss_diag
    
    pause
    
    show text "{size=[size_h1]}{color=[cred]}Cons:{/color}{/size}" as text1:
        align(0.5, 0.25)
    show screen line_align(0.5, 0.25, 280, color=cred, grad=True)
    show text "{size=[size_h3]}- Globally refreshes interaction{/size}" as text2:
        anchor(0, 0) pos(350, 450)
    show text "{size=[size_h3]}- Timer cannot be set too low{/size}" as text3:
        anchor(0, 0) pos(350, 600)
    show text "{size=[size_h3]}- Doesn't work well for Ren'Py 7.5.2/8.0.2 or higher{/size}" as text4:
        anchor(0, 0) pos(350, 750)
    with diss_diag
    
    pause
    
    hide screen line_align
    scene black
    with diss_diag
    
    pause
    
    jump part5a  # "Alright, where were we?"
    

## Part #5: Advanced use Case #######################################################################################################################
label part5a:
    
    show screen math_pan(1) with diss_diag
    
    pause
    
    show screen math_pan(2)
    
    pause
    
    show screen math_pan(3)
    show screen line_pos(380, 810, 210, 3) with dissolve
    
    pause
    
    $ code_text = ["{color=[cblue]}default{/color} {color=[cred]}mouse_x{/color} = 0",
        "{color=[cblue]}default{/color} {color=[cpink]}pan_value{/color} = 0.0",
        ""]
    
    show screen show_code(700, 100, size_h6) with diss_diag
    
    pause
    
    $ code_text += ["{color=[cyellow]}screen{/color} pan_mouse({color=[cpurple]}a{/color}, {color=[cgreen]}radius{/color}=200):"]
    
    pause
    
    $ code_text += ["    {color=[cyellow]}python{/color}:", 
        "        {color=[cred]}mouse_x{/color} = renpy.get_mouse_pos()[[0]",
        ""]
    
    pause
    
    show screen math_pan(4)  # Divide to 3 sections
    
    pause
    
    $ code_text += ["        {color=[cyellow]}if{/color} {color=[cred]}mouse_x{/color} < ({color=[cpurple]}a{/color} - {color=[cgreen]}radius{/color}):",
        "            {color=[cpink]}pan_value{/color} = -1.0"]
    
    pause
    
    $ code_text += ["        {color=[cyellow]}elif{/color} {color=[cred]}mouse_x{/color} < ({color=[cpurple]}a{/color} + {color=[cgreen]}radius{/color}):",
        "            {color=[cpink]}pan_value{/color} = ({color=[cred]}mouse_x{/color} - {color=[cpurple]}a{/color}) / float({color=[cgreen]}radius{/color})"]
    
    pause
    
    $ code_text += ["        {color=[cyellow]}else{/color}:",
        "            {color=[cpink]}pan_value{/color} = 1.0",
        ""]
    
    pause
    
    $ code_text += ["        renpy.music.set_pan({color=[cpink]}pan_value{/color}, delay=0.0)",
        ""]
    
    pause
    
    $ code_text += ["    {color=[cyellow]}timer{/color} 0.05 {color=[cblue]}action{/color} renpy.restart_interaction {color=[cyellow]}repeat{/color} True"]
    
    pause
    
    hide screen math_pan
    hide screen line_pos
    hide screen show_code
    with diss_diag
    
    pause
    
    show text "You made it this far! :)" with diss_diag
    
    pause
    
    hide text with diss_diag
    
    pause
    
    show text "{size=[size_h1]}{color=[cyellow]}Key Points{/color}{/size}" as text1:
        align(0.5, 0.3)
    show screen line_align(0.5, 0.24, 540, color=cyellow, grad=True)
    show text "#1: Player's actions" as text2:
        anchor(0, 0) pos(650, 500) zoom 1.0
    show text "#2: Randomization" as text3:
        anchor(0, 0) pos(650, 665)
    with diss_diag
        
    pause 
    
    show text "#1: Player's actions" as text2:
        anchor(0, 0) pos(650, 500) zoom 1.0
        ease_quad 0.4 zoom 1.05
        ease_quad 0.4 zoom 1.0
    
    pause
    
    show text "#2: Randomization" as text3:
        anchor(0, 0) pos(650, 665) zoom 1.0
        ease_quad 0.4 zoom 1.05
        ease_quad 0.4 zoom 1.0
    
    pause
    
    hide screen line_align
    scene black4k:
        pos(0, 0)
    with diss_diag
    
    pause
    
    $ renpy.music.set_volume(1.0)
    $ renpy.sound.set_volume(1.0)
    $ renpy.music.set_pan(0.0, 0.0)
    $ renpy.sound.set_pan(0.0, 0.0)
    
    $ renpy.show_screen("random_sound_store", 1, _layer="master")
    with diss_diag
    
    pause
    pause
    
    jump part5b
    
label do_random_sound_store:
    $ random_value_store = renpy.random.randint(1, 2)
    
    play sound "audio/announcement" + str(random_value_store) + ".ogg"
    
    pause
    pause
    
    jump part5b
    
label part5b:
    
    $ renpy.show_screen("random_sound_store", 2, _layer="master")
    
    camera:
        ease_quad 1.0 ypos -160
    
    $ code_text = ["{color=[cyellow]}${/color} {color=[cred]}random_value{/color} = renpy.random.randint(1, 2)",
        "",
        "{color=[cyellow]}play{/color} {color=[cblue]}sound{/color} \"{color=[cgreen]}Sound{/color}\" + str({color=[cred]}random_value{/color}) + \"{color=[cgreen]}.ogg{/color}\"",
        ""]
    
    show screen show_code(320, 720, size_h4) with diss_diag
    
    pause
    
    camera:
        ypos 0
    hide screen show_code
    scene black
    with diss_diag
    
    pause
    
    show text "{color=[cblue]}Horizontal Rearrangement{/color}" with diss_diag
    
    pause
    
    hide text with diss_diag
    
    pause
    
    show text "{color=[cyellow]}Queue{/color}" as text1 with diss_diag:
        align(0.5, 0.3)
        
    pause
    
    show text "[back_container]" as text2 with diss_diag
    
    pause
    
    $ back_container += [0]
    show text "[back_container]" as text2 with dissolve
    
    pause
    
    $ back_container += [2]
    show text "[back_container]" as text2 with dissolve
    
    pause
    
    $ back_container += [1]
    show text "[back_container]" as text2 with dissolve
    
    pause
    
    $ back_container += [0]
    show text "[back_container]" as text2 with dissolve
    
    pause
    
    scene black with diss_diag
    
    pause
    
    $ back_container = []
    
    show screen horizontal_demo
    with diss_diag
    
    pause
    
    play music chill_back1
    
    pause
    
    stop music fadeout 2
    hide screen horizontal_demo
    scene black
    with diss_diag
    
    pause
    
    $ code_text = ["{color=[cyellow]}python{/color}:",
        "    {color=[cyellow]}for{/color} i {color=[cyellow]}in{/color} range(5):",
        "        number = renpy.random.randint(1, 3)",
        "        renpy.music.queue(\"{color=[cgreen]}chill{/color}\" + str(number) + \"{color=[cgreen]}.ogg{/color}\")"]
    
    show screen show_code(210, 420, size_h4)
    show nanahira at moveup:
        align(1.0, 1.0) alpha 0.03125 zoom 0.5
    with diss_diag
    
    pause
    
    show screen border_pos_morph(296, 480, 480, 80,  296, 480, 480, 80,  border_color=cblue) with diss_diag  # For loop
    
    pause
    
    show screen border_pos_morph(296, 480, 480, 80,  390, 555, 1275, 150,  border_color=cblue)  # Loop content
    
    pause
    
    show screen border_pos_morph(390, 555, 1275, 150,  390, 555, 920, 80,  border_color=cblue)  # Loop content
    
    pause
    
    show screen border_pos_morph(390, 555, 920, 80,  390, 625, 1275, 80,  border_color=cblue)  # Loop content
    
    pause
    
    hide screen show_code
    hide screen border_pos_morph
    scene black
    with diss_diag
    
    pause
    
    show text "That's all for now !" with diss_diag
    
    pause
    
    hide text with diss_diag
    
    pause
    
    show text "{color=[cblue]}{size=[size_h1]}Dynamic Audio Implementation{/size}{/color}" with diss_diag
    
    pause
    
    hide text with diss_diag
    
    pause
    
    jump part6
    
    
## Part #6: Closing #################################################################################################################################
label part6:
    
    show text "{color=[cyellow]}Special Thanks!{/color}\n\n- Tim Reichert{vspace=32}- Grant Sanderson{vspace=32}- BlackWing BinLan{vspace=32}- You !" with diss_diag
    
    pause
    
    hide text with diss_diag
    
    pause
    
    show text "{color=[cyellow]}Made With :{/color}\n\n- Ranim{vspace=32}- Ren'Py [renpy.version_only]" with diss_diag
    
    pause
    
    hide text with diss_diag
    
    pause
    
    show text "{color=[cblue]}Any Question ?{/color}" with diss_diag
    
    pause
    
    hide text with diss_diag
    
    pause
    
    return
    
    

## Part #7: Extras ##################################################################################################################################
label extra:
    
    show text "Welcome to the {color=[cyellow]}extra{/color} room!\n\nHere are some of the things that \ndidn't make it to the talk." with diss_diag:
        align(0.5, 0.5)
        
    pause
    
    hide text with diss_diag
    
    jump extra_hub
    
# All extra choices goes back to this hub
label extra_hub:
    
    scene multibg
    
    show screen extra_hub_choice with dissolve
    
    pause
    
    # 4 Choice:
    # - Ranim test stuffs
    # - Different panning changes
    # - Music vs Sound queue
    # - Realistic moving sound source
    
    jump extra_hub

# Ranim test stuffs
# Random stuffs. Not that important, but I just leave it here.
label extra1:
    
    hide screen extra_hub_choice
    scene black
    with dissolve
    
    show text "{color=[cblue]}Example of customizable user interface utilities{/color}" as text1 with diss_diag:
        align(0.5, 0.2)

    pause
    
    show screen test1 with diss_diag

    pause
    
    show nanahira behind text1 at moveup with diss_diag:
        xalign 0.5 alpha 0.33 zoom 2.0
        
    pause
    
    hide screen test1
    scene black
    with diss_diag
    
    pause 0.5
    
    play music gentleness
    
    scene i_hubhousehallwaynight
    show may1
    with dissolve
    
    pause 0.75
    
    show may2
    show dialogue1 "I can finally rest now that I have finished doing my groceries."
    
    pause
    
    show dialogue1 "Next time I won't forget to do my responsibilities."
    
    pause
    
    hide dialogue1
    hide may2 with dissolve
    
    pause 0.25
    
    hide may1 with dissolve
    
    pause 0.75
    
    stop music fadeout 2
    
    scene black with dissolve

    jump extra_hub

# Different panning change movements
# In here, I initially made changes in linear, sin, and quadratic. However, you can implement your own function to this as you like.
label extra2:
    
    hide screen extra_hub_choice
    scene black
    with dissolve

    show text "Pan Test" with diss_diag:
        align(0.5, 0.5)
    
    pause
    
    play music crystal_blue
    
    pause
    
    hide text
    show screen pan_oscillation(show_text=True)
    
    pause
    
    hide screen pan_oscillation
    
    pause
    
    python:
        pan_progress = 0.5
        pan_value = 0.0
    show screen pan_oscillation_sin(show_text=True)
    
    pause
    
    hide screen pan_oscillation_sin
    
    pause
    
    python:
        pan_progress = 0.5
        pan_value = 0.0
    show screen pan_oscillation(type="Quadratic", show_text=True)
    
    pause
    
    stop music fadeout 2
    python:
        pan_progress = 0.5
        pan_value = 0.0
    hide screen pan_oscillation
    scene black
    
    jump extra_hub

# Music vs Sound queue
# This section lets you play around more with queue for music and sound channels.
label extra3:
    hide screen extra_hub_choice
    scene black
    with dissolve
    
    stop music fadeout 0
    
    pause 0.1
    
    show screen horizontal_demo with diss_diag
    
    pause
    
    stop music fadeout 1
    
    hide screen horizontal_demo with diss_diag
    
    show screen horizontal_demo_sound with diss_diag
    
    pause
    
    stop sound fadeout 2
    
    hide screen horizontal_demo_sound with diss_diag
    
    jump extra_hub

# Semi-realistic moving audio source
# Note: I say "semi" because this does not include doppler effect when the audio source or mouse position moves.
label extra4:
    hide screen extra_hub_choice
    scene black
    with dissolve
    
    play music crystal_blue
    
    show screen pan_oscillation_mouse_morph(show_text=True) with diss_diag
    
    pause
    
    show screen pan_oscillation_mouse_morph(to_x=480, to_radius=200, show_text=True)
    
    pause
    
    show screen pan_oscillation_mouse_morph(480, 540, 200, 1500, 200, 400, show_text=True)
    
    pause
    
    hide screen pan_oscillation_mouse_morph with diss_diag
    
    show screen pan_oscillation_mouse(type="Quadratic", show_text=True) with diss_diag
    
    pause
    
    stop music fadeout 2
    
    hide screen pan_oscillation_mouse with diss_diag
    
    jump extra_hub
