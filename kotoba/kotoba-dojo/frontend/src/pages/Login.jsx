import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { supabase } from '../lib/supabase';

export default function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState(''); const [password, setPassword] = useState('');
  const [error, setError] = useState(''); const [loading, setLoading] = useState(false);
  if (!supabase) return <main className="auth-card"><h1>Kotoba Dojo</h1><p>Add Supabase credentials to <code>frontend/.env</code> to enable sign-in.</p></main>;
  async function submit(event) { event.preventDefault(); setLoading(true); setError(''); const { error: authError } = await supabase.auth.signInWithPassword({ email, password }); setLoading(false); if (authError) setError(authError.message); else navigate('/', { replace: true }); }
  return <main className="auth-card"><p className="eyebrow">言葉の道場</p><h1>Welcome back.</h1><p>Train your vocabulary one card at a time.</p><form onSubmit={submit}><label>Email<input type="email" value={email} onChange={e => setEmail(e.target.value)} required /></label><label>Password<input type="password" value={password} onChange={e => setPassword(e.target.value)} required /></label>{error && <p className="error">{error}</p>}<button disabled={loading}>{loading ? 'Signing in…' : 'Sign in'}</button></form></main>;
}
