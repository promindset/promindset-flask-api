ssh rajjix "
	cd ~/FlaskApi;
	source .venv/bin/activate;
	git pull;
	pip install -r requirements.txt;
	sudo systemctl restart apache2
"
