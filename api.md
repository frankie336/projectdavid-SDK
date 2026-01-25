# Projectdavid

Methods:

- <code title="get /">client.<a href="./src/projectdavid/_client.py">retrieve_root</a>() -> object</code>

# Health

Methods:

- <code title="get /v1/health">client.health.<a href="./src/projectdavid/resources/health.py">check</a>(\*\*<a href="src/projectdavid/types/health_check_params.py">params</a>) -> object</code>

# Monitor

Methods:

- <code title="post /v1/monitor">client.monitor.<a href="./src/projectdavid/resources/monitor.py">register_run</a>(\*\*<a href="src/projectdavid/types/monitor_register_run_params.py">params</a>) -> object</code>

# Subscribe

Methods:

- <code title="get /v1/subscribe/{run_id}">client.subscribe.<a href="./src/projectdavid/resources/subscribe.py">retrieve_run_events</a>(run_id, \*\*<a href="src/projectdavid/types/subscribe_retrieve_run_events_params.py">params</a>) -> object</code>

# Completions

Methods:

- <code title="post /v1/completions">client.completions.<a href="./src/projectdavid/resources/completions.py">create</a>(\*\*<a href="src/projectdavid/types/completion_create_params.py">params</a>) -> object</code>

# Threads

Types:

```python
from projectdavid.types import (
    ThreadDetailed,
    ThreadDeleteResponse,
    ThreadGetFormattedMessagesResponse,
    ThreadListMessagesResponse,
    ThreadListUserThreadsResponse,
)
```

Methods:

- <code title="post /v1/threads">client.threads.<a href="./src/projectdavid/resources/threads.py">create</a>(\*\*<a href="src/projectdavid/types/thread_create_params.py">params</a>) -> <a href="./src/projectdavid/types/thread_detailed.py">ThreadDetailed</a></code>
- <code title="get /v1/threads/{thread_id}">client.threads.<a href="./src/projectdavid/resources/threads.py">retrieve</a>(thread_id, \*\*<a href="src/projectdavid/types/thread_retrieve_params.py">params</a>) -> <a href="./src/projectdavid/types/thread_detailed.py">ThreadDetailed</a></code>
- <code title="put /v1/threads/{thread_id}">client.threads.<a href="./src/projectdavid/resources/threads.py">update</a>(thread_id, \*\*<a href="src/projectdavid/types/thread_update_params.py">params</a>) -> <a href="./src/projectdavid/types/thread_detailed.py">ThreadDetailed</a></code>
- <code title="delete /v1/threads/{thread_id}">client.threads.<a href="./src/projectdavid/resources/threads.py">delete</a>(thread_id, \*\*<a href="src/projectdavid/types/thread_delete_params.py">params</a>) -> <a href="./src/projectdavid/types/thread_delete_response.py">ThreadDeleteResponse</a></code>
- <code title="get /v1/threads/{thread_id}/formatted_messages">client.threads.<a href="./src/projectdavid/resources/threads.py">get_formatted_messages</a>(thread_id, \*\*<a href="src/projectdavid/types/thread_get_formatted_messages_params.py">params</a>) -> <a href="./src/projectdavid/types/thread_get_formatted_messages_response.py">ThreadGetFormattedMessagesResponse</a></code>
- <code title="get /v1/threads/{thread_id}/messages">client.threads.<a href="./src/projectdavid/resources/threads.py">list_messages</a>(thread_id, \*\*<a href="src/projectdavid/types/thread_list_messages_params.py">params</a>) -> <a href="./src/projectdavid/types/thread_list_messages_response.py">ThreadListMessagesResponse</a></code>
- <code title="get /v1/threads/{thread_id}/runs">client.threads.<a href="./src/projectdavid/resources/threads.py">list_runs</a>(thread_id, \*\*<a href="src/projectdavid/types/thread_list_runs_params.py">params</a>) -> <a href="./src/projectdavid/types/run_list.py">RunList</a></code>
- <code title="get /v1/threads/user/{user_id}">client.threads.<a href="./src/projectdavid/resources/threads.py">list_user_threads</a>(user_id, \*\*<a href="src/projectdavid/types/thread_list_user_threads_params.py">params</a>) -> <a href="./src/projectdavid/types/thread_list_user_threads_response.py">ThreadListUserThreadsResponse</a></code>
- <code title="put /v1/threads/{thread_id}/metadata">client.threads.<a href="./src/projectdavid/resources/threads.py">update_metadata</a>(thread_id, \*\*<a href="src/projectdavid/types/thread_update_metadata_params.py">params</a>) -> <a href="./src/projectdavid/types/thread_detailed.py">ThreadDetailed</a></code>

# Users

Types:

```python
from projectdavid.types import UserRead
```

Methods:

- <code title="post /v1/users">client.users.<a href="./src/projectdavid/resources/users/users.py">create</a>(\*\*<a href="src/projectdavid/types/user_create_params.py">params</a>) -> <a href="./src/projectdavid/types/user_read.py">UserRead</a></code>
- <code title="get /v1/users/{user_id}">client.users.<a href="./src/projectdavid/resources/users/users.py">retrieve</a>(user_id, \*\*<a href="src/projectdavid/types/user_retrieve_params.py">params</a>) -> <a href="./src/projectdavid/types/user_read.py">UserRead</a></code>
- <code title="put /v1/users/{user_id}">client.users.<a href="./src/projectdavid/resources/users/users.py">update</a>(user_id, \*\*<a href="src/projectdavid/types/user_update_params.py">params</a>) -> <a href="./src/projectdavid/types/user_read.py">UserRead</a></code>
- <code title="delete /v1/users/{user_id}">client.users.<a href="./src/projectdavid/resources/users/users.py">delete</a>(user_id, \*\*<a href="src/projectdavid/types/user_delete_params.py">params</a>) -> None</code>

## Assistants

Methods:

- <code title="post /v1/users/{user_id}/assistants/{assistant_id}">client.users.assistants.<a href="./src/projectdavid/resources/users/assistants.py">associate</a>(assistant_id, \*, user_id, \*\*<a href="src/projectdavid/types/users/assistant_associate_params.py">params</a>) -> object</code>
- <code title="delete /v1/users/{user_id}/assistants/{assistant_id}">client.users.assistants.<a href="./src/projectdavid/resources/users/assistants.py">disassociate</a>(assistant_id, \*, user_id, \*\*<a href="src/projectdavid/types/users/assistant_disassociate_params.py">params</a>) -> None</code>

## Apikeys

Types:

```python
from projectdavid.types.users import (
    APIKeyCreate,
    APIKeyCreateResponse,
    APIKeyDetails,
    ApikeyListResponse,
)
```

Methods:

- <code title="post /v1/users/{user_id}/apikeys">client.users.apikeys.<a href="./src/projectdavid/resources/users/apikeys.py">create</a>(user_id, \*\*<a href="src/projectdavid/types/users/apikey_create_params.py">params</a>) -> <a href="./src/projectdavid/types/users/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /v1/users/{user_id}/apikeys/{key_prefix}">client.users.apikeys.<a href="./src/projectdavid/resources/users/apikeys.py">retrieve</a>(key_prefix, \*, user_id, \*\*<a href="src/projectdavid/types/users/apikey_retrieve_params.py">params</a>) -> <a href="./src/projectdavid/types/users/api_key_details.py">APIKeyDetails</a></code>
- <code title="get /v1/users/{user_id}/apikeys">client.users.apikeys.<a href="./src/projectdavid/resources/users/apikeys.py">list</a>(user_id, \*\*<a href="src/projectdavid/types/users/apikey_list_params.py">params</a>) -> <a href="./src/projectdavid/types/users/apikey_list_response.py">ApikeyListResponse</a></code>
- <code title="delete /v1/users/{user_id}/apikeys/{key_prefix}">client.users.apikeys.<a href="./src/projectdavid/resources/users/apikeys.py">revoke</a>(key_prefix, \*, user_id, \*\*<a href="src/projectdavid/types/users/apikey_revoke_params.py">params</a>) -> None</code>

# Runs

Types:

```python
from projectdavid.types import (
    Run,
    RunList,
    RunStatus,
    Tool,
    ToolFunction,
    TruncationStrategy,
    RunRetrieveResponse,
)
```

Methods:

- <code title="post /v1/runs">client.runs.<a href="./src/projectdavid/resources/runs/runs.py">create</a>(\*\*<a href="src/projectdavid/types/run_create_params.py">params</a>) -> <a href="./src/projectdavid/types/run.py">Run</a></code>
- <code title="get /v1/runs/{run_id}">client.runs.<a href="./src/projectdavid/resources/runs/runs.py">retrieve</a>(run_id, \*\*<a href="src/projectdavid/types/run_retrieve_params.py">params</a>) -> <a href="./src/projectdavid/types/run_retrieve_response.py">RunRetrieveResponse</a></code>
- <code title="get /v1/runs">client.runs.<a href="./src/projectdavid/resources/runs/runs.py">list</a>(\*\*<a href="src/projectdavid/types/run_list_params.py">params</a>) -> <a href="./src/projectdavid/types/run_list.py">RunList</a></code>
- <code title="post /v1/runs/{run_id}/cancel">client.runs.<a href="./src/projectdavid/resources/runs/runs.py">cancel</a>(run_id, \*\*<a href="src/projectdavid/types/run_cancel_params.py">params</a>) -> <a href="./src/projectdavid/types/run.py">Run</a></code>
- <code title="get /v1/runs/{run_id}/events">client.runs.<a href="./src/projectdavid/resources/runs/runs.py">stream_events</a>(run_id, \*\*<a href="src/projectdavid/types/run_stream_events_params.py">params</a>) -> None</code>
- <code title="put /v1/runs/{run_id}/metadata">client.runs.<a href="./src/projectdavid/resources/runs/runs.py">update_metadata</a>(run_id, \*\*<a href="src/projectdavid/types/run_update_metadata_params.py">params</a>) -> <a href="./src/projectdavid/types/run.py">Run</a></code>
- <code title="put /v1/runs/{run_id}/status">client.runs.<a href="./src/projectdavid/resources/runs/runs.py">update_status</a>(run_id, \*\*<a href="src/projectdavid/types/run_update_status_params.py">params</a>) -> <a href="./src/projectdavid/types/run.py">Run</a></code>

## Actions

Types:

```python
from projectdavid.types.runs import ActionGetByStatusResponse
```

Methods:

- <code title="get /v1/runs/{run_id}/actions/status">client.runs.actions.<a href="./src/projectdavid/resources/runs/actions.py">get_by_status</a>(run_id, \*\*<a href="src/projectdavid/types/runs/action_get_by_status_params.py">params</a>) -> <a href="./src/projectdavid/types/runs/action_get_by_status_response.py">ActionGetByStatusResponse</a></code>

# Assistants

Types:

```python
from projectdavid.types import AssistantRead, AssistantListResponse
```

Methods:

- <code title="post /v1/assistants">client.assistants.<a href="./src/projectdavid/resources/assistants/assistants.py">create</a>(\*\*<a href="src/projectdavid/types/assistant_create_params.py">params</a>) -> <a href="./src/projectdavid/types/assistant_read.py">AssistantRead</a></code>
- <code title="get /v1/assistants/{assistant_id}">client.assistants.<a href="./src/projectdavid/resources/assistants/assistants.py">retrieve</a>(assistant_id, \*\*<a href="src/projectdavid/types/assistant_retrieve_params.py">params</a>) -> <a href="./src/projectdavid/types/assistant_read.py">AssistantRead</a></code>
- <code title="put /v1/assistants/{assistant_id}">client.assistants.<a href="./src/projectdavid/resources/assistants/assistants.py">update</a>(assistant_id, \*\*<a href="src/projectdavid/types/assistant_update_params.py">params</a>) -> <a href="./src/projectdavid/types/assistant_read.py">AssistantRead</a></code>
- <code title="get /v1/assistants">client.assistants.<a href="./src/projectdavid/resources/assistants/assistants.py">list</a>(\*\*<a href="src/projectdavid/types/assistant_list_params.py">params</a>) -> <a href="./src/projectdavid/types/assistant_list_response.py">AssistantListResponse</a></code>

## VectorStores

Types:

```python
from projectdavid.types.assistants import (
    VectorStoreListResponse,
    VectorStoreAttachResponse,
    VectorStoreDetachResponse,
)
```

Methods:

- <code title="get /v1/assistants/{assistant_id}/vector-stores">client.assistants.vector_stores.<a href="./src/projectdavid/resources/assistants/vector_stores.py">list</a>(assistant_id, \*\*<a href="src/projectdavid/types/assistants/vector_store_list_params.py">params</a>) -> <a href="./src/projectdavid/types/assistants/vector_store_list_response.py">VectorStoreListResponse</a></code>
- <code title="post /v1/assistants/{assistant_id}/vector-stores/{vector_store_id}/attach">client.assistants.vector_stores.<a href="./src/projectdavid/resources/assistants/vector_stores.py">attach</a>(vector_store_id, \*, assistant_id, \*\*<a href="src/projectdavid/types/assistants/vector_store_attach_params.py">params</a>) -> <a href="./src/projectdavid/types/assistants/vector_store_attach_response.py">VectorStoreAttachResponse</a></code>
- <code title="delete /v1/assistants/{assistant_id}/vector-stores/{vector_store_id}/detach">client.assistants.vector_stores.<a href="./src/projectdavid/resources/assistants/vector_stores.py">detach</a>(vector_store_id, \*, assistant_id, \*\*<a href="src/projectdavid/types/assistants/vector_store_detach_params.py">params</a>) -> <a href="./src/projectdavid/types/assistants/vector_store_detach_response.py">VectorStoreDetachResponse</a></code>

# Messages

Types:

```python
from projectdavid.types import MessageCreate, MessageRead, MessageDeleteResponse
```

Methods:

- <code title="post /v1/messages">client.messages.<a href="./src/projectdavid/resources/messages.py">create</a>(\*\*<a href="src/projectdavid/types/message_create_params.py">params</a>) -> <a href="./src/projectdavid/types/message_read.py">MessageRead</a></code>
- <code title="get /v1/messages/{message_id}">client.messages.<a href="./src/projectdavid/resources/messages.py">retrieve</a>(message_id, \*\*<a href="src/projectdavid/types/message_retrieve_params.py">params</a>) -> <a href="./src/projectdavid/types/message_read.py">MessageRead</a></code>
- <code title="delete /v1/messages/{message_id}">client.messages.<a href="./src/projectdavid/resources/messages.py">delete</a>(message_id, \*\*<a href="src/projectdavid/types/message_delete_params.py">params</a>) -> <a href="./src/projectdavid/types/message_delete_response.py">MessageDeleteResponse</a></code>
- <code title="post /v1/messages/assistant">client.messages.<a href="./src/projectdavid/resources/messages.py">save_assistant_message</a>(\*\*<a href="src/projectdavid/types/message_save_assistant_message_params.py">params</a>) -> <a href="./src/projectdavid/types/message_read.py">MessageRead</a></code>
- <code title="post /v1/messages/tools">client.messages.<a href="./src/projectdavid/resources/messages.py">submit_tool_response</a>(\*\*<a href="src/projectdavid/types/message_submit_tool_response_params.py">params</a>) -> <a href="./src/projectdavid/types/message_read.py">MessageRead</a></code>

# Actions

Types:

```python
from projectdavid.types import ActionRead, ActionListPendingResponse
```

Methods:

- <code title="post /v1/actions">client.actions.<a href="./src/projectdavid/resources/actions.py">create</a>(\*\*<a href="src/projectdavid/types/action_create_params.py">params</a>) -> <a href="./src/projectdavid/types/action_read.py">ActionRead</a></code>
- <code title="get /v1/actions/{action_id}">client.actions.<a href="./src/projectdavid/resources/actions.py">retrieve</a>(action_id, \*\*<a href="src/projectdavid/types/action_retrieve_params.py">params</a>) -> <a href="./src/projectdavid/types/action_read.py">ActionRead</a></code>
- <code title="put /v1/actions/{action_id}">client.actions.<a href="./src/projectdavid/resources/actions.py">update</a>(action_id, \*\*<a href="src/projectdavid/types/action_update_params.py">params</a>) -> <a href="./src/projectdavid/types/action_read.py">ActionRead</a></code>
- <code title="delete /v1/actions/{action_id}">client.actions.<a href="./src/projectdavid/resources/actions.py">delete</a>(action_id, \*\*<a href="src/projectdavid/types/action_delete_params.py">params</a>) -> None</code>
- <code title="get /v1/actions/pending/{run_id}">client.actions.<a href="./src/projectdavid/resources/actions.py">list_pending</a>(run_id, \*\*<a href="src/projectdavid/types/action_list_pending_params.py">params</a>) -> <a href="./src/projectdavid/types/action_list_pending_response.py">ActionListPendingResponse</a></code>

# Uploads

Types:

```python
from projectdavid.types import File
```

Methods:

- <code title="post /v1/uploads">client.uploads.<a href="./src/projectdavid/resources/uploads.py">create</a>(\*\*<a href="src/projectdavid/types/upload_create_params.py">params</a>) -> <a href="./src/projectdavid/types/file.py">File</a></code>

# Files

Types:

```python
from projectdavid.types import FileDeleteResponse
```

Methods:

- <code title="get /v1/files/{file_id}">client.files.<a href="./src/projectdavid/resources/files.py">retrieve</a>(file_id, \*\*<a href="src/projectdavid/types/file_retrieve_params.py">params</a>) -> <a href="./src/projectdavid/types/file.py">File</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/projectdavid/resources/files.py">delete</a>(file_id, \*\*<a href="src/projectdavid/types/file_delete_params.py">params</a>) -> <a href="./src/projectdavid/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /v1/files/{file_id}/signed-url">client.files.<a href="./src/projectdavid/resources/files.py">generate_signed_url</a>(file_id, \*\*<a href="src/projectdavid/types/file_generate_signed_url_params.py">params</a>) -> object</code>
- <code title="get /v1/files/{file_id}/base64">client.files.<a href="./src/projectdavid/resources/files.py">get_base64</a>(file_id, \*\*<a href="src/projectdavid/types/file_get_base64_params.py">params</a>) -> object</code>

# VectorStores

Types:

```python
from projectdavid.types import StatusEnum, VectorStore, VectorStoreListResponse
```

Methods:

- <code title="post /v1/vector-stores">client.vector_stores.<a href="./src/projectdavid/resources/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/projectdavid/types/vector_store_create_params.py">params</a>) -> <a href="./src/projectdavid/types/vector_store.py">VectorStore</a></code>
- <code title="get /v1/vector-stores/{vector_store_id}">client.vector_stores.<a href="./src/projectdavid/resources/vector_stores/vector_stores.py">retrieve</a>(vector_store_id, \*\*<a href="src/projectdavid/types/vector_store_retrieve_params.py">params</a>) -> <a href="./src/projectdavid/types/vector_store.py">VectorStore</a></code>
- <code title="get /v1/vector-stores">client.vector_stores.<a href="./src/projectdavid/resources/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/projectdavid/types/vector_store_list_params.py">params</a>) -> <a href="./src/projectdavid/types/vector_store_list_response.py">VectorStoreListResponse</a></code>
- <code title="delete /v1/vector-stores/{vector_store_id}">client.vector_stores.<a href="./src/projectdavid/resources/vector_stores/vector_stores.py">delete</a>(vector_store_id, \*\*<a href="src/projectdavid/types/vector_store_delete_params.py">params</a>) -> None</code>

## Admin

Types:

```python
from projectdavid.types.vector_stores import AdminListByUserResponse
```

Methods:

- <code title="get /v1/vector-stores/admin/by-user">client.vector_stores.admin.<a href="./src/projectdavid/resources/vector_stores/admin.py">list_by_user</a>(\*\*<a href="src/projectdavid/types/vector_stores/admin_list_by_user_params.py">params</a>) -> <a href="./src/projectdavid/types/vector_stores/admin_list_by_user_response.py">AdminListByUserResponse</a></code>

## Files

Types:

```python
from projectdavid.types.vector_stores import VectorStoreFile, FileListResponse
```

Methods:

- <code title="get /v1/vector-stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/projectdavid/resources/vector_stores/files.py">list</a>(vector_store_id, \*\*<a href="src/projectdavid/types/vector_stores/file_list_params.py">params</a>) -> <a href="./src/projectdavid/types/vector_stores/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/vector-stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/projectdavid/resources/vector_stores/files.py">delete</a>(vector_store_id, \*\*<a href="src/projectdavid/types/vector_stores/file_delete_params.py">params</a>) -> None</code>
- <code title="post /v1/vector-stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/projectdavid/resources/vector_stores/files.py">add</a>(vector_store_id, \*\*<a href="src/projectdavid/types/vector_stores/file_add_params.py">params</a>) -> <a href="./src/projectdavid/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="patch /v1/vector-stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/projectdavid/resources/vector_stores/files.py">update_status</a>(file_id, \*, vector_store_id, \*\*<a href="src/projectdavid/types/vector_stores/file_update_status_params.py">params</a>) -> <a href="./src/projectdavid/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>

## Lookup

Methods:

- <code title="get /v1/vector-stores/lookup/collection">client.vector_stores.lookup.<a href="./src/projectdavid/resources/vector_stores/lookup.py">by_collection_name</a>(\*\*<a href="src/projectdavid/types/vector_stores/lookup_by_collection_name_params.py">params</a>) -> <a href="./src/projectdavid/types/vector_store.py">VectorStore</a></code>

# Admin

## Users

Methods:

- <code title="post /v1/admin/users/{target_user_id}/keys">client.admin.users.<a href="./src/projectdavid/resources/admin/users.py">create_api_key</a>(target_user_id, \*\*<a href="src/projectdavid/types/admin/user_create_api_key_params.py">params</a>) -> <a href="./src/projectdavid/types/users/api_key_create_response.py">APIKeyCreateResponse</a></code>
