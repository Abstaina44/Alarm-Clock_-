from playsound import playsound

def play_sound(file_path):
    playsound(file_path)

sound_file = "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages"
play_sound(sound_file)

from datetime import datetime

while True:
    alarm_time = input("Enter the time of alarm to be set (HH:MM:SS AM/PM): ")
    try:
        alarm_datetime = datetime.strptime(alarm_time, "%I:%M:%S %p")
        break
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM:SS AM/PM format.")

print("Setting up alarm..")
while True:
    now = datetime.now()
    if now >= alarm_datetime:
        print("Wake Up!")
        playsound('audio.mp3')
        break