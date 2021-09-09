var popupWindow = window.open(
    chrome.extension.getURL("popup.html"),
    "targetWindow",
    "width=300,height=380"
);

window.close();