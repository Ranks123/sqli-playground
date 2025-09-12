# Proof of Concept: Python-Based Blind SQL Injection Data Extractor

## Overview
This report documents a custom Python script (`blind_sqli_extractor.py`) designed to automate the extraction of sensitive data via a Blind SQL Injection vulnerability. The script systematically retrieves the administrator password by triggering conditional database errors.

## Script Purpose
- **Automates** the process of blind SQL injection exploitation.
- **Detects** the underlying database type (Oracle vs. MySQL/Postgres/MSSQL).
- **Determines** the length of the target password.
- **Extracts** the password character by character using boolean condition timing.

## Technical Details
- **Language:** Python 3
- **Key Libraries:** `requests`
- **Target Vulnerability:** Blind SQL Injection (Error-Based)
- **Method:** Sending payloads that trigger a server error (HTTP 500) only when a guessed character is correct.

## How It Works

### 1. Database Detection
The script sends two test payloads:
- One using `SUBSTRING()` (for MySQL, Postgres, MSSQL)
- One using `SUBSTR()` (for Oracle)
The database type is identified based on which payload triggers an error.

### 2. Password Length Enumeration
It iterates through possible password lengths until a conditional error is triggered, confirming the correct length.

### 3. Password Extraction
For each character position, it iterates through printable ASCII values. A payload is sent that causes a database error *only if* the guessed character is correct.

### 4. Output
The extracted password is printed to the console in real-time.

## Example Usage
```bash
cd ~/projects/sqli-playground/scripts
python3 blind_sqli_extractor.py```
 
###Impact

This tool demonstrates how blind SQLi vulnerabilities can be exploited to:

   Extract complete sensitive data without direct output.

   Automate attacks that would be infeasible manually.

   Adapt to different database backends.

##Remediation

   Use parameterized queries to prevent SQL injection.

   Implement least privilege principles for database users.

   Monitor and log repeated error-based requests.

Author: Ranks123
Date: $(date 2025-9-12)

