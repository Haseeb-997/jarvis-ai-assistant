# 🤖 Jarvis AI Assistant

A voice-controlled AI assistant built with Python using Speech Recognition, Google Gemini AI, Text-to-Speech, and browser automation.

---

## ✨ Features

- 🎙️ Voice activation using the keyword **"Jarvis"**
- 🧠 AI-powered conversations with Google Gemini
- 🌐 Open frequently used websites using voice commands
- 📰 Read the latest news headlines
- 🎵 Play songs from a custom music library
- 🔊 Natural text-to-speech responses
- ⚡ Multiple response modes (Short, Normal, Detailed)
- 🎵 View your complete music library using voice commands

---

## 🛠️ Technologies Used

- Python 3
- SpeechRecognition
- PyAudio
- pyttsx3
- Google Gemini API
- News API
- Requests
- python-dotenv

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/jarvis-ai-assistant.git
```

### 2. Navigate to the project

```bash
cd jarvis-ai-assistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
NEWS_API_KEY=YOUR_NEWS_API_KEY
```

### 5. Run the project

```bash
python src/main.py
```

## ⚙️ How It Works

1. **Run the application**

   ```bash
   python src/main.py
   ```

2. **Initialization**

   The assistant starts by saying:

   ```
   Initializing Jarvis...
   ```

3. **Listening Mode**

   The terminal displays:

   ```
   Listening...
   ```

   At this point, say the wake word:

   ```
   Jarvis
   ```

4. **Activation**

   After detecting the wake word, the assistant responds:

   ```
   Ya
   ```

   The terminal displays:

   ```
   Jarvis Active...
   ```

5. **Give Your Command**

   Now speak your command, for example:

   - Open Google
   - Play Guman
   - News
   - Music Library
   - Short Mode
   - Detailed Mode

6. **Command Execution**

   Jarvis processes your command and responds with speech while performing the requested action.

## 🎤 Supported Voice Commands

| Command | Action |
|---------|--------|
| Jarvis | Activate the assistant |
| Open Google | Opens Google |
| Open YouTube | Opens YouTube |
| Open GitHub | Opens GitHub |
| Open Instagram | Opens Instagram |
| Open LinkedIn | Opens LinkedIn |
| Open Agency | Opens the SixAlps website |
| Open Agency Portal | Opens the SixAlps Staff Portal |
| Open Calculus Corner | Opens Calculus Corner |
| Play *song name* | Plays a song from the music library |
| News | Reads the latest news headlines |
| Short Mode | AI replies in short responses |
| Normal Mode | AI replies in normal responses |
| Detailed Mode | AI replies in detailed responses |
| Music Library / List Songs | Lists all available songs in the music library |

## 📂 Project Structure

```
jarvis-ai-assistant/
│
├── assets/
│   └── screenshots/
│
├── src/
│   ├── main.py
│   └── musicLibrary.py
│
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 📸 Screenshots

### Listening Mode

> *Screenshot coming soon.*

### AI Response

> *Screenshot coming soon.*

### Browser Automation

> *Screenshot coming soon.*

## 🚀 Future Improvements

- Add offline speech recognition
- Add weather updates
- Add system automation (shutdown, restart, volume control)
- Add email sending functionality
- Add WhatsApp message automation
- Add reminder and task management
- Improve AI conversation memory
- Support for custom voice commands