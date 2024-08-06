from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

# Define commands
home_path = os.path.expanduser("~")
script_path = os.path.join(home_path, 'path')

commands = {
    'Swipe Up': ['sudo', os.path.join(script_path, 'ttswipeup.sh')],
    'Swipe Down': ['sudo', os.path.join(script_path, 'ttswipedown.sh')],
    'Block': ['sudo', os.path.join(script_path, 'ttblock.sh')],
    'Block Live': ['sudo', os.path.join(script_path, 'ttliveblock.sh')],
    'Comment': ['sudo', os.path.join(script_path, 'ttcomment.sh')],
    'Back': ['sudo', os.path.join(script_path, 'ttback.sh')],
}

@app.route('/')
def index():
    buttons = [(label, f"/run-script/{label.replace(' ', '-').lower()}") for label in commands.keys()]
    return render_template('index.html', buttons=buttons)

@app.route('/run-script/<script>', methods=['POST'])
def run_script(script):
    script_name = script.replace('-', ' ').title()
    command = commands.get(script_name)
    
    if command:
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            return render_template('index.html', buttons=get_buttons(), output=output)
        except subprocess.CalledProcessError as e:
            error = e.stderr.decode('utf-8')
            return render_template('index.html', buttons=get_buttons(), error=error)
    else:
        return "Invalid script", 404

def get_buttons():
    return [(label, f"/run-script/{label.replace(' ', '-').lower()}") for label in commands.keys()]

if __name__ == '__main__':
    app.run(debug=True, port=8000)

