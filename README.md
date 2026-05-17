# No-Code Sales Automation Blueprints

A ready-to-use project kit for building sales automations in no-code tools such as Zapier, Make, Airtable, HubSpot, Pipedrive, Notion, Google Sheets, Typeform, Calendly, Slack, and Gmail.

The repository is organized around **required inputs**, **automation blueprints**, and a complete example project so you can copy a workflow, fill in the inputs, and build it without writing code.

## What is included

- `docs/input-reference.md` explains every required input and how to format it.
- `blueprints/*.json` contains reusable automation blueprints with triggers, required inputs, build steps, tests, and handoff notes.
- `project/customer-acquisition-automation/` contains a complete sample project that combines lead capture, CRM routing, proposal follow-up, and renewal alerts.
- `scripts/validate_blueprints.py` checks that every blueprint and project input file is valid JSON and includes all required sections.

## Quick start

1. Pick a blueprint from `blueprints/` that matches the process you want to automate.
2. Copy the required input checklist from `docs/input-reference.md`.
3. Fill in `project/customer-acquisition-automation/inputs.json` or create your own project input file using the same structure.
4. Open your no-code tool and build each blueprint step in order.
5. Run the manual tests listed inside each blueprint before turning the workflow on.

## Required inputs before you build

Every project needs these inputs to work reliably:

| Input | Why it matters |
| --- | --- |
| Sales goal | Defines what the automation should achieve, such as booking demos or recovering stalled proposals. |
| Source system | Identifies where the record starts, such as Typeform, Webflow, HubSpot, or Google Sheets. |
| Destination system | Identifies where the automation should create or update the sales record. |
| Field map | Connects incoming fields to CRM, spreadsheet, email, or task fields. |
| Qualification rules | Defines who should be routed, scored, followed up with, or excluded. |
| Owner assignment rules | Ensures every qualified record has an accountable rep or team. |
| Message templates | Provides approved email, SMS, or Slack copy. |
| Error handling owner | Names the person or channel that receives failed automation alerts. |
| Test records | Provides safe examples that prove each path works before launch. |

See the full checklist in `docs/input-reference.md`.

## Blueprint catalog

| Blueprint | Use it when |
| --- | --- |
| `lead-capture-to-crm.json` | New leads need to move from a form, spreadsheet, or landing page into a CRM. |
| `inbound-demo-request-routing.json` | Demo requests need qualification, owner assignment, calendar routing, and Slack alerts. |
| `proposal-follow-up-sequence.json` | Open proposals need automated reminders and rep tasks. |
| `renewal-expansion-alerts.json` | Existing customers need renewal, expansion, or risk alerts before key dates. |

## How to make a project using the blueprints

1. **Define the outcome.** Write one sentence that explains the sales outcome, such as “book more qualified demos from inbound form submissions.”
2. **Create an input file.** Copy `project/customer-acquisition-automation/inputs.json` and replace the sample values with your systems, fields, rules, users, and templates.
3. **Choose blueprints.** Select one or more JSON blueprints and only build the sections that match your current project phase.
4. **Build in order.** Create the trigger first, then add filters, field mapping, actions, notifications, error handling, and tests.
5. **Test with safe data.** Use test records that cannot email real prospects unless you intentionally allow it.
6. **Launch in stages.** Turn on the workflow for one source, one team, or one segment before expanding.
7. **Monitor and improve.** Review failures, duplicates, routing misses, and conversion metrics weekly.

## Validation

Run the validator after editing blueprints or project inputs:

```bash
python3 scripts/validate_blueprints.py
```

The script uses only the Python standard library.
