#!/usr/bin/env python3
"""Validate no-code sales automation blueprint and project input files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT_DIR = ROOT / "blueprints"
PROJECT_INPUTS = ROOT / "project" / "customer-acquisition-automation" / "inputs.json"

BLUEPRINT_REQUIRED_KEYS = {
    "id",
    "name",
    "goal",
    "best_for",
    "required_inputs",
    "trigger",
    "workflow_steps",
    "manual_tests",
    "handoff_instructions",
}

PROJECT_REQUIRED_KEYS = {
    "project_name",
    "sales_goal",
    "business_owner",
    "automation_owner",
    "error_alert_channel",
    "timezone",
    "launch_stage",
    "systems",
    "field_map",
    "qualification_rules",
    "owner_assignment",
    "message_templates",
    "test_records",
}

SYSTEM_REQUIRED_KEYS = {
    "source_system",
    "destination_system",
    "notification_system",
    "task_system",
}


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def require_keys(path: Path, data: dict[str, Any], required_keys: set[str]) -> list[str]:
    missing = sorted(required_keys - data.keys())
    return [f"{path}: missing required key '{key}'" for key in missing]


def require_non_empty_list(path: Path, data: dict[str, Any], key: str) -> list[str]:
    value = data.get(key)
    if not isinstance(value, list) or not value:
        return [f"{path}: '{key}' must be a non-empty list"]
    return []


def validate_blueprint(path: Path) -> list[str]:
    errors: list[str] = []
    data = load_json(path)
    if not isinstance(data, dict):
        return [f"{path}: root value must be an object"]

    errors.extend(require_keys(path, data, BLUEPRINT_REQUIRED_KEYS))
    for key in ("best_for", "required_inputs", "workflow_steps", "manual_tests", "handoff_instructions"):
        errors.extend(require_non_empty_list(path, data, key))

    trigger = data.get("trigger")
    if not isinstance(trigger, dict) or not trigger.get("event"):
        errors.append(f"{path}: trigger.event is required")

    for index, step in enumerate(data.get("workflow_steps", []), start=1):
        if not isinstance(step, dict):
            errors.append(f"{path}: workflow_steps[{index}] must be an object")
            continue
        for key in ("step", "name", "instructions"):
            if key not in step:
                errors.append(f"{path}: workflow_steps[{index}] missing '{key}'")

    for index, test in enumerate(data.get("manual_tests", []), start=1):
        if not isinstance(test, dict):
            errors.append(f"{path}: manual_tests[{index}] must be an object")
            continue
        for key in ("name", "input", "expected_result"):
            if key not in test:
                errors.append(f"{path}: manual_tests[{index}] missing '{key}'")

    return errors


def validate_project_inputs(path: Path) -> list[str]:
    errors: list[str] = []
    data = load_json(path)
    if not isinstance(data, dict):
        return [f"{path}: root value must be an object"]

    errors.extend(require_keys(path, data, PROJECT_REQUIRED_KEYS))

    systems = data.get("systems")
    if not isinstance(systems, dict):
        errors.append(f"{path}: systems must be an object")
    else:
        errors.extend(require_keys(path, systems, SYSTEM_REQUIRED_KEYS))

    for key in ("field_map", "qualification_rules", "message_templates", "test_records"):
        errors.extend(require_non_empty_list(path, data, key))

    owner_assignment = data.get("owner_assignment")
    if not isinstance(owner_assignment, dict):
        errors.append(f"{path}: owner_assignment must be an object")
    else:
        errors.extend(
            require_keys(
                path,
                owner_assignment,
                {"assignment_method", "assignment_rules", "fallback_owner", "sla_minutes"},
            )
        )
        errors.extend(require_non_empty_list(path, owner_assignment, "assignment_rules"))

    return errors


def main() -> int:
    errors: list[str] = []
    blueprint_paths = sorted(BLUEPRINT_DIR.glob("*.json"))
    if not blueprint_paths:
        errors.append(f"{BLUEPRINT_DIR}: no blueprint JSON files found")

    for path in blueprint_paths:
        errors.extend(validate_blueprint(path))

    errors.extend(validate_project_inputs(PROJECT_INPUTS))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(blueprint_paths)} blueprint files and 1 project input file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
