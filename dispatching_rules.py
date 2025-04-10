# AIML333 Assignment 2 - Q3
# Dispatching Rules: FCFS, SPT, EDD
jobs = [
    {'id': 'A', 'AT': 0, 'PT': 11, 'DD': 61},
    {'id': 'B', 'AT': 1, 'PT': 29, 'DD': 45},
    {'id': 'C', 'AT': 2, 'PT': 31, 'DD': 31},
    {'id': 'D', 'AT': 3, 'PT': 1,  'DD': 33},
    {'id': 'E', 'AT': 4, 'PT': 2,  'DD': 32},
]

def schedule_jobs(rule):
    if rule == 'FCFS':
        sorted_jobs = sorted(jobs, key=lambda j: j['AT'])
    elif rule == 'SPT':
        sorted_jobs = sorted(jobs, key=lambda j: (j['PT'], j['AT']))
    elif rule == 'EDD':
        sorted_jobs = sorted(jobs, key=lambda j: (j['DD'], j['AT']))
    else:
        raise ValueError("Unsupported rule")

    current_time = 0
    results = []
    for job in sorted_jobs:
        start_time = max(current_time, job['AT'])
        finish_time = start_time + job['PT']
        flowtime = finish_time - job['AT']
        tardiness = max(finish_time - job['DD'], 0)
        current_time = finish_time

        results.append({
            'Job': job['id'],
            'Start': start_time,
            'Finish': finish_time,
            'Flowtime': flowtime,
            'Tardiness': tardiness
        })

    return results

def print_schedule(rule):
    schedule = schedule_jobs(rule)
    total_flow = sum(job['Flowtime'] for job in schedule)
    total_tard = sum(job['Tardiness'] for job in schedule)
    avg_flow = total_flow / len(schedule)
    avg_tard = total_tard / len(schedule)

    print(f"\n--- {rule} Schedule ---")
    for job in schedule:
        print(f"{job['Job']}: Start={job['Start']}, Finish={job['Finish']}, "
              f"Flowtime={job['Flowtime']}, Tardiness={job['Tardiness']}")
    print(f"Average Flowtime: {avg_flow:.2f}")
    print(f"Average Tardiness: {avg_tard:.2f}")
    print()

# Run all rules
for rule in ['FCFS', 'SPT', 'EDD']:
    print_schedule(rule)
