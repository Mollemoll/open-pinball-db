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

#### Search Machines

| Parameter                | Type | Description                                                         |
|--------------------------|------|---------------------------------------------------------------------|
| q                        | str  | The search query                                                    |
| require_opdb             | bool | Limit results to machines with OPDB ids. Defaults to True           | 
| include_aliases          | bool | Whether to include aliases in the search. Default is True           |
| include_groups           | bool | Whether to include groups in the search. Default is False           |
| include_grouping_entries | bool | Whether to include grouping entries in the search. Default is False |

```python
import opdb
opdb_client = opdb.Client()
opdb_client.search('The Addams Family')
```

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

#### Export Machines and Aliases

Export all machines and aliases into a big json document. According to the OPDB
API docs this endpoint is rate limited to once every hour.

```python
import opdb
opdb_client = opdb.Client(api_key="your_secret_api_key")
opdb_client.export_machines_and_aliases()
```
