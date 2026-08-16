const CACHE_NAME = 'hp-audible-v38';

const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json',
  './harry.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS_TO_CACHE))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) return caches.delete(key);
        })
      )
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // A. 音频与视频流：完全走网络直连 Network Only（支持 HTTP 206 Range 分段请求，解决 iPad PWA 播放弹回）
  if (
    event.request.destination === 'audio' ||
    event.request.destination === 'video' ||
    url.pathname.endsWith('.mp3') ||
    url.pathname.endsWith('.m4a') ||
    url.pathname.endsWith('.wav') ||
    url.hostname.includes('amazonaws.com')
  ) {
    event.respondWith(fetch(event.request));
    return;
  }

  // B. data.json：网络优先（Network First）
  if (url.pathname.endsWith('/data.json')) {
    event.respondWith(
      fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const responseToCache = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, responseToCache));
          }
          return networkResponse;
        })
        .catch(() => caches.match(event.request))
    );
    return;
  }

  // C. 其他静态资源（HTML、CSS、JS、PNG 等）：缓存优先
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse;
      }
      return fetch(event.request).then((networkResponse) => {
        // 允许缓存 200 OK 的同源(basic)和跨域(cors)响应
        if (
          networkResponse &&
          networkResponse.status === 200 &&
          (networkResponse.type === 'basic' || networkResponse.type === 'cors')
        ) {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, responseToCache));
        }
        return networkResponse;
      });
    })
  );
});