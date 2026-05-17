# Build Plan

## Phase 1: Lead capture

- Trigger on a new Typeform demo request.
- Normalize email, name, company, employee count, and product interest.
- Search HubSpot by lowercase email.
- Create or update contact, company, and deal records.
- Assign owner using territory rules.
- Alert Slack with the lead summary and CRM link.

## Phase 2: Demo routing

- Apply qualification rules before sending any external message.
- Choose the owner and calendar link.
- Send the inbound demo confirmation email.
- Create a 15-minute SLA task for the owner.
- Log every action on the CRM timeline.

## Phase 3: Proposal follow-up

- Trigger when a proposal status changes to sent.
- Wait for the approved follow-up interval.
- Re-check status before sending each message.
- Stop if the proposal is signed, declined, expired, or manually paused.
- Create an owner task when a proposal remains open.

## Phase 4: Monitoring and optimization

- Review the automation error channel daily during pilot.
- Review duplicate handling weekly.
- Track demo booking rate, speed to lead, proposal reply rate, and proposal close rate.
- Update qualification rules and templates based on sales team feedback.
