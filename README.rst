plant-disease-classification-api
================================

**plant-disease-classification-api** is a REST API project that aims to classify diseases on plants. It is based on the ML models available at
`https://github.com/abdullahselek/plant-disease-classification-models <https://github.com/abdullahselek/plant-disease-classification-models>`_. I aimed to keep this
API simple so there is only one endpoint available which is responsible from classification. I plan to add more advanced ML models in the future so endpoint is designed
to support this. API has available Swagger interface for quick tests and documentation. After you launch the project it will be available on `docs <http://127.0.0.1:8000/docs#/>`_.

List of contents
----------------

- `Installation <#installation>`_
- `Requirements <#requirements>`_
- `Running tests <#running-tests>`_
- `Running <#running>`_
- `License <#license>`_

Installation
------------

The code is hosted at this `repo <https://github.com/abdullahselek/plant-disease-classification-api>`_. Check out the latest main version anonymously with::

    git clone git://github.com/abdullahselek/plant-disease-classification-api.git
    cd plant-disease-classification-api

Requirements
------------

- Python 3.6 or higher
- Python modules available in requirements.txt
- Installation using ``pip install -r requirements.txt``

Running tests
-------------

- Complete [requirements](#requirements) section
- Install test dependencies using `pip install -r requirements.testing.txt`
- Install local API module ``pip install -e .``
- Run tests ``pytest -s -v tests/``

Running
-------

Launch the API and documentation ``uvicorn plant_disease_classification_api.main:app``, it will be available at http://127.0.0.1:8000.

License
-------

`MIT License <https://github.com/abdullahselek/plant-disease-classification-api/blob/master/LICENSE>`_
