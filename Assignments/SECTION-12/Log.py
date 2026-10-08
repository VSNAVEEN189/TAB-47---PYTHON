'''Log File Analyzer
You'll practice
Parsing logs and writing a summary report
First, programmatically generate a sample log file of 100+ lines, each looking like:

2026-07-11 09:15:32 INFO  User logged in
2026-07-11 09:16:01 ERROR Database timeout

Then parse it and report:
• the count of each log level (INFO / WARNING / ERROR)
• every ERROR line together with its timestamp
• the hour with the most errors (the peak error hour)

Finally, write the summary to a separate output file.'''


logs = []

for i in range(120):
    hour = 9 + (i % 4)

    if i % 5 == 0:
        logs.append(
            f"2026-07-11 {hour:02d}:15:32 ERROR Database timeout\n"
        )

    elif i % 3 == 0:
        logs.append(
            f"2026-07-11 {hour:02d}:20:15 WARNING High memory usage\n"
        )

    else:
        logs.append(
            f"2026-07-11 {hour:02d}:25:10 INFO User logged in\n"
        )


with open("sample.log", "w") as file:
    for log in logs:
        file.write(log)

with open("sample.log", "r") as file:
    lines = file.readlines()

info_count = 0
warning_count = 0
error_count = 0

for line in lines:

    if "INFO" in line:
        info_count += 1

    elif "WARNING" in line:
        warning_count += 1

    elif "ERROR" in line:
        error_count += 1

error_lines = []

for line in lines:

    if "ERROR" in line:

        parts = line.strip().split(" ")

        date = parts[0]
        time = parts[1]

        timestamp = date + " " + time

        error_lines.append(
            timestamp + " - " + line.strip()
        )

error_hours = {}

for line in lines:

    if "ERROR" in line:

        parts = line.split(" ")

        time = parts[1]

        hour = time.split(":")[0]

        if hour not in error_hours:
            error_hours[hour] = 1
        else:
            error_hours[hour] += 1


peak_hour = ""
highest_errors = 0

for hour, count in error_hours.items():

    if count > highest_errors:
        highest_errors = count
        peak_hour = hour

summary = ""

summary += "LOG FILE ANALYSIS\n"
summary += "=================\n\n"

summary += "Log Counts\n"
summary += "INFO: " + str(info_count) + "\n"
summary += "WARNING: " + str(warning_count) + "\n"
summary += "ERROR: " + str(error_count) + "\n\n"

summary += "ERROR LOGS\n"
summary += "==========\n"

for error in error_lines:
    summary += error + "\n"

summary += "\nPEAK ERROR HOUR\n"
summary += "================\n"

summary += (
    peak_hour
    + ":00 - "
    + str(highest_errors)
    + " errors\n"
)

print(summary)

with open("summary.txt", "w") as file:
    file.write(summary)

print("Summary saved to summary.txt")