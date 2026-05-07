# NestList — AI-Powered Universal Registry Builder

NestList is a prototype of an AI-powered registry builder. Answer 7 questions about your situation and get a personalized, priority-ranked registry with clear reasoning for every recommendation — not a generic list.

---

## Features

- **Intake Quiz** — 7 questions covering registry type, living situation, budget, lifestyle, and preferences
- **AI-Generated List** — Personalized, priority-ranked items (Essential / Nice to Have / Skip) with explicit reasoning tailored to *your* situation
- **Registry Management** — Remove, restore, and add custom items via URL
- **Post-Receive Ratings** — Rate what you actually used to power the recommendation flywheel

---

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd Vibe-NestList
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> Requires Python 3.8+. Run `python3 --version` to check. Python comes pre-installed on Mac and most Linux systems.

### 3. Add your Anthropic API key

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder:

```
ANTHROPIC_API_KEY=your_key_here
```

Get a free API key at [console.anthropic.com](https://console.anthropic.com/settings/keys).

### 4. Run

```bash
python3 app.py
```

Open [http://localhost:5001](http://localhost:5001) in your browser.

> **macOS note:** Port 5000 is reserved by AirPlay Receiver on macOS 12+. This app uses port 5001 to avoid the conflict.

---

## Tech Stack

| Layer | Choice |
|---|---|
| Backend | Python + Flask |
| AI | Claude (`claude-sonnet-4-6`) via Anthropic SDK |
| Frontend | Vanilla HTML / CSS / JavaScript |
| Styling | Tailwind CSS (CDN) |
| Storage | Browser `localStorage` — no database needed |

---

## Project Structure

```
Vibe-NestList/
├── app.py              # Flask server + /api/recommend endpoint
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
├── .gitignore
├── README.md
└── templates/
    ├── index.html      # Intake quiz (7-step flow)
    ├── registry.html   # Registry management
    └── rate.html       # Post-receive ratings + flywheel
```

---

## Notes

- Registry data lives in your browser's `localStorage`. Clearing browser storage resets the registry.
- The "Share" button copies the page URL — since data is in `localStorage`, sharing requires the same device/browser in v1.
- Everyone who runs this prototype needs their own Anthropic API key.
