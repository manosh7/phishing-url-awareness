# Test Results

Python version used: 3.12.14 (bundled runtime)  |  Operating system: Windows  |  Date: 2026-11-08

I ran each of the five workbook sample URLs through `phishing_checker.py` and compared the output with the expected warning signs. All five results matched.

| # | Sample URL | Expected result | Actual result | Status |
|---:|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs | No listed warning signs; safety reminder shown | PASS |
| 2 | `http://192.0.2.10/account` | IP address and HTTP warnings | Both warnings shown; 2 warnings | PASS |
| 3 | `http://example.com@sample.invalid/login` | `@` and HTTP warnings | Both warnings shown; 2 warnings | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname parts warning | Warning shown; 1 warning | PASS |
| 5 | `https://xn--example.invalid/` | Punycode warning | Warning shown; 1 warning | PASS |

## Additional Checks

| Check | Input or action | Observed result | PASS/FAIL |
|---|---|---|---|
| Empty input | Press Enter / whitespace only | `No URL entered.`; warning count is zero. | PASS |
| Missing scheme | `www.example.com` | Scheme is treated as `http://`; HTTP warning appears. | PASS |
| URL over 100 characters | `https://example.com/` followed by 100 `a` characters | Unusually long URL warning appears. | PASS |
| Malformed URL | `http://[bad` | `This text is not a valid URL format.`; process continues. | PASS |
| Multiple URL checking | Malformed URL, then `http://192.0.2.10/account` in one session | Both results print; malformed input does not stop the next check. | PASS |
| Quit command `q` | Enter `q` at prompt | Goodbye message prints and the program exits. | PASS |
| Quit command `quit` | Enter `quit` at prompt | Goodbye message prints and the program exits. | PASS |
| Quit command `exit` | Enter `exit` at prompt | Goodbye message prints and the program exits. | PASS |
| Warning count | Clean, informational, and two-warning results | Informational messages count as zero; the two-warning URL reports 2. | PASS |
| Python syntax | Parse `phishing_checker.py` with the Python 3.12.14 runtime | No syntax errors. | PASS |

## Notes

The five required examples produced the workbook's specified warning messages. Empty and malformed input are treated as information rather than warning signs, and the session continues after malformed input.

The checker only examines URL text locally. The required screenshots are saved in `screenshots/sample_run.png` and `screenshots/test_results.png`. The test-results screenshot shows this report open in VS Code, as allowed by the workbook.

