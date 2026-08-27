import { useEffect, useState } from 'react';
import { Navigate, NavLink, Outlet, Route, Routes, useNavigate } from 'react-router-dom';
import { supabase } from './lib/supabase';
import Login from './pages/Login';
import Home from './pages/Home';
import Settings from './pages/Settings';
import Study from './pages/Study';

function ProtectedLayout() {
  const navigate = useNavigate();
  const [ready, setReady] = useState(false);
  const [session, setSession] = useState(null);
  useEffect(() => {
    if (!supabase) { setReady(true); return; }
    supabase.auth.getSession().then(({ data }) => { setSession(data.session); setReady(true); });
    const { data: subscription } = supabase.auth.onAuthStateChange((_event, value) => setSession(value));
    return () => subscription.subscription.unsubscribe();
  }, []);
  if (!ready) return <main className="centered">Loading your dojo…</main>;
  if (!session) return <Navigate to="/login" replace />;
  async function signOut() { await supabase.auth.signOut(); navigate('/login'); }
  return <><header className="navbar"><NavLink className="brand" to="/">Kotoba Dojo</NavLink><nav><NavLink to="/">Home</NavLink><NavLink to="/settings">Settings</NavLink><button className="link-button" onClick={signOut}>Logout</button></nav></header><Outlet /></>;
}

export default function App() {
  return <Routes>
    <Route path="/login" element={<Login />} />
    <Route element={<ProtectedLayout />}>
      <Route path="/" element={<Home />} />
      <Route path="/settings" element={<Settings />} />
      <Route path="/study" element={<Study />} />
    </Route>
    <Route path="*" element={<Navigate to="/" replace />} />
  </Routes>;
}
