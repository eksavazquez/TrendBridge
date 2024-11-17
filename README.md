# TrendBridge  
**Connecting the trends across platforms, one post at a time.**  

---

## Overview  
🚀 **TrendBridge** is a bot that identifies trending topics on X (formerly Twitter) and shares them with users on Bluesky. Stay ahead of the conversation with real-time updates on what's buzzing across platforms!  

---

## Features  
- 🔍 **Real-time trend detection**: Fetches the top trending topics from X.  
- 🛠 **Customizable categories**: Filter trends by region, hashtags, or topics of interest.  
- 🌐 **Seamless cross-platform posting**: Automatically formats and posts trends to Bluesky.  
- 🤖 **Scheduled updates**: Configurable posting intervals to keep your Bluesky feed fresh.  

---

## How It Works  

1. **Fetch Trends from X**:  
   The bot uses the X API to pull trending hashtags, keywords, or topics.  
   
2. **Format for Bluesky**:  
   The content is tailored for Bluesky's audience with engaging and concise posts.  

3. **Post to Bluesky**:  
   Trends are shared in real-time or at scheduled intervals via the Bluesky API.  

---

## Getting Started  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/eksavazquez/TrendBridge.git
   cd TrendBridge

2. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Up API Keys**:
* **X API Key**: Create a developer account on X and obtain an API key.  
* **Bluesky API Key**: Create a developer account on Bluesky and obtain an API key.
* Add these keys to the .env file:
```bash
    X_API_KEY=your_x_api_key
    BLUESKY_API_KEY=your_bluesky_api_key
```
4. **Run the Bot**:
```bash
    python trendbridge.py
```
## Configuration Options
Modify the `config.yaml` file to:

* Adjust trend-fetching regions (e.g., Global, US, Japan).
* Set posting intervals (e.g., every hour, twice a day).
* Enable/disable specific categories (e.g., Sports, Entertainment).

## Example Post
Here’s what a post might look like:

Trending Now on X 🌟
🚀 #SpaceExploration is trending!
NASA announces its new Mars mission.
Join the conversation on Bluesky!

## Planned Features
Trend Comparison: Highlight differences in trends between X and Bluesky.
Engagement Metrics: Track how users engage with the posted trends.
Localized Trends: Automatically adjust trends based on the user's region.
## Contributions
Contributions are welcome! Feel free to open issues, suggest features, or submit pull requests.

## License
This project is licensed under the MIT License.

Stay trendy, stay connected! 🌐
