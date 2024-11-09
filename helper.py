from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()


def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Fetch the number of messages
    num_messages = df.shape[0]

    # Fetch the total number of words
    words = [word for message in df['message'] for word in message.split()]

    # Fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>'].shape[0]

    # Fetch number of links shared
    links = [url for message in df['message'] for url in extract.find_urls(message)]

    return num_messages, len(words), num_media_messages, len(links)


def most_busy_users(df):
    x = df['user'].value_counts().head()
    user_percent_df = (df['user'].value_counts(normalize=True) * 100).round(2).reset_index()
    user_percent_df.columns = ['name', 'percent']
    return x, user_percent_df


def create_wordcloud(selected_user, df):
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = f.read().splitlines()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[(df['user'] != 'group_notification') & (df['message'] != '<Media omitted>')]

    def remove_stop_words(message):
        return " ".join([word for word in message.lower().split() if word not in stop_words])

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc


def most_common_words(selected_user, df):
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = f.read().splitlines()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[(df['user'] != 'group_notification') & (df['message'] != '<Media omitted>')]
    words = [word for message in temp['message'] for word in message.lower().split() if word not in stop_words]

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    most_common_df.columns = ['Word', 'Frequency']
    return most_common_df






def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    # Create emoji_df with column names and check for empty DataFrame
    emoji_df = pd.DataFrame(Counter(emojis).most_common(), columns=['Emoji', 'Count'])

    return emoji_df


def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    timeline['time'] = timeline['month'] + "-" + timeline['year'].astype(str)
    return timeline


def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df.groupby('only_date').count()['message'].reset_index()


def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()


def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()


def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
