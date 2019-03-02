import subprocess
params = ['convert', 'mypdf.pdf', 'thumb.jpg']
subprocess.check_call(params)
