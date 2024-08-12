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

## Tools and Techonology used: 
- > React,
- > Djnago,
- > Rest Api,
- > Taildwind css 

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



--------------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx------------------------------




# Little talk on Our Time on Hackathon of IIc

**Theme:** Mental Health and Well-Being of Students
*Precautionary Measures | Preliminary Stage Support | Post-Stage Support*

---

- Hi, I am Rujal aka Luv, the overall Time & Surrounding in Hackathon was filled with vibe of extraordinary for hacking the thon. We as team Incodable had the great time, with all the codes, sarcastic talks, humorous jokes and sweet songs.
  
-  While speaking on time of **cracking the coding**, the Hackathon began from 12:00 AM with the Theme, the idea was needed to be uploaded till 1:00 pm, we were approaching the idea by dealing with ** Unique & Simple ** idea and at last sticked with the project proposal of 'Pariwar' which was simple and very unique among all the players around us.
  
-  Then the next couple of hour we spend on making/ designing the database schema. And after designing we went to the journey of programming.
  
-  **The Hard as Rock time** touched us at the time period of 10:30 PM-- 6:30 AM, we got stuck in one problem to save the particular data from post request, we spent whole time solving the problem. The angel at the time was Mr Abuzer, who was suggesting us to take rest and solve it later but we were in race to drag the solution on the table, as he noted his grounded words I being selfish went to sleep around 1:30 AM then the solution directly crash on my mind, I woke up, took sticky notes of green color and wrote the solution with that stupid pen of IIC, and handed to Mr.Osama. He, was also furious over the time, cause the same thing was just working on his Computer but not on mine, he was indeed crazy on checking the code dissimilarity between his and mine. Then maybe he also thought about taking a nap. As morning begin, I was in washroom the instant God-mode was enabled in me and started to think why the code was not working, And suddenly the angel moment was drawing near to our group, when we sat on computer. We truly made the solution out and it started working to save the data.
  
-  The **Enjoyment Factors** that affected us were,
  > 1) Dialogues : " Dekh Raha Hai Binod?.......", also the " kuch bhi bolunga to bibaad ho jayega ";
  > 2) Spelling Mistake by me : made serious mistake on database Module spellings ;
  > 3) Mr Osama's Sweet and soft Song:  His sweet voice could hurt anyone and also one of us was brutally hurt the most, (Guess on whom);
  > 4) Mr Jeeten's Sarcasm & humorous Jokes: at the specific time;
  > 5) The Long route to Sagarmatha, OOOpps! so sad on us, climbing the stairs from down to very top floor;
  > 6) The 2 stairs down restroom made us to hold for long period ;
  > 7) The Guys in our room were the known fellows to me ;
  
-  **The Movement Of the Presentation**: Wow and Alas goes at the same time, My laptop heart was not fully functioning, but we were situated to present with my laptop. As time passed by, the path way from the situated room to presenting room felt like super ghost-scary walk. The factor of matter like: (laptop malfunction, terrified question raise, stuck in work of Backend server and many more) were eating my mind. I was as nervous as the time of "my first purpose", legs-fingers were getting trembled; the one with tab, one with coat-well dressed, one with neat beard and another business field Judge were firing questions after questions, where Mr. jeeten of our team was alike south indian hero who swallowed the bullet and answered all the questions calmly that was matter of fact.

- The time I somehow managed to survive was, the 1hrs 16 min lecture from one well established CA, talked about (How could we start a Startup in Nepal ?)
  
- **The Result Announcement**: The time frame of room, the AC at max, panel of judge speaking about AI. All the seats were filled with participants, camera man struggling to click perfect moment of pictures. My brain filled with stupid thoughts what if we were not announced, what if they make us to "----" also when are they letting us free. After the panel talk by all the respected person, finally was the time for Certificate distribution, where our team were declared for "Runner Up" title. Opps but not in First position, weaken me a little bit and was not able to think "is it really our team standing in the stage? ". (I followed them late -blame to my imaginary thoughts) and cherished that the Runner Up Award is also not bad, then my mind sets posing that we won "Runner up" position wwwoooowwww!!!!

  
- **The Bye**: So after the announcement, we had a photo session. The last meetup talk with those sweet volunteers, the handsome Judge who gave positive review on our idea, that was a valuable asset.
  





--------------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx------------------------------
