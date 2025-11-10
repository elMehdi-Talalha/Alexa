import speech_recognition as sr
import pyautogui
import pyttsx3
import webbrowser
import psutil
import subprocess
import os
import time
import requests
import wikipedia

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
    
    def search_web(self, query):
        """Search the web using Google"""
        try:
            self.speak(f"Searching for {query}")
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            print(f"✓ Searching for: {query}")
            return True
        except Exception as e:
            self.speak("Could not search the web")
            print(f"Error: {e}")
            return False
    
    def get_weather(self, city="Oujda"):
        """Get current weather using wttr.in API"""
        try:
            self.speak(f"Getting weather for {city}")
            url = f"https://wttr.in/{city}?format=%C+%t+%h+%w"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                weather_data = response.text.strip()
                self.speak(f"The weather in {city} is {weather_data}")
                print(f"🌤️  Weather: {weather_data}")
                return True
            else:
                self.speak("Could not get weather information")
                return False
        except Exception as e:
            self.speak("Weather service is not available")
            print(f"Error: {e}")
            return False
    
    def search_wikipedia(self, query):
        """Search Wikipedia and get summary"""
        try:
            self.speak(f"Searching Wikipedia for {query}")
            wikipedia.set_lang("en")
            summary = wikipedia.summary(query, sentences=2)
            print(f"📚 Wikipedia: {summary}")
            self.speak(summary)
            return True
        except wikipedia.exceptions.DisambiguationError as e:
            self.speak(f"Multiple results found. Please be more specific")
            print(f"Options: {e.options[:3]}")
            return False
        except wikipedia.exceptions.PageError:
            self.speak(f"No Wikipedia page found for {query}")
            return False
        except Exception as e:
            self.speak("Could not search Wikipedia")
            print(f"Error: {e}")
            return False
    
    def get_news(self):
        """Get latest news headlines from NewsAPI"""
        try:
            self.speak("Fetching latest news headlines")
            # Using free news API that doesn't require key
            url = "https://saurav.tech/NewsAPI/top-headlines/category/general/us.json"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles', [])[:3]
                
                if articles:
                    self.speak("Here are the top news headlines")
                    for i, article in enumerate(articles, 1):
                        headline = article.get('title', 'No title')
                        print(f"📰 {i}. {headline}")
                        self.speak(f"Headline {i}. {headline}")
                    return True
                else:
                    self.speak("No news found")
                    return False
            else:
                self.speak("Could not fetch news")
                return False
        except Exception as e:
            self.speak("News service is not available")
            print(f"Error: {e}")
            return False
    
    def shutdown_laptop(self):
        """Shutdown laptop using Alt+F4 and Enter"""
        try:
            self.speak("Shutting down the laptop")
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(0.5)
            pyautogui.press('enter')
            print("💻 Laptop shutting down...")
            return True
        except Exception as e:
            self.speak("Could not shutdown laptop")
            print(f"Error: {e}")
            return False
    
    def search_youtube(self, query):
        """Open YouTube and search for a query"""
        try:
            self.speak(f"Searching YouTube for {query}")
            search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            print(f"✓ Searching YouTube for: {query}")
            return True
        except Exception as e:
            self.speak("Could not search YouTube")
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
        if any(word in command for word in ["stop", "exit", "quit", "goodbye", "bye"]):
            self.speak("Goodbye! Have a great day!")
            return False
        
        # Shutdown command
        if "shutdown" in command or "shut down" in command:
            self.shutdown_laptop()
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
        
        # Weather command
        elif "weather" in command:
            if "in" in command:
                city = command.split("in")[-1].strip()
                self.get_weather(city)
            else:
                self.get_weather()
        
        # News command
        elif "news" in command or "headlines" in command:
            self.get_news()
        
        # Wikipedia search command
        elif "wikipedia" in command or "who is" in command or "what is" in command or "tell me about" in command:
            query = command.replace("wikipedia", "").replace("who is", "").replace("what is", "").replace("tell me about", "").strip()
            if query:
                self.search_wikipedia(query)
            else:
                self.speak("What should I search for?")
        
        # General web search command
        elif "search" in command and "youtube" not in command:
            query = command.replace("search", "").replace("for", "").strip()
            if query:
                self.search_web(query)
            else:
                self.speak("What should I search for?")
        
        # YouTube search command
        elif "youtube" in command and "search" in command:
            query = command.replace("search youtube", "").replace("youtube search", "").replace("search on youtube", "").replace("for", "").strip()
            if query:
                self.search_youtube(query)
            else:
                self.speak("What should I search for on YouTube?")
        
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
            self.speak("I can play or pause videos. Open or close applications. Search the web and YouTube. Get weather and news. Answer questions from Wikipedia. Shutdown the laptop. And open websites.")
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
        print("   • 'Alexa search ronaldo' - Search Google")
        print("   • 'Alexa youtube search messi' - Search YouTube")
        print("   • 'Alexa weather' - Get weather in Oujda")
        print("   • 'Alexa weather in Paris' - Get weather in other city")
        print("   • 'Alexa news' - Get latest headlines")
        print("   • 'Alexa who is Einstein' - Wikipedia search")
        print("   • 'Alexa what is Python' - Wikipedia search")
        print("   • 'Alexa open [app/website]' - Open application or website")
        print("   • 'Alexa close [app]' - Close application")
        print("   • 'Alexa shutdown' - Shutdown laptop")
        print("   • 'Alexa goodbye' - Exit")
        print("\n" + "=" * 60)
        
        self.speak("Hello mehdi! I'm Alexa. I'm here to help you!")
        
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