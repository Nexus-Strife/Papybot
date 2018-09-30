#! /usr/bin/env python

#File used to launch the server: "python run.py"
from views import app

if __name__ == "__main__":
	app.run(debug=False)
