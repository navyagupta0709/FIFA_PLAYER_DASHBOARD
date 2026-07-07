import os
from flask import Flask, render_template

app = Flask(__name__)

# Paste the "Share" / embed link you get after publishing your workbook to Tableau Public.
# It looks like: https://public.tableau.com/views/YourWorkbookName/YourDashboardName
TABLEAU_VIEW_URL = os.environ.get(
    "TABLEAU_VIEW_URL",
    "https://public.tableau.com/views/FIFAPlayerAnalysis/Dashboard1"
)


@app.route("/")
def home():
    return render_template("index.html", tableau_url=TABLEAU_VIEW_URL)


@app.route("/health")
def health():
    # Simple endpoint Render can ping to confirm the service is alive
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
