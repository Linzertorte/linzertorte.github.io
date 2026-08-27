import { useEffect, useState } from 'react';
import { api } from '../lib/api';

export default function Settings() {
  const [books, setBooks] = useState([]);
  const [error, setError] = useState('');
  const [saving, setSaving] = useState(null);

  useEffect(() => { api('/api/books').then(data => setBooks(data.books)).catch(error => setError(error.message)); }, []);

  async function saveLimit(bookId, limit) {
    setSaving(bookId);
    try {
      await api(`/api/books/${bookId}/settings`, { method: 'PATCH', body: JSON.stringify({ daily_new_limit: Number(limit) }) });
      setBooks(items => items.map(item => item.book_id === bookId ? { ...item, daily_new_limit: Number(limit) } : item));
    } catch (error) { setError(error.message); } finally { setSaving(null); }
  }

  return <main className="page">
    <h1>Deck settings</h1>
    {error && <p className="error">{error}</p>}
    <section className="book-list">{books.map(book => <article className="book-row" key={book.book_id}>
      <h2>{book.name}</h2>
      <label>New cards/day<input type="number" min="0" max="999" defaultValue={book.daily_new_limit} onBlur={event => saveLimit(book.book_id, event.target.value)} /></label>
      {saving === book.book_id && <span className="saving">Saving…</span>}
    </article>)}</section>
  </main>;
}
