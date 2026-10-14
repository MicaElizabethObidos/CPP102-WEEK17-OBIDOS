# Test Cases – Simulated Device Monitoring and Alert System

Tested by: Obidos, Mica Elizabeth N.        Date: October 12, 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | View initial readings, choose 1 | Five readings: 28, 31, 35, 37, 29 | Five readings displayed correctly: 28, 31, 35, 37, 29 | Pass |
| TC02 | Add a valid reading, choose 2, enter 33 | "Reading added successfully." | Reading 33 added successfully. | Pass |
| TC03 | Non-numeric input, choose 2, enter abc | Rejected; list unchanged | Non-numeric input rejected; list unchanged. | Pass |
| TC04 | Below valid range, choose 2, enter -5 | Rejected; list unchanged | Reading rejected because it is below the valid range. | Pass |
| TC05 | Above valid range, choose 2, enter 120 | Rejected; list unchanged | Reading rejected because it exceeds the valid range. | Pass |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING | 30 °C displayed with WARNING status. | Pass |
| TC07 | Choose 3 | 35 °C -> WARNING | 35 °C displayed with WARNING status. | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Total: 160, Average: 32.00, Minimum: 28, Maximum: 37, Status: ATTENTION REQUIRED | Pass |
| TC09 | Invalid menu choice, enter 9 | Error message; menu shown again | Invalid choice message displayed; menu shown again. | Pass |
| TC10 | Exit, choose 5 | Exit message; program ends | Exit message displayed; program terminated. | Pass |

## Bugs Found and Fixed

One issue tested was the acceptance of invalid readings. Inputs such as abc, -5, and 120 must not be added to the readings list. This was addressed by adding input validation to reject non-numeric values and readings outside the allowed range of 0–50 °C. After validation, the list remained unchanged when invalid inputs were entered.
