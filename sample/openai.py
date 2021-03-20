import os, sys, toml, openai
from colored import style
from sample import log, const, config

def generate_bash(user_input):
  log.debug('openai.generate_bash("' + user_input + '"): ')
  start_sequence = "\nA:"
  restart_sequence = "\nQ: "

  openai.api_key = config.get('OPENAI_API_KEY')

  prompt_content = const.SHOW_AND_TELL + restart_sequence + user_input + start_sequence
  
  try:
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

    log.debug(prompt_content + output.choices[0].text)

    return output.choices[0].text
  except:
    log.debug('Wrong API key.')
    return False