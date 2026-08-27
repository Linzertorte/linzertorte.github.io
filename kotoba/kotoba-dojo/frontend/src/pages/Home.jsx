import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../lib/api'; import { todayNumber } from '../lib/date';

export default function Home() {
  const navigate = useNavigate(); const [home, setHome] = useState(null); const [error, setError] = useState('');
  useEffect(() => { api('/api/books').then(({ books, current_book_id }) => { if (!current_book_id) return navigate('/settings', { replace: true }); const book = books.find(item => item.book_id === current_book_id); return api(`/api/books/${book.book_id}/home?today=${todayNumber()}`).then(setHome); }).catch(e => setError(e.message)); }, [navigate]);
  if (error) return <main className="page"><p className="error">{error}</p></main>;
  if (!home) return <main className="page">Loading your practice…</main>;
  return <main className="page hero"><p className="eyebrow">Today’s practice</p><h1>{home.book.name}</h1><div className="stats"><article><strong>{home.review_count}</strong><span>cards due</span></article><article><strong>{home.book.remaining_new_cards}</strong><span>new cards left</span></article></div><button onClick={() => navigate('/study')}>Start study</button></main>;
}
