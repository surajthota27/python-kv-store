# ⚡ Mini-Redis: Asynchronous In-Memory Key-Value Store

An ultra-fast, lightweight, in-memory data structure store written entirely in pure Python using `asyncio` and raw TCP sockets. 

This project is a custom implementation of a Redis-like caching layer designed to intercept heavy database queries, manage volatile data with Time-To-Live (TTL) expirations, and handle high-throughput concurrent client connections without blocking.

## 🧠 Why I Built This
Modern applications—like high-traffic food delivery platforms—frequently query the same data (e.g., nearby restaurant menus or active driver locations). Hitting a persistent disk database (like MongoDB or PostgreSQL) for every identical request causes high I/O latency and CPU bottlenecks. 

I built this memory cache to sit between the application server (e.g., an Express.js backend) and the database to serve frequently requested data from volatile RAM in $O(1)$ time complexity, protecting the primary database from traffic spikes.

## ✨ Core Features
* **Asynchronous I/O:** Utilizes Python's `asyncio` event loop to handle thousands of concurrent TCP connections on a single thread, avoiding the memory overhead of multi-threading.
* **$O(1)$ Time Complexity:** Core operations (`SET`, `GET`, `DEL`) are backed by heavily optimized hash maps.
* **Custom Protocol Parser:** Reads raw byte streams over TCP and safely deserializes them into actionable server commands.
* **Time-To-Live (TTL):** Supports expiring keys for volatile session management.
* **LRU Eviction (In Progress):** Implements `collections.OrderedDict` to automatically evict the least recently used data when memory capacity is reached.

## 🚀 Quick Start

### 1. Start the Server
Clone the repository and run the main server file. It requires no external dependencies.
```bash
git clone [https://github.com/yourusername/mini-redis.git](https://github.com/yourusername/mini-redis.git)
cd mini-redis
python src/server.py
