# Family Cybersecurity Learning Kit

A flexible, hands-on cybersecurity curriculum for an adult and a curious young learner. It combines physical puzzles, browser investigation, local web security exercises, AI trust-boundary activities, and incident-response missions.

## Start here

1. Read [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md) for the 12-session plan, setup, timing, scripts, hints, and answer guidance.
2. Print [PRINTABLE_CARDS.md](PRINTABLE_CARDS.md) for scope cards, scenario clues, and mission props.
3. Run `python3 local_lab.py` and visit `http://127.0.0.1:8765/` for the fictional local web lab. Stop it with Ctrl+C.
4. Run `python3 make_fixtures.py` in a working folder to create fictional text files for integrity and recovery exercises. Use `--reset` to restore those exercise files.

The lab listens on localhost and uses fictional records. Keep practice within a scope you and the learner explicitly agree on. Check current age and supervision rules before using any outside platform.

## Contents

- `INSTRUCTOR_GUIDE.md` — 12 detailed sessions, three missions, challenge extensions, and pacing guidance.
- `PRINTABLE_CARDS.md` — printable role cards, clues, answer notes, and worksheets.
- `local_lab.py` — local-only web lab for access-control and race-condition demonstrations.
- `make_fixtures.py` — creates harmless fictional text fixtures; no executable payloads.

## Reuse and license

Written materials are licensed under [CC BY 4.0](LICENSE-CONTENT.md). Code is licensed under the [MIT License](LICENSE-CODE). These licenses let others reuse and adapt the materials with attribution and the code under permissive terms.
