Livefyre API Client
-------------------

::

    from livefyre.client import LivefyreClient
    client = LivefyreClient("...domain...", "...domain secret key...")
    client.ping()

Running Tests
=============

::

    export LIVEFYRE_CLIENT_SECRET=...
    export LIVEFYRE_CLIENT_ID=...
    export LIVEFYRE_API_ENDPOINT=...
    
    python setup.py nosetests

