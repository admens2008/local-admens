#!/usr/bin/env python3

from website import create_app

# app = create_app()

if __name__ == '__main__':
	app = create_app()
	app.run(debug=True)