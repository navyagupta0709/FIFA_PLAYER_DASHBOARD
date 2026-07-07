# FIFA Player Analysis — Dashboard + Flask + Render

## Dataset
FIFA 22 Complete Player Dataset (Kaggle, by Stefano Leone):
https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset

Download `players_22.csv` (either manually, or via the Kaggle API — both options
are in the notebook).

## Project structure
```
fifa-project/
├── FIFA_Player_Analysis.ipynb   # Colab notebook: cleaning + EDA + exports
├── app.py                       # Flask app
├── templates/
│   └── index.html               # Page that embeds the Tableau dashboard
├── requirements.txt
├── Procfile                     # Render start command
├── render.yaml                  # Render blueprint (optional one-click deploy)
└── README.md
```

## Step 1 — Run the notebook
1. Open `FIFA_Player_Analysis.ipynb` in Google Colab.
2. Upload `players_22.csv` when prompted.
3. Run all cells. This cleans the data, generates the charts, and exports:
   - `fifa_players_clean.csv`
   - `club_strength_summary.csv`
   - `country_rating_summary.csv`
   - `position_counts.csv`

## Step 2 — Build the Tableau dashboard
1. Open Tableau Desktop or Tableau Public (free) and connect to `fifa_players_clean.csv`.
2. Build sheets for: rating distribution, top clubs, top countries, value vs. rating,
   wage analysis, position breakdown.
3. Combine into one Dashboard.
4. Publish to Tableau Public: Server → Save to Tableau Public.
5. Copy the workbook's share URL — it will look like:
   `https://public.tableau.com/views/YourWorkbook/YourDashboard`

## Step 3 — Point the Flask app at your dashboard
Open `app.py` and replace the default `TABLEAU_VIEW_URL` with your own link
(or set it as an environment variable — see below).

## Step 4 — Run locally
```bash
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000

## Step 5 — Deploy to Render
1. Push this folder to a GitHub repo.
2. On Render.com: New → Web Service → connect your repo.
3. Settings:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
4. Add an environment variable `TABLEAU_VIEW_URL` with your published Tableau link.
5. Deploy. Render will give you a live URL like `https://fifa-player-analysis.onrender.com`.

(If you'd rather skip manual setup, `render.yaml` lets Render auto-configure
the service when you use "New → Blueprint".)
