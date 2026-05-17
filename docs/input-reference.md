# Input Reference

Use this checklist before building any sales automation. The automations are intentionally no-code, but they still need precise inputs so every trigger, filter, action, and test behaves predictably.

## Global project inputs

| Field | Required | Format | Example |
| --- | --- | --- | --- |
| `project_name` | Yes | Short text | `Customer Acquisition Automation` |
| `sales_goal` | Yes | Outcome sentence | `Convert qualified inbound leads into booked demos.` |
| `business_owner` | Yes | Person or role | `Head of Sales Operations` |
| `automation_owner` | Yes | Person or role | `RevOps Manager` |
| `error_alert_channel` | Yes | Email, Slack channel, or task queue | `#sales-automation-alerts` |
| `timezone` | Yes | IANA timezone | `America/New_York` |
| `launch_stage` | Yes | `draft`, `pilot`, or `live` | `pilot` |

## System inputs

| Field | Required | Format | Example |
| --- | --- | --- | --- |
| `source_system` | Yes | App name and object | `Typeform: Demo Request Form` |
| `destination_system` | Yes | App name and object | `HubSpot: Contact and Deal` |
| `notification_system` | Yes | App name and channel | `Slack: #inbound-demo-requests` |
| `task_system` | Yes | App name and object | `Asana: Sales Follow-up Project` |
| `calendar_system` | Conditional | App name and calendar | `Calendly: Account Executive Routing` |

`calendar_system` is required for booking or demo-routing workflows and optional for proposal or renewal workflows.

## Field map inputs

A field map tells the no-code tool where each value comes from and where it should go.

| Field | Required | Format | Example |
| --- | --- | --- | --- |
| `source_field` | Yes | Exact field name from the trigger app | `Work Email` |
| `destination_field` | Yes | Exact field name in the destination app | `email` |
| `data_type` | Yes | `text`, `email`, `number`, `date`, `boolean`, `url`, or `picklist` | `email` |
| `fallback_value` | Conditional | Default value if source is empty | `Unknown` |
| `transform` | No | Plain-language transform | `Lowercase before matching duplicates.` |

## Qualification rule inputs

Use qualification rules to decide whether an automation should continue, branch, or stop.

| Field | Required | Format | Example |
| --- | --- | --- | --- |
| `rule_name` | Yes | Short text | `Qualified company size` |
| `field` | Yes | Field from mapped data | `employee_count` |
| `operator` | Yes | `equals`, `contains`, `greater_than`, `less_than`, `is_known`, or `is_unknown` | `greater_than` |
| `value` | Conditional | Comparison value | `50` |
| `on_match` | Yes | Automation behavior | `continue` |
| `on_no_match` | Yes | Automation behavior | `stop_and_notify` |

## Owner assignment inputs

| Field | Required | Format | Example |
| --- | --- | --- | --- |
| `assignment_method` | Yes | `round_robin`, `territory`, `named_owner`, or `account_match` | `territory` |
| `assignment_rules` | Yes | Ordered list of rules | `United States East -> Alex Rivera` |
| `fallback_owner` | Yes | Person, role, or queue | `Inbound SDR Queue` |
| `sla_minutes` | Yes | Number | `15` |

## Message template inputs

| Field | Required | Format | Example |
| --- | --- | --- | --- |
| `template_name` | Yes | Short text | `Inbound demo confirmation` |
| `channel` | Yes | `email`, `sms`, `slack`, or `task` | `email` |
| `subject` | Conditional | Required for email | `Thanks for requesting a demo` |
| `body` | Yes | Approved message with merge fields | `Hi {{first_name}}, thanks for reaching out.` |
| `send_from` | Conditional | Sender identity | `assigned_owner` |

## Test record inputs

Every workflow should include at least three test records:

1. A happy-path record that should complete the workflow.
2. A disqualified record that should stop cleanly.
3. A broken or missing-field record that should trigger error handling.

Each test record should include expected results for created records, updated records, notifications, tasks, emails, and error alerts.
