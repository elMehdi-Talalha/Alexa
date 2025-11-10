import speech_recognition as sr
import pyautogui
import pyttsx3
import webbrowser
import psutil
import subprocess
import os

class AlexaAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        self.video_playing = False
        
    def speak(self, text):
        """Make Alexa speak"""
        print(f"🤖 Alexa: {text}")
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    
    def listen(self):
        """Listen for voice commands"""
        with sr.Microphone() as source:
            print("\n📊 Calibrating...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print(f"🎤 Alexa is listening... Say 'Alexa' first!")
            
            try:
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=10)
                print("🔄 Processing...")
                
                command = self.recognizer.recognize_google(audio, language='en-US').lower()
                print(f"✓ You said: '{command}'")
                return command
            except sr.UnknownValueError:
                print("❌ Could not understand")
                return None
            except sr.WaitTimeoutError:
                print("⏱️  Timeout - no speech detected")
                return None
            except Exception as e:
                print(f"❌ Error: {e}")
                return None
    
    def control_video(self, action):
        """Control video playback with spacebar"""
        try:
            if action == "play" or action == "start":
                pyautogui.press('space')
                self.video_playing = True
                self.speak("Playing video")
                print("▶️  VIDEO PLAYING")
            elif action == "pause" or action == "stop":
                pyautogui.press('space')
                self.video_playing = False
                self.speak("Video paused")
                print("⏸️  VIDEO PAUSED")
            return True
        except Exception as e:
            self.speak("Could not control video")
            print(f"Error: {e}")
            return False
    
    def open_website(self, url):
        """Open website"""
        try:
            self.speak(f"Opening {url}")
            if not url.startswith('http'):
                url = 'https://' + url
            webbrowser.open(url)
            print(f"✓ Opened {url}")
            return True
        except Exception as e:
            self.speak("Could not open website")
            print(f"Error: {e}")
            return False
    
    def open_application(self, app_name):
        """Open application"""
        try:
            self.speak(f"Opening {app_name}")
            pyautogui.press('win')
            pyautogui.write(app_name, interval=0.05)
            pyautogui.press('enter')
            print(f"✓ {app_name} opened")
            return True
        except Exception as e:
            self.speak(f"Could not open {app_name}")
            print(f"Error: {e}")
            return False
    
    def close_application(self, app_name):
        """Close application by name"""
        try:
            self.speak(f"Closing {app_name}")
            
            # App name mappings to process names
            process_map = {
                "chrome": "chrome.exe",
                "google chrome": "chrome.exe",
                "notepad": "notepad.exe",
                "calculator": "calculatorapp.exe",
                "calc": "calculatorapp.exe",
                "word": "winword.exe",
                "excel": "excel.exe",
                "powerpoint": "powerpnt.exe",
                "git" : "git",
                "discord": "discord.exe",
                "steam": "steam.exe",
                "vscode": "code.exe",
                "vs code": "code.exe",
                "spotify": "spotify.exe",
                "whatsapp": "whatsapp.exe",
            }
            
            # Find process name
            process_name = process_map.get(app_name.lower(), f"{app_name}.exe")
            
            # Kill the process
            killed = False
            for proc in psutil.process_iter(['name']):
                try:
                    if process_name.lower() in proc.info['name'].lower():
                        proc.kill()
                        killed = True
                        print(f"✓ Closed {proc.info['name']}")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            if killed:
                self.speak(f"{app_name} closed")
                return True
            else:
                self.speak(f"{app_name} is not running")
                return False
                
        except Exception as e:
            self.speak(f"Could not close {app_name}")
            print(f"Error: {e}")
            return False
    
    def process_command(self, command):
        """Process Alexa commands"""
        if command is None:
            return True
        
        # Check if command starts with "alexa"
        if not command.startswith("alexa"):
            print("💡 Tip: Start your command with 'Alexa'")
            return True
        
        # Remove "alexa" from command
        command = command.replace("alexa", "").strip()
        
        # Exit commands
        if any(word in command for word in ["stop", "exit", "quit", "goodbye", "bye", "shutdown"]):
            self.speak("Goodbye! Have a great day!")
            return False
        
        # Video control commands
        if any(word in command for word in ["play video", "start video", "play the video"]):
            self.control_video("play")
        elif any(word in command for word in ["pause video", "stop video", "pause the video"]):
            self.control_video("pause")
        
        # Close application commands
        elif "close" in command:
            app_name = command.replace("close", "").strip()
            if app_name:
                self.close_application(app_name)
            else:
                self.speak("What should I close?")
        
        # Open commands
        elif "open" in command or "start" in command or "launch" in command:
            target = command.replace("open", "").replace("start", "").replace("launch", "").strip()
            
            # Website mappings
            websites = {
                "google": "google.com",
                "youtube": "youtube.com",
                "facebook": "facebook.com",
                "instagram": "instagram.com",
                "amazon": "amazon.com",
                "gmail": "gmail.com",
                "chatgpt": "chatgpt.com",
                "claude": "claude.ai",
                "spotify": "spotify.com",
                "github": "github.com",
            }
            
            # Check if it's a website
            is_website = False
            for key, url in websites.items():
                if key in target:
                    self.open_website(url)
                    is_website = True
                    break
            
            # If not a website, try opening as application
            if not is_website and target:
                self.open_application(target)
        
        # Help command
        elif "help" in command or "what can you do" in command:
            self.speak("I can play or pause videos. Open or close applications. And open websites.")
            self.speak("Just say Alexa followed by your command.")
        else:
            self.speak("I didn't understand that command")
        
        return True
    
    def run(self):
        """Main loop"""
        print("=" * 60)
        print("🤖 ALEXA VOICE ASSISTANT")
        print("=" * 60)
        print("\n📋 COMMANDS:")
        print("   • 'Alexa play video' - Play video")
        print("   • 'Alexa pause video' - Pause video")
        print("   • 'Alexa open [app/website]' - Open application or website")
        print("   • 'Alexa close [app]' - Close application")
        print("   • 'Alexa goodbye' - Exit")
        print("\n" + "=" * 60)
        
        self.speak("Hello mehdi! I'm Alexa. im here to help you?")
        
        while True:
            try:
                command = self.listen()
                should_continue = self.process_command(command)
                
                if not should_continue:
                    break
                
            except KeyboardInterrupt:
                self.speak("Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    alexa = AlexaAssistant()
    alexa.run()