import subprocess


# opens a new process and runs the script given
def call_script(script_path):
    subprocess.Popen([script_path], shell=True, creationflags=subprocess.SW_HIDE)


