# chesstempo Python player

An activity worker for [chesstempo] implemented with the [sdk-python].

# Build

Create a virtual environment and activate it:

    python -m venv .venv
    source .venv/bin/activate

Upgrade `pip` and install requirements:

    pip install -U pip
    pip install -r requirements.txt

Run the activity worker:

    python activity_worker.py

[chesstempo]: https://github.com/sevein/chesstempo
[sdk-python]: https://github.com/temporalio/sdk-python
