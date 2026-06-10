#!/usr/bin/env python3
"""Grade yutto-downloader eval outputs."""
import json
import sys
import os

def check_command(path, assertions):
    """Read command and check all assertions."""
    with open(path) as f:
        cmd = f.read().strip()
    
    results = []
    for a in assertions:
        name = a["name"]
        check = a["check"]
        
        if check == "starts_with":
            expected = a["expected"]
            passed = cmd.startswith(expected)
            evidence = f"Command starts with '{expected}': {passed}"
        elif check == "contains":
            expected = a["expected"]
            passed = expected in cmd
            evidence = f"Command contains '{expected}': {passed}"
        elif check == "not_contains":
            expected = a["expected"]
            passed = expected not in cmd
            evidence = f"Command does not contain '{expected}': {passed}"
        elif check == "contains_any":
            options = a["options"]
            passed = any(o in cmd for o in options)
            evidence = f"Command contains any of {options}: {passed}"
        else:
            passed = False
            evidence = "Unknown check type"
        
        results.append({
            "text": name,
            "passed": passed,
            "evidence": evidence
        })
    
    return results

def main():
    if len(sys.argv) < 3:
        print("Usage: grade.py <command_txt_path> <assertions_json_path>")
        sys.exit(1)
    
    cmd_path = sys.argv[1]
    assertions_path = sys.argv[2]
    
    with open(assertions_path) as f:
        assertions_data = json.load(f)
    
    results = check_command(cmd_path, assertions_data["assertions"])
    
    output = {
        "graded_at": "",
        "results": results,
        "summary": {
            "passed": sum(1 for r in results if r["passed"]),
            "total": len(results),
            "pass_rate": sum(1 for r in results if r["passed"]) / len(results) if results else 0
        }
    }
    
    print(json.dumps(output, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
