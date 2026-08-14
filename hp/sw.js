// 每次修改了 html/js/json 想强制让用户更新时，把版本号 +1
const CACHE_NAME = 'hp-audible-v2';

// 核心应用 Shell（静态资源 + 结构数据）
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './data.json',
  './manifest.json',
  './harry.png'
];

// 1. 安装阶段：预缓存核心静态资源
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('SW: 预缓存核心文件...');
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting(); // 强制激活新的 SW
});

// 2. 激活阶段：清理旧版本的 Cache
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

// 3. 请求拦截阶段：分策略处理
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // A. AWS S3 视频文件：直接走网络（Network Only），绝不进 SW 缓存，避免占满手机内存
  if (url.hostname.includes('amazonaws.com') || event.request.destination === 'video') {
    event.respondWith(fetch(event.request));
    return;
  }

  // B. 其他静态资源（HTML / JSON / PNG等）：缓存优先，离线可用
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse; // 命中缓存直接返回
      }
      // 未命中缓存则去网络请求，并顺手存入 Cache
      return fetch(event.request).then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      });
    })
  );
});