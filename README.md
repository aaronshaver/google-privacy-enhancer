Google Privacy Enhancer
=====================

Are you worried about Google assembling a profile on you based on your search engine history?

Google Privacy Enhancer performs random searches at random intervals while you are logged into your Google account. This "fuzzes" your search history, making it difficult for Google or other parties -- such as anyone monitoring your web traffic over the wire -- to gather information about you. This doesn't guarantee privacy or anonymity, but it should frustrate the efforts of those who would like to follow you, analyze you, and sell to you on the web.

Google Privacy Enhancer interacts with Google.com, but it could be adapted for use with other sites, such as Amazon.com. (Have you noticed your Amazon search history influencing targeted ads on sites other than Amazon? It happens!)

Installation and Usage
------------

1. Install Python 3.x on your machine: https://www.python.org/downloads/
2. Install Selenium for Python: `pip install selenium`
  3. Python 3.4+ comes with pip
  4. If Python isn't in your PATH, you might need to do something like `C:\Python34>Scripts\pip.exe install selenium`
3. Install Firefox on your machine: http://www.mozilla.org/en-US/firefox/new/
  4. You can easily use other browsers such as Chrome. It's a one-line code change to use a different driver for Selenium; search for examples on the Web.
4. Run the script from your commandline: `script.py`
5. On your own system using Scheduled Tasks or other means, you might schedule the script to run for as long as you'd like. Set it to run at particular times of the day (e.g. in the middle of the night if you don't want it interrupting you), or if you'd prefer to have the search results look more human, you could start the script on random time intervals instead of having large blocks of search data show up all at once.
