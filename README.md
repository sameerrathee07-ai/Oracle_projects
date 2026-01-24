Python Voice Assistant

Overview:-
This project is a simple voice-controlled assistant built using Python. It listens to spoken commands through the microphone, understands them using an online speech recognition service, and responds using spoken output. The goal of the project is to demonstrate how speech input, speech output, and a basic graphical interface can work together in a single application.
The assistant is designed to be lightweight, easy to understand, and focused on core functionality rather than advanced artificial intelligence.

What the Assistant Can Do:-
The assistant currently supports a small set of predefined voice commands. For example, it can respond to greetings, tell the current time in a human-friendly format, speak today’s date, and exit the application when asked. If the assistant does not recognize a command, it informs the user instead of failing silently.

How It Works:-
When the application starts, it activates the system microphone and waits for the user to speak. The spoken audio is sent to an online speech recognition service, which converts it into text. This text is then checked against known commands.
Once a valid command is detected, the assistant generates a spoken response using an online text-to-speech service. The audio is played immediately and discarded afterward so no unnecessary files remain on the system.
A simple graphical window is used to show the current state of the assistant, such as whether it is idle, listening, or recognizing speech. The voice processing runs in the background so the interface remains responsive.

Design Approach:-
This projectfollows a rule-based approach rather than natural language processing. Each command is explicitly defined, which keeps the logic simple and predictable. The application separates the user interface from the voice processing logic, making the code easier to understand and maintain.

Limitations:-
The assistant depends on an internet connection for both speech recognition and speech output. It also only responds to predefined commands and does not support free-form conversation or learning.

Purpose:-
This project was created for learning and demonstration purposes. It focuses on understanding how voice input, speech output, threading, and a basic GUI can be integrated into a single Python application.

Author
Sameer
