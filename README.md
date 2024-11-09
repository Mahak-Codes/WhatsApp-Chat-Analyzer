
# WhatsApp Chat Analyzer

WhatsApp Chat Analyzer is a data analysis tool for exploring WhatsApp chat data. This tool provides insights into chat statistics, such as the number of messages, media shared, most active users, and word frequencies. It also generates visualizations, such as word clouds and activity heatmaps, for better understanding user interactions and trends within a chat.

## Features

- **User Statistics:** Analyze messages, words, and media shared.
- **Active Users:** Identify the most active users in the chat.
- **Word Cloud:** Generate a word cloud to visualize the most common words used.
- **Timeline Analysis:** Monthly and daily message timelines.
- **Activity Analysis:** Visualize weekly and monthly activity patterns.
- **Emoji Analysis:** Discover frequently used emojis in the chat.
  
## Live Demo:
 ```bash
https://whatsapp-chat-analyzer-mahak-codes.streamlit.app/
```

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Mahak-Codes/WhatsApp-Chat-Analyzer.git
   cd WhatsApp-Chat-Analyzer
   ```

2. **Install Dependencies:**
   Ensure you have Python installed, then install dependencies from `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Export WhatsApp Chat:**
   - Export the chat data from WhatsApp (without media).
   - Save the file as `.txt`.

2. **Upload Chat Data:**
   - Upload the exported chat file to the application.
   - Select the user or analyze the entire chat by choosing "Overall."

3. **View Analysis:**
   - Explore various insights such as message frequency, most common words, most active users, emojis used, and more.

## Project Structure

```plaintext
WhatsApp-Chat-Analyzer/
│
├── app.py                   # Main application file for running Streamlit
├── helper.py                # Helper functions for data processing
├── requirements.txt         # Dependencies for the project
├── README.md                # Project documentation
├── stop_hinglish.txt        # Stopwords file for filtering common words
|
```

## Dependencies

This project requires Python 3 and the following libraries, listed in `requirements.txt`:

- pandas
- numpy
- streamlit
- wordcloud
- matplotlib
- seaborn
- emoji
- urlextract

## Sample Visualizations

- **Word Cloud:** Shows the most common words in the chat.
- **Activity Heatmap:** Visualizes chat activity throughout the week.
- **Emoji Distribution:** Highlights the most frequently used emojis.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance the functionality or improve the analysis.

## License

This project is licensed under the MIT License. See the [License](LICENSE) file for more details.
