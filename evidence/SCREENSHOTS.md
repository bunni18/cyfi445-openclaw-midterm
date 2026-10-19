# Screenshot index

All screenshots are cropped to the terminal (VM IP address and other windows removed).

| File | Shows |
|---|---|
| f01_node18.png | VM shipped with Node.js 18.19.1 |
| f02_nvm_install.png | nvm installs Node.js 24.22.0 |
| f03_node24.png | Node 24 / npm 11 confirmed |
| f04_npm_view_pack.png | Published version and hashes; `npm pack` download |
| f05_hash_verify.png | SHA-1 and SHA-512 match registry; SHA-256 recorded; install |
| f06_scripts_blocked.png | npm 11 blocked install scripts |
| f07b_reinstall_version.png | Reinstall with `--allow-scripts`; only OpenClaw script still blocked |
| f08_postinstall_doctor.png | Postinstall script run manually; `openclaw doctor` |
| f09a–f09d | Doctor prompts: webhook defaults, Gateway token, disable skills, no daemon |
| f10a–f10d | Onboarding: security, one agent, Frankie / Ask first, scan permission |
| f11a–f11d | Provider list, Ollama, local only, Ollama unreachable |
| f12a_* / f12b | Course repo `.env.example` (localhost only); model setup skipped |
| f13a–f13d | Google provider, error 429, key detected (masked), `curl` test of flash-lite |
| f14_models_set.png | `openclaw models set google/gemini-3.5-flash-lite` |
| f15a–f15d | TUI disconnected, Gateway error, `gateway.mode local`, TUI connected |
| f16_data_hash.png | Data copied and SHA-256 hashed |
| f17a–f17d | M0, M1, M2, M3 prompts and responses in the TUI |
| f18_m1_export.png | M1 trajectory export (45 events) |
| f19_m1_raw_jsonl.png | Raw `events.jsonl` lines for call_1345322 |
| f20_script.png | Creating and running `summarize.py` |
| f21a, f21b | M1 tool-call summary |
| f22a–f22c | M2 export and tool-call summary |
| f23a, f23b | M0 export; summary prints no tool calls |
| f24a–f24c | M3 export and tool-call summary |
| f25_sessions_list.png | `sessions_list` call in the trajectory (seq 98–124) |
| f26a_mkdir.png | Agent reply to the pasted `mkdir` |
| f26b_chat_sessions.png | Agent's own session list in chat (self-report) |
| f27_transcripts_help.png | `openclaw transcripts` help |
| f28c, f28b, f28 | Main-session export; tool search; `write` of `.gitkeep` |
| f29_config_agents.png | `openclaw config get agents` |
