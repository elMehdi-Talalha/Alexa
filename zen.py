import speech_recognition as sr
import pyautogui
import pyttsx3
import webbrowser
import psutil
import subprocess
import os
import time

class ZenAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        self.video_playing = False
        self.programming_mode = False
        
    def speak(self, text):
        """Make Zen speak"""
        print(f"🧘 Zen: {text}")
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
            print(f"🎤 Zen is listening... Say 'Zen' first!")
            
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
            if not url.startswith('http') and not url.startswith('file'):
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
            
            # Special handling for specific apps
            app_paths = {
                "vscode": "code",
                "vs code": "code",
                "visual studio code": "code",
                "spotify": "spotify",
            }
            
            if app_name.lower() in app_paths:
                subprocess.Popen(app_paths[app_name.lower()], shell=True)
            else:
                pyautogui.press('win')
                time.sleep(0.3)
                pyautogui.write(app_name, interval=0.05)
                time.sleep(0.3)
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
                "git": "git.exe",
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
    
    def start_programming_session(self):
        """Start a complete programming session"""
        try:
            self.speak("Starting your programming session. Opening Spotify, VS Code, Pomodoro Timer, and Chrome.")
            self.programming_mode = True
            
            print("\n🚀 Launching Programming Session...")
            print("=" * 60)
            
            # 1. Open Spotify
            print("🎵 Opening Spotify...")
            self.open_application("spotify")
            time.sleep(2)
            
            # 2. Open VS Code
            print("💻 Opening VS Code...")
            self.open_application("vscode")
            time.sleep(2)
            
            # 3. Open Pomodoro Timer in Chrome
            print("⏰ Opening Pomodoro Timer...")
            pomodoro_path = "file:///C:/Users/bismiallah/Desktop/Python/CLOCK/pomodoro-timer/website-clock-pomodoro/src/index.html"
            self.open_website(pomodoro_path)
            time.sleep(2)
            
            # 4. Open additional Chrome tabs
            print("🌐 Opening Chrome...")
            websites = [
                "https://github.com",
                "https://stackoverflow.com",
                "https://chatgpt.com"
            ]
            
            for site in websites:
                self.open_website(site)
                time.sleep(1)
            
            print("=" * 60)
            print("✅ Programming session ready!")
            self.speak("Programming session is ready. Good luck with your coding!")
            
            return True
        except Exception as e:
            self.speak("There was an error starting the programming session")
            print(f"Error: {e}")
            return False
    
    def end_programming_session(self):
        """End programming session"""
        try:
            self.speak("Ending programming session. Closing applications.")
            self.programming_mode = False
            
            # Close applications
            time.sleep(1)
            self.close_application("spotify")
            time.sleep(1)
            self.close_application("vscode")
            time.sleep(1)
            self.close_application("chrome")
            
            self.speak("Programming session ended. Great work!")
            return True
        except Exception as e:
            self.speak("Could not end programming session")
            print(f"Error: {e}")
            return False
    
    def process_command(self, command):
        """Process Zen commands"""
        if command is None:
            return True
        
        # Check if command starts with "zen"
        if not command.startswith("zen"):
            print("💡 Tip: Start your command with 'Zen'")
            return True
        
        # Remove "zen" from command
        command = command.replace("zen", "").strip()
        
        # Exit commands
        if any(word in command for word in ["stop", "exit", "quit", "goodbye", "bye", "shutdown"]):
            self.speak("Goodbye Mehdi! Stay focused and productive!")
            return False
        
        # Programming session commands
        if "start programming session" in command or "programming session" in command:
            self.start_programming_session()
        elif "end programming session" in command or "stop programming session" in command:
            self.end_programming_session()
        
        # Focus mode
        elif "focus mode" in command or "enter focus mode" in command:
            self.speak("Entering focus mode. Minimize distractions and maximize productivity.")
            # Close distracting apps
            for app in ["discord", "whatsapp", "instagram"]:
                self.close_application(app)
        
        # Video control commands
        elif any(word in command for word in ["play video", "start video", "play the video"]):
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
                "chat gpt": "chatgpt.com",
                "claude": "claude.ai",
                "spotify": "spotify.com",
                "github": "github.com",
                "stackoverflow": "stackoverflow.com",
                "stack overflow": "stackoverflow.com",
                "reddit": "reddit.com",
                "twitter": "twitter.com",
                "linkedin": "linkedin.com",
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
        
        # System status
        elif "how are you" in command or "status" in command:
            if self.programming_mode:
                self.speak("I'm here and ready. Programming mode is active. Let's build something amazing!")
            else:
                self.speak("I'm here and ready to help you stay focused and productive!")
        
        # Help command
        elif "help" in command or "what can you do" in command:
            self.speak("I'm Zen, your productivity assistant.")
            self.speak("Say start programming session to launch your full coding environment.")
            self.speak("I can also play or pause videos, open or close applications, and open websites.")
            self.speak("Say focus mode to minimize distractions.")
        else:
            self.speak("I didn't understand that command. Say Zen help for assistance.")
        
        return True
    
    def run(self):
        """Main loop"""
        print("=" * 60)
        print("🧘 ZEN VOICE ASSISTANT - PRODUCTIVITY MODE")
        print("=" * 60)
        print("\n📋 POWER COMMANDS:")
        print("   • 'Zen start programming session' - Launch full coding setup")
        print("   • 'Zen end programming session' - Close all coding apps")
        print("   • 'Zen focus mode' - Close distracting apps")
        print("   • 'Zen play video' - Play video")
        print("   • 'Zen pause video' - Pause video")
        print("   • 'Zen open [app/website]' - Open application or website")
        print("   • 'Zen close [app]' - Close application")
        print("   • 'Zen goodbye' - Exit")
        print("\n" + "=" * 60)
        
        self.speak("Hello Mehdi! I'm Zen, your productivity assistant. How can I help you focus today?")
        
        while True:
            try:
                command = self.listen()
                should_continue = self.process_command(command)
                
                if not should_continue:
                    break
                
            except KeyboardInterrupt:
                self.speak("Goodbye Mehdi! Stay productive!")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    zen = ZenAssistant()
    zen.run()