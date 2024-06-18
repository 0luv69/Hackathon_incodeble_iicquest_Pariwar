# Pariwar Web Application Documentation

## Overview
Pariwar is a web application designed to facilitate communication and support within families and extended family networks. It provides a platform where individuals, especially students who may find it challenging to communicate directly with their parents, can seek advice and support from other family members or individuals playing familial roles.

## Key Features
- **User Roles:** Users can sign up and identify themselves with roles such as father, son, mother, grandfather, grandmother, or brother, facilitating targeted communication.
- **Issue Posting:** Users can post their concerns anonymously or publicly, seeking suggestions from other users who match specific familial roles or relationships.
- **Feedback and Suggestions:** Family members and other users can provide suggestions and feedback on posted issues, fostering a supportive environment.
- **Relationship Building:** Users can establish relationships with other members based on received suggestions, enabling further communication through private messaging.

## Personnel Involved
**Front End Developers:**
- Jeeten Mandal
- Mohammad Abuzer Khan

**Back End Developers:**
- Rujal Baniya
- Md Oshma

## User Guide / Frequently Asked Questions

### How do I sign up?
1. Click on the "Log In" button in the upper right corner.
2. Enter your username, email, age, select your character (father, son, mother, grandfather, grandmother, or brother), and set your password.
3. Submit the form and check your email for the OTP (One-Time Password).
4. Enter the OTP to confirm and be redirected to the home page.

### What appears on my feed?
Your feed will display issues and suggestions from users who match your selected familial role or relationship.

### How do I post issues and view them?
1. Enter your issue's title, description, and specify the preferred character for suggestions.
2. Submit your issue. You will receive a confirmation notification.
3. To view your posted issues, click on the "My Issues" button in the navigation bar.

### How can I provide suggestions?
Navigate to the feed section on the home page, find relevant posts based on your character, and click the "Reply" button to provide suggestions.

### How do I send messages to someone who suggested something?
Go to the "Relations" tab in the navbar and select the specific character you wish to communicate with.

### How do I communicate with suggested individuals and build relations?
Click on the "Suggested" link to view messages from characters you are interested in. Click the "Relate" button to establish a relationship and start sharing your issues.

## Conclusion
Pariwar aims to bridge communication gaps within families by leveraging a structured platform where users can seek and provide support, anonymously if desired, across a wide range of familial relationships. It promotes empathy, understanding, and constructive dialogue among its users.




--------------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx------------------------------
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
