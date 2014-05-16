function isVisible(elem) {
  return (elem && (elem.offsetWidth > 0 || elem.offsetHeight > 0));
}

var nodes = document.evaluate('//div/h3/a', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null );
var rand = Math.floor(Math.random() * nodes.snapshotLength);
var item = nodes.snapshotItem(rand);

if (item && isVisible(item)) {
  try {
    if (self.options.click) {
      item.click();      
    }
  } catch (ignore) { }
  self.postMessage(true);
} else {
  self.postMessage(false);
}
