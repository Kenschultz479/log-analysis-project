# Brute Force Detection Lab

## Overview
This lab simulates a brute force login attack by analyzing repeated failed login attempts from the same source IP.

## Objective
Detect suspicious authentication patterns that may indicate password guessing or unauthorized access attempts.

## Files
- `sample_logs.txt` - simulated authentication log data
- `brute_force_detector.py` - Python script that identifies repeated failed logins from the same IP
- `incident_report.md` - summary of findings and recommended response actions

## Skills Demonstrated
- Log analysis
- Python scripting
- Brute force detection
- Incident documentation
- Basic threat investigation

## Example Detection Logic
The script flags a possible brute force event when the same IP address generates 3 or more failed login attempts.

## MITRE ATT&CK
- T1110 - Brute Force