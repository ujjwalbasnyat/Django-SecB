# Database Schema

This document describes the minimal database schema for the tutorial blog application.

## 1. Users
Stores people who write posts or leave comments.

- `id` — Primary key (UUID or auto-incrementing integer)
- `username` — String (unique)
- `email` — String (unique)
- `password_hash` — String (never store raw passwords)
- `role` — Enum (`admin`, `author`, `reader`) — optional, helpful for permissions
- `created_at` — Timestamp

## 2. Posts
The core content of the blog.

- `id` — Primary key
- `author` — ForeignKey → `Users` (e.g., `author_id`)
- `category` — ForeignKey → `Categories` (optional)
- `title` — String
- `slug` — String (unique; URL-friendly, e.g. `my-first-post`)
- `content` — Text/Markdown
- `excerpt` — String (short summary for listings)
- `image_url` — String (link to cover photo)
- `status` — Enum (`draft`, `published`)
- `published_at` — Timestamp (nullable for drafts)
- `created_at` — Timestamp
- `updated_at` — Timestamp

## 3. Categories
Used to group posts.

- `id` — Primary key
- `name` — String (e.g., "Technology", "Lifestyle")
- `slug` — String (unique)

## 4. Comments (optional)
If you want to support user interaction.

- `id` — Primary key
- `post` — ForeignKey → `Posts` (e.g., `post_id`)
- `user` — ForeignKey → `Users` (e.g., `user_id`)
- `content` — Text
- `created_at` — Timestamp

---

## Notes & Suggestions

- Use `ForeignKey` constraints for referential integrity.
- Add indexes on frequently queried fields like `slug`, `author_id`, and `published_at`.
- Use `TextField` for `content` (Markdown supported in rendering layer).
- Consider using Django's `AbstractUser` or a custom user model if you need extra fields.
- For the tutorial's "minimum possible" path, implement `Posts`, a simple `User` (or Django's built-in user), and register `Post` in the admin first.
