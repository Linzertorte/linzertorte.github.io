import { useCallback, useEffect, useState } from 'react'; import { useNavigate } from 'react-router-dom'; import { api } from '../lib/api'; import { todayNumber } from '../lib/date';
const ratings = ['again', 'hard', 'good', 'easy'];
export default function Study() {
  const navigate = useNavigate(); const [bookId, setBookId] = useState(null); const [card, setCard] = useState(null); const [done, setDone] = useState(false); const [error, setError] = useState(''); const [submitting, setSubmitting] = useState(false);
  const loadNext = useCallback(async (id) => { try { const data = await api(`/api/books/${id}/next?today=${todayNumber()}`); setDone(Boolean(data.done)); setCard(data.card || null); } catch (e) { setError(e.message); } }, []);
  useEffect(() => { api('/api/books').then(data => { if (!data.current_book_id) return navigate('/settings', { replace: true }); setBookId(data.current_book_id); loadNext(data.current_book_id); }).catch(e => setError(e.message)); }, [loadNext, navigate]);
  async function review(rating) { if (!card || !bookId) return; setSubmitting(true); try { await api(`/api/books/${bookId}/review`, { method: 'POST', body: JSON.stringify({ word_id: card.word_id, rating, today: todayNumber() }) }); await loadNext(bookId); } catch (e) { setError(e.message); } finally { setSubmitting(false); } }
  if (error) return <main className="page"><button className="back" onClick={() => navigate('/')}>← Back</button><p className="error">{error}</p></main>;
  if (done) return <main className="page study"><button className="back" onClick={() => navigate('/')}>← Back</button><p className="eyebrow">Complete</p><h1>That’s all for now.</h1><p>Come back when you have more words due.</p></main>;
  if (!card) return <main className="page">Preparing your next card…</main>;
  return <main className="page study"><button className="back" onClick={() => navigate('/')}>← Back</button><p className="eyebrow">{card.is_new ? 'New word' : 'Review'}</p><section className="flashcard"><p className="japanese">{card.japanese}</p><p className="reading">{card.reading}</p><p>{card.meaning}</p></section><div className="ratings">{ratings.map(rating => <button className={rating} key={rating} onClick={() => review(rating)} disabled={submitting}>{rating}</button>)}</div></main>;
}
