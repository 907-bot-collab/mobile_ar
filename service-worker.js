// Service Worker for AR Surgery Training PWA
// Handles offline functionality and app-like behavior

const CACHE_NAME = 'ar-surgery-v1.0.0';
const urlsToCache = [
  '/',
  '/index.html',
  '/surgery-data.js',
  '/manifest.json'
];

// Install event - cache resources
self.addEventListener('install', function(event) {
  console.log('🔧 Service Worker: Installing...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('📦 Service Worker: Caching files');
        return cache.addAll(urlsToCache);
      })
      .then(() => self.skipWaiting())
  );
});

// Activate event - clean old caches
self.addEventListener('activate', function(event) {
  console.log('✅ Service Worker: Activating...');
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          if (cacheName !== CACHE_NAME) {
            console.log('🗑️ Service Worker: Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Cache hit - return response
        if (response) {
          console.log('📋 Service Worker: Serving from cache:', event.request.url);
          return response;
        }

        // Cache miss - fetch from network
        console.log('🌐 Service Worker: Fetching from network:', event.request.url);
        return fetch(event.request);
      }
    )
  );
});

// Background sync for offline functionality
self.addEventListener('sync', function(event) {
  console.log('🔄 Service Worker: Background sync triggered');
  if (event.tag === 'background-sync') {
    event.waitUntil(doBackgroundSync());
  }
});

// Push notifications (if needed for medical alerts)
self.addEventListener('push', function(event) {
  console.log('🔔 Service Worker: Push received');
  const options = {
    body: event.data ? event.data.text() : 'AR Surgery Training Update',
    icon: 'data:image/svg+xml,🏥',
    badge: 'data:image/svg+xml,🏥'
  };

  event.waitUntil(
    self.registration.showNotification('AR Surgery Training', options)
  );
});

function doBackgroundSync() {
  // Handle background sync for offline data
  return Promise.resolve();
}
