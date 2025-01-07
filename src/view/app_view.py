import os, time


class AppView:
    def display_message(self, msg, sleep_time=0):
        print(msg)
        time.sleep(sleep_time)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

