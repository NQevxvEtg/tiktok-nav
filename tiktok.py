from flask import Flask, request
import subprocess
import os

home_path = os.path.expanduser("~")

script_path = home_path + '/path/'

ttswipeup = os.path.join(script_path, 'ttswipeup.sh')
ttswipedown = os.path.join(script_path, 'ttswipedown.sh')
ttblock = os.path.join(script_path, 'ttblock.sh')
ttliveblock = os.path.join(script_path, 'ttliveblock.sh')
ttcomment = os.path.join(script_path, 'ttcomment.sh')

# Command to execute the script with sudo
ttswipeup_command = ['sudo', ttswipeup]
ttswipedown_command = ['sudo', ttswipedown]
ttblock_command = ['sudo', ttblock]
ttliveblock_command = ['sudo', ttliveblock]
ttcomment_command = ['sudo', ttcomment]

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
        <form method="POST" action="/run-script1">
            <button type="submit" class="button">Swipe Up</button>
        </form>
        <form method="POST" action="/run-script2">
            <button type="submit" class="button">Swipe Down</button>
        </form>
        <form method="POST" action="/run-script3">
            <button type="submit" class="button">Block</button>
        </form>
        <form method="POST" action="/run-script4">
            <button type="submit" class="button">Block Live</button>
        </form>
        <form method="POST" action="/run-script5">
            <button type="submit" class="button">Comment</button>
        </form>
        <div id="output"></div>
    '''

@app.route('/run-script1', methods=['POST'])
def run_script1():
    return run_script(ttswipeup_command)

@app.route('/run-script2', methods=['POST'])
def run_script2():
    return run_script(ttswipedown_command)

@app.route('/run-script3', methods=['POST'])
def run_script3():
    return run_script(ttblock_command)

@app.route('/run-script4', methods=['POST'])
def run_script4():
    return run_script(ttliveblock_command)

@app.route('/run-script5', methods=['POST'])
def run_script5():
    return run_script(ttcomment_command)


def run_script(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        return f'''
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
        <form method="POST" action="/run-script1">
            <button type="submit" class="button">Swipe Up</button>
        </form>
        <form method="POST" action="/run-script2">
            <button type="submit" class="button">Swipe Down</button>
        </form>
        <form method="POST" action="/run-script3">
            <button type="submit" class="button">Block</button>
        </form>
        <form method="POST" action="/run-script4">
            <button type="submit" class="button">Block Live</button>
        </form>
        <form method="POST" action="/run-script5">
            <button type="submit" class="button">Comment</button>
        </form>
            <div id="output">
                <h3>Script output:</h3>
                <pre>{output}</pre>
            </div>
        '''
    except subprocess.CalledProcessError as e:
        error = e.stderr.decode('utf-8')
        return f'''
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
        <form method="POST" action="/run-script1">
            <button type="submit" class="button">Swipe Up</button>
        </form>
        <form method="POST" action="/run-script2">
            <button type="submit" class="button">Swipe Down</button>
        </form>
        <form method="POST" action="/run-script3">
            <button type="submit" class="button">Block</button>
        </form>
        <form method="POST" action="/run-script4">
            <button type="submit" class="button">Block Live</button>
        </form>
        <form method="POST" action="/run-script5">
            <button type="submit" class="button">Comment</button>
        </form>
            <div id="output">
                <h3>An error occurred:</h3>
                <pre>{error}</pre>
            </div>
        '''

if __name__ == '__main__':
    app.run(debug=True, port=8000)
