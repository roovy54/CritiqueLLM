# Imports
from flask import Flask, request, render_template
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from templates_and_modules import reasoning_modules, SWOT_template
import json

# Creating mistral client and using the fine-tuned open-mistral-7b
api_key = "EIWurv5V0iQNBqbI4LixU5e8zInSyyPx"

client = MistralClient(api_key=api_key)
fine_tuned_model_id = "f1db735a-7d76-4cf6-bdbf-04b8a4a7181d"
retrieved_jobs = client.jobs.retrieve(fine_tuned_model_id)

model = retrieved_jobs.fine_tuned_model

# Flask backend
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def index():
    if request.method == 'POST':
        user_input = request.form['idea']
        response = get_response_from_llm(user_input)
        return render_template('index.html', user_input=user_input, response=response)
    return render_template('index.html')


# Function to get the output from the LLM
def generate_completion(prompt):
  chat_response = client.chat(
    model=model,
    messages=[ChatMessage(role="user", content=prompt)]
  )

  return chat_response.choices[0].message.content


# Function to generate the SWOT template and the output
def SWOT(user_task, reasoning_modules):
  SWOT_prompt = SWOT_template.format(user_task, reasoning_modules)
  output = generate_completion(SWOT_prompt)
  return output

# Gets the output and converts to SWOT
def get_response_from_llm(user_input):
    SWOT_output = SWOT(user_input, reasoning_modules)
    SWOT_json = json.loads(SWOT_output)

    return SWOT_json

if __name__ == '__main__':
    app.run(debug=True)
