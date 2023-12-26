define e = Character("Eileen")
define cblue = "#4AB2D7"
define cgreen = "#4AB8A7"
define cyellow = "#F8E500"
define cred = "#FF6F51"
define cpurple = "#D575C4"
define cpink = "#CA6C7A"
define cbrown = "#746357"
define cgray = "#1F1F1F"
define clblue = "#9ED5E6"
define cdblue = "#269DC8"
define diss_diag = ImageDissolve("disslr", 1.0, ramplen=256)
define diss = Dissolve(1.0)
define timer_dur = 0.0325
define size_h1 = 72
define size_h2 = 64  # Default size
define size_h3 = 56
define size_h4 = 48
define size_h5 = 42
define size_h6 = 36

image tim = Movie(fps=30, size=(256, 256), channel='movie', play="tim.mp4", mask="tim.mp4", mask_channel=None, loop=True)

style dialogue_text1:
    size size_h2
    align(0.5, 0.875)
    #color "#0f0f0f"
    text_align 0.5
    slow_cps True
    slow_abortable True  # Skippable only if a normal text is also skippable in the background. ""
    outlines [ (9, "#0f0f0f17", absolute(0), absolute(0)), (6, "#0f0f0f30", absolute(0), absolute(0)),  (3, "#0f0f0f90", absolute(0), absolute(0)) ]
    font "cmunss.ttf"
image dialogue1 = ParameterizedText(style="dialogue_text1")

default passed_switch_crossfade = False
define back_sequence = ["audio/chill_back1.ogg", "audio/chill_back2.ogg", "audio/chill_back3.ogg"]
define back_index = {"audio/chill_back1.ogg": "0", "audio/chill_back2.ogg": "1", "audio/chill_back3.ogg": "2", "None": "-1"}
default back_container = []

# Mouse configuration
define config.mouse = {}
define config.mouse["say"] = [("images/util/empty32.png", 0, 0)]
define config.mouse["with"] = [("images/util/empty32.png", 0, 0)]
define config.mouse["pause"] = [("images/util/cursor32.png", 0, 0)]
define config.mouse["button"] = [("images/util/empty32.png", 0, 0)]

## Transforms #######################################################################################################################################
transform moveup(y=0.5):
    yalign y+0.02
    ease_quad 1.0 yalign y
    
transform arrowhead(angle, color, alpha=1.0):
    matrixcolor TintMatrix(color)
    rotate angle
    alpha alpha
    
transform diss_show(dur=0.5):
    alpha 0.0
    ease_quad dur alpha 1.0

# Resolution: 1920, 1080

## Utility Functions ################################################################################################################################
init python:
    import math
    def sin(angle):
        return math.sin(math.radians(angle))
    def cos(angle):
        return math.cos(math.radians(angle))
        
    def round_num(num, dec_point=2):
        return (num//pow(10, -dec_point)) / float(pow(10, dec_point))
        
    def quad_left_side(x):  # Transform for 0 to 0.5. From ease_quad
        return 2 * x * x
    def quad_right_side(x):  # Transform for 0.5 to 1. From ease_quad
        return 1 - pow(-2 * x + 2, 2) / 2
    def pan_denormalize(x):  # Convert from 0 to 1 into -1 to 1
        return x * 2 - 1
        
    def distance(x, y):
        return math.sqrt((x*x)+(y*y))
    
    renpy.music.register_channel("back", "music", loop=True)
    renpy.music.register_channel("drums", "music", loop=True)
    renpy.music.register_channel("pattern", "music", loop=True)

## Utility Screens ##################################################################################################################################
screen rectangle_pos(x, y, sizex, sizey, color="#fff", alpha=1.0, transform_name=diss_show):
    zorder 1
    
    add "whi" at transform_name:
        alpha alpha
        matrixcolor TintMatrix(color)
        pos(x, y)
        size(sizex, sizey)

screen border_pos(x, y, sizex, sizey, width=3, border_color="#fff", alpha=1.0):
    zorder 1
    
    add "whi":
        alpha alpha
        matrixcolor TintMatrix(border_color)
        pos(x, y)
        size(sizex, sizey)
    add "bla":
        pos(x+width, y+width)
        size(sizex-width*2, sizey-width*2)
        
screen border_align(x, y, sizex, sizey, width=3, border_color="#fff", alpha=1.0):
    zorder 1
    
    add "whi":
        alpha alpha
        matrixcolor TintMatrix(border_color)
        align(x, y)
        size(sizex, sizey)
    add "bla":
        pos(int((1920*x) - (sizex*x-width)), int((1080*y) - (sizey*y-width)))
        size(sizex-width*2, sizey-width*2)
        
screen border_pos_circ(x, y, radius=540, width=4, border_color="#fff", alpha=1.0):
    zorder 1
    
    add "whicirl":
        alpha alpha
        matrixcolor TintMatrix(border_color)
        pos(x, y)
        size(radius*2, radius*2)
    add "whicirl":
        matrixcolor TintMatrix("#000")
        pos(x+width, y+width)
        size((radius-width)*2, (radius-width)*2)

default morph_progress = 0.0
default morth_change = 0.0
default curr_x = 0
default curr_y = 0
default curr_sizex = 0
default curr_sizey = 0
default curr_radius = 0
screen border_pos_morph(from_x, from_y, from_sizex, from_sizey, to_x, to_y, to_sizex, to_sizey, duration_multiplier=1.0, width=4, border_color="#fff", alpha=1.0):
    zorder 1
 
    python:
        morph_progress += (timer_dur/2)*duration_multiplier
        if morph_progress > 1.0:
            morph_progress = 1.0
            
        if morph_progress < 0.5:
            morph_change = quad_left_side(morph_progress)
        else:
            morph_change = quad_right_side(morph_progress)
        
        curr_x = from_x + int((to_x-from_x)*morph_change)
        curr_y = from_y + int((to_y-from_y)*morph_change)
        curr_sizex = from_sizex + int((to_sizex-from_sizex)*morph_change)
        curr_sizey = from_sizey + int((to_sizey-from_sizey)*morph_change)
            
    use border_pos(curr_x, curr_y, curr_sizex, curr_sizey, width, border_color, alpha)
 
    if morph_progress != 1.0:
        timer timer_dur/2 action renpy.restart_interaction repeat True
    
screen line_pos(x, y, length, width=3, angle=0, color="#fff", grad=False):
    zorder 1
    
    if grad:
        add "gradline":
            matrixcolor TintMatrix(color)
            pos(x, y)
            size(length, width)
            rotate angle
    else:
        add "whi":
            matrixcolor TintMatrix(color)
            pos(x, y)
            size(length, width)
            rotate angle

screen line_align(x, y, length, width=3, angle=0, color="#fff", grad=False, offx=0, offy=0):
    zorder 1
    
    if grad:
        add "gradline":
            matrixcolor TintMatrix(color)
            align(x, y)
            size(length, width)
            rotate angle
            offset(offx, offy)
    else:
        add "whi":
            matrixcolor TintMatrix(color)
            align(x, y)
            size(length, width)
            rotate angle
            offset(offx, offy)

screen arrow_pos(x, y, length, width=32, angle=0, color="#fff", alpha=1.0):
    zorder 1
    
    frame at arrowhead(angle, color, alpha):
        background Frame("arrowhead", Borders(0, 1, 31, 1))
        area(x, y-(length//2), length, width)
        
screen arrow_align(x, y, length, width=32, angle=0, color="#fff"):
    zorder 1
    
    frame at arrowhead(angle, color):
        background Frame("arrowhead", Borders(0, 1, 31, 1))
        area(int((1920*x) - (max(length, width) * x)), int((1080*y) - (max(length, width) * y)), length, width)  # A hacky implementation of positioning.

transform xadasd:
    alpha 0.5
default dur = 0.0
default curr = 0.0
default progress = 0.0
default amplitude = 1.0
screen audio_progress(x, y, width=720, height=80, channel="music", color="#fff", show_text=False):
    zorder 1
    
    python:
        dur = renpy.music.get_duration(channel=channel)
        curr = renpy.music.get_pos(channel=channel)
        
        
        if dur != None and curr != None and dur != 0:
            progress = curr/dur
        else:
            progress = 0.0
            
        if renpy.music.is_playing(channel=channel):
            amplitude = renpy.audio.audio.get_channel(channel).context.secondary_volume + 0.25
        else:
            amplitude = 0.25
        
    
    # Box
    use border_pos(x, y, width, height, 5, color, alpha=amplitude)
    
    # Line
    use line_pos(x+int(width*progress)-(height//2), y, height, 5, angle=90)
    
    if show_text:
        text channel + " (" + str((progress // 0.001) * 0.1) + "%)":
            color color
            pos(x+width+32, y+height-80)

    timer timer_dur action renpy.restart_interaction repeat True


## Slide Screens ####################################################################################################################################
screen test1():
    zorder 2
    
    # Box
    use border_pos(355, 410, 500, 600, 3)
    use border_align(0.75, 0.85, 500, 600, 3, cyellow)
    
    # Text
    text "Test 1":
        align(0.3, 0.675)
    text "Test 2":
        align(0.7, 0.675)
        
    # Line
    use line_pos(400, 500, 100, 4)
    use line_pos(450, 500, 110, 5, 60, cred)
    use line_align(0.5, 0.0, 1024, color=cgreen, grad=True, offy=-200)
        
    # Arrow
    use arrow_pos(1200, 500, 110, 28)
    use arrow_pos(1240, 540, 100, 32, 120, cpurple)
    use arrow_align(0.5, 0.67, 140, 32, 0, cgreen)


default pan_progress = 0.5  # From 0 to 1 (linear)
default pan_value = 0.0  # From -1 to 1
default pan_go_up = True
default volume_progress = 1.0  # From 0 to 1 (linear)
default volume_value = 1.0  # From 0 to 1

screen pan_oscillation(x=960, y=540, type="Linear", show_text=False):
    zorder 2
    
    python:
        if pan_go_up == True:
            pan_progress += 0.01
        else:
            pan_progress -= 0.01
        
        if pan_progress >= 1.0:
            pan_go_up = False
        elif pan_progress <= 0.0:
            pan_go_up = True
        
        # Linear
        if type == "Linear":
            pan_value = pan_progress*2-1.0
        elif type == "Quadratic":
            if pan_progress < 0.5:
                pan_value = pan_denormalize( quad_left_side(pan_progress) )
            else:
                pan_value = pan_denormalize( quad_right_side(pan_progress) )
        else:
            pan_value = 0.0
            
        renpy.music.set_pan(pan_value, 0, channel='music')
    
    # Arrow
    if pan_value >= 0.0:
        use arrow_pos(x, y, int(pan_value*200), width=32, angle=0, color="#fff")
    else:
        use arrow_pos(x+1+int(pan_value*200), y, int(-pan_value*200), width=32, angle=180, color="#fff")
    
    # Text
    if show_text:
        text "Pan: [type]":
            align(0.5, 0.25)
        text str(round_num(pan_value, 5)):
            align(0.5, 0.75)
        
    timer timer_dur action renpy.restart_interaction repeat True

screen pan_oscillation_sin(x=960, y=540, show_text=False):
    zorder 2
    
    python:
        pan_progress += 1.5
        
        # Sin
        pan_value = sin(pan_progress)
        
        renpy.music.set_pan(pan_value, 0, channel='music')
    
    # Arrow
    if pan_value >= 0.0:
        use arrow_pos(x, y, int(pan_value*200), width=32, angle=0, color="#fff")
    else:
        use arrow_pos(x+1+int(pan_value*200), y, int(-pan_value*200), width=32, angle=180, color="#fff")
    
    # Text
    if show_text:
        text "Pan: sin(x)":
            align(0.5, 0.25)
        text str(round_num(pan_value, 5)):
            align(0.5, 0.75)
        
    timer timer_dur action renpy.restart_interaction repeat True

default mouse_x = 0
default mouse_y = 0
screen pan_oscillation_mouse(x=960, y=540, radius=300, type="Linear", volume_change=True, show_text=False):
    zorder 2
    
    python:
        mouse_x, mouse_y = renpy.get_mouse_pos()
        
        # Pan
        if mouse_x < x-radius:
            pan_progress = 0.0
        elif mouse_x < x+radius:
            pan_progress = (mouse_x - x + radius) / float(2 * radius)
        else:
            pan_progress = 1.0
            
        # Volume (distance to a point)
        if volume_change:
            volume_progress = 1.0 - distance((mouse_x-x)/float(radius), (mouse_y-y)/float(radius))
        else:
            volume_progress = 1.0
        
        # Linear
        if type == "Linear":
            pan_value = pan_progress*2-1.0
            
            if volume_progress < 0.0:
                volume_value = 0.0
            else:
                volume_value = volume_progress
        elif type == "Quadratic":
            if pan_progress < 0.5:
                pan_value = pan_denormalize( quad_left_side(pan_progress) )
            else:
                pan_value = pan_denormalize( quad_right_side(pan_progress) )
                
            if volume_progress < 0.0:
                volume_value = 0.0
            elif volume_progress < 0.5:
                volume_value = quad_left_side(volume_progress)
            else:
                volume_value = quad_right_side(volume_progress)
        else:
            pan_value = 0.0
            volume_value = 1.0
        
        renpy.music.set_volume(volume_value, channel="music")
        renpy.music.set_pan(pan_value, 0, channel='music')
    
    # Radius
    use border_pos_circ(x-radius, y-radius, radius, width=4, border_color=cblue)
    
    # Arrow
    if pan_value >= 0.0:
        use arrow_pos(x, y, int(pan_value*200), width=32, angle=0, color="#fff", alpha=volume_value)
    else:
        use arrow_pos(x+1+int(pan_value*200), y, int(-pan_value*200), width=32, angle=180, color="#fff", alpha=volume_value)
        
    # Text
    if show_text:
        text "Type: [type]":
            align(0.5, 0.3)
        text "Pan: " + str(round_num(pan_value, 5)):
            align(0.5, 0.75)
        text "Volume: " + str(round_num(volume_value, 5)):
            align(0.5, 0.85)
        text "Mouse: (" + str(mouse_x) + ", " + str(mouse_x) + ")":
            align(0.5, 0.95)
        
    timer timer_dur action renpy.restart_interaction repeat True
    
screen pan_oscillation_mouse_simple(x=960, y=540, radius=200, show_text=False):
    zorder 2
    
    python:
        mouse_x = renpy.get_mouse_pos()[0]
        
        # Pan 
        if mouse_x < x-radius:
            pan_value = -1.0
        elif mouse_x < x+radius:
            pan_value = (mouse_x - x) / float(radius)
        else:
            pan_value = 1.0
            
        renpy.music.set_pan(pan_value, 0.0)
    
    # Radius
    use border_pos_circ(x-radius, y-radius, radius, width=4, border_color=cblue)
    
    # Arrow
    if pan_value >= 0.0:
        use arrow_pos(x, y, int(pan_value*200), width=32, angle=0, color="#fff")
    else:
        use arrow_pos(x+1+int(pan_value*200), y, int(-pan_value*200), width=32, angle=180, color="#fff")
        
    # Text
    if show_text:
        text "Pan: " + str(round_num(pan_value, 5)):
            align(0.5, 0.75)
        text "Mouse: (" + str(mouse_x) + ", " + str(mouse_x) + ")":
            align(0.5, 0.95)
        
    timer timer_dur action renpy.restart_interaction repeat True
    
screen pan_oscillation_mouse_morph(from_x=960, from_y=540, from_radius=300, to_x=960, to_y=540, to_radius=300, duration_multiplier=1.0, type="Linear", volume_change=True, show_text=False):
    zorder 2
 
    python:
        morph_progress += (timer_dur/2)*duration_multiplier
        if morph_progress > 1.0:
            morph_progress = 1.0
            
        if morph_progress < 0.5:
            morph_change = quad_left_side(morph_progress)
        else:
            morph_change = quad_right_side(morph_progress)
        
        curr_x = from_x + int((to_x-from_x)*morph_change)
        curr_y = from_y + int((to_y-from_y)*morph_change)
        curr_radius = from_radius + int((to_radius-from_radius)*morph_change)
            
    use pan_oscillation_mouse(x=curr_x, y=curr_y, radius=curr_radius, type=type, volume_change=volume_change, show_text=show_text)
    
    if morph_progress != 1.0:
        timer timer_dur/2 action renpy.restart_interaction repeat True

screen all_channel_test():
    zorder 2
    use audio_progress(200, 200, color=cblue, show_text=True)
    use audio_progress(200, 350, color=cgreen, channel="sound", show_text=True)
    use audio_progress(200, 500, color=cred, channel="voice", show_text=True)

default crossfade_switched = False
screen crossfade_channel1(x, y):
    zorder 2
    
    use audio_progress(x, y, color=cblue, show_text=True)
    use audio_progress(x, y+200, color=cgreen, channel="sound", show_text=True)
    
    textbutton "Switch":
        align(0.5, 0.875)
        text_size size_h3
        sensitive passed_switch_crossfade == False
        
        action ToggleVariable("crossfade_switched"), Jump("switch_crossfade")
        
    button:
        area(0,0,100,100)
        keysym "z"
        sensitive passed_switch_crossfade == False
        
        action Jump("part3b")
        
screen crossfade_channel2(x, y):
    zorder 2
    
    use audio_progress(x, y, width=480, color=cblue, show_text=True)
    use audio_progress(x, y+125, width=480, color=cgreen, channel="sound", show_text=True)

default code_text = [""]
screen show_code(x, y, size=size_h3, code_text=code_text):
    zorder 2
    vbox:
        spacing size//4
        pos(x, y)
        
        for i in code_text:
            text i at diss_show:
                size size
                font "cmunbtl.ttf"

default may_base_visible = True
default may_eyes_visible = True
default may_mouth_visible = True
default may_base = 1
default may_eyes = 1
default may_mouth = 1
screen character_config():
    zorder 2
    
    if may_base_visible:
        add "may_base" + str(may_base) at diss_show(0.2):
            xpos 200
    if may_eyes_visible:
        add "may_eyes" + str(may_eyes) at diss_show(0.2):
            xpos 200
    if may_mouth_visible:
        add "may_mouth" + str(may_mouth) at diss_show(0.2):
            xpos 200
    
    vbox:
        spacing 40
        pos(1100, 400)
        
        hbox:
            textbutton "Base : ":
                text_size size_h4
                action SetVariable("may_base", may_base+1), If(may_base>2, true=(SetVariable("may_base", 1)))
            textbutton str(may_base_visible):
                text_size size_h4
                action ToggleVariable("may_base_visible")
        
        hbox:
            textbutton "Eyes : ":
                text_size size_h4
                action SetVariable("may_eyes", may_eyes+1), If(may_eyes>1, true=(SetVariable("may_eyes", 1)))
            textbutton str(may_eyes_visible):
                text_size size_h4
                action ToggleVariable("may_eyes_visible")
                
        hbox:
            textbutton "Mouth : ":
                text_size size_h4
                action SetVariable("may_mouth", may_mouth+1), If(may_mouth>1, true=(SetVariable("may_mouth", 1)))
            textbutton str(may_mouth_visible):
                text_size size_h4
                action ToggleVariable("may_mouth_visible")

default chill_back_play = True
default chill_drums_play = True
default chill_pattern_play = True
default chill_back = 1
default chill_drums = 1
default chill_pattern = 1
screen music_config_bars(x=300, y=200):
    zorder 2
    
    text "{color=[cblue]}Back ([chill_back]){/color}":
        pos(x, y)
    use audio_progress(x, y+100, color=cblue, channel="back")
    text "{color=[cgreen]}Drums ([chill_drums]){/color}":
        pos(x, y+250)
    use audio_progress(x, y+350, color=cgreen, channel="drums")
    text "{color=[cred]}Pattern ([chill_pattern]){/color}":
        pos(x, y+500)
    use audio_progress(x, y+600, color=cred, channel="pattern")
    
screen music_config(show_debug = False):
    zorder 2
    
    python:
        if chill_back_play:
            renpy.music.set_volume(1.0, channel="back")
        else:
            renpy.music.set_volume(0.0, channel="back")
            
        if chill_drums_play:
            renpy.music.set_volume(1.0, channel="drums")
        else:
            renpy.music.set_volume(0.0, channel="drums")
            
        if chill_pattern_play:
            renpy.music.set_volume(1.0, channel="pattern")
        else:
            renpy.music.set_volume(0.0, channel="pattern")
            
        if renpy.music.is_playing(channel='back') and str(renpy.music.get_playing(channel='back')) != "<sync drums loop 0>audio/chill_back"+str(chill_back)+".ogg":
            renpy.music.play("<sync drums loop 0>audio/chill_back"+str(chill_back)+".ogg", channel='back', loop=True)
        if renpy.music.is_playing(channel='drums') and str(renpy.music.get_playing(channel='drums')) != "<sync pattern loop 0>audio/chill_drums"+str(chill_drums)+".ogg":
            renpy.music.play("<sync pattern loop 0>audio/chill_drums"+str(chill_drums)+".ogg", channel='drums', loop=True)
        if renpy.music.is_playing(channel='pattern') and str(renpy.music.get_playing(channel='pattern')) != "<sync back loop 0>audio/chill_pattern"+str(chill_pattern)+".ogg":
            renpy.music.play("<sync back loop 0>audio/chill_pattern"+str(chill_pattern)+".ogg", channel='pattern', loop=True)
    
    use music_config_bars
    
    if show_debug:
        vbox:
            text str(renpy.music.get_playing(channel='back'))
            text str(renpy.music.get_playing(channel='drums'))
            text str(renpy.music.get_playing(channel='pattern'))
    
    vbox:
        spacing 40
        pos(1150, 400)
        
        hbox:
            textbutton "Back : ":
                text_size size_h4
                action SetVariable("chill_back", chill_back+1), If(chill_back>2, true=(SetVariable("chill_back", 1)))
            textbutton str(chill_back_play):
                text_size size_h4
                action ToggleVariable("chill_back_play")
        
        hbox:
            textbutton "Drums : ":
                text_size size_h4
                action SetVariable("chill_drums", chill_drums+1), If(chill_drums>2, true=(SetVariable("chill_drums", 1)))
            textbutton str(chill_drums_play):
                text_size size_h4
                action ToggleVariable("chill_drums_play")
                
        hbox:
            textbutton "Pattern : ":
                text_size size_h4
                action SetVariable("chill_pattern", chill_pattern+1), If(chill_pattern>3, true=(SetVariable("chill_pattern", 1)))
            textbutton str(chill_pattern_play):
                text_size size_h4
                action ToggleVariable("chill_pattern_play")

default nanahira_x = 0.5
default nanahira_y = 0.65
screen screen_demo(phase=1):
    zorder 2
    
    if phase != 9:
        use border_pos(500, 350, 900, 600)
    
    if phase == 2:
        add "nanahira" at diss_show:
            align(0.5, 0.65)
    
    elif phase == 3:
        add "nanahira":
            align(nanahira_x, nanahira_y)
        
        vbox at diss_show:
            align(0.9, 0.625)
            spacing 12
            textbutton "Move Her Up!":
                action SetVariable("nanahira_y", nanahira_y-0.01)
            textbutton "Move Her Down!":
                action SetVariable("nanahira_y", nanahira_y+0.01)
            textbutton "Move Her Left!":
                action SetVariable("nanahira_x", nanahira_x-0.01)
            textbutton "Move Her Right!":
                action SetVariable("nanahira_x", nanahira_x+0.01)
    
    elif phase == 4:
        text "Timer: 1 seconds":
            align(0.5, 0.975)
        add "nanahira" at diss_show:
            align(nanahira_x, 0.65)
            
        textbutton "Reset Her!":
            align(0.84, 0.625)
            action SetVariable("nanahira_x", 0.5)
    
        timer 1 action SetVariable("nanahira_x", nanahira_x+0.01) repeat True
        
    elif phase == 5:
        text "Timer: 0.5 seconds":
            align(0.5, 0.975)
        add "nanahira":
            align(nanahira_x, 0.65)
            
        textbutton "Reset Her!":
            align(0.84, 0.625)
            action SetVariable("nanahira_x", 0.5)
    
        timer 0.5 action SetVariable("nanahira_x", nanahira_x+0.005) repeat True
        
    elif phase == 6:
        text "Timer: 0.1 seconds":
            align(0.5, 0.975)
        add "nanahira":
            align(nanahira_x, 0.65)
            
        textbutton "Reset Her!":
            align(0.84, 0.625)
            action SetVariable("nanahira_x", 0.5)
    
        timer 0.1 action SetVariable("nanahira_x", nanahira_x+0.001) repeat True
    
    elif phase == 7:
        text "Timer: 0.05 seconds":
            align(0.5, 0.975)
        add "nanahira":
            align(nanahira_x, 0.65)
            
        textbutton "Reset Her!":
            align(0.84, 0.625)
            action SetVariable("nanahira_x", 0.5)
    
        timer 0.05 action SetVariable("nanahira_x", nanahira_x+0.0005) repeat True
    
    elif phase == 8:
        python:
            mouse_x, mouse_y = renpy.get_mouse_pos()
        
        text "Timer: 0.05 seconds":
            align(0.5, 0.975)
        text "Mouse is at: ([mouse_x], [mouse_y])" at diss_show:
            pos(625, 625)
        
        timer 0.05 action renpy.restart_interaction repeat True
    
    elif phase == 9:
        python:
            mouse_x, mouse_y = renpy.get_mouse_pos()
        
        text "Mouse is at: ([mouse_x], [mouse_y])" at diss_show:
            pos(625, 75)
        
        timer 0.05 action renpy.restart_interaction repeat True
    
screen math_pan(phase=1):
    zorder 2
    
    text "{color=[cgreen]}radius{/coloe} = 200":
        align(0.14, 0.1)
    
    if phase >= 4:
        use rectangle_pos(0, 230, 200, 420, cblue, 0.5)
        use rectangle_pos(200, 230, 400, 420, cgreen, 0.5)
        use rectangle_pos(600, 230, 75, 420, cred, 0.5)
    
    #use border_pos_circ(260, 240, 200, width=4, border_color=cblue)
    use pan_oscillation_mouse_simple(400, 440, 200)
    
    use line_pos(200, 480, 400, 5)
    
    text "({color=[cpurple]}a{/color}, b)":
        pos(380, 460)
    
    if phase >= 2:
        
        text "-1" at diss_show:
            pos(170, 690)
        
        text "0" at diss_show:
            pos(380, 690)
        
        text "1" at diss_show:
            pos(580, 690)
    
    if phase >= 3:
        
        text "f({color=[cred]}x{/color}) = " at diss_show:
            pos(180, 870)
            
        text "{color=[cred]}x{/color} - {color=[cpurple]}a{/color}" at diss_show:
            pos(420, 820)
            
        text "{color=[cgreen]}radius{/color}" at diss_show:
            pos(400, 930)

default button_clicked_store = False
default random_value_store = 0
screen random_sound_store(type=1):
    zorder 2
    
    if type == 1:
        textbutton "Click Me !":
            text_size size_h2
            align(0.3, 0.5)
            action Jump("do_random_sound_store")
    else:
        textbutton "Click Me !":
            text_size size_h2
            align(0.3, 0.5)
            action SetVariable("button_clicked_store", True), SetVariable("random_value_store", renpy.random.randint(1, 2))
    
    if random_value_store == 0:
        use line_pos(850, 470, 130, 4, color=cgray)
    else:
        use line_pos(850, 470, 130, 4, color=cblue)
    
    if random_value_store == 1:
        use line_pos(882, 338, 195, 4, 90, color=cblue)
        use line_pos(980, 275, 130, 4, color=cblue)
        text "{color=[clblue]}Sound 1{/color}":
            align(0.7, 0.3)
    else:
        use line_pos(882, 338, 195, 4, 90, color=cgray)
        use line_pos(980, 275, 130, 4, color=cgray)
        text "{color=[cgray]}Sound 1{/color}":
            align(0.7, 0.3)
        
    if random_value_store == 2:
        use line_pos(882, 537, 195, 4, 90, color=cblue)
        use line_pos(980, 665, 130, 4, color=cblue)
        text "{color=[clblue]}Sound 2{/color}":
            align(0.7, 0.7)
    else:
        use line_pos(882, 537, 195, 4, 90, color=cgray)
        use line_pos(980, 665, 130, 4, color=cgray)
        text "{color=[cgray]}Sound 2{/color}":
            align(0.7, 0.7)
    
    if type == 2:
        if button_clicked_store:
            timer timer_dur action SetVariable("button_clicked_store", False), Play("sound", "audio/announcement" + str(random_value_store) + ".ogg")

default curr_queue = []
screen horizontal_demo():
    python:
        if len(renpy.audio.audio.get_channel('music').queue) != 0:
            curr_queue = []
            for i in renpy.audio.audio.get_channel('music').queue:
                curr_queue.append( int(back_index[i.filename]) )
        else:
            curr_queue = []
    
    text "Queue: [curr_queue]":
        align(0.5, 0.3)
    
    text "Currently playing: " + back_index[str(renpy.music.get_playing(channel='music'))] :
        pos(420, 590)
    use audio_progress(420, 700, color=cblue, show_text=True)
    
    hbox:
        align(0.5, 0.4)
        spacing 32
        
        textbutton "Add":
            action Queue("music", back_sequence[renpy.random.randint(0, 2)], clear_queue=False)
        textbutton "Reset Queue":
            action SetField(renpy.audio.audio.get_channel('music'), "queue", [])
        textbutton "Stop Music":
            action Stop("music")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
