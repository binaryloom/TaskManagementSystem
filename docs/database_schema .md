# Database Schema

The database schema of the Task Management System consists of the following tables:

- **BaseModel (Abstract)**: The abstract base class model for other database tables, providing common fields such as status, created_at, updated_at, created_by, and updated_by.
- **User**: Represents user information including username, email, and mobile number.
- **Board**: Stores information about boards, which are containers for lists of tasks.
- **List**: Represents lists of tasks within boards.
- **Task**: Contains information about individual tasks including title, description, assigned list, assigned users, and due date.

```mermaid
erDiagram
    BaseModel ||--o{ Board : operates
    BaseModel ||--o{ List : operates
    BaseModel ||--o{ Task : operates
    User ||--o{ Board : owns
    Board ||--o{ List : contains
    List ||--o{ Task : contains
    Task {
        string title
        text description
        date due_date
    }
    User {
        string username
        string email
        string mobile_no
    }
    Board {
        string name
    }
    List {
        string name
    }
    BaseModel {
        bool status
        datetime created_at
        datetime updated_at
        User created_by
        User updated_by
    }
```
