// 修改版本号以触发 SW 更新
const CACHE_NAME = 'hp-audible-app-v1';

// 安装阶段：不缓存任何文件，直接跳过等待
self.addEventListener('install', (event) => {
  self.skipWaiting();
});

// 激活阶段：清空之前遗留的所有 Cache 存储，并立即接管页面
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          console.log('正在清理旧缓存:', key);
          return caches.delete(key);
        })
      );
    })
  );
  self.clients.claim();
});

// 请求拦截：Network Only 策略，直接走网络请求
self.addEventListener('fetch', (event) => {
  event.respondWith(fetch(event.request));
});