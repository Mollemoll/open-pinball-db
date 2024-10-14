## Python Open Pinball Database Client

This is a Python client for the Open Pinball Database API.

### Installation

```bash
pip install open-pinball-db
```

```python
import open_pinball_db
opdb_client = open_pinball_db.Client()

# Start using the client
```

## Usage

### Public API (no authentication required)

#### Get changelog
    
```python
import open_pinball_db
opdb_client = open_pinball_db.Client()
opdb_client.get_changelog()
```

#### Typeahead search

| Parameter       | Type | Description                                               |
|-----------------|------|-----------------------------------------------------------|
| q               | str  | The search query                                          |
| include_aliases | bool | Whether to include aliases in the search. Default is True |
| include_groups  | bool | Whether to include groups in the search. Default is False |

```python
import open_pinball_db
opdb_client = open_pinball_db.Client()
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
import open_pinball_db
opdb_client = open_pinball_db.Client(api_key="your_secret_api_key")
opdb_client.search('The Addams Family')
```

#### Get Machine By OPDB ID

| Parameter | Type | Description                |
|-----------|------|----------------------------|
| opdb_id   | str  | The IPDB ID of the machine |

```python
import open_pinball_db
opdb_client = open_pinball_db.Client(api_key="your_secret_api_key")
opdb_client.get_machine("OPDB-ID")
```

#### Get Machine By IPDB ID

| Parameter | Type | Description                |
|-----------|------|----------------------------|
| ipdb_id   | int  | The IPDB ID of the machine |

```python
import open_pinball_db
opdb_client = open_pinball_db.Client(api_key="your_secret_api_key")
opdb_client.get_machine_by_ipdb_id(1234)
```

#### Export Machines and Aliases

Export all machines and aliases into a big json document. According to the OPDB
API docs this endpoint is rate limited to once every hour.

```python
import open_pinball_db
opdb_client = open_pinball_db.Client(api_key="your_secret_api_key")
opdb_client.export_machines_and_aliases()
```

#### Export Machines Groups

Export all machine groups as a single JSON document.

```python
import open_pinball_db
opdb_client = open_pinball_db.Client(api_key="your_secret_api_key")
opdb_client.export_machine_groups()
```

### Handling Exceptions

The client can raise the following exceptions:

| Exception         | Description                                                                   |
|-------------------|-------------------------------------------------------------------------------|
| OpdbError         | Base exception class for all exceptions                                       |
| OpdbMissingApiKey | Raised when trying to access private parts of the OPDB API without an API key |
| OpdbHttpError     | Raised upon http errors. Contains status code and message.                    |
| OpdbTimeoutError  | Raised upon timeout errors.                                                   |
