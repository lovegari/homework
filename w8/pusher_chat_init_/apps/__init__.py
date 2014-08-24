from flask import Flask
import os
import pusher

app = Flask('apps')
p = pusher.Pusher(
  app_id='86640',
  key='214cdb7f3f113b1df141',
  secret='bc95f3ac6945ea46b0b7'
)

userlist = {}

import controller