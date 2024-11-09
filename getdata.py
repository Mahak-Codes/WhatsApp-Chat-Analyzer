import re
import pandas as pd


def preprocess(data):
    # Updated pattern to match date with AM/PM format
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[APMapm]{2}\s-\s'

    # Split messages and extract dates based on the pattern
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    # Create DataFrame with messages and dates
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Convert 'message_date' to datetime
    df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %I:%M %p - ')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Initialize lists for users and messages
    users = []
    messages = []
    for message in df['user_message']:
        # Split each message into user and content
        entry = re.split(r'([\w\W]+?):\s', message)
        if len(entry) > 2:  # Message with user
            users.append(entry[1])
            messages.append(" ".join(entry[2:]).replace('<This message was edited>', '').strip())
        else:  # System message or media
            users.append('group_notification')
            messages.append(entry[0].replace('<Media omitted>', '').strip())

    # Add user and message columns to DataFrame
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    # Additional date-related columns
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Generate period column
    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(f"{hour}-00")
        elif hour == 0:
            period.append("00-1")
        else:
            period.append(f"{hour}-{hour + 1}")

    df['period'] = period

    # Filter out encryption and disappearing message notifications
    df = df[~df['message'].str.contains('Messages and calls are end-to-end encrypted', case=False)]
    df = df[~df['message'].str.contains('You use a default timer for disappearing messages', case=False)]

    return df
