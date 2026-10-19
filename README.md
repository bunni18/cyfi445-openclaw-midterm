# Exploring AI Agent Tool Calling with OpenClaw

CYFI 445 midterm project, University of Baltimore.
Team: Brenda Bailey (brenda.bailey@ubalt.edu) and Kelly Jorge (kelly.jorge@ubalt.edu).

We installed OpenClaw on the course VM, connected it to a hosted Gemini model, ran the four starter questions (M0–M3), and used OpenClaw's trajectory records to check which tool calls really happened.

## Repository contents

| Path | Contents |
|---|---|
| `data/` | The three synthetic starter files, unchanged (SHA-256 below) |
| `prompts.md` | Exact prompts, expected answers, and agent responses for M0–M3 |
| `scripts/summarize.py` | Prints every `tool.call` / `tool.result` from a trajectory export |
| `evidence/tool_call_sequences.md` | Tool-call tables for M0–M3 and the main session, from the trajectories |
| `evidence/screenshots/` | Redacted, terminal-only screenshots (index in `evidence/SCREENSHOTS.md`) |
| `diagram/` | Architecture diagram (`m1_architecture.svg` source and `.png`) and results chart |
| `config.example.md` | Safe summary of the agent settings (no keys or tokens) |

## Environment

| Item | Value |
|---|---|
| Platform | OpenClaw 2026.10.4 (build `383c124`) |
| Host | University of Baltimore course VM `tsurugi02` (Linux) |
| Runtime | Node.js 24.22.0 via nvm (VM default was 18.19.1) |
| Model | `google/gemini-3.5-flash-lite`, Google Gemini API, free tier |
| Agent | `frankie` ("Frankie"), single agent |
| Gateway | Local mode, `ws://127.0.0.1:18789`, token auth |

## Reproduce the setup

```bash
# 1. Node.js 24 with nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.bashrc
nvm install 24 && nvm alias default 24

# 2. Download and verify the package before installing
npm view openclaw@latest version dist.shasum dist.integrity
mkdir -p ~/openclaw-install && cd ~/openclaw-install
npm pack openclaw@latest
sha1sum openclaw-*.tgz                                   # must equal dist.shasum
openssl dgst -sha512 -binary openclaw-*.tgz | base64 -w0; echo   # must equal dist.integrity (after "sha512-")

# 3. Install from the verified file (npm 11 blocks install scripts by default)
npm install -g --allow-scripts=@google/genai,esbuild,koffi,protobufjs,openclaw ./openclaw-*.tgz
cd "$(npm root -g)/openclaw" && node scripts/postinstall-bundled-plugins.mjs && cd -
openclaw --version                                       # OpenClaw 2026.10.4 (383c124)

# 4. Health check and onboarding
openclaw doctor
openclaw onboard        # one agent, "Ask first"; model setup skipped (course model unreachable)

# 5. Model: key from an environment variable only, never in a file
export GEMINI_API_KEY='<your key>'
openclaw models set google/gemini-3.5-flash-lite

# 6. Start the Gateway and the chat
openclaw config set gateway.mode local
nohup openclaw gateway > ~/gateway.log 2>&1 &
openclaw
```

## Run the tests

```bash
mkdir -p ~/.openclaw/workspace/midterm_data
cp data/* ~/.openclaw/workspace/midterm_data/
sha256sum ~/.openclaw/workspace/midterm_data/*
```

Run each prompt in `prompts.md` in a new chat session. Then export and summarize each session:

```bash
cd ~/.openclaw/workspace
openclaw sessions export-trajectory --session-key "agent:frankie:<session-id>" --workspace . --output m1
python3 scripts/summarize.py .openclaw/trajectory-exports/m1/events.jsonl
```

## Data hashes (SHA-256)

```
0f19f59480e1a291058757e9ad0236ea66a187f4bb1ba9c5a42020a9acd8efec  devices.csv
126296a31f97285a04aa3249fbf5bc35b812c6b3c7cc8583187dd78ff70da54c  auth_events.csv
71eeb5c53b9905f114b63c7e120055ca9154cac6ae8e5fcd766bc60dc8c34a49  alert_rule.txt
```

## Evidence note

The raw trajectory bundles (`events.jsonl`, `tools.json`, `prompts.json`, etc.) for sessions m0, m1, m2, m3, and main remain on the course VM at `~/.openclaw/workspace/.openclaw/trajectory-exports/`. The course VM cannot upload to GitHub. Their tool-call contents are reproduced in `evidence/tool_call_sequences.md` and shown in the screenshots. The bundles are available on request.

## Security

No API keys or Gateway tokens are stored in this repository. Screenshots are cropped to the terminal to remove the VM IP address and other windows. The Gemini key was supplied only as the `GEMINI_API_KEY` environment variable and will be revoked after the presentation.

## AI assistance

We used Claude (Anthropic) for setup and troubleshooting commands, interpreting trajectory output, writing `summarize.py`, drawing the diagram and chart, and drafting documentation. We ran every command ourselves and checked every call ID and result against our exported trajectories.
