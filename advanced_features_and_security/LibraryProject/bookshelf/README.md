## Permissions and Groups Setup

### Model Permissions
- **Book Model**:
  - `can_view`: Allows viewing of books.
  - `can_create`: Allows creation of books.
  - `can_edit`: Allows editing of books.
  - `can_delete`: Allows deletion of books.

### Groups and Permissions
- **Editors**: 
  - `can_create`
  - `can_edit`
- **Viewers**:
  - `can_view`
- **Admins**:
  - `can_view`
  - `can_create`
  - `can_edit`
  - `can_delete`

### Views and Permissions
- **Add Book**: Requires `can_create` permission.
- **Edit Book**: Requires `can_edit` permission.
- **Delete Book**: Requires `can_delete` permission.

### Testing
1. Create users and assign them to the relevant groups.
2. Verify that users can only perform actions according to their permissions.
