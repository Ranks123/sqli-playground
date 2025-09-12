# SQLi Playground

A repository showcasing practical SQL Injection (SQLi) vulnerabilities, proof-of-concept exploits, and demonstration scripts. Built for educational purposes to understand web application security.

## 📁 Contents

- **Proof of Concept Reports:** Detailed write-ups of successful SQLi exploits.
- **Scripts:** Python automation for exploitation and data extraction.
- **Screenshots:** Visual evidence of vulnerabilities and exploits.
- **Demo Video:** A quick screen recording showing an exploit in action.

## 🔍 Proof of Concept Reports

1.  **[SQLi-Labs Lesson 1 Exploit](./report-dvwa.md)**  
    - **Type:** Union-Based SQL Injection  
    - **Vulnerability:** Error-based extraction via unprotected `id` parameter.  
    - **Result:** Extraction of database version and name.

2.  **[PortSwigger Blind SQLi Lab Exploit](./report-psql-lab.md)**  
    - **Type:** Time-Based Blind SQL Injection  
    - **Vulnerability:** Conditional time delays via cookie parameter.  
    - **Result:** Extraction of administrator password.

3.  **[Python SQLi Automation](./report-automation.md)**  
    - **Type:** Automated Blind SQL Injection  
    - **Vulnerability:** Error-based blind extraction via Python scripting.  
    - **Result:** Demonstrates automated password extraction.

## 🛠️ Scripts


- **[Blind SQLi Data Extractor](./scripts/blind_sqli_extractor.py)**  
  A Python script that automates the extraction of sensitive data via error-based blind SQL injection. Features database detection, length enumeration, and character-by-character extraction.

## 🎥 Demo Video

*(Link to demo video will be added here)*

## ⚠️ Disclaimer

This project is for **educational and ethical testing purposes only**. Always ensure you have explicit permission before testing any system. The vulnerabilities demonstrated are in intentionally vulnerable applications (e.g., DVWA, SQLi-Labs) run in isolated environments.

---

## 📝 Author

Created by [Ranks123](https://github.com/Ranks123).
