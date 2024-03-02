# Software Requirements Specification (SRS) for Task Management REST API

[![Deploy Task MS documentation to Github Pages](https://github.com/binaryloom/TaskManagementSystem/actions/workflows/pages_docs.yml/badge.svg)](https://github.com/binaryloom/TaskManagementSystem/actions/workflows/pages_docs.yml)

## 1. Introduction

The Task Management REST API is a backend service designed to handle task organization, assignment, and tracking for individuals and teams. This document outlines the essential functional requirements of the API.

## 2. Scope

The API will provide endpoints for creating, retrieving, updating, and deleting boards, lists, and tasks. It will support user authentication and authorization for secure access to resources.

## 3. Functional Requirements

### 3.1 User Management

- **FR-1:** Users can register a new account.
- **FR-2:** Users can authenticate securely.
- **FR-3:** Users can update their profile information.
- **FR-4:** Users can reset their password.

### 3.2 Board Management

- **FR-5:** Users can create a new board.
- **FR-6:** Users can retrieve existing boards.
- **FR-7:** Users can delete a board they own.

### 3.3 List Management

- **FR-8:** Users can create a new list within a board.
- **FR-9:** Users can retrieve existing lists within a board.
- **FR-10:** Users can delete a list they own.

### 3.4 Task Management

- **FR-11:** Users can create a new task within a list.
- **FR-12:** Users can retrieve existing tasks within a list.
- **FR-13:** Users can update the details of a task they own.
- **FR-14:** Users can assign a task to team members.
- **FR-15:** Users can set due dates for tasks.
- **FR-16:** Users can move tasks between lists.

## 4. Non-functional Requirements

- **NFR-1:** Security: The API must implement secure authentication mechanisms (e.g., JWT).
- **NFR-2:** Performance: The API should respond to requests promptly, with minimal latency.
- **NFR-3:** Scalability: The API should handle a growing number of users and tasks efficiently.
- **NFR-4:** Reliability: The API should be highly available, with minimal downtime for maintenance.

## 5. Constraints

- The API will be developed using Django REST Framework.
- The database management system will be PostgreSQL.

## 6. Assumptions

- Users have access to the internet for accessing the API endpoints.
- Proper input validation will be enforced to ensure data integrity.

## 7. Glossary

- **Board:** Represents a project or workflow.
- **List:** Represents a stage or category within a board.
- **Task:** Represents a unit of work or activity within a list.

```sh
sphinx-apidoc -o . ..

sphinx-apidoc -o . docs
```

pages_docs.yml

name: Deploy docs to gh-pages

on:
push:
branches: [master] # branch to trigger deployment for github pages

jobs:
pages:
runs-on: ubuntu-20.04
environment:
name: github-pages
url: ${{ steps.deployment.outputs.page_url }}
permissions:
pages: write
id-token: write
steps: - id: deployment
uses: sphinx-notes/pages@v3

name: Deploy Task MS docs to pages

on:

- push

jobs:
build_deploy_docs:
runs-on: ubuntu-latest
env:
GITHUB_PAT: ${{ secrets.GITHUB_TOKEN }}

    steps:
      - name: Checkout
        uses: actions/checkout@v2.3.4

      - name: Setup Python
        uses: actions/setup-python@v2.2.1
        with:
          python-version: 3.10
      - name: Install dependencies
        run: pip install -r docs/requirements.txt

      - name: Make the sphinx docs
        run: |
          make -C docs clean
          make -C docs html
      - name: Init new repo in dist folder & commit generated files
        run: |
          cd docs/_build/html
          git init
          touch .nojekyll
          git add -A
          git config --local user.email "extinctCoder@outlook.com"
          git config --local user.name "extinctCoder"
          git commit -m "Sphinx docs deploy"

      - name: Force push to destination folder
        uses: ad-m/github-push-action@v0.5.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: gh-pages
          force: true
          directory: ./docs/build/html
