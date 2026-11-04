#!/usr/bin/env python3
"""Tự động soạn tuần học: gọi API GPT 13 lần (meta, 6 buổi, 6 Challenge),
tự kiểm tra, tự sửa lỗi, rồi ghi 13 file JSON vào thư mục out/.
Cách dùng:
  pip install openai
  export OPENAI_API_KEY=sk-...        (Windows: set OPENAI_API_KEY=sk-...)
  python3 gen_week.py                 # chạy hết
  python3 gen_week.py --only mon ch-wed   # chỉ làm lại một vài phần
Tuỳ chọn: --model gpt-5  --prompt ../PROMPT-soan-tuan-1-GPT.md  --out out
"""
import argparse, json, os, re, sys, time, collections

PARTS = ["meta","mon","tue","wed","thu","fri","sat",
         "ch-mon","ch-tue","ch-wed","ch-thu","ch-fri","ch-sat"]
DAYS = {"mon":"Thứ 2","tue":"Thứ 3","wed":"Thứ 4","thu":"Thứ 5","fri":"Thứ 6","sat":"Thứ 7"}

def task_for(p):
    if p == "meta":
        return 'Soạn PHẦN `meta` (part:"meta") của tuần 1 gồm bảng từ vựng 32 từ chia 4 sub, tên nhân vật và nghề nghiệp từng bài đọc, đúng định dạng meta trong prompt.'
    if p.startswith("ch-"):
        return f'Soạn PHẦN challenge của buổi {DAYS[p[3:]]} (part:"challenge", day:"{p[3:]}"), đủ số câu theo bảng số lượng.'
    return f'Soạn PHẦN session của buổi {DAYS[p]} (part:"session", day:"{p}"), đủ mọi bước và đủ số câu theo bảng số lượng.'

def walk(o):
    if isinstance(o, dict):
        yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)

def validate(p, text):
    errs = []
    try: d = json.loads(text)
    except Exception as e: return None, [f"JSON không hợp lệ: {e}"]
    want = "meta" if p == "meta" else ("challenge" if p.startswith("ch-") else "session")
    if d.get("part") != want: errs.append(f'part phải là "{want}"')
    if p != "meta":
        day = p[3:] if p.startswith("ch-") else p
        if d.get("day") != day: errs.append(f'day phải là "{day}"')
    whys, qs = collections.Counter(), collections.Counter()
    n = 0
    for o in walk(d):
        opts = o.get("options")
        if isinstance(opts, list) and "answer" in o:
            n += 1
            ids = [str(x).strip().lower() for x in opts]
            if len(set(ids)) != len(ids): errs.append(f"options trùng nhau: {opts}")
            a = o["answer"]
            ok = (isinstance(a, int) and 0 <= a < len(opts)) or a in opts
            if not ok: errs.append(f'answer "{a}" không trùng đúng một chuỗi trong options {opts}')
        if isinstance(o.get("why"), str): whys[o["why"].strip().lower()] += 1
        q = o.get("q") or o.get("text")
        if isinstance(q, str) and ("answer" in o or "options" in o):
            qs[(q.strip().lower(), str(o.get("answer")))] += 1
    for w, c in whys.items():
        if c >= 5: errs.append(f'lời giải thích lặp {c} lần (mỗi câu phải có why riêng): "{w[:60]}"')
    for (q, _), c in qs.items():
        if c >= 4: errs.append(f'câu hỏi lặp {c} lần (tối đa 3): "{q[:60]}"')
    MALE = "Tom|Ben|Jack|David|Peter|Nam|Minh|John|Mike|Sam|Bob|Tony|Long|Huy|Khoa"; FEM = "grandmother|mother|sister|aunt|mom|mum|grandma|daughter|girl|woman|wife"
    for o in walk(d):
        tx = str(o.get("text") or o.get("q") or ""); ans = o.get("answer")
        full = tx.replace("___", ans) if isinstance(ans, str) else tx
        if re.search(rf"\b({MALE})\b\s+(is|was)\s+(my|his|her|a|the)\s+({FEM})\b", full, re.I): errs.append(f'tên con trai đi với từ chỉ nữ: "{full[:60]}"')
        if "___" in tx and isinstance(ans, str):
            before = tx.split("___")[0].strip()
            if before and not re.search(r"[.?!]$", before) and ans[:1].isupper() and not ans.startswith("I") and before: errs.append(f'chỗ trống giữa câu nhưng đáp án viết hoa: "{tx[:50]}" -> {ans}')
    generic = sum(1 for o in walk(d) if str(o.get("q","")).strip().lower().startswith("who or what is mentioned"))
    if generic: errs.append(f'{generic} câu hỏi chung chung "Who or what is mentioned?": phải hỏi đúng nội dung câu nghe')
    if p != "meta" and n < 15: errs.append(f"chỉ có {n} câu trắc nghiệm, quá ít so với bảng số lượng")
    return d, errs[:25]

def extract_json(s):
    m = re.search(r"```(?:json)?\s*(.*?)```", s, re.S)
    return (m.group(1) if m else s).strip()

def call(client, model, system, msgs, max_tokens):
    r = client.chat.completions.create(model=model, messages=[{"role":"system","content":system}]+msgs,
        response_format={"type":"json_object"}, max_completion_tokens=max_tokens)
    return r.choices[0].message.content

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="gpt-5"); ap.add_argument("--out", default="out")
    ap.add_argument("--prompt", default=os.path.join(os.path.dirname(__file__), "..", "PROMPT-soan-tuan-1-GPT.md"))
    ap.add_argument("--only", nargs="*"); ap.add_argument("--retries", type=int, default=3)
    ap.add_argument("--max-tokens", type=int, default=32000)
    a = ap.parse_args()
    from openai import OpenAI
    client = OpenAI()
    system = open(a.prompt, encoding="utf-8").read() + \
      "\n\n# CHẾ ĐỘ TỰ ĐỘNG\nBạn chạy trong script. Mỗi lần chỉ trả về MỘT đối tượng JSON của đúng phần được yêu cầu, không kèm lời giải thích, không bỏ qua câu nào."
    os.makedirs(a.out, exist_ok=True)
    meta_path = os.path.join(a.out, "week1-meta.json")
    for p in (a.only or PARTS):
        path = os.path.join(a.out, f"week1-{p}.json")
        ctx = ""
        if p != "meta" and os.path.exists(meta_path):
            ctx = "\n\nĐÂY LÀ PHẦN META ĐÃ CHỐT, phải dùng đúng từ vựng, nhân vật, nghề nghiệp này:\n" + open(meta_path, encoding="utf-8").read()
        msgs = [{"role":"user","content":task_for(p)+ctx}]
        good = None
        for t in range(1, a.retries+1):
            print(f"[{p}] lần {t}...", flush=True)
            try: out = call(client, a.model, system, msgs, a.max_tokens)
            except Exception as e:
                print("  lỗi API:", e); time.sleep(10*t); continue
            d, errs = validate(p, extract_json(out))
            if not errs: good = d; break
            print(f"  {len(errs)} lỗi, yêu cầu sửa:", *errs[:5], sep="\n   - ")
            msgs += [{"role":"assistant","content":out},
                     {"role":"user","content":"Phần này còn lỗi, hãy sửa đúng các chỗ sau và trả lại TOÀN BỘ JSON của phần này (câu nào đã đúng thì giữ nguyên):\n- " + "\n- ".join(errs)}]
        if good is None:
            print(f"[{p}] KHÔNG đạt sau {a.retries} lần, lưu bản cuối vào {path}.bad"); open(path+".bad","w",encoding="utf-8").write(out); continue
        json.dump(good, open(path,"w",encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"[{p}] OK -> {path}")
    print("\nXong. Kéo thả các file trong thư mục", a.out, "vào trang tải bài của web.")

if __name__ == "__main__":
    main()
