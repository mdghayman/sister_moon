import tdl

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

def handle_keys():
    global player_x, player_y
    user_input = tdl.event.key_wait()
    #movement keys
    if user_input.key == 'UP':
        player_y -= 1
    elif user_input.key == 'DOWN':
        player_y += 1
    elif user_input.key == 'LEFT':
        player_x -=1
    elif user_input.key == 'RIGHT':
        player_x +=1
    #toggle fullscreen and exit game
    if user_input.key == 'ENTER' and user_input.alt:
        tdl.set_fullscreen(not tdl.get_fullscreen())
    elif user_input.key == 'ESCAPE':
        return True

tdl.set_font('dejavu16x16_gs_tc.png', greyscale=True, altLayout=True)
root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Sister Moon", fullscreen=False)
con = tdl.Console(SCREEN_WIDTH, SCREEN_HEIGHT)

player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

while not tdl.event.is_window_closed():

    root.draw_char(player_x, player_y, '@', bg=None, fg=(255,255,255))

    tdl.flush()

    root.draw_char(player_x, player_y, ' ', bg = None)

    #handle keys and exit game if needed
    exit_game = handle_keys()
    if exit_game:
        break
