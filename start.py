import os
import pathlib

# Write secrets from Railway env vars into .streamlit/secrets.toml
secrets_dir = pathlib.Path("/app/.streamlit")
secrets_dir.mkdir(exist_ok=True)

KEYS = [
    "SUPABASE_URL",
    "SUPABASE_KEY",
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "SENDGRID_API_KEY",
    "SENDGRID_FROM_EMAIL",
    "FRED_API_KEY",
]

lines = []
for key in KEYS:
    val = os.environ.get(key, "")
    if val:
        lines.append(f'{key} = "{val}"')

(secrets_dir / "secrets.toml").write_text("\n".join(lines))
print(f"✅ Wrote {len(lines)} secrets")

# ── Brand theme: kills Streamlit's default red accents on every native
# widget (toggles, sliders, radios, checkboxes, focus states, charts).
# This single file is the difference between "template" and "product".
config = """[theme]
primaryColor = "#1a6fe0"
backgroundColor = "#f5f8fd"
secondaryBackgroundColor = "#ffffff"
textColor = "#07111f"
font = "sans serif"

[browser]
gatherUsageStats = false
"""
with open(".streamlit/config.toml", "w") as f:
    f.write(config)
print("✅ Brand theme written")

port = os.environ.get("PORT", "8501")
print(f"✅ Starting on port {port}")

os.execvp("streamlit", [
    "streamlit", "run", "app-2.py",
    f"--server.port={port}",
    "--server.address=0.0.0.0",
    "--server.headless=true",
    "--server.enableCORS=false",
    "--server.enableXsrfProtection=false",
    "--server.enableWebsocketCompression=false",
])
