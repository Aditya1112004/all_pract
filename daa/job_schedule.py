class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id  # Unique identifier for the job
        self.deadline = deadline  # Deadline of the job
        self.profit = profit  # Profit if the job is completed

# Function to perform job sequencing with deadlines
def job_sequencing(jobs, max_deadline):
    # Sort jobs by descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Initialize time slots (all initially free)
    slots = [-1] * max_deadline  # -1 indicates free slot
    total_profit = 0  # Track total profit
    job_sequence = []  # Track job sequence

    for job in jobs:
        # Try to find a free slot from the last possible time slot to the first
        for j in range(min(max_deadline - 1, job.deadline - 1), -1, -1):
            if slots[j] == -1:  # Check if slot is free
                slots[j] = job.job_id  # Assign job to the slot
                total_profit += job.profit  # Add profit
                job_sequence.append(job.job_id)  # Record job in sequence
                break  # Move to the next job

    return job_sequence, total_profit

# Example usage
jobs = [
    Job('A', 2, 100),
    Job('B', 1, 19),
    Job('C', 2, 27),
    Job('D', 1, 25),
    Job('E', 3, 15)
]
max_deadline = 3
job_sequence, total_profit = job_sequencing(jobs, max_deadline)

print("Job sequence:", job_sequence)
print("Total profit:", total_profit)
