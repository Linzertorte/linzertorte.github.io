const CACHE_NAME = 'hp-audible-v9';

// 核心 App Shell 静态资源
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json',
  './harry.png'
];

// 1. 安装阶段
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('SW: 预缓存 App Shell...');
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

// 2. 激活阶段：清理旧版本缓存
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('SW: 清除旧缓存 ->', key);
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// 3. 请求拦截
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // A. 视频文件：直接走网络（Network Only），支持进度条拖动
  if (url.hostname.includes('amazonaws.com') || event.request.destination === 'video') {
    event.respondWith(fetch(event.request));
    return;
  }

  // B. data.json：网络优先（Network First）
  if (url.pathname.endsWith('/data.json') || url.pathname.endsWith('data.json')) {
    event.respondWith(
      fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const responseToCache = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              // 捕获可能由于跨域或异常导致的 put 报错
              cache.put(event.request, responseToCache).catch(() => {});
            });
          }
          return networkResponse;
        })
        .catch(() => {
          // 断网时回退到缓存
          return caches.match(event.request);
        })
    );
    return;
  }

  // C. 其他静态资源（HTML / PNG 等）：缓存优先（Cache First）
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse;
      }
      return fetch(event.request).then((networkResponse) => {
        // 只缓存同源的成功响应（避免把 opaque 响应或 404 存进去）
        if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache).catch(() => {});
          });
        }
        return networkResponse;
      });
    })
  );
});