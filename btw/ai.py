import os, sys, toml, openai
from . import log, const, config
from .History import History
from colored import style

def generate_bash(user_input):
  log.debug('openai.generate_bash("' + user_input + '"): ')
  start_sequence = "\nA:"
  restart_sequence = "\nQ: "

  openai.api_key = config.get('OPENAI_API_KEY')
  history = History()

  prompt_content = const.SHOW_AND_TELL
  prompt_content += history.get_q_and_a()
  prompt_content += restart_sequence + user_input + start_sequence

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

  except openai.error.AuthenticationError as e:
    log.error['arg']('[ OpenAI ] : ' + str(e))
    return False