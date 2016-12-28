# Minecraft Population Logger
A command line tool to monitor the population of Minecraft servers. It creates
csv files containing the population data measured at regular intervals.

## Installation
1. Install Python 3. This may be compatibe with Python 2, but I wouldn't know.
2. Install the [mcstatus](https://github.com/Dinnerbone/mcstatus) library
wherever you've got Python instaled.

## Usage
Navigate to the directory containing this script and execute the following:
```bash
python poplog.py example.net:25565 mc.test.com:12345
```
Replace example.net and what-not with an endless list of servers you'd like to
monitor.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License
MIT, do whatever you want with it.
