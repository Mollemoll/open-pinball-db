## Python Open Pinball Database Client

This is a Python client for the Open Pinball Database API.

### Installation

To come...

## Usage

### Public API (no authentication required)

#### Get changelog
    
```python
import opdb
opdb_client = opdb.Client()
opdb_client.get_changelog()
```

#### Typeahead search

| Parameter       | Type | Description                                               |
|-----------------|------|-----------------------------------------------------------|
| q               | str  | The search query                                          |
| include_aliases | bool | Whether to include aliases in the search. Default is True |
| include_groups  | bool | Whether to include groups in the search. Default is False |

```python
import opdb
opdb_client = opdb.Client()
opdb_client.typeahead_search('The Addams Family')
```

### Private API (authentication required)

Get your free api key at [Open Pinball Database](https://opdb.org/).

#### Get Machine By OPDB ID

| Parameter | Type | Description                |
|-----------|------|----------------------------|
| opdb_id   | str  | The IPDB ID of the machine |

```python
import opdb
opdb_client = opdb.Client(api_key="your_secret_api_key")
opdb_client.get_machine("OPDB-ID")
```

#### Get Machine By IPDB ID

| Parameter | Type | Description                |
|-----------|------|----------------------------|
| ipdb_id   | int  | The IPDB ID of the machine |

```python
import opdb
opdb_client = opdb.Client(api_key="your_secret_api_key")
opdb_client.get_machine_by_ipdb_id(1234)
```
