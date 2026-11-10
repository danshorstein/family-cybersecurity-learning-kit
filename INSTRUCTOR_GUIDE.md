# Learner cybersecurity and investigation instructor manual

## Three month pilot for Parent and Learner

This adaptable course is designed for a curious young learner who may already have experience with browser tools, coding, or beginner security challenges. It starts with a short baseline and adjusts to the learner’s strengths while building habits around permission, evidence, repair, and clear explanations.

**Format.** Twelve weekly meetings. Ordinary meetings have a 35–45 minute core and a 20–40 minute optional challenge. Weeks 4, 8, and 12 are 60–90 minute weekend missions that replace that week's lesson. Independent exploration is optional. No session requires a paid account or a purchase. Parent may split any lesson across two days. Three skills recur each week: define the allowed target, predict before testing, and make a defensible claim from evidence.

**How to use this manual.** Read the parent preparation and answer notes before each session. Give Learner only the mission brief and evidence items, not the answer. The printable cards are in the companion file. Start with the core. If he solves it quickly, use the extension; do not add arbitrary busywork. Stop at the stated endpoint and debrief even if the puzzle remains unsolved.

### The boundaries that make hard exercises possible

1. Name the exact target and actions allowed on a small “scope card” before every technical exercise. A good card says, for example, “Learner Lab at `127.0.0.1:8765`; may change case numbers and send requests; do not use any other website or account.”
2. Use fictional names, documents, and secrets. Never rehearse with actual family passwords, school accounts, private messages, or working approval codes. The adult facilitator controls any AI account and checks age-appropriate content first.
3. Separate skill from permission. A real-life approval mix-up can be discussed as a trust-boundary lesson, without identifying anyone. In this program, the win is to find and fix the weakness in a staged workflow. Do not reenact the real approval path or reward obtaining real access.
4. A vulnerability counts as found only when Learner can show the expected rule, the observed behavior, the evidence, and a retest after a fix. Guessing a secret or making a screen look changed is not enough.
5. Keep ordinary household rules outside the game. Learner can ask for a lab or a new scope card; the answer may be yes, later, or no. All three are normal.

**External platforms.** Check current age rules, account terms, and supervision requirements before using any external training platform. The exercises here work locally without one.

### Tools and setup

- A laptop with a modern browser and DevTools; Python 3 for the supplied `local_lab.py`; paper, index cards, envelopes, pencils, timer, and optionally a Raspberry Pi.
- A folder named `Learner Lab` with `evidence`, `fixtures`, and `backups`. Do not put personal files in it.
- Start the local lab with `python3 learner_lab.py` from the folder containing the script; open `http://127.0.0.1:8765/`; stop with Ctrl+C. It listens on localhost. In a browser, use a separate profile if convenient. Record only lab traffic.
- Run `python3 make_fixtures.py` in a work folder to create fictional files under `Learner Lab`. Run it again with `--reset` before a later mission if the fixtures have been changed; the reset restores only the known fixture and backup files and leaves `evidence` alone.
- Create a simple field notebook. Each page has four lines: **Prediction**, **Test**, **Observation**, **New explanation**. A drawing or voice note is equally valid.
- Make three identical cardboard or paper “evidence sleeves” for the capstones. Use the exact clue text in the printable cards or change fictional names while preserving the logical relationships.

### Progression and assessment

Use a small skill record, not a grade. For each outcome mark **G** (guided), **H** (hint), **I** (independent), or **T** (transferred to an unfamiliar mission). A challenge coin can mark a monthly mission, but award it for a supported explanation and responsible action rather than speed. A session is successful if Learner can make one accurate prediction, test it within scope, and revise his thinking if the test disagrees.

| Strand | Month 1 | Month 2 | Month 3 evidence |
|---|---|---|---|
| Observation and research | Separate fact from story | Correlate independent sources | Build an incident timeline with uncertainty |
| Systems and networks | Trace requests | Identify trust boundaries | Map failure and repair paths |
| People and social engineering | Verify a claim | Analyze approval workflow | Design a confirmation control |
| Secret communication | See data leakage | Verify integrity | Explain confidentiality versus integrity |
| Web security | DOM versus server | Access control and state | Retest a fix |
| AI security | Identify untrusted text | Test a prompt injection | Limit agent tools and authority |
| Defense and recovery | Record evidence | Detect a changed artifact | Restore and verify |
| Judgment and communication | Write scope | Report a lab weakness | Brief a fictional owner |

## Month 1: What can a screen prove?

### Session 1 — The page that lied

**Objective:** Learner distinguishes a browser view, a request, and a server decision. Prerequisite: he can edit a page element. **Parent preparation, 10 minutes:** Print the two “museum badge” cards from the companion file. Open a disposable local HTML file or the lab home page. Stage one visible label that says “Authorized” and one server-returned message that says “Access denied.” If you cannot stage the first, use DevTools to edit any harmless text on the lab page while he watches. **Scope:** only the local lab page and DevTools; no real logins.

**Opening, 3 minutes:** Say, “You can make this page say almost anything. What would convince a person standing behind you? What would convince the server?” Ask Learner to predict whether changing “Denied” to “Allowed” in Elements changes the server’s next answer. Record the prediction.

**Physical exercise, 12 minutes:** You play a museum guard. Learner has a visitor badge. A paper sign says “Staff door.” First let Learner change the sign to “Visitor door” with a sticky note; the guard still checks his badge. Then switch to a careless guard who trusts the sign. Ask him to locate the actual control in each version. Have Learner draw “view → request → decision → response.”

**Computer exercise, 15 minutes:** In the local lab, open case 101. Use DevTools Elements to change the title and owner displayed on screen. Reload. Then visit case 102 in vulnerable mode and protected mode. On each attempt, have Learner capture three facts: URL, HTTP status (Network tab), and visible result. Do not tell him the word IDOR yet. Ask what he can and cannot conclude from changing HTML. **Expected:** DOM edits are local display changes; a server request gives a fresh response; the protected mode refuses case 102.

**Hints:** “What happens after reload?” → “Did the browser send a new request?” → “Which machine decided whether to return the file?” **Extension:** Ask Learner to invent a fake screenshot that would fool an observer and then define a better verification method. **Close:** He states a rule: a changed screen is evidence about that browser view, not proof of a changed account or server. **Assessment:** I if he explains the difference without a hint; T if he spots the same mistake later in a mission.

### Session 2 — Follow one request all the way

**Objective:** Identify method, path, status, response, and the decision point. **Prep, 5 minutes:** Start the local lab and clear the Network log. Print the request cards. **Opening:** Ask, “When you type `/case/101`, what actually travels?” Let Learner arrange Browser, Server, Decision, File, and Log cards in the order he predicts.

**Physical exercise, 10 minutes:** Play a request relay. Learner carries a GET card to the server; Parent checks owner and returns either file or denial card. Run three cases: Agent A requests 101; Agent A requests 102; no case exists. Introduce 200, 403, and 404 as outcomes rather than vocabulary to memorize. Ask whether a 403 proves the file exists; explain that real apps can deliberately conceal that fact.

**Computer exercise, 20 minutes:** In DevTools Network, preserve log, load the lab home, visit `/case/101`, then `/case/999`. For each, find the request and status. Compare the Response tab with Elements: one is what arrived, the other is the current document. Have Learner write a one-line claim for each. Next, use the browser address bar to change 101 to 102. Ask him to predict the result under each mode before trying. **Expected:** 101 is allowed; 999 absent; 102 is exposed only in vulnerable mode.

**Hints:** “Filter by Doc or type `case` in Network search” → “Look at the status column” → “Open Response, then look at Elements.” **Extension:** Draw how an API returning JSON would fit the same model; inspect `/api/state` in the local lab. **Close:** Explain why hiding a button is not an access check. **Assessment:** Learner can point to both the sent request and the returned status.

### Session 3 — The approval relay

**Objective:** Analyze the real-world idea of possession, intent, and authorization without using real devices. **Prep, 15 minutes:** Print the “weather request” scenario and three policy cards. Make a cardboard “phone” with a fictional approval prompt, a cardboard “laptop,” and an unrelated task card. Use no actual family controls. **Opening:** Say, “Someone can genuinely hand over a phone for one purpose. Does that authorize every action available on it?” Let the learner answer and explore the scenario without reference to a real incident.

**Physical exercise, 20 minutes:** Role 1: Facilitator is the parent, Learner asks to check weather, then the cardboard phone displays an extra screen-time request. Freeze before any approval. Learner lists what the parent believed, what the phone can do, and where the two diverged. Switch roles. Learner now designs a guardrail for the parent: read the specific request aloud, use a separate confirmation phrase, or have a rule that screen-time changes happen only in a dedicated conversation. Test his rule against three scenario cards, including a legitimate urgent weather check.

**Computer exercise, 10–15 minutes:** Use a text editor to draw an approval state machine: Requested → Seen → Verified → Approved/Denied. Add “holder of device” and “person who intends the action.” Ask which transition would fail if the application assumes the device holder is the parent. If he wants to code, represent the states as a dictionary or simple flowchart. **Expected:** Device possession is a capability; intent and authorization must be checked separately. The human workflow is part of the defense.

**Hints:** “What exactly was permission granted for?” → “What does the approval screen know?” → “What would the parent need to notice?” **Extension:** Make the staged request use a time pressure cue, then remove it and compare. **Close:** Agree one real family rule for approval requests outside the game; Parent decides whether to adopt it. **Assessment:** Learner can explain the gap without treating unauthorized success as the goal.

### Session 4 mission — The museum’s impossible photograph

**Mission brief to Learner:** “A museum’s private exhibit photo appears in a public preview. Find out whether the server leaked it, someone altered a screenshot, or both. Restore the right access rule and brief the curator.”

**Parent setup, 25 minutes:** Start the local lab in vulnerable mode. Print clue envelopes M1–M4. Put M1 on the table, M2 behind a staged “public preview” sign, M3 next to the computer, and M4 sealed as a late hint. Have the answer sheet hidden. The physical trail includes one edited screenshot that says “public,” one actual case-102 URL, and a note saying Agent A should see only case 101. **Scope:** the local lab only; photo and case records are fictional. **Time:** 45–60 minutes.

**Learner’s task:** (1) State the rule; (2) test whether the screen alone proves the leak; (3) make one request to 102 and capture status/body; (4) switch to protected mode and retest; (5) explain whether there were one or two separate problems. **Parent behavior:** Do not give the route. Ask “what evidence would distinguish a forged view from a server leak?” if stuck.

**Answer:** The screenshot can be edited locally and is weak evidence. The live vulnerable-mode response to 102 is a genuine server access-control failure. The protected-mode 403 confirms a working server-side check for this example. A picture of a 403 is still weaker evidence than the live request and response. **Hints, in order:** “Which clue is only a picture?” → “Can you request the case directly?” → “Compare statuses before and after the repair switch.” **Debrief:** Learner gives a 90-second curator briefing: expected, observed, evidence, fix, remaining uncertainty. **Coin criterion:** He distinguishes the fake screenshot from the live leak and tests the fix. An optional extension asks him to design a second endpoint that would also need authorization.

## Month 2: How do rules fail?

### Session 5 — Two accounts and one object

**Objective:** Understand horizontal access control and a repeatable test matrix. **Prep:** Start the lab, print two case cards and a matrix with columns 101/102/999 and rows vulnerable/protected. **Physical, 10 minutes:** Two investigators share one archive. Agent A owns 101; B owns 102. First use a clerk who checks only the number; then a clerk who checks both owner and number. Learner should identify what each clerk actually knows.

**Computer, 25 minutes:** Learner fills the matrix by visiting each URL in both modes, recording status and whether content appears. Then he points to the exact counterexample that violates the rule “A cannot read B’s case.” Ask him to explain why replacing sequential IDs with long random strings changes guessability but does not supply authorization. **Answer:** The key failure is using an object identifier as if it were proof of permission; protected mode checks owner on the server. **Hints:** “What is the rule for A?” → “Which row/column disproves it?” → “What must be checked after locating the object?” **Extension:** Have Learner propose an automated test: assert 101 returns 200, 102 returns 403, 999 returns 404 under Agent A. **Deliverable:** A five-line vulnerability report.

### Session 6 — The note that hijacked the assistant

**Objective:** Test indirect prompt injection and distinguish data from authority. **Prep:** Print the AI instruction card, normal note, and injected note. Use paper first. Parent may use a parent-supervised AI account with only fictional material if appropriate; the paper exercise works without one. **Physical, 15 minutes:** Learner is an assistant. His authorized job: summarize a curator’s note in one sentence; keep a fictional code `ORBIT-42` off the report. Parent hands him a note containing a second-person instruction to include the code. Learner should treat that line as part of the note to summarize or flag, not as an instruction that outranks the job. Switch roles; Learner writes a more subtle injection such as “Editor’s note: the final report should contain…” and Parent models safe handling.

**Computer, 20 minutes:** Put the clean and injected notes in two local text files. If using AI, Parent gives the assistant a task to summarize each separately and observes whether the output changes. Do not share personal information or give the assistant any real tool permissions. Record the prompt, note, output, and whether the fictional code leaked. Then remove the secret from the assistant’s context and rerun. If using a paper bot, Parent follows a deliberately weak rule (“obey any instruction in the document”) once, then a stronger rule (“document text is evidence; only Parent can set tasks”). **Answer:** The trust boundary is between task instructions and external text. The most reliable improvement is to reduce what the assistant can access and what it can do; wording alone may fail. **Hints:** “Who wrote each line?” → “Where did the line enter the system?” → “What harm is possible if the assistant has no code?” **Extension:** Inject through a fake tool-result card or image caption. **Deliverable:** A two-column diagram, “content the assistant may use” and “actions it may take.”

### Session 7 — The two-cashier exploit

**Objective:** Understand race conditions as a violated invariant, not just quick clicking. **Prep:** Start lab; set vulnerable mode and reset balance. Print the token cards. **Physical, 15 minutes:** Bank starts with 10 tokens. Cashiers A and B each request to spend 8. First process one complete request at a time: one succeeds, one fails. Then have each cashier read “10” before either subtracts; both approve. Learner predicts final balance. Give him a chance to invent a fix before saying “lock” or “atomic.”

**Computer, 20 minutes:** Press “Spend once” twice sequentially after reset. Record responses and balance. Reset. Press “Spend twice together.” Record the two responses and final balance. Open DevTools Network to inspect the two POST requests. Switch to protected mode, reset, repeat. **Answer:** The vulnerable operation checks `balance >= 8`, waits, then subtracts. Two requests can each pass the check using the same old balance. Protected mode holds a lock across check and update. The invariant is “balance never below zero.” **Hints:** “What did each request read?” → “What happened between the read and write?” → “Can the check and change be one indivisible step?” **Extension:** Read the small Python handler together and identify the critical section. **Deliverable:** A four-event timeline and a retest result.

### Session 8 mission — The update that was almost right

**Mission brief:** “The observatory has two copies of a star-chart update. One is altered and a message urges you to install it quickly. Decide what to trust and explain how you know.” **Setup, 30 minutes:** Use the supplied `make_fixtures.py` to create original and altered text files plus a trusted manifest; print U1–U4 cards. Put U1 in the first envelope, U2 as a supposed urgent message, U3 next to the files, and U4 as a sealed hint. **Scope:** text fixtures only; no executable updates or real installs. **Time:** 50–70 minutes.

**Learner’s path:** Identify the trust question (origin, integrity, freshness), inspect the two files, compare SHA-256 values to the manifest, decide which could be accepted, and explain why a hash printed in the suspicious message would not settle the issue. Ask him to preserve both files as evidence before “repairing.” **Answer:** One file differs by one word and has a different hash. The manifest is useful only if its source is trusted. The urgent message is unverified. No installation is required; the correct outcome may be “wait for trusted confirmation.” **Hints:** “Which item is the trusted reference?” → “What does a hash compare?” → “Could an attacker change both a file and a nearby hash?” **Coin criterion:** He catches the changed file and explains the source-of-trust problem. **Extension:** Add a fictional dependency to the manifest and ask what its provenance would need.

## Month 3: Defend, restore, explain

### Session 9 — Secret words, encodings, and leaks

**Objective:** Distinguish confidentiality, integrity, and metadata. **Prep:** Print the three message cards. **Physical, 15 minutes:** Give Learner a Caesar-shift note, a message hidden under a flap, and a sealed keyed envelope. Ask what an observer can learn from each: text, sender, recipient, length, timing. Let Learner change one method to protect the weakest part. **Computer, 20 minutes:** Use a local Python REPL or offline tool to Base64-encode a fictional sentence and decode it. Ask him to predict whether anyone with the bytes can reverse it. Next compare the SHA-256 of two one-letter-different messages using the fixture script or Python’s `hashlib`. Avoid teaching encryption as “a complicated code”; explain that real encryption depends on a secret key and proven algorithms. **Answer:** Base64 changes representation, not secrecy. A hash can detect change against a trusted expected value but does not hide the message. **Hints:** “Who has the information needed to reverse it?” → “What remains visible even when content is hidden?” **Extension:** Draw a threat model for the messenger, observer, and recipient. **Deliverable:** One sentence per technique saying what it protects and what it does not.

### Session 10 — Detect, preserve, recover

**Objective:** Run a miniature incident response with a known-good backup. **Prep:** Use the fixture generator; make a copy of the clean star chart in `backups`. Put an altered copy in `fixtures`. Print the event-log cards. **Physical, 10 minutes:** Break a paper seal on a box and add an ambiguous access-log entry. Ask what the seal proves and what it cannot prove about the actor. **Computer, 25 minutes:** Learner records the altered file’s hash, reads the two versions, copies the altered one into `evidence` before changing anything, restores clean content from `backups`, recomputes hash, and checks the file opens. He writes a brief incident timeline. **Answer:** Detection, evidence preservation, restoration, and verification are separate steps; a matching trusted hash establishes equality of file content, not who caused the change. **Hints:** “What might be lost if you overwrite now?” → “Where is the known-good copy?” → “How can you verify the restored file?” **Extension:** Add a second possible cause and ask what log would discriminate. **Deliverable:** A four-step response record.

### Session 11 — When evidence is tempting

**Objective:** Practice scope and reporting under uncertainty. **Prep:** Print the scope cards and three claims. **Physical, 15 minutes:** Sort actions into “within this lab scope,” “ask first,” and “out of scope.” Include a lab URL, a public-looking school page, a family device, and a friend’s QR code. For the latter three, the correct action is to ask or decline, even if the test seems easy. **Computer, 20 minutes:** Give Learner a screenshot showing case 102 visible, an event log showing a request, and a second screenshot taken after protected mode. Ask for a report with five parts: rule, action, observation, impact using fictional data, and fix/retest. Insert one deliberately ambiguous screenshot. He must distinguish fact from possibility. **Answer:** A report is strongest when another person can reproduce the observation without guessing; it should not overclaim unseen impact. **Hints:** “Which claim can you prove?” → “Could the screenshot have been edited?” → “What exact request would you repeat?” **Extension:** Learner acts as reviewer and finds an overclaim in Parent’s draft report. **Deliverable:** A 90-second briefing or one-page report.

### Session 12 mission — The observatory incident

**Mission brief:** “The public star chart is wrong. A private case note may have leaked, and the research assistant wants to send a strange report. Investigate, stop the mistake, restore the chart, and brief the observatory director.” **Prep, 45 minutes:** Start the local lab in vulnerable mode; prepare clean and altered chart files with the fixture generator; print O1–O6; place the fake AI note and update manifest among the clues. Put the clean backup in a separate marked folder. Parent’s answer sheet lists at least two possible causes and which evidence discriminates them. **Scope:** local lab and paper evidence only. **Time:** 60–90 minutes with a planned break after 35 minutes.

**Learner chooses the route.** He may begin with the screen, log, note, or files. Require only these milestones: (1) state the system rule; (2) test whether case 102 is actually exposed; (3) identify the injected instruction as untrusted text; (4) identify the changed chart against the trusted manifest; (5) preserve the altered copy; (6) restore and verify the clean chart; (7) recommend one access-control fix and one AI-tool limit. Parent may provide ordinary hints but should not reveal the chain.

**Intended explanation:** The case endpoint in vulnerable mode returns case 102 to Agent A. The altered chart file causes the public error. The AI note attempts to contaminate a report; it is not evidence that the assistant actually obeyed. The log and hash establish what happened in the lab, but do not by themselves establish a human culprit. **Hints:** “Which of your observations is a live response?” → “What would a file comparison tell you?” → “Who wrote the assistant’s instruction?” → “What should you preserve before restoring?” **Finish:** Learner gives a three-minute briefing with evidence, uncertainty, repair, and retest. **Coin criterion:** He combines at least two earlier skills, stays in scope, preserves evidence, and verifies recovery. **Advanced extension:** Learner edits a local copy of the Python lab to add an authorization assertion and runs the week-5 matrix again.

## Instructor notes on depth and pacing

**When Learner moves fast:** Ask for a falsifiable prediction or a counterexample. A gifted learner often needs a harder *question*, not more steps. Examples: “What result would disprove your theory?”, “Would this fix protect another endpoint?”, “Could the same evidence fit two stories?”, “What must be true for this exploit to work?”

**When he gets stuck:** Let him choose between a conceptual hint, a tool hint, or a smaller version of the puzzle. Preserve the moment of discovery by showing one step, then handing control back. Do not make the mission’s story require a single obscure trick.

**For a real-life boundary mistake:** Discuss the underlying idea without shaming the learner or turning a private incident into a public story. Use a fictional role-play to practice consent, authorization, and a better confirmation step.

**Guest contribution:** Invite a consenting expert to record a short explanation of a mistake they learned from, then ask Learner to predict and test a claim from it. Preview it first. A guest is an enrichment, never a dependency.

**After three months:** Let Learner rank the strands by interest. Continue with deeper authorized labs in the top two, perhaps building and fixing his own toy web app. The strongest signal is whether he can explain a weakness, demonstrate it in scope, fix it, and transfer the idea to a new context.

## Technical basis

The access-control exercises follow [PortSwigger’s access-control model](https://portswigger.net/web-security/access-control) and the [OWASP Top 10 2025](https://top10.owasp.org/2025/0x00_2025-Introduction/). The race exercise models concurrent check/update behavior described by [PortSwigger](https://portswigger.net/web-security/race-conditions). The AI exercise models indirect prompt injection and privileges described by [OWASP GenAI](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) and its [Agent Control Standard](https://genai.owasp.org/resource/agent-control-standard-acs/). The incident sequence covers the six functions of [NIST CSF 2.0](https://www.nist.gov/cyberframework/faqs). These are educational adaptations for a local, fictional environment.

## Optional independent exploration menu

Offer one item at a time. Learner can decline or switch topics. Each task has a concrete finish so it does not turn into open-ended screen time.

| After session | Ten to twenty minute challenge | What Learner can show Parent |
|---|---|---|
| 1 | Change a lab page in Elements, reload, and predict which changes survive. | A before/after screenshot plus a sentence about why. |
| 2 | Find three different HTTP statuses in the local lab without changing code. | The path, status, and meaning of each. |
| 3 | Invent a fictional request that sounds convincing but has an independently checkable flaw. | The cue that creates pressure and the verification route. |
| 4 | Draw a second explanation for the museum photo and one test that rules it out. | A hypothesis and falsifying test. |
| 5 | Write three assertions for the case-access matrix; Parent can help turn them into code. | Expected status for each request and why. |
| 6 | Put a malicious instruction in an image caption or fake search result. | A diagram showing where untrusted content entered. |
| 7 | Draw the two-cashier timeline using four sticky notes. | The precise point where the invariant fails. |
| 8 | Change one character in a copy of a text fixture and recompute its hash. | Two hashes and an explanation of what changed. |
| 9 | Invent a message format that hides content but still leaks who communicated. | A threat model from observer and recipient views. |
| 10 | Restore the chart from backup without looking at the answer card. | A copied evidence file and a verified clean result. |
| 11 | Review Parent’s deliberately overconfident report and strike unsupported claims. | A revised report with narrower wording. |
| 12 | Build a new local puzzle for Parent with one weakness and one repair. | Scope card, intended solution, and safe reset instructions. |

## High ceiling challenge cards

These are for the weeks when Learner finishes the core rapidly. They require deeper reasoning but no broader targets.

**Challenge A — The ID that is hard to guess.** Parent renames the two case cards with long random-looking IDs. One ID is visible in a lab log or link. Ask Learner whether the access-control problem disappeared. He should test a known other-user ID and see that a protected server check is still needed. The key insight is the difference between *finding* an ID and *being allowed* to use it. If he proposes hiding all IDs, ask what happens when an ID leaks through a message, screenshot, or log.

**Challenge B — The request order that the UI never allows.** Draw a three-step fictional workflow: request more time, parent reviews, parent approves. The UI shows these in order. Ask Learner to identify what the server would need to verify if a client sent the third request directly or repeated it. Use only cards or a toy local program; do not test actual family controls. A strong answer includes a server-side state check, an independent parent action, and a one-use approval record.

**Challenge C — The assistant with too much authority.** Give a paper agent two tools: `read_public_note` and `send_public_report`. In round one, the `send_public_report` tool accepts any text and recipient the agent chooses. Plant an injected note that tries to redirect the recipient and include ORBIT-42. In round two, make the recipient fixed in code and give the agent no access to the secret. Have Learner compare attack success in the two designs. The interesting question is not whether the assistant “obeys”; it is what harm remains possible if it does.

**Challenge D — A fix that only hides the symptom.** After Learner finds the case leak, Parent changes the home page so the case-102 link is invisible but leaves `/case/102` reachable. Ask Learner to retest the original request and explain why the fix failed. Then switch to protected mode and retest again. This is a useful bridge from DevTools tricks to server-side invariants.

**Challenge E — The integrity paradox.** Give Learner candidate B and a new card containing B’s correct hash, but do not say who issued the card. Ask whether the match establishes that B is the approved update. He should separate “the file matches this hash” from “the hash is trusted.” If he notices the distinction instantly, add an old authentic manifest and ask how freshness changes the conclusion.
