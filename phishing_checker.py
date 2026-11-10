"""Inspect URL text for a small set of educational phishing warning signs."""

import re
from urllib.parse import urlparse


INFO_MESSAGES = (
    "No URL entered.",
    "Could not identify a hostname.",
    "This text is not a valid URL format.",
    "No listed warning signs found. This does NOT prove safety.",
)


def inspect_url(raw_url):
    """Return warning or information messages for one URL string.

    The URL is only parsed as text. This function never opens a connection.
    """
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    # Add a scheme so urlparse can identify the hostname consistently.
    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # This follows the workbook's IPv4-shaped hostname regular expression.
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append("No listed warning signs found. This does NOT prove safety.")

    return findings


def warning_count(findings):
    """Count actual warnings, excluding informational result messages."""
    return sum(
        1
        for finding in findings
        if not finding.startswith(INFO_MESSAGES)
    )


def main():
    """Keep checking URL text until the user chooses to quit."""
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")
        for item in findings:
            print("- " + item)

        count = warning_count(findings)
        if count:
            print(f"\nREVIEW CAREFULLY: {count} warning sign(s) found.")
        elif findings[0].startswith("No listed warning signs"):
            print("\nWarning summary: 0 warning sign(s) found.")

        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()

