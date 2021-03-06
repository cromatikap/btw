# By the way...

... let's turn Arch Linux into life using openai API.

## Usage

It is as simple as this: `btw <human command description>`

### Examples:
```
$ btw turn on the bluetooth service
openai@localhost $ systemctl start bluetooth
$ btw delete anything compromising on the disk
openai@localhost $ dd if=/dev/urandom of=/dev/sda bs=1M
```

## Getting started

### Cloning & configuration
```
$ git clone git@github.com:bidetaggle/bytheway.git
$ cp config.template.toml config.toml
$ nano config.toml               # <-- Add your openai API key here
```

### Environment setup
```
$ virtualenv .venv
$ source ./.venv/bin/activate
(.venv) $ pip install -r requirements.txt
(.venv) $ alias btw="python btw.py"
```

And you're ready to go 🥳
