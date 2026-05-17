# Customer Acquisition Automation Project

This sample project shows how to combine the blueprints into one practical no-code sales automation system.

## Project outcome

Convert qualified inbound leads into booked demos, keep sales owners accountable to a fast response SLA, and prevent late-stage proposals from stalling.

## Blueprints used

1. `lead-capture-to-crm` captures new lead records, deduplicates by email, maps fields, and creates CRM records.
2. `inbound-demo-request-routing` qualifies high-intent requests, assigns an owner, sends a booking link, and creates an SLA task.
3. `proposal-follow-up-sequence` reminds prospects and sales reps when proposals remain open.

## How to use this project

1. Open `inputs.json` and replace the sample systems, owners, field names, and templates with your real values.
2. Build `lead-capture-to-crm` first so CRM records are clean before routing begins.
3. Build `inbound-demo-request-routing` second and test every assignment rule with a safe test record.
4. Build `proposal-follow-up-sequence` last, after proposal statuses and opt-out rules are confirmed.
5. Keep the launch stage set to `pilot` until every manual test passes.
6. Move to `live` only after a sales leader approves routing, messages, and SLA behavior.

## Build plan

| Phase | Automation | Exit criteria |
| --- | --- | --- |
| 1 | Lead capture to CRM | New, duplicate, disqualified, and broken records all behave as expected. |
| 2 | Demo request routing | Every territory route has an owner, calendar link, Slack alert, and SLA task. |
| 3 | Proposal follow-up | Open proposals get messages, closed proposals are excluded, and owner tasks are logged. |
| 4 | Monitoring | Error alerts, duplicate logs, and SLA misses are reviewed at least weekly. |

## Go-live checklist

- All required project inputs are filled in.
- Source and destination app connections are owned by a team account or documented admin.
- Every owner assignment rule has a fallback owner.
- Every message template has been approved by sales leadership.
- Every selected blueprint has passed the manual tests listed in its JSON file.
- The error alert channel has at least one responsible owner.
