import webbrowser

# This opens the browser if not open, and a new tab if browser is already open
webbrowser.open("https://python.org")

# We can also do this to make sure a new window is opened
# new=0 by default
webbrowser.open("https://python.org", new=1)

# This definitely opens a separate Web Browser Window
webbrowser.open_new("https://python.org")
