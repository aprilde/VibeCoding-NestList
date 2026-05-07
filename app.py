from flask import Flask, render_template, request, jsonify
from anthropic import Anthropic
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

api_key = os.environ.get("ANTHROPIC_API_KEY")
client = Anthropic(api_key=api_key) if api_key else None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registry")
def registry():
    return render_template("registry.html")


@app.route("/rate")
def rate():
    return render_template("rate.html")


@app.route("/api/recommend", methods=["POST"])
def recommend():
    if not client:
        return jsonify({"error": "ANTHROPIC_API_KEY is not set. Add it to your .env file."}), 500

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        prompt = build_recommendation_prompt(data)

        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )

        response_text = message.content[0].text.strip()

        # Extract JSON array from response
        json_match = re.search(r"\[.*\]", response_text, re.DOTALL)
        if json_match:
            items = json.loads(json_match.group())
        else:
            items = json.loads(response_text)

        return jsonify({"items": items})

    except json.JSONDecodeError as e:
        return jsonify({"error": f"Failed to parse AI response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def build_recommendation_prompt(data):
    registry_type = data.get("registry_type", "baby")
    first_time = data.get("first_time", True)
    living_situation = data.get("living_situation", "not specified")
    budget = data.get("budget", "not specified")
    lifestyle = data.get("lifestyle", [])
    preferences = data.get("preferences", [])
    notes = data.get("notes", "")

    budget_labels = {
        "under_500": "under $500",
        "500_1500": "$500–$1,500",
        "1500_5000": "$1,500–$5,000",
        "5000_plus": "$5,000+",
    }
    living_labels = {
        "apartment_small": "apartment / small space (limited storage)",
        "house_yard": "house with yard (ample indoor and outdoor space)",
        "urban_condo": "urban condo or townhouse (moderate space, city setting)",
        "suburban_house": "suburban house (comfortable space)",
    }
    type_labels = {
        "baby": "a new baby",
        "wedding": "a wedding",
        "new_home": "a new home",
    }

    lifestyle_str = ", ".join(lifestyle) if lifestyle else "none specified"
    prefs_str = ", ".join(preferences) if preferences else "none specified"
    budget_str = budget_labels.get(budget, budget)
    living_str = living_labels.get(living_situation, living_situation)
    type_str = type_labels.get(registry_type, registry_type)

    return f"""You are NestList's recommendation engine. Generate a personalized, prioritized registry for this specific person.

REGISTRY TYPE: {type_str}
FIRST TIME: {"Yes" if first_time else "No, they have prior experience"}
LIVING SITUATION: {living_str}
TOTAL BUDGET: {budget_str}
LIFESTYLE: {lifestyle_str}
PREFERENCES: {prefs_str}
NOTES: {notes if notes else "None"}

Generate 18-22 registry items. Be opinionated and specific:

- "Essential": Things they will definitely use given THEIR specific situation
- "Nice to Have": Genuinely useful but not critical for their context
- "Skip": Include a few items you'd normally recommend but that DON'T fit this specific person — explain exactly why

The "reason" field MUST reference their situation directly. Examples:
  Good: "You're in a small apartment with limited storage — this folds flat and lives behind a door"
  Bad: "A must-have for new parents"

Return ONLY a valid JSON array. No markdown, no explanation, no code fences. Just the raw JSON array.

Each item schema:
{{
  "name": "Product name",
  "category": "Category",
  "priority": "Essential" | "Nice to Have" | "Skip",
  "price_range": "$X–$Y",
  "reason": "One sentence tailored to this user's situation",
  "search_query": "Best search term to find this product"
}}"""


if __name__ == "__main__":
    app.run(debug=True, port=5001)
