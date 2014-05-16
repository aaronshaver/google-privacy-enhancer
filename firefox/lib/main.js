const { BrowserSearchEngines } = require("browser-search-engine");
const gSearch = BrowserSearchEngines.get('Google');
const { storage } = require("sdk/simple-storage");
const { Request } = require("sdk/request");
const { Page } = require("sdk/page-worker");
const { setTimeout, clearTimeout } = require('sdk/timers');
const { data } = require('sdk/self');
const { prefs } = require("sdk/simple-prefs");

const ONE_SECOND = 1000;
const ONE_MINUTE = ONE_SECOND * 60;

const MAX_DELAY_TIME = 45 * ONE_SECOND;

var timeoutId;
var searches = 0;

// on load of the add-on get some words and assume our cache is always good
// if you want to be clever you should dump this cache after a certain amount of time
if (!storage.words) {
  Request({
    url: "https://raw.githubusercontent.com/clarkbw/GooglePrivacyEnhancer/master/word_list.txt",
    onComplete: function (response) {
      var result = response.text.split('\n');
      result = result.map(function (x) {
        return x.trim();
      });
      storage.words = result;
    }
  }).get();
}

function performSearch() {
  // grab a random term from the words
  var term = storage.words[Math.floor(Math.random() * storage.words.length)];
  // build a URL from the Firefox Search Service
  var url = gSearch.getSubmission(term);
  // console.log(term, "URL", url);
  // Create a page-worker to run our search service
  Page({
    contentScriptFile: data.url("search-worker.js"),
    contentURL: url,
    contentScriptOptions : { click : prefs.clickOnResults },
    onMessage: function(message) {
      if (++searches < prefs.totalSearches) {
        timeoutId = setTimeout(performSearch, Math.floor(Math.random() * MAX_DELAY_TIME));        
      }
      this.destroy();
    }
  });
}

exports.main = function () {
  timeoutId = setTimeout(performSearch, ONE_SECOND);
};

exports.onUnload = function () {
  clearTimeout(timeoutId);
};
