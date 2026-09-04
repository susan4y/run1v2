import anvil.server
import gradio as gr
from flask import Flask

# 1. Create your Flask app
flask_app = Flask(__name__)

@flask_app.route("/api")
def hello():
  return {"message": "Hello from Flask!"}

# 2. Create your Gradio interface
def greet(name):
  return f"Hello {name}!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# 3. Mount Flask inside Gradio and launch
app = gr.mount_wsgi_app(flask_app)

if __name__ == "__main__":
  demo.launch()

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
