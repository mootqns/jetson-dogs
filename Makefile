run:
	nohup python3 src/flask_app.py > logs/flask.log 2>&1 &
	nohup ngrok http 5000 > logs/ngrok.log 2>&1 &
	nohup python3 src/detection.py > logs/detection.log 2>&1 &
	@echo "processes started: flask_app.py, ngrok, detection.py"

stop:
	-kill `pgrep -f flask_app.py`
	-kill `pgrep -f ngrok`
	-kill `pgrep -f detection.py`
	@echo "processes stopped: flask_app.py, ngrok, detection.py"
