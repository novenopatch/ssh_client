import getpass
from fabric import Connection, Config
from save import Save
from Enumeration import SaveData

import pygame
import pygame_gui

save = Save()
server_address = save.get_data(SaveData.SERVER_ADDRESS)
password = save.get_data(SaveData.PASSWORD)
user = save.get_data(SaveData.USER)
port = save.get_data(SaveData.PORT)
alias = save.get_data(SaveData.ALIAS)
# config = Config(overrides={'sudo':{'password':password}})


message_start = "Enter Command :"
message_rest = "Enter the rest or " + "Enter to end" + ' :'


def return_command(run: str, alias: dict) -> str:
    command = ""
    run_split = run.split(" ")
    if run == command:
        return command
    else:
        for part in run_split:
            if part in [i for i in alias]:
                command = command + " " + part.replace(part, alias[part])
            else:
                command = command + " " + part
        return command





def run_command(conn: Connection, command: str):
    result_command = ""
    try:
        result_command = conn.run(command)
    except Exception as e:
        result_command = e
    finally:
        return result_command


# launch()
save.save_data()

pygame.init()

pygame.display.set_caption('Ssh client')
window_surface = pygame.display.set_mode((800, 700))
manager = pygame_gui.UIManager((800, 700))

background = pygame.Surface((800, 700))
background.fill(manager.ui_theme.get_colour('dark_bg'))

console_window = pygame_gui.windows.UIConsoleWindow(rect=pygame.rect.Rect((1, 43), (800, 600)),
                                                    manager=manager)
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((640, 630), (150, 40)),
                                            text='Exit',
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True
connection = Connection(server_address, user=user, port=port, connect_kwargs={"password": password}, )
while is_running:
    time_delta = clock.tick(60) / 1000.0
    # print(console_window.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if (event.type == pygame_gui.UI_CONSOLE_COMMAND_ENTERED and event.ui_element == console_window):
            command = event.command
            command = return_command(command, alias)
            str_result = f"{command} \n {run_command(connection, command)}"
            console_window.add_output_line_to_log(str_result, remove_line_break=False)
            if command == 'clear':
                console_window.clear_log()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
        console_window.process_event(event)
        manager.process_events(event)
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
