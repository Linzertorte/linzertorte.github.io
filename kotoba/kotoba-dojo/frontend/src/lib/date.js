const EPOCH = { year: 2024, month: 6, day: 23 };

function utcCalendarDay({ year, month, day }) {
  return Date.UTC(year, month - 1, day);
}

export function todayNumber() {
  const parts = new Intl.DateTimeFormat('en-CA', {
    year: 'numeric', month: 'numeric', day: 'numeric'
  }).formatToParts(new Date()).reduce((result, part) => {
    if (part.type !== 'literal') result[part.type] = Number(part.value);
    return result;
  }, {});
  return Math.round((utcCalendarDay(parts) - utcCalendarDay(EPOCH)) / 86_400_000);
}
