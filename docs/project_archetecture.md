# Project Architecture

The Task Management System follows a typical client-server architecture, with a frontend application communicating with a backend API server. Here's an overview of the architecture:

## Backend Architecture

```mermaid
graph TD;
    django_frontend["Django Frontend"] --> views["Views and Serializers"];
    api_server["Django REST Framework (DRF)"] --> views;
    django_admin["Django Admin Panel"] --> views;
    views --> orm_layer["Models"];
    orm_layer --> F["Database"];

```

- **Django Frontend**: The frontend is built using Django, a high-level Python web framework that facilitates rapid development and clean, pragmatic design.
- **Django REST Framework (DRF)**: DRF is used to build the RESTful API endpoints that handle communication between the frontend and backend.
- **Django Admin Panel**: A customized Django admin panel is developed to provide administrative access for managing users, boards, lists, tasks, and other application entities.
- **Database**: Django ORM is utilized to interact with the underlying relational database. PostgreSQL is the preferred choice for its robustness and scalability, but other databases supported by Django can also be used.
- **Models**: The backend consists of Django models that define the structure of the database schema. These models include User, Board, List, and Task, as outlined in the Database Schema section.
- **Views and Serializers**: Views are implemented using Django views or viewsets, while serializers handle the conversion of Django model instances to JSON format for API responses.

## Frontend Architecture

- **Vue.js Frontend (Future)**: There are plans to migrate to a Vue.js-based frontend in the future for improved interactivity and user experience. This frontend will be built using Vue.js components, pinia for state management, and Vue Router for client-side routing.
- **Components**: Frontend components are organized using Django templates for the Django frontend and Vue.js components for the Vue.js frontend. Each component is responsible for rendering a specific part of the user interface.
- **State Management**: Vuex is used for state management in the Vue.js frontend, while Django templates handle state management in the Django frontend.

## Communication

```mermaid
graph LR;
    frontend[Frontend] --> backend[RESTful API Endpoints];
    backend --> frontend;
```

- **RESTful API**: Both frontend applications communicate with the backend through RESTful API endpoints provided by Django REST Framework. These endpoints handle CRUD (Create, Read, Update, Delete) operations for tasks, boards, lists, and users.
- **HTTP Protocol**: Communication between the frontend and backend occurs over HTTP protocol, with JSON payloads exchanged between client and server.

## Deployment Architecture

```mermaid
graph TD;
    new_feature["New Feature"] --> feature_request{Feature Request};
    feature_request --> |denied| new_feature;
    feature_request --> |approved| main_checkout["Checkout from Main Branch"];
    main_checkout --> |development| dev_commit[Development Commit];
    dev_commit --> |deploy test| test_env{Test Environment};
    test_env --> |failed| dev_commit;
    test_env --> |passed| pull_request["Pull request To Main"];
    pull_request --> image_deploy["Deploy Image in GHCR"];
    pull_request --> image_docs["Deploy docs in gh_pages"];
```

The deployment architecture of the Task Management System follows a streamlined process to deploy new features and updates. Here's an overview:

- **New Feature**: Represents the implementation of a new feature in the application.
- **Feature Request**: Indicates the process of submitting a feature request, which may be either approved or denied.
- **Checkout from Main Branch**: Upon approval of a feature request, the codebase is checked out from the main branch for further development.
- **Development Commit**: Commits are made to the development branch to implement the approved feature.
- **Test Environment**: A test environment is deployed for testing the newly developed feature.
- **Pull Request to Main**: After testing, a pull request is initiated to merge the feature into the main branch.
- **Deploy Image in GHCR**: Upon merging into the main branch, the Docker image is deployed to the GitHub Container Registry (GHCR).
- **Deploy docs in gh_pages**: Documentation updates are deployed to the gh_pages branch for publishing.

This process ensures a systematic approach to deploying changes while maintaining code quality and consistency.

## Scalability Considerations

- **Horizontal Scaling**: The architecture is designed to support horizontal scaling by deploying multiple instances of the backend API server behind a load balancer to distribute incoming traffic.
- **Database Sharding**: As the application grows, database sharding techniques can be employed to distribute database load across multiple database servers.

## High-Level Overview

The Task Management System architecture consists of a Django backend providing RESTful API endpoints, a Django frontend for server-rendered UI, a Vue.js frontend for interactive UI (future), and communication between them through HTTP protocol. The application also includes a customized Django admin panel for administrative tasks. Docker containers, GitHub Container Registry, and CI/CD pipelines are used for deployment and automation.

This architecture ensures modularity, scalability, and maintainability, making it well-suited for both small-scale deployments and future growth.
