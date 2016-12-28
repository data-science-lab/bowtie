# 引入下面的代码，然后在bash中运行
# > nohup python my_python_program.py &

import logging

logging.basicConfig(level=logging.DEBUG,
	format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
	datefmt='%a, %d %b %Y %H:%M:%S',
	filename='mycalc.log',
	filemode='w')

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)

logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This is debug message')

