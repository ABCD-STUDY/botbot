# botbot

Sends out information about the ABCD study.

## Minimal setup for development

Use python for the botbot.

Install Homebrew. Use:
```
brew install python3
```

### Example using discord.py (not working)

Now install discord:
```
python3 -m pip install -U discord
python3 -m pip install -U asyncio
```

### Example using disco-py (working)
(Using python 2.7, see https://github.com/b1naryth1ef/disco)

```
pip install disco-py
python -m disco.cli --token=<YOUR TOKEN> --run-bot --plugin botbot2
```
