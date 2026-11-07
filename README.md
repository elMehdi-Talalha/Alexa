# ALEXA – DESKTOP VOICE ASSISTANT

**Technical Project Report**

**Prepared by:** Mehdi Talalha  
**Institution:** Mehdi Ben Berka Secondary School  
**Academic Year:** 2026–2027  
**Date:** November 2026

---

# Table of Contents

1. Introduction
2. Project Presentation and Objectives
3. Functional and Technical Requirements
4. Technologies Used
5. System Architecture and Design
6. Implementation and Development
7. Testing and Evaluation
8. Conclusion
9. References

---

# 1. Introduction

Most of the time, when we want to do something on a computer, we use a keyboard or a mouse. This works perfectly well, but I became interested in finding another way to interact with a computer, one that would allow me to give instructions simply by speaking.

This idea led me to develop **Alexa**, a desktop voice assistant using Python.

The principle behind the project is quite simple: the user gives a voice command, the program recognizes what was said, and then performs the requested action. For example, instead of opening a browser and searching for YouTube manually, the user can simply say: "Alexa, open YouTube."

To make this possible, I used several Python libraries. Each one has a different role, from recognizing speech to controlling the keyboard and managing running applications.

The project was also an opportunity for me to put what I have learned in programming into practice, especially object-oriented programming, conditional statements, loops, and the use of external libraries.

# 2. Project Presentation and Objectives

## 2.1. Project Overview

Alexa is a desktop voice assistant that I developed to perform some everyday computer operations through voice commands.

To interact with it, the user first needs to say the keyword **"Alexa"**, followed by the desired instruction.

Here are some examples of commands supported by the application:

- "Alexa, open YouTube."
- "Alexa, open Visual Studio Code."
- "Alexa, close Chrome."
- "Alexa, play video."
- "Alexa, pause video."
- "Alexa, goodbye."

Once a command is received, the program processes it and tries to identify the action requested by the user. It then calls the appropriate function and, whenever possible, gives a spoken response to confirm what happened.

## 2.2. Project Objectives

When I started working on this project, I wanted to build something practical rather than just write a program that displays information on the screen.

I focused on a few main objectives:

- **Voice control:** Make it possible to interact with the computer without typing every instruction.
- **Opening websites:** Access frequently used websites through simple commands.
- **Application management:** Launch or close selected desktop applications.
- **Video control:** Play and pause videos using voice instructions.
- **Voice responses:** Allow the assistant to respond instead of displaying messages only in the terminal.
- **Time saving:** Make some common computer operations quicker and easier.

I also wanted to keep the code organized so that I could add more commands and features later.

# 3. Functional and Technical Requirements

Before starting the implementation, I identified the main operations that the assistant needed to perform.

## 3.1. Functional Requirements

The following table summarizes the functionalities I planned to include in the project.

| ID | Requirement | Description |
|---|---|---|
| FR01 | Voice recognition | Capture the user's voice and convert it into text. |
| FR02 | Activation keyword | Check whether the command starts with "Alexa". |
| FR03 | Website navigation | Open predefined websites in the default browser. |
| FR04 | Application launching | Open desktop applications through the Windows Start menu. |
| FR05 | Application termination | Find and terminate selected running processes. |
| FR06 | Video control | Play or pause videos using keyboard automation. |
| FR07 | Voice responses | Respond to the user using a computer-generated voice. |
| FR08 | Help system | Inform the user about the available commands. |
| FR09 | Application exit | Stop the assistant when an exit command is received. |

## 3.2. Hardware Requirements

Since the application relies on voice interaction, it needs a few basic hardware components:

- **Computer:** A machine running Windows.
- **Microphone:** Used to capture the user's voice.
- **Speakers or headphones:** Used to hear Alexa's responses.
- **Internet connection:** Required for Google's online speech recognition service.

## 3.3. Software Requirements

The software requirements are:

- **Operating system:** Microsoft Windows.
- **Programming language:** Python 3.
- **Libraries:** SpeechRecognition, PyAutoGUI, pyttsx3, and psutil.
- **Development environment:** Any Python-compatible code editor or IDE.

# 4. Technologies Used

I chose Python for this project mainly because it is relatively easy to work with and offers a large number of libraries for automation and system interaction.

Instead of implementing everything from scratch, I used existing libraries, each responsible for a specific part of the application.

## 4.1. SpeechRecognition

The first library I needed was **SpeechRecognition**, since the whole project depends on understanding what the user says.

It allows the program to capture audio through a microphone and convert spoken words into text.

I mainly used two functions:

- `recognize_google()`: Sends the recorded audio to Google's speech recognition service and returns the recognized sentence.
- `adjust_for_ambient_noise()`: Helps the recognizer adapt to the surrounding noise before recording.

For example, when I say "Alexa, open YouTube", the library converts my speech into text so that the rest of the program can process it.

## 4.2. PyAutoGUI

**PyAutoGUI** is the library I used whenever Alexa needed to interact with the keyboard.

One of its main uses in my project is opening desktop applications through the Windows Start menu.

Here is the code responsible for this operation:

```python
pyautogui.press('win')
pyautogui.write(app_name, interval=0.05)
pyautogui.press('enter')
```

The program presses the Windows key, types the application's name, and presses Enter.

I also used PyAutoGUI to simulate the spacebar when controlling video playback.

## 4.3. pyttsx3

I didn't want Alexa to communicate only through text displayed in the terminal. I wanted it to have spoken responses as well.

For this reason, I used **pyttsx3**, a library that converts text into speech.

It also allowed me to configure some voice settings, such as:

- **Voice:** Selects one of the available voices.
- **Rate:** Controls the speaking speed.
- **Volume:** Adjusts the volume of the generated speech.

This library is used whenever Alexa needs to respond to the user.

## 4.4. Webbrowser

The `webbrowser` module is part of Python's standard library, so there was no need to install it separately.

I used it to open websites in the default browser.

For example, if the user asks Alexa to open YouTube, the program finds the corresponding URL and passes it to the browser.

## 4.5. psutil

I also wanted Alexa to be able to close applications, not just open them.

For this purpose, I used **psutil**.

This library gives access to information about processes running on the computer. The program searches for the process associated with the requested application and attempts to terminate it.

For example, Chrome normally runs under the process name `chrome.exe`.

## 4.6. subprocess and os

I also imported the `subprocess` and `os` modules.

Both are included in Python's standard library and provide additional ways to interact with the operating system.

However, although they are imported in the current project, they are not directly used by the implemented functionalities.

# 5. System Architecture and Design

Before writing the different functions, I needed to think about how the application would work as a whole.

I decided to organize the project around a main class called `AlexaAssistant`. This allowed me to keep the different operations together instead of writing everything in one large block of code.

## 5.1. General Architecture

The assistant works through a sequence of operations.

It all starts when the user speaks. The microphone captures the audio, SpeechRecognition converts it into text, and the program checks whether the instruction starts with "Alexa".

After that, the command is analyzed and the corresponding function is called.

The general process can be summarized as follows:

1. The user gives a voice command.
2. The microphone captures the audio.
3. SpeechRecognition converts the audio into text.
4. The program checks for the activation keyword.
5. The command is analyzed.
6. The requested operation is executed.
7. Alexa responds to the user.

**Figure 1: General Architecture of the Application**

*[Insert the general architecture diagram here.]*

## 5.2. Class Structure

I used **Object-Oriented Programming (OOP)** to organize the application.

The main class, `AlexaAssistant`, contains the methods responsible for the different operations.

Here are the main methods:

| Method | Role |
|---|---|
| `__init__()` | Initializes the recognizer and the assistant's settings. |
| `speak()` | Makes Alexa respond using speech synthesis. |
| `listen()` | Captures and recognizes voice commands. |
| `control_video()` | Handles video playback commands. |
| `open_website()` | Opens a website in the browser. |
| `open_application()` | Launches a desktop application. |
| `close_application()` | Attempts to close a running application. |
| `process_command()` | Analyzes the command and selects the appropriate action. |
| `run()` | Keeps the assistant running and listening for instructions. |

I found this organization useful because each method has a clear purpose. If I need to modify how Alexa opens websites, for example, I can work on that particular method without having to rewrite the entire application.

## 5.3. Command Processing

Recognizing speech is only part of the job. The program also needs to understand what the user wants to do.

For this reason, I used conditional statements such as `if`, `elif`, and `else` inside the command-processing function.

The program checks the recognized sentence and compares it with different predefined conditions.

For example:

- If the command contains **"close"**, the program identifies the application that needs to be closed.
- If it contains **"open"**, Alexa checks whether the requested name exists in the website dictionary.
- If the requested name is not found among the websites, the program attempts to open it as a desktop application.
- Other conditions handle video playback, help requests, and exit commands.

This is a relatively simple approach, but it was sufficient for the commands I wanted to support in this version.

# 6. Implementation and Development

Once I had the general structure in mind, I started implementing the different parts of the assistant.

I worked on the functionalities separately and then connected them through the command-processing method.

## 6.1. Initializing the Assistant

The first thing I implemented was the initialization method.

It creates the speech recognizer and defines some settings that affect how the assistant listens.

```python
def __init__(self):
    self.recognizer = sr.Recognizer()
    self.recognizer.energy_threshold = 300
    self.recognizer.dynamic_energy_threshold = True
    self.recognizer.pause_threshold = 0.8
    self.video_playing = False
```

There are a few parameters worth explaining:

- **`energy_threshold`:** Defines the initial audio energy level used to detect speech.
- **`dynamic_energy_threshold`:** Allows the recognizer to adjust to changes in background noise.
- **`pause_threshold`:** Determines how long the program waits during a pause before considering the sentence finished.
- **`video_playing`:** A variable I used to keep track of the playback state.

These settings help prepare the assistant before it starts listening to commands.

## 6.2. Implementing Voice Recognition

After initialization, I worked on the listening function.

The goal was to capture the user's voice and convert it into a text command.

```python
with sr.Microphone() as source:
    self.recognizer.adjust_for_ambient_noise(
        source, duration=1
    )

    audio = self.recognizer.listen(
        source, timeout=8, phrase_time_limit=10
    )

    command = self.recognizer.recognize_google(
        audio, language='en-US'
    ).lower()
```

First, the program accesses the microphone and adjusts the recognizer to the surrounding noise.

It then records the user's speech. Once the recording is complete, `recognize_google()` sends the audio to Google's recognition service and returns the recognized sentence.

I also convert the result to lowercase. This makes it easier to compare commands without worrying about uppercase and lowercase letters.

I included exception handling as well, because speech recognition does not always work perfectly. For example, the microphone might not capture anything, or the service might fail to recognize the sentence.

## 6.3. Making Alexa Speak

I wanted the assistant to give feedback after receiving a command.

For example, if I ask it to open a website, it should be able to respond instead of remaining silent.

I implemented this using the `speak()` method and the `pyttsx3` library.

```python
def speak(self, text):
    print(f"Alexa: {text}")

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)

    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()
```

The method receives a text string and converts it into speech.

I also configured the speaking rate to 170 and the volume to 1.0. If more than one voice is available, the program selects the second one.

The response is also printed in the terminal, which makes it possible to see what Alexa is saying.

## 6.4. Opening Websites

One of the first practical features I wanted to add was opening websites through voice commands.

To do this, I created a dictionary containing the names of the websites and their corresponding addresses.

```python
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
    "github": "github.com"
}
```

When Alexa receives a command such as "open YouTube", it searches for YouTube in this dictionary.

If the website exists, the program uses the `open_website()` method and the `webbrowser` module to open it.

I chose this method because adding another website is straightforward: I only need to add its name and URL to the dictionary.

## 6.5. Opening Desktop Applications

Opening a desktop application is slightly different from opening a website.

Instead of using a URL, I needed a way for Python to interact with Windows.

I decided to use PyAutoGUI to simulate the actions normally performed by a user through the Start menu.

```python
pyautogui.press('win')
pyautogui.write(app_name, interval=0.05)
pyautogui.press('enter')
```

The process is simple:

1. Press the Windows key.
2. Type the application's name.
3. Press Enter.

For example, when I say "Alexa, open Visual Studio Code", the program searches for it through the Start menu and attempts to launch it.

## 6.6. Closing Desktop Applications

I also implemented a feature that allows Alexa to close selected applications.

For this part, I used `psutil` instead of keyboard automation.

First, I created a dictionary linking application names to their process names.

```python
process_map = {
    "chrome": "chrome.exe",
    "notepad": "notepad.exe",
    "discord": "discord.exe",
    "vscode": "code.exe",
    "spotify": "spotify.exe"
}
```

The program then searches through the running processes to find a match.

If it finds the requested application, it attempts to terminate the corresponding process using `kill()`.

If the application is not running or the operation fails, Alexa informs the user.

One thing worth mentioning is that terminating a process this way can close an application without allowing it to save unfinished work.

## 6.7. Controlling Video Playback

Another feature I added was the ability to play and pause videos using voice commands.

I used PyAutoGUI to simulate pressing the spacebar.

```python
if action == "play" or action == "start":
    pyautogui.press('space')
    self.video_playing = True
    self.speak("Playing video")

elif action == "pause" or action == "stop":
    pyautogui.press('space')
    self.video_playing = False
    self.speak("Video paused")
```

On many video platforms, the spacebar is used to play or pause a video.

Instead of controlling the video player directly, Alexa sends this keyboard command to the active window.

I also added the `video_playing` variable to keep an internal record of the playback state.

However, this method depends on the active window. If another application is selected, pressing the spacebar might perform a different action.

## 6.8. Processing Commands

At this point, the individual functionalities were ready. The next step was to connect them.

I implemented the `process_command()` method for this purpose.

It receives the recognized sentence and checks what the user wants Alexa to do.

Before processing the instruction, the program checks whether the activation keyword is present.

```python
if command is None:
    return True

if not command.startswith("alexa"):
    print("Tip: Start your command with Alexa")
    return True

command = command.replace("alexa", "").strip()
```

If no command was recognized, the function simply returns.

If the sentence does not start with "Alexa", the program ignores it and displays a short reminder.

Otherwise, it removes the activation keyword and processes the remaining text.

The function then checks the command against the different conditions implemented in the project.

Depending on the instruction, Alexa can:

- Close an application.
- Open a website.
- Launch a desktop application.
- Play or pause a video.
- Display the available commands.
- Exit the program.

If the instruction does not match any of the supported commands, Alexa responds that it did not understand.

## 6.9. Running the Assistant

The final part is the `run()` method.

Its job is to keep Alexa running instead of executing only one command and then stopping.

I used a `while` loop so that the assistant could continuously listen for new instructions.

The general process is:

1. Start the assistant.
2. Listen for a command.
3. Send the recognized sentence to `process_command()`.
4. Execute the requested operation.
5. Return to listening for another command.

The loop continues until the user gives an exit command. When `process_command()` returns `False`, the assistant stops running.

# 7. Testing and Evaluation

After implementing the different features, I needed to think about how to check whether they were working correctly.

I prepared several test cases covering the main commands supported by Alexa.

## 7.1. Functional Testing

| Test ID | Voice Command | Expected Result |
|---|---|---|
| T01 | Alexa, open YouTube | Opens YouTube in the browser. |
| T02 | Alexa, open Google | Opens Google in the browser. |
| T03 | Alexa, open Notepad | Launches Notepad. |
| T04 | Alexa, close Chrome | Attempts to close Chrome. |
| T05 | Alexa, play video | Sends the spacebar command. |
| T06 | Alexa, pause video | Sends the spacebar command. |
| T07 | Alexa, help | Explains the available commands. |
| T08 | Alexa, goodbye | Terminates the assistant. |
| T09 | An unrecognized command | Provides an appropriate response. |
| T10 | A command without Alexa | Ignores the instruction. |

These tests cover the main functionalities I wanted to include in the project.

The expected results still need to be compared with the actual results obtained during execution. This makes it possible to identify which features work correctly and which ones need further improvement.

## 7.2. Error Handling

While developing the application, I also had to consider what might happen when something goes wrong.

For example, the microphone might not recognize a command, the requested application might not be running, or the speech recognition service might become unavailable.

I used Python's `try` and `except` statements to handle these situations.

This helps prevent certain errors from immediately stopping the entire program.

## 7.3. Limitations

Although I managed to implement the main features I had planned, the application still has some limitations.

**Command recognition:** The assistant relies on predefined keywords. It cannot understand every possible way of expressing the same instruction.

**Internet connection:** The speech recognition feature depends on Google's online service, so an internet connection is required.

**Video playback:** The spacebar method works only when the active window supports that shortcut. Its behaviour can therefore change depending on the application being used.

**Closing applications:** The use of `psutil` can terminate a process without giving the user an opportunity to save unfinished work.

**Supported applications:** The current version only recognizes the websites and application names configured in its dictionaries.

## 7.4. Possible Improvements

There are several things I would like to improve if I continue developing this project.

For example:

- Add a graphical interface instead of relying mainly on the terminal.
- Implement offline speech recognition.
- Support more websites and desktop applications.
- Improve command recognition so that Alexa can understand different expressions for the same instruction.
- Add more computer-control features.
- Make the interaction more flexible and natural.

These improvements could make the assistant more reliable and useful in everyday situations.

# 8. Conclusion

Developing Alexa was a good opportunity to work on a practical Python project and see how different libraries can be combined to create a functional application.

I started with a simple idea: being able to control some computer operations using my voice. During the development, this idea turned into a desktop assistant capable of recognizing commands, opening websites, launching applications, closing selected processes, and controlling video playback.

One of the things I found interesting was that each functionality required a different approach. For example, I used SpeechRecognition to understand commands, PyAutoGUI to interact with the keyboard, and psutil to manage running processes.

The project also helped me improve my understanding of object-oriented programming, conditional statements, loops, and exception handling. More importantly, I learned how to use external libraries to solve practical problems instead of relying only on basic Python instructions.

Of course, the assistant is not perfect yet. Its command recognition is still limited, and some operations depend on the active window or an internet connection. There is still plenty of room for improvement.

Nevertheless, I am satisfied with what I managed to build. It gave me a better understanding of how desktop automation works and encouraged me to explore more advanced ways of interacting with computers.

# 9. References

During the development of this project, I consulted the following documentation:

1. **Python Documentation:**  
   https://docs.python.org/3/

2. **SpeechRecognition – Python Package:**  
   https://pypi.org/project/SpeechRecognition/

3. **PyAutoGUI Documentation:**  
   https://pyautogui.readthedocs.io/

4. **pyttsx3 – Python Package:**  
   https://pypi.org/project/pyttsx3/

5. **psutil Documentation:**  
   https://psutil.readthedocs.io/

6. **Python Webbrowser Documentation:**  
   https://docs.python.org/3/library/webbrowser.html