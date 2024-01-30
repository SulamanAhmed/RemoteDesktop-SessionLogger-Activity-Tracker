import pandas as pd
from datetime import datetime, timedelta
import os

def get_todays_date_formatted():
    # Get today's date and format it as 'YYYY-MM-DD'
    return datetime.today().strftime("%Y-%m-%d")

def calculate_work_hours(data, user, log_messages):
    data = sorted([(datetime.strptime(time_str, "%m/%d/%Y %I:%M:%S %p"), code) for time_str, code in data], key=lambda x: x[0])
    open_time = None
    total_work_duration = timedelta()
    previous_event = None
    previous_time = None

    for time, code in data:
        if code in [21, 25]:  # Open connection
            if open_time is None:
                open_time = time
                log_messages.append(f"{user} - Connection opened at {time}")
            elif previous_event in [23, 24] and previous_time != time:
                total_work_duration += time - open_time
                log_messages.append(f"{user} - Connection closed at {previous_time}, Duration: {time - open_time}")
                log_messages.append(f"{user} - Connection reopened at {time}")
                open_time = time
        elif code in [23, 24] and open_time is not None:  # Close connection
            if previous_event in [21, 25] and previous_time == time:
                continue
            work_duration = time - open_time
            total_work_duration += work_duration
            log_messages.append(f"{user} - Connection closed at {time}, Duration: {work_duration}")
            open_time = None

        previous_event = code
        previous_time = time

    total_hours = int(total_work_duration.total_seconds() // 3600)
    total_minutes = int((total_work_duration.total_seconds() % 3600) // 60)
    return f"{total_hours} hours, {total_minutes} minutes"

# Get today's date in the required format and construct the filename
today_date_str = get_todays_date_formatted()
filename = os.path.join(r'C:\Users\Sulaman\Desktop', f'output-detailed-{today_date_str}.csv')

# Check if the file exists
if not os.path.exists(filename):
    print(f"File not found: {filename}")
    exit()

df = pd.read_csv(filename)

# List of keywords to track
keywords = ['Sulaman']
total_work_dict = {}
log_messages = []

for keyword in keywords:
    filtered_df = df[df['Message'].str.contains(keyword, na=False)]
    data = filtered_df[['TimeCreated', 'Id']].values.tolist()
    total_work_time = calculate_work_hours(data, keyword, log_messages)
    total_work_dict[keyword] = total_work_time
    print(f"Total work time for {keyword}: {total_work_time}\n")

# Create a summary DataFrame
summary_df = pd.DataFrame(list(total_work_dict.items()), columns=['Keyword', 'TotalWorkTime'])

# Save the summary CSV and log text files to the desktop
desktop_path = r'C:\Users\Sulaman\Desktop'
summary_csv_filename = os.path.join(desktop_path, f'work_time_summary-{today_date_str}.csv')
summary_df.to_csv(summary_csv_filename, index=False)
print(f"Work time summary has been saved to {summary_csv_filename}.")

log_txt_filename = os.path.join(desktop_path, f'work_time_logs-{today_date_str}.txt')
with open(log_txt_filename, 'w') as log_file:
    log_file.write('\n'.join(log_messages))
print(f"Work time logs have been saved to {log_txt_filename}.")
