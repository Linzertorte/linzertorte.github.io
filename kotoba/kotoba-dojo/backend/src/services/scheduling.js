import {createEmptyCard, fsrs, Rating} from 'ts-fsrs';
const scheduler = fsrs();
const ratingMap = {
  again: Rating.Again,
  hard: Rating.Hard,
  good: Rating.Good,
  easy: Rating.Easy
};
function toFsrsCard(history) {
  return {
    due: new Date(history.due),
    stability: history.stability,
    difficulty: history.difficulty,
    elapsed_days: history.elapsed_days ?? 0,
    scheduled_days: history.scheduled_days ?? 0,
    reps: history.reps ?? 0,
    lapses: history.lapses ?? 0,
    state: history.state,
    last_review: history.last_review
      ? new Date(history.last_review)
      : undefined
  };
}
function applicationDay(date) {
  return Math.floor((Date.UTC(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDate()) - Date.UTC(2024, 5, 23)) / 86_400_000);
}
export function initialCard() {
  return createEmptyCard(new Date());
}
export function scheduleCard(existing, rating) {
  if (!ratingMap[rating]) 
    throw new Error('Invalid rating.');
  const now = new Date();
  const result = scheduler.next(toFsrsCard(existing), now, ratingMap[rating]);
  return result.card;
}
export function historyFromFsrs(wordId, card) {
  return {
    word_id: wordId,
    due: card
      .due
      .toISOString(),
    due_day: applicationDay(card.due),
    stability: card.stability,
    difficulty: card.difficulty,
    elapsed_days: card.elapsed_days,
    scheduled_days: card.scheduled_days,
    reps: card.reps,
    lapses: card.lapses,
    state: card.state,
    last_review: card.last_review
      ?.toISOString() || null
  };
}
export function dueOnOrBefore(history, today) {
  return history.due_day <= today;
}
