# Fast-API with DB Connection Pools

## Problem Statement

### Some common problems with database connections
1. Database connection limit exceeded
2. Database connection timeout
3. Database connection is not closed properly
4. Database connection is not released properly

创建一个 Postgres 数据库表, 包含 `id`, `fname`, `lname`, `email`, `password` 这些字段：

```sql
CREATE TABLE public.user
(
    id serial PRIMARY KEY,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);
```

连接池的创建参考：https://github.com/tiangolo/fastapi/discussions/9097
