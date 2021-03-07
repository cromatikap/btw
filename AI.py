import os, sys, toml, openai, const, debug
from colored import style

CONF = toml.load('config.toml')

def generate_bash(user_input):
  start_sequence = "\nA:"
  restart_sequence = "\nQ: "

  openai.api_key = CONF['OPENAI_API_KEY']

  prompt_content = const.SHOW_AND_TELL + restart_sequence + user_input + start_sequence

  output = openai.Completion.create(
    engine="davinci",
    prompt=prompt_content,
    temperature=0.5,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.2,
    presence_penalty=0,
    stop=["\n"]
  )

  if(CONF['DEBUG']):
    debug.p(prompt_content + output.choices[0].text)

  return output.choices[0].text
  # return 'deactivated'