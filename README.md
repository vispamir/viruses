
# Virus Chart

A simple GUI for create chart of Viruses.

## How to run

To run Virus Chart in development mode; Just use steps below:

1. Install `python3`, `pip`, `virtualenv` in your system.
2. Clone the project `https://github.com/vispamir/virus-chart`.
3. Make development environment ready using commands below:

  ```bash
  git clone https://github.com/vispamir/virus-chart && cd virus-chart
  virtualenv -p python3 build  # Create virtualenv named build
  source build/bin/activate
  sudo apt-get install python3-tk
  pip install -r requirements.txt
  ```

4. Run `Virus Chart` using `python main.py`

## Run On Windows

If You're On A Windows Machine , Make Environment Ready By Following Steps Below:
1. Install `python3`, `pip`, `virtualenv`
2. Clone the project using:  `git clone https://github.com/vispamir/virus-chart`.
3. Make Environment Ready Like This:
  ``` Command Prompt
  cd virus-chart
  git clone https://github.com/vispamir/virus-chart
  virutalenv -p "PATH\TO\Python.exe" build # Give Full Path To python.exe
  build\Scripts\activate # Activate The Virutal Environment
  pip install -r requirements.txt
  ```
4. Run `Virus Chart` using `python main.py`