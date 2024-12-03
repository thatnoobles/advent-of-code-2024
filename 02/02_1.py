def report_safe(levels: list[int]):
    levels = [int(x) for x in report.split(" ")]

    # check for all increasing / all decreasing
    if levels != sorted(levels) and levels != sorted(levels, reverse=True):
        return False

    for i in range(0, len(levels) - 1):
        if abs(levels[i + 1] - levels[i]) not in range(1, 4):
            return False

    return True

#############################

reports = []

with open("input.txt", "r") as file:
    reports = file.readlines()

safe_reports = 0

for report in reports:
    levels = [int(x) for x in report.strip().split(" ")]
    safe_reports += 1 if report_safe(levels) else 0

print(safe_reports)