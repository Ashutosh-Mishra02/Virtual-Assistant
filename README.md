# Jarvis - A Simple Python Virtual Assistant

Jarvis is a basic virtual assistant created using Python that can perform a variety of tasks such as searching Wikipedia, opening applications, performing calculations, taking notes, telling jokes, sending emails, setting reminders, and more.

## Features

### 1. **Greeting and Time-Based Salutation**
   - Greets the user based on the current time of day.

### 2. **Voice Commands**
   - Takes voice commands using the `speech_recognition` library and processes them to execute tasks.

### 3. **Wikipedia Search**
   - Searches for a query on Wikipedia and reads out a summary.

### 4. **Web Browsing**
   - Opens popular websites like YouTube and Google.

### 5. **Time Check**
   - Tells the current time.

### 6. **Email Handling**
   - Sends an email to a specified recipient using the SMTP protocol.

### 7. **Opening Applications**
   - Opens common desktop applications like Notepad and Calculator.

### 8. **Arithmetic Calculations**
   - Performs basic arithmetic operations.

### 9. **Note Taking**
   - Creates and reads notes stored in a text file.

### 10. **Jokes**
   - Tells random jokes from a predefined list.

### 11. **Reminders**
   - Sets a simple reminder after a specified delay in seconds.

### 12. **Music Playback**
   - Plays music from a specified directory on the system.

### 13. **Exit**
   - Ends the assistant session.

## Requirements

To run Jarvis, you'll need the following Python libraries:

- `datetime`
- `pyttsx3`
- `speech_recognition`
- `wikipedia`
- `webbrowser`
- `smtplib`
- `os`
- `random`
- `time`

You can install the required libraries using `pip`:

```bash
pip install pyttsx3 speechrecognition wikipedia
