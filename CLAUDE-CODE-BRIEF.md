# CLAUDE CODE BUILD BRIEF — Update the 12-Week Plan Site (v2)

**Project:** Upgrade my existing `12-week-plan.html` dashboard into the complete v2 operating plan.
**Owner:** Daniel Ikusawe. **Date:** 12 June 2026.
**Files in this folder:** `12-week-plan.html` (the current site you built — single file, CSS vars, JS-rendered panels, IDs like `panel-overview`, `panel-w1`…`panel-w12`, `panel-projects`, `panel-goals`, `panel-sops`, sidebar `sb-streak` / `sb-money`), `daniel-12-week-operating-plan.md` (full plan text — use as content source where this brief doesn't override it).

**Working rules for you (Claude Code):** keep it a single HTML file · keep the existing design system (CSS variables, current theme, nav, sidebar) — extend, don't redesign · localStorage is fine for checkbox/streak persistence (this runs locally/GitHub Pages) · small commits with clear messages, one per section below · after all edits: open locally, verify every panel renders, then push.

---

## EDIT 1 — Overview panel (`panel-overview`)

Replace the description with: "One system: mentorship, Vekora, school, builds. 12 honest Fridays, one protected maths grade, one niche, one demo at 10/10, prices held — everything else is noise."

Stats row must show: Friday streak (n/12) · £ banked vs target · sends this week vs quota · current week number. Money targets for the bar: W2 £450–900 · W6 £1,400–2,000 · W8 £2,000–2,800 · W12 £2,500–4,000 · 1 Dec £3,000/mo run rate.

## EDIT 2 — NEW panel: "Offer Ladder" (add to nav after Overview)

Render this table exactly, with the gate column prominent:

| Stage | When | Product | Price | Unlock gate |
|---|---|---|---|---|
| 0 — Diagnose & Respond | NOW | £200 Lead-Leak Audit (48h video + 1-page plan) · £900 "Never Miss A Job" foundation (GBP setup + instant SMS enquiry alerts + landing page if needed) · £250–350/mo Response & Visibility retainer | floors locked | none |
| 1 — Instant Response System | Monday (weekend build) | missed-call text-back + enquiry auto-acknowledge (Twilio webhook → Cloud Run → SMS) | £500 setup, folds into retainer | working live demo |
| 2 — AI Lead Qualification | ~Aug | qualify → score → reply → book, under 30s | £950/mo + £500 setup | demo runs 10/10 |
| 3 — Custom Tools | Month 4–6 | £10–25k scoped builds, licence-first (secure value up front — AIC principle), AIC back-up on delivery | per scope | validated problem + Dee |
| 4 — Product | Year 2+ | Vekora OS: productised Stage 2 + 12 months outcome data | SaaS | niche data moat |

Under the table, a red rules strip: "Never sell a stage you cannot demo · No discounts — trim scope · Ownership terms in writing before deposit · Sell outcomes, never 'AI' or 'automation'."

## EDIT 3 — NEW panel: "Markets & Outreach" (two-market structure)

**Proving ground (selling NOW):** driving instructors (can't answer mid-lesson; £1,400+ LTV per student; WhatsApp-native; zero saturation) + waste cluster (live deal — service it). Purpose: cash, case studies with hard ROI numbers, outcome data. Graduation niche for Stage 2: commercial security.

**Destination market (researching NOW, selling via gates):** mid-market B2B at £20–100k/month revenue — recruitment, property (commercial/lettings groups), professional services, logistics, sales orgs. Note prominently: this is AIC's own client class and Dee's Week 6 sector list — the subcontract track is a door into it. **Entry gates: 2–3 documented case studies with hard numbers + Stage 2 live at 10/10 + AIC track record (from autumn 2026). Week 8 problem-discovery shortlist must be built from THESE sectors' workflows, not trades.** Until the gates open, destination-market activity = research and the harvest question only.

Include: the UK call script (proof-first opener: "I'm Daniel, I'm local — I built the site for Vas Heating… when I searched 'driving lessons [town]' you're not in the map results… and I'm guessing you can't answer mid-lesson — so where do those calls go?"), the WhatsApp audit message, the harvest question ("what's the biggest time-eater on the office side?"), follow-up cadence day 0/3/7/monthly.

Quota table: term weeks 30 sends/wk (10 × Tue–Thu) · mock weeks 0 · summer 50/wk (10/weekday). Gates: reply rate calculated at 50 sends; <5% at 150 sends → niche review with Dee. **Niche-hop counter: 1 used (trades → instructors). Next hop requires 150 logged sends of data.**

## EDIT 4 — Week panels (`panel-w1` … `panel-w12`)

Sync each week's tasks/deliverables to `daniel-12-week-operating-plan.md` (Weekly Objectives Matrix + week sections), with these v2 changes:
- W1 (current): add "Vas repaired ✅ sent — present 3 options on reply" · "lead discovery WhatsApp" · "UAT-UK account" · "CV v14".
- W2: build = **Instant Response System** (Twilio + Cloud Run) as the weekend project alongside Dee's deploy week — it IS the deployable project. Demo target: Monday.
- W3–4: mocks, flexible-week protocol, minimum Fridays only. Add editable date fields: first mock ___ , last mock ___ , term ends ___.
- W5: Dee's GCP/Claude API content + Month 1 retro (CCA = yes · stack question · "£1,000/day criteria" question) + metric sheet live.
- W6: mini product = Audit Generator. W7: TMUA booked Mon 20 July + MCP + CCA M1. W8: agentic build + 10-problem shortlist (Dee's Week 6 method) + 3 validated problems verbatim + hackathon registered + CCA M2. W9: Demo rebuild + 20-test log + PS draft 1 + CCA M3. W10: demo 10/10 → Stage 2 unlocks + hackathon shipped. W11: MVP build (Dee's spec: 1 role, 3 JTBD, 3 must-haves, won't-do list) + CCA M4 + Loom demo asset (30/30/90/30 structure) + 20-prospect list. W12: outreach sequence (drafts past Dee first) + subcontractor readiness scored + 12-week retro. CCA exam: Month 4, cohort-gated — show as "scheduled", not dated.

## EDIT 5 — NEW panel: "Build Pipeline" (the find → solve → ship loop)

Render as a 7-step visual: 1 FIND (10-workflow shortlist: pain, who, hrs/wk, incumbent, why LLM-native, viability — plus the live harvest question) → 2 VALIDATE (one real conversation, never skipped) → 3 SPEC (1-page MVP: one role, 3 jobs-to-be-done, max 3 must-haves, explicit won't-do list) → 4 BUILD (happy path end-to-end, Claude Code as junior dev, commit every 2h) → 5 HARDEN (top 3 failure modes + 5 documented test inputs) → 6 SHIP (deploy, README, About) → 7 SELL (Loom 30/30/90/30, 20 prospects, 4-message sequence, Dee reviews before send).

## EDIT 5b — Add to Offer Ladder panel: Stage 2.5 (destination tier, gated)

| 2.5 — Full-Funnel Growth System | 2027, mid-market only | paid acquisition (Google/Meta) feeding the Stage 2 qualify/book system — ads + response + qualification as ONE revenue pipeline. Ads are part of the core growth stack, not a bolt-on | retainer £1.5–3.5k/mo, or ad management at 10–15% of spend on £5–20k/mo budgets | 2–3 case studies + Stage 2 at 10/10 + first AIC subcontract delivered |

## EDIT 5c — Add to Build Pipeline panel: "Growth Skills Track (Ads)"

Purpose line at top: **"Learn ads at owner level — well enough to price, hire, and audit media buyers, and eventually delegate to ad-management agents I build. Not to become a media buyer."**

Sequenced block with dates and a hard budget cap:
- **Now–Aug:** none. Proving-ground phase; Dee's documented position stands (ads-first agency model = crowded/low-margin). Ads enter as a component of revenue systems, on schedule.
- **Sept 2026:** learn by owning a real campaign — £100–200 TOTAL cap of own money on Google Ads promoting the Vekora £200 audit. Track CPC, CTR, cost-per-lead, cost-per-sale in the metric sheet. Google Skillshop fundamentals alongside (free).
- **Q4 2026:** second micro-campaign (Meta lead forms, same cap), written up after analysis.
- **2027:** first client ad budget, small, inside a Stage 2.5 retainer only, gates open.
- **2027+:** delegation phase — hire first freelance media buyer against your own checklist; spec the ad-reporting/optimisation agent as a build (candidate for the tools pipeline).
Banner rule: "Ads are learned by spending. Cap holds until retainer MRR ≥ £1,500/mo."

## EDIT 6 — Projects panel (`panel-projects`)

Replace list with the gated side-projects table: TMUA Tracker (W7) · Instant Response System (W2 — promoted to core) · AI Revision Tutor with SM-2 + classmate users (Aug) · Agent-Based Market Simulation (Aug, Imperial PS piece) · Review-Request System (Sept, needs 2 retainers) · Voice Receptionist demo (needs Stage 2 client #1). Rule banner: "One active at a time · summer only · Fridays in first · not on this list = not built this year."

## EDIT 7 — Goals panel (`panel-goals`)

Three columns: **Money** (the cumulative table from Edit 1) · **Imperial** (UAT-UK ✓ → book 20 Jul → TMUA daily hour from W7 → PS draft Aug → UCAS Oct → maths B→A*: revision wins all collisions until papers hit A) · **Person** (Bible daily · Atomic Habits first, then Art of War; Greene books read critically, not as playbooks · gym Mon/Wed/Sat · protein every meal · 21:30 cutoff · Sunday rest · "every Friday submitted is a vote for the person you're becoming").

## EDIT 8 — SOPs panel (`panel-sops`)

Keep existing SOP/tools content; add the Life Guardrails checklist from the .md (school beats business · Friday sacred · documents describe reality · 45-min escalation rule · pricing floors · ownership in writing · one niche · money rules incl. 20–25% tax set-aside + API billing alert · security basics · parents informed · no new strategy docs) and the Kill Conditions (150-send rule · 1 Dec £1,500/3-broken-Fridays rule · October maths-B rule).

## EDIT 9 — Sidebar

`sb-streak`: Friday streak n/12 with a manual "Friday submitted" button (localStorage). `sb-money`: £ banked (manual entry) vs current target. Add a third widget: "Today's 3" — free-text trio pulled from the current week's objectives.

## EDIT 10 — NEW panel: "Income Streams — Scaling Map"

Banner: **"Streams aren't collected, they're compounded: proof reprices you, delegation frees you, each stream funds the next one's build."**

Three-column timeline:

**NOW (17, 2026):** Audits £200 · Foundation builds £900 · Retainers £250–350/mo. Run rate target £500–1,500/mo by Sept. Job of this stage: proof, case studies, data — not the money.

**AT 18 (through 2027):** Retainers scaled by CLIENT-CLASS JUMP, not by charging trades more — mid-market (multi-instructor driving schools, multi-truck waste, security firms, recruitment/lettings) at **£1.5–3.5k/mo** [gates: 2–3 case studies with hard ROI numbers + Stage 2 at 10/10 + AIC co-credibility] · AIC subcontract days £500→£750–1,000 · first licence-first tool £10–25k · ISA opens on 18th birthday. Run rate: £2,500–5,000/mo pre-A-levels; **£5–10k/mo in the pre-Imperial summer at full intensity**; maintenance mode during exams by design.

**AT 21 (2030):** Delegated agency MRR £3–8k/mo (VA/junior on delivery, you on sales+QA) · day rates £1,000–2,500 · repeatable tool builds 2–4/yr · **Vekora OS product MRR — the concentrated equity bet (7-figure paper valuation at £15–25k MRR, 100% owned)** · elite internship summers £3–8k/mo (bought by the maths grade + Imperial network) · ISA compounding.

**Equity rules strip (red):** "Cash floor ALWAYS — the licence fee alone covers cost + profit · equity kicker 5–15% ON TOP, never instead · revenue-generating companies only · most kickers expire worthless and that's fine, they were free · the concentrated equity position is my own cap table." 

**Money rules addendum (add to EDIT 8 money rules):** "Betting is an expense category, not an income stream — excluded permanently."

## Acceptance criteria

Every panel renders with no console errors · checkboxes persist across refresh · all v2 content above present · mock-date fields editable · existing visual style preserved · committed in ≤10 clean commits · pushed and live URL confirmed.
