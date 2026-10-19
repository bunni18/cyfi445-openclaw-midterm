# Prompts, expected answers, and responses

`DATA_DIR` = `/home/student/.openclaw/workspace/midterm_data`. Each prompt ran once, in its own new TUI session, worded exactly as in `STARTER.md`.

| ID | Session | Exact prompt | Expected answer | Agent response (TUI) | Correct |
|---|---|---|---|---|---|
| M0 | `tui-89d5343b-49a5-4b5f-924f-fee68924035a` | Without reading any files, what is 2 + 2? | 4 | "4" | Yes |
| M1 | `tui-e4dd29e6-df40-47a1-b412-c187ddc18b77` | Using DATA_DIR/devices.csv, who owns device D-101? Cite the device ID you used. | Elena Ortiz | "Device D-101 is owned by Elena Ortiz (Device ID: D-101)." | Yes |
| M2 | `tui-e16c35ad-64ed-4e1f-977e-21b0b69908da` | First identify the owner of D-102 from DATA_DIR/devices.csv. Then use DATA_DIR/auth_events.csv to report the outcome and UTC time of event E-005. | Maya Chen; E-005 succeeded at 2026-09-01 10:01:00 UTC | "The owner of device D-102 is Maya Chen. For event E-005: UTC Time: 2026-09-01T10:01:00Z; Outcome: succeeded" | Yes |
| M3 | `tui-e0697cc0-8bbe-45ad-90fb-1534a1613541` | Using DATA_DIR/devices.csv, who owns D-999? Do not invent a record. | D-999 is absent | "Based on .../devices.csv, D-999 is not listed in the file, and no record or owner exists for it." | Yes |

No prompt had to be changed.
