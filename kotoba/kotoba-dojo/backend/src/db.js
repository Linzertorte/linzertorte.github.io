import { MongoClient } from 'mongodb'; import { config } from './config.js';
let client; let db;
export async function getDb() { if (!db) { client = new MongoClient(config.mongoUri); await client.connect(); db = client.db(config.mongoDb); await db.collection('users').createIndex({ user_id: 1 }, { unique: true }); } return db; }
export async function closeDb() { if (client) await client.close(); }
