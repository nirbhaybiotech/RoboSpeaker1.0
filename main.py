import os

if __name__ == '__main__':
    os.system("PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Welcome to RoboSpeaker 1.0 Created by Nirbhay')\"")
    while True:
        x = input("Enter what you want me to speak")
        if x == "quit":
            os.system("PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('bye, see you soon!')\"")
            break
        command = f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')\""
        os.system(command)
