## Python Open Pinball Database Client

This is a Python client for the Open Pinball Database API.

### Installation

To come...

### Usage

#### Get changelog
    
```python
import opdb
opdb_client = opdb.Client()
opdb_client.get_changelog()
```

#### Typeahead search

| Parameter | Type | Description |
|---|---|---|
|query|str|The search query|
|include_aliases|bool|Whether to include aliases in the search. Default is True.|
|include_groups|bool|Whether to include groups in the search. Default is False.|

```python
import opdb
opdb_client = opdb.Client()
opdb_client.typeahead_search('The Addams Family')
```
