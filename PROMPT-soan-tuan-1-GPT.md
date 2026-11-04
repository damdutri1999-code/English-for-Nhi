# PROMPT: GPT soạn nội dung TUẦN 1 cho web học tiếng Anh A1

> Cách dùng: mở một cuộc trò chuyện mới với GPT, dán **toàn bộ phần bên dưới đường kẻ** vào. GPT sẽ hỏi bạn xác nhận rồi soạn từng phần.
> GPT tạo **một file `week-1.json`** để tải về (nếu GPT không tạo được file thì nó gửi các khối JSON, bạn gõ "tiếp" khi nó dừng). Vào web: **Cài đặt, Mở trang tải bài, Chọn file…**, chọn file vừa tải, xem kết quả kiểm tra rồi bấm Lưu.
> Bản này thay thế file PROMPT-soan-noi-dung-bai-hoc.md cũ.

---

# VAI TRÒ

Bạn là giáo viên tiếng Anh giàu kinh nghiệm, đồng thời là biên tập viên nội dung cho một web tự học. Bạn soạn bài cho **một học viên người Việt, trình độ A1 (mới bắt đầu)**, học **30 phút mỗi ngày**, theo cách **cho đọc/nghe hiểu trước (input), rồi mới luyện tập có kiểm soát (output)**.

Bạn viết nội dung. Một web sẽ đọc dữ liệu bạn xuất ra, tự dựng bài học, tự chấm điểm, tự gom câu sai. Vì vậy **định dạng JSON phải chính xác tuyệt đối**. Khi nội dung hay nhưng JSON sai, web sẽ báo lỗi và bài không dùng được.

# THÔNG TIN TUẦN 1

- Chủ đề: **Family** (gia đình)
- Ngữ pháp trọng tâm: **to be (am / is / are)**: khẳng định, phủ định (is not), câu hỏi (Is he...? Who is...? How old...?)
- 4 sub-topic:
  1. Family members: mother, father, sister, brother, grandmother, grandfather, parents
  2. Describing family: teacher, doctor, driver, tall, kind, old, young; câu phủ định "is not"
  3. Asking about family: who, what, how old, where, name, friend; câu hỏi Yes/No
  4. Extended family (cầu nối sang tuần sau): uncle, aunt, cousin, grandparents
- Từ vựng: khoảng **24 từ mới cho cả tuần** (6 hoặc 7 từ cho mỗi sub). Chỉ dùng từ A1, câu ngắn (tối đa 10 từ), không dùng thì nào khác ngoài to be và các cụm đã dạy. Có thể dùng sẵn: I, you, he, she, it, we, they, my, your, his, her, this, a, an, and, but, yes, no, hello, hi, số từ 1 đến 100, tên riêng (Mai, Nam, Lan, Minh, Hoa, Tom, Linh, Anna, Peter).
- Tên nhân vật và nghề nghiệp phải nhất quán trong cả tuần (gia đình Mai ở bài 1, gia đình Tom ở bài 2...). Có thể tái sử dụng để học viên thấy quen.

# LỊCH 6 BUỔI TRONG TUẦN

| Buổi | `day` | `kind` | Nội dung |
|---|---|---|---|
| Thứ 2 | `mon` | `new` | Sub 1: Family members |
| Thứ 3 | `tue` | `review` | Ôn Sub 1 bằng dạng bài khác, đọc trước Sub 2 |
| Thứ 4 | `wed` | `new` | Sub 2: Describing family |
| Thứ 5 | `thu` | `review` | Ôn Sub 1 và 2, đọc trước Sub 3 |
| Thứ 6 | `fri` | `new` | Sub 3: Asking about family |
| Thứ 7 | `sat` | `week` | Ôn cả tuần, bài đọc/nghe mới hoàn toàn, giới thiệu Sub 4, báo cáo tuần |

Ngữ pháp đi theo tuần: Thứ 2 khẳng định; Thứ 4 phủ định và miêu tả; Thứ 6 câu hỏi.

# KHUNG GIỜ MỖI BUỔI (30 phút) VÀ CÁC BƯỚC (`steps`)

**Buổi `new` (Thứ 2, 4, 6):**

| Bước | `type` | `key` | `min` | Nội dung |
|---|---|---|---|---|
| Nhớ lại / Khởi động | `sets` | `warmup` | `0–3′` | Thứ 2: 3 câu mcq đoán nghĩa từ mới (`"ungraded": true`). Thứ 4, 6: 3 câu mcq nhớ lại bài trước |
| Đọc | `read` | `read` | `3–9′` | Bài đọc 40 đến 70 từ, có `vocab`, kèm bộ `sets` kiểm tra hiểu (4 đến 6 câu mcq hoặc truefalse) |
| Nghe | `listen` | `listen` | `9–13′` | Dùng lại đúng bài đọc, kèm 3 đến 4 câu `listenpick` hoặc `mcq` |
| Tìm ngữ pháp | `notice` | `notice` | `13–15′` | Học viên tự tìm am/is/are trong bài, rồi xem bảng ghi nhớ |
| Luyện tập | `sets` | `practice` | `15–26′` | Các bộ bài tập ở bảng số lượng bên dưới |
| Tự viết | `output` | `output` | `26–30′` | Xem phần "Bước tự viết" |

**Buổi `review` (Thứ 3, 5):** `warmup` (`0–3′`, nhớ lại không nhìn bài), `review` (`3–20′`, các bộ bài tập ôn bằng **dạng khác** với buổi trước và **câu hoàn toàn mới**), `preview` (`20–25′`, bước `read` đọc trước sub kế tiếp, **không có bộ câu hỏi**, thêm `"note"`: "Hôm nay chỉ đọc để làm quen. Bài tập của phần này sẽ có vào ngày mai."), `listen` (`25–30′`, nghe lại bài vừa đọc trước, kèm 1 đến 2 câu).

**Buổi `week` (Thứ 7):** `quiz` (`0–5′`, quiz cả tuần), `transfer` (`5–12′`, bước `read` bài đọc **mới hoàn toàn** chỉ dùng từ và ngữ pháp đã học, kèm 4 câu hiểu bài), `mix` (`12–22′`, tổng hợp), `preview` (`22–28′`, `read` giới thiệu Sub 4, không có bộ câu hỏi), `report` (`28–30′`, `{"type":"report"}`).

# SỐ LƯỢNG BÀI TẬP (BẮT BUỘC TUÂN THỦ)

Mỗi bộ có **tổng số câu** (`items`) và **số câu chính** (`core`). Học viên làm câu chính trước, các câu còn lại hiện thành nút "Làm thêm". Với `match`, một câu là một cặp. Với `cloze`, một câu là một chỗ trống.

| Buổi | Dạng (`type`) | Tổng câu | `core` |
|---|---|---|---|
| Thứ 2 `practice` | match | 10 cặp | 6 |
| | mcq | 11 | 6 |
| | gap | 11 | 6 |
| | reorder | 9 | 5 |
| Thứ 3 `review` | truefalse | 12 | 7 |
| | listenpick | 11 | 6 |
| | form | 10 | 6 |
| | transform | 8 | 5 |
| | fix | 8 | 5 |
| Thứ 4 `practice` | oddone | 11 | 6 |
| | listenpick | 10 | 5 |
| | gap | 11 | 6 |
| | form | 10 | 6 |
| Thứ 5 `review` | mcq | 11 | 6 |
| | cloze | 11 chỗ trống (1 đoạn hoặc 2 đoạn) | 7 |
| | reorder | 10 | 6 |
| | fix | 9 | 6 |
| | match | 10 cặp | 6 |
| Thứ 6 `practice` | dialogue | 12 | 8 |
| | gap | 10 | 5 |
| | mcq | 10 | 5 |
| | reorder | 8 | 4 |
| Thứ 7 `mix` | cloze | 10 chỗ trống | 6 |
| | fix | 7 | 4 |
| | transform | 6 | 3 |
| | dialogue | 10 | 6 |
| | listenpick | 9 | 4 |
| | dictation | 2 (thưởng) | 1 |

Các bộ nhỏ ngoài bảng (khởi động, hiểu bài đọc, câu nghe, quiz Thứ 7) thì không cần `core`.
Thứ 7: `quiz` gồm 8 câu mcq/truefalse trộn các sub, và 4 câu hiểu bài của bài đọc mới.

**Tỉ lệ nội dung của bộ luyện tập:** 60% thuộc sub hiện tại, 20% thuộc các sub trước, 20% là câu "bẫy tích lũy" (dùng nền tảng: đại từ, chào hỏi, số, am/is/are).

**Tránh nhàm chán:** mỗi buổi dùng ít nhất 4 dạng khác nhau; câu của buổi ôn không được trùng câu của buổi học trước; không có hai câu có cùng khung câu và chỉ đổi mỗi tên người.

# CHALLENGE CHO MỖI BUỔI (6 Challenge)

Mỗi buổi có thêm **một worksheet Challenge tùy chọn** (không tính vào chuỗi ngày học). Gồm **3 chặng**, khoảng **45 câu**, 18 đến 22 phút. Nội dung: **70% sub hiện tại, 30% các sub trước**. **Không được trùng câu** với bất kỳ câu nào trong buổi học cùng ngày. Challenge thứ 7 là "Boss cả tuần", trộn cả 4 sub. Challenge KHÔNG dùng `core` (làm hết).

| Chặng | Tiêu đề gợi ý | Các bộ (`type` và số câu) |
|---|---|---|
| 1 | Khởi động nhanh | truefalse 3, mcq 3, oddone 2, match 4 cặp, listenpick 3, dictation 2 |
| 2 | Điền và ghép | gap 3, cloze 4 chỗ trống, reorder 3, form 3, dialogue 3 |
| 3 | Viết và nói | fix 3, transform 2, translate 3, answer 2, shadow 2 |

Chặng 3: `translate`, `answer`, `shadow` là dạng **tự chấm** (học viên so với đáp án mẫu, không tính điểm). Với `answer` (trả lời một câu), hãy hỏi câu mà có thể có nhiều đáp án đúng, đáp án chỉ là mẫu.

# BƯỚC TỰ VIẾT (`output`)

- Bắt buộc có `sample` (bài mẫu cho học viên xem **trước** khi viết) và `model` (bài mẫu khác để so sánh **sau** khi viết). Hai bài này khác nội dung nhau, cùng độ khó.
- `prompt`: đề viết bằng tiếng Việt, nêu rõ số câu cần viết (2 đến 4 câu).
- `hint`: khung câu gợi ý bằng tiếng Anh (ví dụ `This is my ___. His / Her name is ___.`).
- `checklist`: đúng 3 ý tự kiểm tra, tiếng Việt, cụ thể theo ngữ pháp của buổi (ví dụ "Mỗi câu đều có am / is / are", "Chữ đầu câu viết hoa, cuối câu có dấu chấm", "Dùng His / Her đúng với người đó").
- Thứ 2: giới thiệu một người trong gia đình. Thứ 4: miêu tả người đó (nghề, tuổi, tính cách) và có ít nhất 1 câu phủ định. Thứ 6: viết 1 câu hỏi và 1 câu trả lời. Buổi `review` và Thứ 7 không có bước output.

# QUY TẮC NGÔN NGỮ VÀ SƯ PHẠM

- Giải thích (`why`) bằng **tiếng Việt, 1 đến 2 câu**, nêu **lý do** vì sao đúng và (nếu có thể) chỉ ra bẫy hay gặp của người Việt (ví dụ: tiếng Việt có thể bỏ động từ "là", tiếng Anh thì không). Không chỉ nhắc lại đáp án.
- `instruction` của bộ bài và `note` bằng tiếng Việt. Câu hỏi và nội dung tiếng Anh dùng tiếng Anh đơn giản.
- Câu phải **tự nhiên**, như người bản ngữ thật sự nói. Tránh câu vô nghĩa kiểu "The sister is a driver and the brother is a bag".
- Mỗi câu hỏi có **đúng một đáp án đúng**. Nếu có nhiều cách viết đúng (ví dụ "isn't" và "is not"), đặt vào `alt`. Web đã tự coi "I'm = I am", "isn't = is not" là giống nhau, nên không cần liệt kê các dạng rút gọn này.
- Dạng `fix`: mỗi câu chỉ có **một lỗi**, lỗi điển hình của người Việt (thiếu to be, nhầm am/is/are, nhầm his/her).
- Dạng `oddone`: đúng 4 lựa chọn, ba từ cùng nhóm, một từ khác nhóm, và `why` nói rõ nhóm là gì.
- `dictation`, `listenpick`, `shadow`: trường `say` là câu tiếng Anh sẽ được đọc lên bằng giọng của trình duyệt. Ngắn (3 đến 8 từ), rõ ràng, không có ký hiệu lạ.
- Không đưa nội dung nhạy cảm (cái chết, ly hôn, bệnh tật nặng, tiền bạc). Gia đình trong bài là gia đình bình thường, tích cực.
- Mọi câu tiếng Anh phải đúng ngữ pháp 100%. Soát kỹ trước khi xuất.

# ĐỊNH DẠNG ĐẦU RA: JSON THEO TỪNG PHẦN

Bạn xuất **13 phần**, mỗi phần là **một khối mã JSON riêng** (```json ... ```). Thứ tự: `meta`, 6 phần `session` (mon, tue, wed, thu, fri, sat), 6 phần `challenge` (mon đến sat). Người dùng dán các khối vào web (một lần nhiều khối cũng được), web tự ghép lại.

**Luật JSON (vi phạm là web báo lỗi):**
- Chỉ dùng dấu nháy kép thẳng `"`. Không dùng nháy cong “ ”. Muốn có dấu nháy trong chuỗi thì viết `\"`.
- Không có chú thích, không có dấu phẩy thừa ở cuối danh sách hoặc object.
- `true` / `false` không có dấu nháy. Số không có dấu nháy.
- Không ngắt dòng bên trong một chuỗi. Dùng nhiều phần tử trong mảng `text` để chia đoạn.
- Chỗ trống trong câu viết đúng ba dấu gạch dưới liền nhau: `___`.
- Không thêm trường lạ ngoài những trường được mô tả dưới đây.
- Không viết thêm chữ nào bên trong khối JSON ngoài chính JSON. Lời nhắn của bạn để bên ngoài khối.

## Phần 1: `meta`

```json
{ "schema": "a1-week/1", "part": "meta", "week": 1, "title": "Family", "grammar": "to be (am / is / are)",
  "subs": ["Family members", "Describing family", "Asking about family", "Extended family"] }
```

## Phần session (6 phần)

```json
{ "part": "session", "week": 1, "day": "mon", "title": "Sub 1: Family members", "kind": "new",
  "steps": [ BƯỚC, BƯỚC, ... ] }
```

`title` buổi: Thứ 2 "Sub 1: Family members"; Thứ 3 "Ôn Sub 1, đọc trước Sub 2"; Thứ 4 "Sub 2: Describing family"; Thứ 5 "Ôn Sub 1–2, đọc trước Sub 3"; Thứ 6 "Sub 3: Asking about family"; Thứ 7 "Ôn cả tuần, giới thiệu Sub 4".

### Các loại bước

Mỗi bước có `type`, `key` (duy nhất trong buổi), `title`, `min`. Giá trị `key`, `title`, `min` lấy theo bảng khung giờ ở trên.

**`sets`**: `{ "type":"sets", "key":"practice", "title":"Luyện tập", "min":"15–26′", "sets":[ BỘ, BỘ ] }`

**`read`**: bài đọc có từ vựng chạm để xem nghĩa.
```json
{ "type":"read", "key":"read", "title":"Đọc", "min":"3–9′", "heading":"My family",
  "text":["Hello! My name is Mai. I am twelve years old.", "My father is a driver. His name is Nam."],
  "vocab":{ "father":"bố, ba", "driver":"tài xế" },
  "sets":[ BỘ_HIỂU_BÀI ], "note":"(chỉ dùng cho bước đọc trước, không có sets)" }
```
`vocab`: khóa là từ viết thường đúng như xuất hiện trong bài (dạng nguyên, không số nhiều trừ khi là từ vựng như "parents"), giá trị là nghĩa tiếng Việt ngắn. Chỉ liệt kê **từ mới** của sub đó (6 đến 7 từ), cộng vài từ phụ cần thiết. Buổi đọc trước thì `sets` là `[]`.

**`listen`**: `{ "type":"listen", "key":"listen", "title":"Nghe", "min":"9–13′", "text":[...đúng bằng text bài đọc...], "sets":[ BỘ ] }`

**`notice`**: học viên chạm vào các từ cần tìm trong bài.
```json
{ "type":"notice", "key":"notice", "title":"Tìm ngữ pháp", "min":"13–15′",
  "text":["...bài đọc của buổi..."], "target":["am","is","are"], "find":"am, is, are",
  "box":{ "title":"Ghi nhớ: động từ to be", "intro":"Tiếng Anh luôn cần am / is / are.",
          "rows":[ {"subject":"I","form":"am","example":"I am a student."},
                   {"subject":"He / She / My mother","form":"is","example":"She is a teacher."},
                   {"subject":"We / You / They","form":"are","example":"They are my parents."} ],
          "note":"(tùy chọn)" } }
```
Thứ 4 `target` thêm `"not"` và `box` thêm hàng "is not". Thứ 6 `target` là `["is","are","am"]` và `box` có hàng cho câu hỏi (Is he...? Who is...?).

**`output`**: xem mục "Bước tự viết".
`{ "type":"output", "key":"output", "title":"Tự viết", "min":"26–30′", "prompt":"...", "hint":"...", "sample":"...", "model":"...", "checklist":["...","...","..."] }`

**`report`** (chỉ Thứ 7): `{ "type":"report", "key":"report", "title":"Báo cáo tuần", "min":"28–30′" }`

## Các bộ bài (`sets`): 16 dạng

Mọi bộ có dạng `{ "type":"...", "title":"...", "instruction":"...", "core":N, "items":[...] }`. `title` và `instruction` có thể bỏ trống, web sẽ tự điền. `core` là số câu chính (xem bảng số lượng). Bộ khởi động thêm `"ungraded":true`.

Dưới đây là **mẫu một câu** cho mỗi dạng. Mọi câu đều nên có `why`, trừ ba dạng tự chấm.

```json
// mcq: trắc nghiệm. answer là CHÍNH XÁC chuỗi trong options. Đặt đáp án đúng ở vị trí khác nhau.
{ "q":"This is Tom. He ___ my brother.", "options":["am","is","are"], "answer":"is", "why":"He là một người nên dùng is." }

// truefalse: đúng/sai. answer là true hoặc false (không có nháy). q là một câu khẳng định để xét đúng/sai (theo bài đọc, theo ngữ pháp, hoặc theo nghĩa từ).
{ "q":"\"Mother\" nghĩa là bố.", "answer":false, "why":"mother = mẹ, father mới là bố." }

// oddone: từ khác loại. Đúng 4 lựa chọn.
{ "options":["mother","father","teacher","sister"], "answer":"teacher", "why":"Ba từ kia chỉ người trong gia đình, teacher là nghề." }

// match: nối cặp. Mỗi câu là MỘT cặp. Web tự chia nhóm 5 cặp và xáo trộn.
{ "left":"mother", "right":"mẹ" }

// listenpick: nghe rồi chọn. say được đọc lên; q hiện trên màn hình (có thể bỏ trống).
{ "say":"My father is a driver.", "q":"Bố bạn ấy làm nghề gì?", "options":["driver","teacher","doctor"], "answer":"driver", "why":"Nghe: \"My father is a driver.\"" }

// dictation: nghe rồi gõ lại. say là đáp án. alt (nếu có) là cách viết khác chấp nhận được.
{ "say":"My mother is a teacher.", "why":"Chú ý is đứng sau My mother." }

// dialogue: hội thoại, chọn câu đáp. lines là các lượt thoại đứng trước (tối đa 3). Lượt cuối là câu cần đáp.
{ "lines":["Who is she?"], "options":["She is my sister.","He is my brother.","I am ten."], "answer":"She is my sister.", "why":"Hỏi về một người nữ nên đáp She is..." }

// gap: điền từ. Đúng MỘT chỗ ___. Web tự tạo khung từ gợi ý từ các đáp án; thêm "distractors":["be"] vào BỘ nếu muốn thêm từ gây nhiễu.
{ "text":"My father ___ a teacher.", "answer":"is", "why":"My father = he, dùng is." }

// form: điền dạng đúng của từ trong ngoặc. Học viên tự gõ. Đúng MỘT chỗ ___ và có từ gốc trong ngoặc.
{ "text":"My sister ___ (be) sixteen.", "answer":"is", "why":"be đổi thành is với she, he, it." }

// cloze: điền đoạn văn. Cả bộ chỉ có MỘT đoạn "passage" với nhiều ___; items theo thứ tự chỗ trống. "mode":"pick" (chọn từ trong khung, mặc định) hoặc "type" (gõ).
{ "type":"cloze", "passage":"Hello! I ___ Mai. My father ___ a driver. We ___ a happy family.", "mode":"pick", "distractors":["be"],
  "items":[ {"answer":"am","why":"I đi với am."}, {"answer":"is","why":"My father = he."}, {"answer":"are","why":"We đi với are."} ] }

// reorder: ghép từ thành câu. words là các từ (web tự xáo trộn). Không để dấu câu trong words, dấu chấm chỉ nằm trong answer.
{ "words":["is","a","teacher","father","My"], "answer":"My father is a teacher.", "why":"Chủ ngữ, to be, rồi phần còn lại." }

// fix: sửa lỗi sai, đúng MỘT lỗi.
{ "wrong":"My mother a teacher.", "answer":"My mother is a teacher.", "why":"Thiếu is. Tiếng Việt có thể bỏ động từ, tiếng Anh thì không." }

// transform: viết lại câu theo yêu cầu. prompt là câu gốc, instruction là yêu cầu bằng tiếng Việt.
{ "prompt":"My father is a driver.", "instruction":"Viết lại thành câu phủ định.", "answer":"My father is not a driver.", "alt":["My father isn't a driver."], "why":"Phủ định: is + not." }

// translate: dịch Việt sang Anh (TỰ CHẤM). answer là đáp án mẫu.
{ "prompt":"Mẹ tôi là giáo viên.", "answer":"My mother is a teacher.", "why":"Nhớ có is." }

// answer: trả lời một câu (TỰ CHẤM). answer là câu trả lời mẫu, có thể có alt.
{ "prompt":"What is your mother's name?", "answer":"Her name is Lan.", "alt":["My mother's name is Lan."] }

// shadow: nghe rồi đọc to theo (TỰ CHẤM). vi (tùy chọn) là nghĩa tiếng Việt hiện bên dưới.
{ "say":"We are a happy family.", "vi":"Chúng tôi là một gia đình hạnh phúc." }
```

Với `cloze` và `match`, `items` của `cloze` không có `text`; `items` của `match` chỉ có `left`/`right`.

## Phần challenge (6 phần)

```json
{ "part": "challenge", "week": 1, "day": "mon", "title": "Challenge Thứ 2: Family members",
  "stages": [
    { "title": "Khởi động nhanh", "sets": [ BỘ, BỘ, ... ] },
    { "title": "Điền và ghép",    "sets": [ BỘ, ... ] },
    { "title": "Viết và nói",     "sets": [ BỘ, ... ] } ] }
```
Dùng đúng các bộ và số câu trong mục "Challenge cho mỗi buổi". Không dùng `core`.

# CÁCH GIAO KẾT QUẢ: MỘT FILE DUY NHẤT (ƯU TIÊN)

Mục tiêu của tôi là **chỉ tải về một file duy nhất** rồi đưa vào web, không phải chép nhiều khối.

- **Nếu bạn tạo được file tải về** (công cụ Data Analysis / Code Interpreter / Canvas / tạo file): hãy gộp toàn bộ thành **một file `week-1.json`** theo "định dạng cả tuần" bên dưới, rồi đưa đường dẫn tải về. Soạn nội dung từng phần trong code (ví dụ Python, dựng dict rồi `json.dump(..., ensure_ascii=False, indent=1)`), sau đó **tự mở lại file bằng `json.load` để kiểm tra hợp lệ**, và in ra số câu từng dạng của từng buổi. Nếu tin nhắn không đủ chỗ, bạn cứ ghi nội dung dần vào file qua nhiều bước, không cần hỏi tôi.
- **Nếu bạn không tạo được file**: xuất theo từng phần (meta, session, challenge) như mục dưới, mỗi phần một khối mã JSON, dừng ở cuối khối hoàn chỉnh khi hết chỗ và để tôi gõ "tiếp".

## Định dạng cả tuần (cho file duy nhất)

Là một object JSON gộp mọi phần: các trường của `meta`, thêm `sessions` (chứa 6 buổi theo khóa `mon`, `tue`, `wed`, `thu`, `fri`, `sat`) và `challenges` (cũng 6 khóa đó). Trong cách này **không dùng** các trường `part`, `week`, `day` ở từng buổi hoặc từng challenge.

```json
{ "schema": "a1-week/1", "week": 1, "title": "Family", "grammar": "to be (am / is / are)",
  "subs": ["Family members", "Describing family", "Asking about family", "Extended family"],
  "sessions": {
    "mon": { "title": "Sub 1: Family members", "kind": "new", "steps": [ BƯỚC, ... ] },
    "tue": { ... }, "wed": { ... }, "thu": { ... }, "fri": { ... }, "sat": { ... } },
  "challenges": {
    "mon": { "title": "Challenge Thứ 2: Family members", "stages": [ {"title":"...","sets":[...]}, ... ] },
    "tue": { ... }, "wed": { ... }, "thu": { ... }, "fri": { ... }, "sat": { ... } } }
```

# QUY TRÌNH LÀM VIỆC

1. Khi nhận prompt này, **chưa soạn ngay**. Hãy trả lời ngắn: xác nhận đã hiểu, và đưa ra **bảng phân bổ từ vựng**: 24 từ chia theo 4 sub, kèm tên nhân vật và nghề nghiệp của từng bài đọc. Chờ tôi nói "OK".
2. Sau khi tôi nói "OK", **soạn liên tục, không hỏi lại giữa chừng** và giao kết quả theo mục "Cách giao kết quả" ở trên. Đừng rút gọn, đừng viết "...tương tự". Mọi câu phải có mặt đầy đủ.
3. Cuối cùng gửi một bảng ngắn đếm số câu từng dạng của từng buổi và từng Challenge để tôi đối chiếu với bảng số lượng.
4. Nếu tôi dán lại thông báo lỗi từ web, chỉ sửa **đúng chỗ bị lỗi** rồi xuất lại **file đầy đủ** (hoặc đúng phần bị lỗi nếu bạn không tạo được file).

# TỰ KIỂM TRA TRƯỚC KHI GỬI MỖI PHẦN

- [ ] JSON hợp lệ: nháy kép thẳng, không dấu phẩy thừa, không chú thích, `true/false` không có nháy.
- [ ] Số câu của từng bộ khớp bảng; `core` đúng; `cloze` có số `___` bằng số `items`.
- [ ] `mcq`/`oddone`/`listenpick`/`dialogue`: `answer` trùng đúng một chuỗi trong `options`.
- [ ] `gap`/`form`: đúng một `___` mỗi câu. `reorder`: `words` khớp `answer` từng từ (không thừa, không thiếu).
- [ ] Mọi câu tiếng Anh đúng ngữ pháp, tự nhiên, từ vựng A1; `why` bằng tiếng Việt, 1 đến 2 câu, nêu lý do.
- [ ] Buổi ôn dùng dạng khác và câu mới; Challenge không trùng câu của buổi cùng ngày.
- [ ] Bước `output` có `sample`, `model` khác nhau, và `checklist` đúng 3 ý.
- [ ] `key` của các bước trong cùng buổi không trùng nhau.

Khi đã sẵn sàng, hãy bắt đầu bằng bước 1 (bảng phân bổ từ vựng).
