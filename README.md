Google Privacy Enhancer
=====================

Are you worried about websites assembling a profile on you based on your search engine history? Would you like your searching to be more private?

Google Privacy Enhancer performs random searches at random intervals while you are logged into your Google account for as long as you let it run. This acts to "fuzz" your search history, making it difficult for Google or other parties -- such as anyone monitoring your web traffic over the wire -- to assemble a profile on you.

Google Privacy Enhancer interacts with Google.com, but it could be adapted for use with other sites, such as Amazon.com. (Have you noticed your Amazon search history influencing targeted ads on sites other than Amazon? I have!)

Installation and Usage
------------

1. Install Python 3.x on your machine: https://www.python.org/downloads/
2. Install Selenium for Python: `pip install selenium`
  3. Python 3.4+ comes with pip
  4. If Python isn't in your PATH, you might need to do something like `C:\Python34>Scripts\pip.exe install selenium`
3. Install Firefox on your machine: http://www.mozilla.org/en-US/firefox/new/
  4. You can easily use other browsers such as Chrome. It's a one-line code change to use a different driver for Selenium; search for examples on the Web.
4. Run the script from your commanndline: `script.py`
5. Let the script run for as long as you'd like. You could even have the script run at particular times of day (e.g. in the middle of your night) on a schedule if you don't want it interrupting you, or if you want to make the search windows look realistic as opposed to big blocks of searching at once.
