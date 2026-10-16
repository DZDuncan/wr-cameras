.PHONY: stream

stream: streamer.py
	uv run streamer.py

receive: receiver.py
	uv run receiver.py

amcrest: amcrest.py
	set -a; . ./.env; set +a; uv run amcrest.py