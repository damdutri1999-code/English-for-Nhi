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

-- Chỉ mở đúng dòng tiến độ của hai học viên và các dòng bài học w1..w30 (Nhi), t1..t30 (Trí)
create policy "kv_read" on public.kv for select to anon, authenticated
  using (id in ('learner-nhi-7k3q9x2m', 'learner-tri-5m8w2c4h', 'learner-bw-4h8n2k6q') or id ~ '^[wtb][0-9]+$');
create policy "kv_insert" on public.kv for insert to anon, authenticated
  with check (id in ('learner-nhi-7k3q9x2m', 'learner-tri-5m8w2c4h', 'learner-bw-4h8n2k6q') or id ~ '^[wtb][0-9]+$');
create policy "kv_update" on public.kv for update to anon, authenticated
  using (id in ('learner-nhi-7k3q9x2m', 'learner-tri-5m8w2c4h', 'learner-bw-4h8n2k6q') or id ~ '^[wtb][0-9]+$')
  with check (id in ('learner-nhi-7k3q9x2m', 'learner-tri-5m8w2c4h', 'learner-bw-4h8n2k6q') or id ~ '^[wtb][0-9]+$');


-- ===== Âm thanh do GV tải lên (kéo thả ở trang "GV soạn bài") =====
-- Bucket công khai "audio" (mọi học viên nghe được); chỉ nhận file âm thanh tối đa 50 MB.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('audio', 'audio', true, 52428800, array['audio/mpeg','audio/mp3','audio/mp4','audio/x-m4a','audio/aac','audio/wav','audio/x-wav','audio/ogg'])
on conflict (id) do update set public = true, file_size_limit = 52428800, allowed_mime_types = excluded.allowed_mime_types;

drop policy if exists "audio doc" on storage.objects;
create policy "audio doc" on storage.objects for all to anon
  using (bucket_id = 'audio') with check (bucket_id = 'audio');
