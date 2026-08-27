import 'dotenv/config';
const required = ['MONGODB_URI', 'SUPABASE_URL'];
export function validateConfig() { const missing = required.filter(key => !process.env[key]); if (missing.length) throw new Error(`Missing environment variables: ${missing.join(', ')}`); }
export const config = { port: Number(process.env.PORT || 3001), origin: process.env.FRONTEND_ORIGIN || 'http://localhost:5173', mongoUri: process.env.MONGODB_URI, mongoDb: process.env.MONGODB_DB || 'kotoba_dojo', supabaseUrl: process.env.SUPABASE_URL, issuer: process.env.SUPABASE_JWT_ISSUER || `${process.env.SUPABASE_URL}/auth/v1` };
