import {getDb} from '../db.js';
import {books} from '../data/books.js';
function defaultBookState() {
  return {
    next_word_id: 1,
    daily_new_limit: 20,
    daily_new: {
      date: null,
      count: 0
    },
    words_history: []
  };
}
export async function getUser(authUser) {
  const db = await getDb();
  const users = db.collection('users');
  let user = await users.findOne({user_id: authUser.id});
  if (!user) {
    const userBooks = Object.fromEntries(books.map(book => [book.book_id, defaultBookState()]));
    user = {
      user_id: authUser.id,
      user_name: authUser.name,
      current_book_id: null,
      books: userBooks
    };
    await users.insertOne(user);
  }
  return user;
}
export function currentDayCount(book, today) {
  return book.daily_new
    ?.date === today
      ? book.daily_new.count
      : 0;
}
export function bookState(user, bookId) {
  return user.books
    ?.[bookId];
}
export async function saveUser(user) {
  const db = await getDb();
  await db
    .collection('users')
    .replaceOne({
      user_id: user.user_id
    }, user);
}
