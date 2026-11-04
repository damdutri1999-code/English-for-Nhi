-- Dán toàn bộ vào Supabase: SQL Editor > New query > Run
create table if not exists public.kv (
  id   text primary key,
  data jsonb not null,
  at   bigint not null default 0
);

alter table public.kv enable row level security;

drop policy if exists "kv_read"   on public.kv;
drop policy if exists "kv_insert" on public.kv;
drop policy if exists "kv_update" on public.kv;

-- Chỉ mở đúng dòng tiến độ và các dòng bài học w1..w18
create policy "kv_read" on public.kv for select to anon, authenticated
  using (id = 'learner-nhi-7k3q9x2m' or id ~ '^w[0-9]+$');
create policy "kv_insert" on public.kv for insert to anon, authenticated
  with check (id = 'learner-nhi-7k3q9x2m' or id ~ '^w[0-9]+$');
create policy "kv_update" on public.kv for update to anon, authenticated
  using (id = 'learner-nhi-7k3q9x2m' or id ~ '^w[0-9]+$')
  with check (id = 'learner-nhi-7k3q9x2m' or id ~ '^w[0-9]+$');
