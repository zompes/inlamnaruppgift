from browser import window
j = window.jQuery
from Application import Application

# INTE KLART, SAKNAR ÅTMINSTONE SPELARLOOPEN OCH NÄTVERK

# Create a new application
j('body').html(str(Application()))