def report_safe(levels: list[int], error_tolerated: bool):
    originally_safe = True

    # check for all increasing / all decreasing
    if levels != sorted(levels) and levels != sorted(levels, reverse=True):
        originally_safe = False

    if originally_safe:
        for i in range(0, len(levels) - 1):
            if abs(levels[i + 1] - levels[i]) not in range(1, 4):
                originally_safe = False

    if originally_safe:     # report is safe without alterations
        return True
    elif error_tolerated:   # report is unsafe with one defect already found
        return False
    
    for i in range(len(levels)):
        levels_altered = levels.copy()
        levels_altered.pop(i)
        if report_safe(levels_altered, True):
            return True

    return False

#############################

reports = []

with open("input.txt", "r") as file:
    reports = file.readlines()

safe_reports = 0

for report in reports:
    levels = [int(x) for x in report.strip().split(" ")]
    safe_reports += 1 if report_safe(levels, False) else 0

print(safe_reports)