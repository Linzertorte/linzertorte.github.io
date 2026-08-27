import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../lib/api';
import { todayNumber } from '../lib/date';

export default function Home() {
  const navigate = useNavigate();
  const [decks, setDecks] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    api('/api/books')
      .then(({ books }) => Promise.all(books.map(book =>
        api(`/api/books/${book.book_id}/home?today=${todayNumber()}`)
          .then(home => ({ ...home, word_count: book.word_count }))
      )))
      .then(setDecks)
      .catch(error => setError(error.message));
  }, []);

  if (error) return <main className="page"><p className="error">{error}</p></main>;
  if (!decks) return <main className="page">Loading your decks…</main>;

  return <main className="page hero">
    <h1>Your decks</h1>
    <section className="deck-list">
      {decks.map(({ book, review_count: reviewCount, word_count: wordCount }) => <article className="deck-card" key={book.book_id}>
        <div><h2>{book.name}</h2><p>{wordCount} words</p></div>
        <div className="deck-stats"><span>{reviewCount} due</span><span>{book.remaining_new_cards} new</span></div>
        <button onClick={() => navigate(`/study?book=${encodeURIComponent(book.book_id)}`)}>Start study</button>
      </article>)}
    </section>
  </main>;
}
