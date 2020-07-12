from pygame import mixer
import psutil
from time import sleep
class Battery_checker:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    mixer.init()
    def play_song(self):
        print('Music Playing..')
        mixer.music.load('C:/Users/Admin/Documents/Download Intro Song   Chill intro music  10 Second(MP3_160K).mp3')
        mixer.music.play()
    def stop_song(self):
        mixer.music.stop()
    def battery_checker(self):
        while True:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            while battery.percent < 50 and not plugged:
                while True:
                    battery = psutil.sensors_battery()
                    plugged = battery.power_plugged
                    if not plugged:
                        self.play_song()
                        sleep(10)
                    if plugged:
                        self.stop_song()
            while battery.percent == 100 and plugged:
                while True:
                    battery = psutil.sensors_battery()
                    plugged = battery.power_plugged
                    if plugged:
                        self.play_song()
                        sleep(10)
                    if not plugged:
                        self.stop_song()

if __name__ == '__main__':
    bat = Battery_checker()
    bat.battery_checker()
