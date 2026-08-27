# Kotoba Dojo

A vocabulary-learning starter application with a React PWA frontend and an Express/MongoDB backend.

## Local development

1. Copy `frontend/.env.example` to `frontend/.env` and provide your Supabase URL and publishable key.
2. Copy `backend/.env.example` to `backend/.env` and provide MongoDB and Supabase credentials.
3. Install each project independently:

   ```sh
   cd frontend && npm install
   cd ../backend && npm install
   ```

4. Start the backend with `npm run dev` in `backend/`, then start the frontend with `npm run dev` in `frontend/`.

The sample vocabulary book is intentionally held in the backend (`src/data/books.js`), separately from user progress in MongoDB.
