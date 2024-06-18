









------------------------------------------------------------------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----------------------------------------------------------------------------
# API Documentation

## Accounts API

### 1. Login API
- **Endpoint:** `/api/login/`
- **Method:** `POST`

#### **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

#### **Response:**
  ```json
{
  "posted": true,
  "user_id": integer,
  "user_name": "string",
  "access": "string",
  "refresh": "string"
}
```

### 2. Register API
- **Endpoint:** `/api/register/`
- **Method:** `POST`

#### **Request Body:**
  ```json
{
  "username": "string",
  "email": "string",
  "password": "string",
  "age": integer,
  "character": "string"
}
```

#### **Response:**
  ```json
{
  "posted": true,
  "id": integer
}
```

## Profile API

### 1. Get Profile API

- **Endpoint:** `/api/get_profile/`
- **Method:** `POST`

#### **Request Body:** `User id `
  ```json
{
  "id": integer
}
```

#### **Response:**
  ```json
{
  "success": true,
  "data": {
    "id": integer,
    "username": "string",
    "email": "string",
    "is_verified": boolean,
    "age": integer,
    "character": "string"
  }
}
```

## Issue Segment

### 1. Post Issue API

- **Endpoint:** `/api/post_issue/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "id": integer,
  "title": "string",
  "description": "string",
  "preferred_char": "string"
}
```

#### **Response:**
  
  ```json
{
  "posted": true,
  "payload": {
    "id": integer,
    "title": "string",
    "description": "string",
    "preferred_char": "string"
  }
}
```

### 2. Get All Issues API

- **Endpoint:** `/api/get_all_issues/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "id": integer
}
```

#### **Response:**
  
  ```json
{
  "success": true,
  "payload": [
    {
      "id": integer,
      "title": "string",
      "description": "string",
      "preferred_char": "string"
    },
    {
      "id": integer,
      "title": "string",
      "description": "string",
      "preferred_char": "string"
    },
    ...
  ]
}
```

### 3. Get Issues by Character API

- **Endpoint:** `/api/get_issue_character/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "id": integer
}
```

#### **Response:**
  
  ```json
{
  "success": true,
  "payload": [
    {
      "id": integer,
      "title": "string",
      "description": "string",
      "preferred_char": "string"
    },
    {
      "id": integer,
      "title": "string",
      "description": "string",
      "preferred_char": "string"
    },
    ...
  ]
}
```

### 4. Get Issues by User API

- **Endpoint:** `/api/get_issue_by_user/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "id": integer
}
```

#### **Response:**
  
  ```json
{
  "success": true,
  "payload": [
    {
      "id": integer,
      "title": "string",
      "description": "string",
      "preferred_char": "string"
    },
    {
      "id": integer,
      "title": "string",
      "description": "string",
      "preferred_char": "string"
    },
    ...
  ]
}
```

### 5. Get Specific Issue API

- **Endpoint:** `/api/get_specific_issue/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "issue_id": integer
}
```

#### **Response:**
  
  ```json
{
  "success": true,
  "payload": {
    "id": integer,
    "title": "string",
    "description": "string",
    "preferred_char": "string"
  }
}
```

## Reply / Suggestion Segment

### 1. Post Reply API

- **Endpoint:** `/api/post_reply/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "issued_id": integer,
  "reply_user_id": integer,
  "message": "string"
}
```

#### **Response:**
  
  ```json
{
  "posted": true,
  "payload": {
    "id": integer,
    "message": "string",
    "created_at": "datetime",
    "updated": "datetime",
    "replied_by": {
      "id": integer,
      "username": "string"
    },
    "issued_by": integer
  }
}
```

### 2. Get Issue Replies API

- **Endpoint:** `/api/get_issue_reply/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "id": integer
}
```

#### **Response:**
  
  ```json
{
  "success": true,
  "payload": [
    {
      "id": integer,
      "message": "string",
      "created_at": "datetime",
      "updated": "datetime",
      "replied_by": {
        "id": integer,
        "username": "string"
      },
      "issued_by": integer
    },
    {
      "id": integer,
      "message": "string",
      "created_at": "datetime",
      "updated": "datetime",
      "replied_by": {
        "id": integer,
        "username": "string"
      },
      "issued_by": integer
    },
    ...
  ]
}
```

### 3. Get All Replies API

- **Endpoint:** `/api/get_reply_list/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "issued_id": integer
}
```

#### **Response:**
  
  ```json
{
  "success": true,
  "payload": [
    {
      "id": integer,
      "message": "string",
      "created_at": "datetime",
      "updated": "datetime",
      "replied_by": {
        "id": integer,
        "username": "string"
      },
      "issued_by": integer
    },
    {
      "id": integer,
      "message": "string",
      "created_at": "datetime",
      "updated": "datetime",
      "replied_by": {
        "id": integer,
        "username": "string"
      },
      "issued_by": integer
    },
    ...
  ]
}
```

## Relation Segment

### 1. Update Relation API

- **Endpoint:** `/api/relation_update/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "suggested_by": integer,
  "issued_by": integer
}
```

#### **Response:**
  
  ```json
{
  "posted": true,
  "payload": {
    "id": integer,
    "suggested_by": integer,
    "issued_by": integer,
    "relation_name": "string"
  }
}
```

### 2. Get User Relations API

- **Endpoint:** `/api/get_particular_relation/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "id": integer
}
```

#### **Response:**
  
  ```json
{
  "posted": true,
  "payload": [
    {
      "id": integer,
      "suggested_by": {
        "id": integer,
        "username": "string"
      },
      "issued_by": {
        "id": integer,
        "username": "string"
      },
      "relation_name": "string"
    },
    {
      "id": integer,
      "suggested_by": {
        "id": integer,
        "username": "string"
      },
      "issued_by": {
        "id": integer,
        "username": "string"
      },
      "relation_name": "string"
    },
    ...
  ]
}
```

## Chat API

### Get Chat by Relation ID

- **Endpoint:** `/api/chat/get/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "relation_id": integer
}
```

#### **Response (Success):**
  
  ```json
{
  "success": true,
  "payload": [
    {
      "username": "string",
      "sender": {
        "id": integer,
        "username": "string"
      },
      "message": "string",
      "relation": integer,
      "date": "datetime"
    },
    ...
  ]
}
```

#### **Response (Failure):**
  
  ```json
{
  "success": false,
  "message": "string"
}
```

### Post Chat

- **Endpoint:** `/api/chat/post/`
- **Method:** `POST`

#### **Request Body:**
  
  ```json
{
  "sender_id": integer,
  "message": "string",
  "relation_id": integer
}
```

#### **Response (Success):**
  
  ```json
{
  "success": true
}
```

#### **Response (Failure):**
  
  ```json
{
  "success": false,
  "message": "string"
}
```
