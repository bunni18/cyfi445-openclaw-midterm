"""Summarize tool calls in an OpenClaw trajectory export.

Usage: python3 summarize.py <path-to-events.jsonl>
Prints one line per runtime tool.call / tool.result event:
sequence number, event type, call ID, tool name, and a short detail.
"""
import json, sys

for line in open(sys.argv[1]):
    e = json.loads(line)
    if e.get("source") != "runtime" or e.get("type") not in ("tool.call", "tool.result"):
        continue
    d = e.get("data", {})
    if e["type"] == "tool.call":
        a = d.get("args", {})
        info = a.get("title") or a.get("path") or ""
    else:
        info = "success=" + str(d.get("success")) + " " + json.dumps(d.get("result", ""))[:120]
    print(e["seq"], e["type"], d.get("toolCallId"), d.get("name"), info)
