export const books = [
  { book_id: 'book1', name: 'Japanese Foundations', words: [{ word_id: 1, japanese: '食べる', reading: 'たべる', meaning: 'to eat' }, { word_id: 2, japanese: '飲む', reading: 'のむ', meaning: 'to drink' }, { word_id: 3, japanese: '行く', reading: 'いく', meaning: 'to go' }, { word_id: 4, japanese: '見る', reading: 'みる', meaning: 'to see' }] },
  { book_id: 'book2', name: 'Everyday Japanese', words: [{ word_id: 1, japanese: '約束', reading: 'やくそく', meaning: 'promise; appointment' }, { word_id: 2, japanese: '準備', reading: 'じゅんび', meaning: 'preparation' }, { word_id: 3, japanese: '大切', reading: 'たいせつ', meaning: 'important; precious' }] }
];
export function findBook(bookId) { return books.find(book => book.book_id === bookId); }
