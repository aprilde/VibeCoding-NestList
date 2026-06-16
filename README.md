# NestList — AI-Powered Universal Registry Builder

A product management portfolio prototype exploring how AI can solve the knowledge gap at the heart of the registry experience.

**[▶ Watch the demo](https://github.com/aprilde/VibeCoding-NestList/releases/tag/v1.0)**

---

## The Problem

People building registries for major life moments don't know what they actually need. They face hundreds of product options, contradictory recommendations, and generic "most popular" lists that ignore their actual situation — their space, their budget, their lifestyle, their experience level.

Existing registry tools solve the logistics of gift giving. NestList solves the knowledge gap of the person building the list.

---

## The Core Insight

Every registry platform is sitting on a valuable and completely untapped signal: whether the items people registered for were actually useful. That signal disappears after the gift is received.

NestList captures it through a post-purchase rating system — and feeds it back into personalized recommendations for future users. Over time the engine gets smarter based on what people in similar situations actually used, not what brands pay to promote.

---

## How It Works

**1. Intake Quiz**
Users answer 6–8 questions about their situation: life event, first time or not, living space, budget, lifestyle, and preferences. This takes under two minutes.

**2. AI-Generated Priority List**
The system returns a personalized, priority-ranked registry with explicit reasoning for each item — why it is right for this user's specific situation, and what to skip and why. Three tiers: Essential, Nice to Have, Skip for Your Situation.

**3. Registry Management**
Users accept, remove, or swap items. They can add anything from any retailer via URL — this is a universal registry, not a walled garden.

**4. Post-Receive Ratings (The Flywheel)**
After their life event, users rate items they received: used constantly, used occasionally, never used, or wish I had registered for this instead. These ratings improve future recommendations for users with similar profiles.

---

## Product Decisions Worth Noting

**Why show reasoning?**
Most recommendation systems hide their logic. NestList surfaces it explicitly — "we skipped the wipe warmer because you mentioned a minimal setup preference and travel frequency." Transparent reasoning builds trust and helps users make better decisions when they disagree with a suggestion.

**Why universal vs. curated catalog?**
Walled garden registries create lock-in but limit user trust. A universal registry (add via URL from any retailer) puts the user's needs first. The value is in the recommendation layer, not the product catalog.

**Why ratings over reviews?**
Reviews capture sentiment at purchase. Ratings captured post-use capture actual utility — a fundamentally different and more valuable signal for a recommendation engine. "Did you use this?" is a better question than "did you like it?"

**Why priority tiers over ranked lists?**
A ranked list of 200 items is still overwhelming. Three honest priority tiers with a curated Essential list gives users a clear starting point while preserving flexibility.

---

## What This Prototype Demonstrates

- AI-powered personalization based on structured user inputs
- Explicit reasoning as a UX pattern for recommendation trust
- Feedback loop design (the ratings flywheel)
- Consumer product thinking around a high-stakes, low-expertise life moment
- Universal commerce integration pattern

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

## Running the Prototype

### 1. Clone the repository

```bash
git clone https://github.com/aprilde/VibeCoding-NestList.git
cd VibeCoding-NestList
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> Requires Python 3.8+. Python comes pre-installed on Mac and most Linux systems. Run `python3 --version` to check.

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

## Project Structure

```
VibeCoding-NestList/
├── app.py              # Flask server + /api/recommend endpoint
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
└── templates/
    ├── index.html      # Intake quiz (7-step flow)
    ├── registry.html   # Registry management
    └── rate.html       # Post-receive ratings + flywheel
```

---

## Status

This is a product management portfolio prototype built to demonstrate consumer product thinking and AI-native PM workflows. It is not a production application.

Registry data lives in your browser's `localStorage` — clearing browser storage resets the registry.

---

## About

Built by April De Zen, Product [linkedin.com/in/april-de-zen](https://linkedin.com/in/april-de-zen)
