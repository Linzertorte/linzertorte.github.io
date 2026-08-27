import {useEffect, useState} from 'react';
import {useNavigate} from 'react-router-dom';
import {api} from '../lib/api';

export default function Settings() {
  const navigate = useNavigate();
  const [books,
    setBooks] = useState([]);
  const [current,
    setCurrent] = useState(null);
  const [error,
    setError] = useState('');
  const [saving,
    setSaving] = useState(null);
  useEffect(() => {
    api('/api/books').then(data => {
      setBooks(data.books);
      setCurrent(data.current_book_id);
    }).catch(e => setError(e.message));
  }, []);
  async function select(bookId) {
    setSaving(bookId);
    try {
      await api('/api/me/current-book', {
        method: 'PATCH',
        body: JSON.stringify({book_id: bookId})
      });
      setCurrent(bookId);
    } catch (e) {
      setError(e.message);
    } finally {
      setSaving(null);
    }
  }
  async function saveLimit(bookId, limit) {
    setSaving(bookId);
    try {
      await api(`/api/books/${bookId}/settings`, {
        method: 'PATCH',
        body: JSON.stringify({daily_new_limit: Number(limit)})
      });
      setBooks(items => items.map(item => item.book_id === bookId
        ? {
          ...item,
          daily_new_limit: Number(limit)
        }
        : item));
    } catch (e) {
      setError(e.message);
    } finally {
      setSaving(null);
    }
  }
  return <main className="page">
    <p className="eyebrow">Configuration</p>
    <h1>Your books</h1>{error && <p className="error">{error}</p>}
    <section className="book-list">{books.map(book => <article className="book-row" key={book.book_id}>
        <div>
          <h2>{book.name}</h2>
          <p>{book.word_count}
            words</p>
        </div>
        <label>New cards/day<input
          type="number"
          min="0"
          max="999"
          defaultValue={book.daily_new_limit}
          onBlur={e => saveLimit(book.book_id, e.target.value)}/></label>
        <button
          className={current === book.book_id
          ? 'selected'
          : 'secondary'}
          disabled={saving === book.book_id || current === book.book_id}
          onClick={() => select(book.book_id)}>{current === book.book_id
            ? 'Selected'
            : 'Select'}</button>
      </article>)}</section>{current && <button className="secondary" onClick={() => navigate('/')}>Back home</button>}</main>;
}
