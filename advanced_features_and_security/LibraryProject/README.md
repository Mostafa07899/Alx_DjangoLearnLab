README.MD
HALA MADRID


# Django Advanced Features and Security

## Overview
This system uses Django groups and permissions to restrict access to parts of the application.

## Permissions
- `can_view`: Can view documents.
- `can_create`: Can create documents.
- `can_edit`: Can edit documents.
- `can_delete`: Can delete documents.

## Groups
- **Viewers**: Assigned `can_view`.
- **Editors**: Assigned `can_create` and `can_edit`.
- **Admins**: Assigned all permissions.

## How to Test
1. Create users and assign them to groups in Django admin.
2. Log in as these users and attempt to access the views.
3. Verify that permissions are enforced correctly.

## Files
- `models.py`: Contains the `Document` model and custom permissions.
- `views.py`: Includes views with permission checks.
- `admin.py`: Sets up groups and permissions programmatically.
