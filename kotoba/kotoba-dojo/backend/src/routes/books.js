import {Router} from 'express';
import {findBook, books} from '../data/books.js';
import {getUser, bookState, currentDayCount, saveUser} from '../services/users.js';
import {dueOnOrBefore, historyFromFsrs, initialCard, scheduleCard} from '../services/scheduling.js';
const router = Router();
function validToday(value) {
  return Number.isInteger(Number(value)) && Number(value) >= 0 && Number(value) < 1_000_000;
}
function access(user, bookId) {
  const source = findBook(bookId);
  const state = bookState(user, bookId);
  if (!source || !state) 
    return null;
  return {source, state};
}
function remaining(source, state, today) {
  const allowedToday = Math.max(0, state.daily_new_limit - currentDayCount(state, Number(today)));
  const unintroducedWords = source
    .words
    .filter(word => word.word_id >= state.next_word_id)
    .length;
  return Math.min(allowedToday, unintroducedWords);
}
router.get('/', async(req, res, next) => {
  try {
    const user = await getUser(req.authUser);
    res.json({
      current_book_id: user.current_book_id,
      books: books
        .filter(book => user.books
        ?.[book.book_id])
        .map(book => ({
          book_id: book.book_id,
          name: book.name,
          word_count: book.words.length,
          daily_new_limit: user.books[book.book_id].daily_new_limit
        }))
    });
  } catch (error) {
    next(error);
  }
});
router.patch('/current-book', async(req, res, next) => {
  try {
    const user = await getUser(req.authUser);
    if (!access(user, req.body.book_id)) 
      return res.status(404).json({error: 'Book not available to this user.'});
    user.current_book_id = req.body.book_id;
    await saveUser(user);
    res.json({current_book_id: user.current_book_id});
  } catch (error) {
    next(error);
  }
});
router.get('/:bookId/home', async(req, res, next) => {
  try {
    if (!validToday(req.query.today)) 
      return res.status(400).json({error: 'A valid today value is required.'});
    const user = await getUser(req.authUser);
    const item = access(user, req.params.bookId);
    if (!item) 
      return res.status(404).json({error: 'Book not available to this user.'});
    const reviewCount = item
      .state
      .words_history
      .filter(card => dueOnOrBefore(card, Number(req.query.today)))
      .length;
    res.json({
      book: {
        book_id: item.source.book_id,
        name: item.source.name,
        daily_new_limit: item.state.daily_new_limit,
        new_cards_introduced_today: currentDayCount(item.state, Number(req.query.today)),
        remaining_new_cards: remaining(item.source, item.state, req.query.today)
      },
      review_count: reviewCount
    });
  } catch (error) {
    next(error);
  }
});
router.get('/:bookId/next', async(req, res, next) => {
  try {
    if (!validToday(req.query.today)) 
      return res.status(400).json({error: 'A valid today value is required.'});
    const user = await getUser(req.authUser);
    const item = access(user, req.params.bookId);
    if (!item) 
      return res.status(404).json({error: 'Book not available to this user.'});
    const history = item
      .state
      .words_history
      .find(card => dueOnOrBefore(card, Number(req.query.today)));
    let word;
    let isNew = false;
    if (history) 
      word = item.source.words.find(candidate => candidate.word_id === history.word_id);
    else if (remaining(item.source, item.state, req.query.today) > 0) {
      word = item
        .source
        .words
        .find(candidate => candidate.word_id === item.state.next_word_id);
      isNew = Boolean(word);
    }
    if (!word) 
      return res.json({done: true});
    res.json({
      done: false,
      card: {
        word_id: word.word_id,
        japanese: word.japanese,
        reading: word.reading,
        meaning: word.meaning,
        is_new: isNew
      }
    });
  } catch (error) {
    next(error);
  }
});
router.post('/:bookId/review', async(req, res, next) => {
  try {
    const {word_id: wordId, rating, today} = req.body;
    if (!validToday(today) || !['again', 'hard', 'good', 'easy'].includes(rating)) 
      return res.status(400).json({error: 'A valid word, rating, and today value are required.'});
    const user = await getUser(req.authUser);
    const item = access(user, req.params.bookId);
    const word = item
      ?.source
        .words
        .find(candidate => candidate.word_id === Number(wordId));
    if (!item || !word) 
      return res.status(404).json({error: 'Book or word not available to this user.'});
    const index = item
      .state
      .words_history
      .findIndex(card => card.word_id === word.word_id);
    const isNew = index === -1;
    if (isNew && (word.word_id !== item.state.next_word_id || remaining(item.source, item.state, today) <= 0)) 
      return res.status(409).json({error: 'This new card is no longer available.'});
    const card = isNew
      ? initialCard()
      : item.state.words_history[index];
    const scheduled = scheduleCard(card, rating);
    const updated = historyFromFsrs(word.word_id, scheduled);
    if (isNew) {
      item
        .state
        .words_history
        .push(updated);
      const count = currentDayCount(item.state, Number(today));
      item.state.daily_new = {
        date: Number(today),
        count: count + 1
      };
      item.state.next_word_id += 1;
    } else 
      item.state.words_history[index] = updated;
    await saveUser(user);
    res.json({card: updated});
  } catch (error) {
    next(error);
  }
});
router.patch('/:bookId/settings', async(req, res, next) => {
  try {
    const limit = Number(req.body.daily_new_limit);
    if (!Number.isInteger(limit) || limit < 0 || limit > 999) 
      return res.status(400).json({error: 'daily_new_limit must be an integer from 0 to 999.'});
    const user = await getUser(req.authUser);
    const item = access(user, req.params.bookId);
    if (!item) 
      return res.status(404).json({error: 'Book not available to this user.'});
    item.state.daily_new_limit = limit;
    await saveUser(user);
    res.json({book_id: req.params.bookId, daily_new_limit: limit});
  } catch (error) {
    next(error);
  }
});
export default router;
