# PROMPT: GPT soạn nội dung TUẦN 1 cho web học tiếng Anh A1–A2

> Cách dùng: mở một cuộc trò chuyện mới với GPT, dán **toàn bộ phần bên dưới đường kẻ** vào. GPT sẽ hỏi bạn xác nhận rồi soạn từng phần.
> GPT gửi **một file `week-1.json`**. Vào web: **Cài đặt, Mở trang tải bài**, kéo thả file vào ô, web kiểm tra, xem kết quả rồi bấm Lưu. (Nếu GPT không tạo được file, nó gửi các khối JSON, bạn dán vào.)
> Bản này thay thế file PROMPT-soan-noi-dung-bai-hoc.md cũ.

---

# VAI TRÒ

Bạn là giáo viên tiếng Anh giàu kinh nghiệm, đồng thời là biên tập viên nội dung cho một web tự học. Bạn soạn bài cho **một học viên người Việt, trình độ A1–A2 (đã có chút nền tảng, đang ôn lại và củng cố từ gốc)**, học **30 phút mỗi ngày**, theo cách **cho đọc/nghe hiểu trước (input), rồi mới luyện tập có kiểm soát (output)**.

Bạn viết nội dung. Một web sẽ đọc dữ liệu bạn xuất ra, tự dựng bài học, tự chấm điểm, tự gom câu sai. Vì vậy **định dạng JSON phải chính xác tuyệt đối**. Khi nội dung hay nhưng JSON sai, web sẽ báo lỗi và bài không dùng được.

# THÔNG TIN TUẦN 1

- Chủ đề: **Family** (gia đình)
- Ngữ pháp trọng tâm: **to be (am / is / are)**: khẳng định, phủ định (is not), câu hỏi (Is he...? Who is...? How old...?)
- 4 sub-topic:
  1. Family members: mother, father, sister, brother, grandmother, grandfather, parents, children (gợi ý 8 từ; thêm "'s" sở hữu cách)
  2. Describing family: teacher, doctor, driver, tall, kind, friendly, funny, busy (cộng old, young đã quen); câu phủ định "is not / isn't"
  3. Asking about family: who, what, how old, where, name, friend, from, big; câu hỏi Yes/No và câu trả lời ngắn
  4. Extended family (cầu nối sang tuần sau): uncle, aunt, cousin, grandparents, neighbour, relative, together, close
- Trình độ A1–A2: học viên đã từng học tiếng Anh nhưng còn yếu và rời rạc. Nội dung phải **nền tảng nhưng không trẻ con**: tình huống đời thường của người lớn hoặc thanh thiếu niên, không nhàm như giáo trình cho trẻ nhỏ, và đủ thách thức để thấy tiến bộ.
- Từ vựng: khoảng **32 từ mới cho cả tuần** (8 từ cho mỗi sub), gồm từ A1 cốt lõi và một số từ A2 dễ gặp (ví dụ friendly, funny, strong, busy, engineer, farmer, neighbour). Không dùng từ ngoài A2.
- Câu và bài đọc: câu tối đa **12 từ**; được dùng từ nối đơn giản **and, but, because, too, very, also**; được dùng sở hữu cách **'s** (my mother's name), viết tắt **I'm, isn't, aren't, he's**. Bài đọc **60 đến 90 từ** (khoảng 6 đến 9 câu).
- Ngữ pháp: chỉ dùng **to be** (đủ các dạng: khẳng định, phủ định, câu hỏi, câu trả lời ngắn Yes, she is. / No, she isn't.), tính từ sở hữu và đại từ. **Không dùng** hiện tại đơn (do/does), thì quá khứ, there is/are, can. Những thứ này để dành cho các tuần sau.
- Có thể dùng sẵn: I, you, he, she, it, we, they, my, your, his, her, our, their, this, a, an, and, but, because, yes, no, hello, hi, số từ 1 đến 100, tên riêng (Mai, Nam, Lan, Minh, Hoa, Tom, Linh, Anna, Peter).
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
| Nhớ lại / Khởi động | `sets` | `warmup` | `0–3′` | Thứ 2: 6 câu mcq đoán nghĩa từ mới (`"ungraded": true`, `core` 3). Thứ 4, 6: 6 câu mcq nhớ lại bài trước (`core` 3) |
| Đọc | `read` | `read` | `3–9′` | Bài đọc 60 đến 90 từ, có `purpose` (mục tiêu đọc) và `vocab`, kèm **2 bộ `sets`**: (1) bộ hiểu bài (4 đến 6 câu chính, mcq hoặc truefalse) và (2) bộ **vận dụng** `"role":"apply"` (xem mục "Bài đọc phải được vận dụng"), mỗi bộ có thêm 3 câu làm thêm |
| Nghe | `listen` | `listen` | `9–13′` | Dùng lại đúng bài đọc, kèm câu chính 3 đến 4, cộng thêm 3 câu làm thêm (`listenpick` hoặc `mcq`) |
| Tìm ngữ pháp | `notice` | `notice` | `13–15′` | Học viên tự tìm am/is/are trong bài, rồi xem bảng ghi nhớ |
| Luyện tập | `sets` | `practice` | `15–26′` | Các bộ bài tập ở bảng số lượng bên dưới |
| Tự viết | `output` | `output` | `26–30′` | Xem phần "Bước tự viết" |

**Buổi `review` (Thứ 3, 5):** `warmup` (`0–3′`, nhớ lại không nhìn bài), `review` (`3–20′`, các bộ bài tập ôn bằng **dạng khác** với buổi trước và **câu hoàn toàn mới**), `preview` (`20–25′`, bước `read` đọc trước sub kế tiếp, **chỉ có bộ vận dụng nhẹ 2 câu, không có bộ hiểu bài đầy đủ**, thêm `"note"`: "Hôm nay chỉ đọc để làm quen. Bài tập của phần này sẽ có vào ngày mai."), `listen` (`25–30′`, nghe lại bài vừa đọc trước, kèm 1 đến 2 câu).

**Buổi `week` (Thứ 7):** `quiz` (`0–5′`, quiz cả tuần), `transfer` (`5–12′`, bước `read` bài đọc **mới hoàn toàn** chỉ dùng từ và ngữ pháp đã học, kèm 4 câu hiểu bài), `mix` (`12–22′`, tổng hợp), `preview` (`22–28′`, `read` giới thiệu Sub 4, có `purpose` và bộ vận dụng nhẹ 2 câu), `report` (`28–30′`, `{"type":"report"}`).

# SỐ LƯỢNG BÀI TẬP (BẮT BUỘC TUÂN THỦ)

Mỗi bộ có **tổng số câu** (`items`) và **số câu chính** (`core`). Học viên làm câu chính trước (vừa 30 phút), các câu còn lại hiện thành nút "Làm thêm" để luyện nhiều hơn. Với `match`, một câu là một cặp. Với `cloze`, một câu là một chỗ trống. **Các câu "làm thêm" phải là câu mới hoàn toàn, không lặp câu chính, đủ chất lượng như câu chính.**

| Buổi | Dạng (`type`) | Tổng câu | `core` |
|---|---|---|---|
| Thứ 2 `practice` | match | 14 cặp | 6 |
| | mcq | 17 | 6 |
| | gap | 17 | 6 |
| | reorder | 13 | 5 |
| Thứ 3 `review` | truefalse | 18 | 7 |
| | listenpick | 17 | 6 |
| | form | 14 | 6 |
| | transform | 11 | 5 |
| | fix | 11 | 5 |
| Thứ 4 `practice` | oddone | 17 | 6 |
| | listenpick | 16 | 5 |
| | gap | 17 | 6 |
| | form | 14 | 6 |
| Thứ 5 `review` | mcq | 17 | 6 |
| | cloze | 15 chỗ trống (1 đến 3 đoạn) | 7 |
| | reorder | 14 | 6 |
| | fix | 12 | 6 |
| | match | 14 cặp | 6 |
| Thứ 6 `practice` | dialogue | 16 | 8 |
| | gap | 16 | 5 |
| | mcq | 16 | 5 |
| | reorder | 12 | 4 |
| Thứ 7 `mix` | cloze | 14 chỗ trống | 6 |
| | fix | 10 | 4 |
| | transform | 9 | 3 |
| | dialogue | 14 | 6 |
| | listenpick | 15 | 4 |
| | dictation | 5 (thưởng) | 1 |

**Các bộ nhỏ cũng phải tăng thêm 3 câu "làm thêm"** (xuyên suốt cả tuần), `core` bằng số câu gốc:

| Bộ nhỏ | Câu chính (`core`) | Tổng câu |
|---|---|---|
| Khởi động / Nhớ lại (`warmup`, mcq) | 3 | 6 |
| Hiểu bài đọc (bộ trong bước `read`) | 4 đến 6 | thêm 3 câu mỗi bộ |
| Vận dụng bài đọc (`role:"apply"`) | 3 đến 4 | thêm 3 câu mỗi bộ |
| Câu nghe (bộ trong bước `listen`) | 3 đến 4 | thêm 3 câu mỗi bộ |
| Thứ 7 `quiz` (mcq/truefalse trộn các sub) | 8 | 14 |
| Thứ 7 hiểu bài đọc mới | 4 | 7 |

Bước `read` đọc trước và các bước làm quen (`preview`) chỉ có bộ vận dụng nhẹ 2 câu (không tính câu làm thêm).

**Tỉ lệ nội dung của bộ luyện tập:** 60% thuộc sub hiện tại, 20% thuộc các sub trước, 20% là câu "bẫy tích lũy" (dùng nền tảng: đại từ, chào hỏi, số, am/is/are).

**HẠN CHẾ LẶP CÂU (quy tắc cứng):** Một câu hỏi **được phép xuất hiện lặp lại, nhưng tối đa 3 lần trong toàn bộ file** (tính cả bản gốc; lần thứ 4 trở đi là vi phạm). Khi một câu lặp lại thì **lời giải thích (`why`) được giữ nguyên giống bản gốc**. Chỉ lặp khi thật sự có lợi cho việc ôn tập, và ưu tiên câu mới. Các lần lặp nên đổi dạng bài hoặc đổi thứ tự lựa chọn. Một câu là "lặp" nếu giống câu khác về nội dung (kể cả chỉ đổi tên người hoặc đổi một từ). Cụ thể:
- Mỗi câu lặp tối đa 3 lần, kể cả giữa các buổi, giữa bước đọc, nghe, luyện tập, Challenge, và giữa câu chính với câu làm thêm. Câu hiểu bài ở bước đọc/nghe không được dùng lại ở phần luyện tập.
- Trong cùng một bộ bài, không lặp câu; và không để hai câu hỏi cùng kiểm tra đúng một thông tin theo cùng một cách.
- Câu khởi động và câu quiz Thứ 7 cũng phải là câu **mới**, không lấy lại câu đã dùng trước đó.
- Buổi ôn kiểm tra lại kiến thức cũ bằng câu hoàn toàn mới, không nhắc lại câu cũ.
- Các câu `listenpick`, `dictation`, `shadow` dùng câu nói (`say`) khác nhau.
- Bài đọc và bài nghe của một buổi là cùng một văn bản (được phép), nhưng mọi câu hỏi, câu bài tập phải khác nhau.
Trước khi xuất, hãy **tự rà toàn bộ câu, đếm số lần mỗi câu xuất hiện** (nếu tạo file bằng code, hãy kiểm tra bằng chương trình; câu nào xuất hiện từ 4 lần trở lên thì thay bằng câu mới). Web sẽ báo cảnh báo nếu một câu lặp quá 3 lần.

**Tránh nhàm chán:** mỗi buổi dùng ít nhất 4 dạng khác nhau; câu của buổi ôn không được trùng câu của buổi học trước; không có hai câu có cùng khung câu và chỉ đổi mỗi tên người. Vì số câu nhiều, hãy đa dạng hóa: đổi chủ ngữ, đổi tình huống, đổi từ vựng, đổi kiểu hỏi.

# CHALLENGE CHO MỖI BUỔI (6 Challenge)

Mỗi buổi có thêm **một worksheet Challenge tùy chọn** (không tính vào chuỗi ngày học). Gồm **3 chặng**, khoảng **93 câu** (học viên làm theo sức, không bắt buộc làm hết trong một lần). Nội dung: **70% sub hiện tại, 30% các sub trước**. **Không được trùng câu** với bất kỳ câu nào trong buổi học cùng ngày. Challenge thứ 7 là "Boss cả tuần", trộn cả 4 sub. Challenge KHÔNG dùng `core` (làm hết).

| Chặng | Tiêu đề gợi ý | Các bộ (`type` và số câu) |
|---|---|---|
| 1 | Khởi động nhanh | truefalse 6, mcq 6, oddone 5, match 7 cặp, listenpick 6, dictation 5 |
| 2 | Điền và ghép | gap 6, cloze 7 chỗ trống, reorder 6, form 6, dialogue 6 |
| 3 | Viết và nói | fix 6, transform 5, translate 6, answer 5, shadow 5 |

Chặng 3: `translate`, `answer`, `shadow` là dạng **tự chấm** (học viên so với đáp án mẫu, không tính điểm). Với `answer` (trả lời một câu), hãy hỏi câu mà có thể có nhiều đáp án đúng, đáp án chỉ là mẫu.

# BƯỚC TỰ VIẾT (`output`)

- Bắt buộc có `sample` (bài mẫu cho học viên xem **trước** khi viết) và `model` (bài mẫu khác để so sánh **sau** khi viết). Hai bài này khác nội dung nhau, cùng độ khó.
- `prompt`: đề viết bằng tiếng Việt, nêu rõ số câu cần viết (3 đến 5 câu).
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
{ "type":"read", "key":"read", "title":"Đọc", "min":"3–9′", "heading":"My family", "purpose":"Đọc để tìm: Mai có những ai trong gia đình?",
  "text":["Hello! My name is Mai. I am twelve years old.", "My father is a driver. His name is Nam."],
  "vocab":{ "father":"bố, ba", "driver":"tài xế" },
  "sets":[ BỘ_HIỂU_BÀI, BỘ_VẬN_DỤNG ], "note":"(chỉ dùng cho bước đọc trước)" }
```
`vocab`: khóa là từ viết thường đúng như xuất hiện trong bài (dạng nguyên, không số nhiều trừ khi là từ vựng như "parents"), giá trị là nghĩa tiếng Việt ngắn. Chỉ liệt kê **từ mới** của sub đó (khoảng 8 từ), cộng vài từ phụ cần thiết. 

**Bài đọc phải được vận dụng, không đọc suông.** Đọc xong rồi bấm "xong" là vô nghĩa. Mỗi bước `read` phải làm đủ 3 việc, tùy theo nội dung của buổi và của tuần:
1. `purpose`: một câu tiếng Việt nêu **mục tiêu đọc cụ thể** trước khi đọc, bắt học viên đọc để tìm hoặc so sánh một điều gì đó, ví dụ "Đọc để tìm: Mai có những ai trong gia đình?" hoặc "Đọc để so sánh: gia đình Linh khác gia đình bạn ở điểm nào?". Không viết kiểu "Hãy đọc bài".
2. Bộ **hiểu bài** (không có `role`): câu hỏi tìm thông tin ngay trong bài.
3. Bộ **vận dụng** có `"role":"apply"`: 3 đến 4 câu **dùng chính nội dung và mẫu câu của bài** vào một việc có ý nghĩa, và việc đó phải gắn với chủ đề của tuần (tuần 1: gia đình, giới thiệu người). Chọn dạng phù hợp với buổi: `answer` (trả lời câu hỏi về bản thân theo mẫu trong bài, ví dụ "Who is your mother?"), `transform` hoặc `reorder` (viết lại câu trong bài về người khác, ví dụ đổi "My father is a driver" thành câu về "My mother"), `fix` (sửa đoạn giới thiệu sai về một người trong bài), `gap` hoặc `cloze` (hoàn thành đoạn giới thiệu mới dùng cùng mẫu câu). Câu vận dụng **không được chép lại nguyên câu trong bài**, phải buộc học viên tự dùng từ và mẫu câu đã đọc. `instruction` của bộ này nói rõ việc cần làm bằng tiếng Việt, ví dụ "Dùng mẫu câu trong bài để nói về mẹ của Mai."
Bước đọc trước (`preview`) cũng phải có `purpose` và **một bộ vận dụng nhẹ 2 câu** (ví dụ đoán nghĩa từ mới theo ngữ cảnh, hoặc tìm trong bài người nào được nhắc), vì đọc trước mà không làm gì thì học viên không nhớ. Câu đầy đủ của bài sẽ có vào ngày mai.

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

Mọi bộ có dạng `{ "type":"...", "instruction":"...", "core":N, "items":[...] }`.

**QUY TẮC ĐẶT TÊN (rất quan trọng, vì học viên là người Việt A1 đọc trực tiếp):**
- `type` (mcq, gap, cloze, match...) chỉ là **mã kỹ thuật nội bộ**, học viên **không bao giờ thấy**. Dùng đúng mã trong bảng dưới đây.
- **Không viết `title` cho bộ bài** (bỏ hẳn trường này). Web tự hiện tên tiếng Việt cho từng dạng. Tuyệt đối không viết `"title":"Mcq"`, `"Gap"`, `"Cloze"`, `"Word form"`, `"Dialogue"`...
- `instruction` là **một câu yêu cầu bằng tiếng Việt đơn giản, riêng cho bộ đó**, nói rõ việc cần làm và nội dung cần chú ý, ví dụ: "Chọn am, is hoặc are cho mỗi câu.", "Nối từ tiếng Anh với nghĩa tiếng Việt.", "Nghe rồi chọn nghề nghiệp đúng." Không viết chung chung kiểu "Hoàn thành từng câu." hay "Làm bài.". Có thể bỏ trống nếu không có gì riêng cần nói, web sẽ dùng yêu cầu mặc định.
- Mọi chữ học viên đọc (tiêu đề bước, `instruction`, `why`, `hint`, tiêu đề Challenge) viết bằng **tiếng Việt dễ hiểu**, không dùng thuật ngữ tiếng Anh như MCQ, cloze, word form, gap fill.

Bảng **mã `type` và tên tiếng Việt web hiển thị** (để bạn hiểu, không cần ghi tên vào file):

| type | Tên hiển thị cho học viên |
|---|---|
| mcq | Chọn đáp án |
| truefalse | Đúng hay Sai |
| oddone | Tìm từ khác loại |
| match | Nối cặp |
| listenpick | Nghe và chọn |
| dictation | Nghe và viết lại |
| dialogue | Chọn câu đáp lại |
| gap | Điền từ vào chỗ trống |
| form | Đổi dạng từ |
| cloze | Điền vào đoạn văn |
| reorder | Xếp thành câu |
| fix | Tìm và sửa lỗi |
| transform | Viết lại câu |
| translate | Dịch sang tiếng Anh |
| answer | Trả lời bằng tiếng Anh |
| shadow | Nghe và đọc theo |

 `core` là số câu chính (xem bảng số lượng). Bộ khởi động thêm `"ungraded":true`.

Dưới đây là **mẫu một câu** cho mỗi dạng. Mọi câu đều nên có `why`, trừ ba dạng tự chấm.

```json
// mcq: chọn đáp án. answer là CHÍNH XÁC chuỗi trong options. Đặt đáp án đúng ở vị trí khác nhau.
{ "q":"This is Tom. He ___ my brother.", "options":["am","is","are"], "answer":"is", "why":"He là một người nên dùng is." }

// truefalse: đúng hay sai. answer là true hoặc false (không có nháy). q là một câu khẳng định để xét đúng/sai (theo bài đọc, theo ngữ pháp, hoặc theo nghĩa từ).
{ "q":"\"Mother\" nghĩa là bố.", "answer":false, "why":"mother = mẹ, father mới là bố." }

// oddone: từ khác loại. Đúng 4 lựa chọn.
{ "options":["mother","father","teacher","sister"], "answer":"teacher", "why":"Ba từ kia chỉ người trong gia đình, teacher là nghề." }

// match: nối cặp. Mỗi câu là MỘT cặp. Web tự chia nhóm 5 cặp và xáo trộn.
{ "left":"mother", "right":"mẹ" }

// listenpick: nghe rồi chọn. say được đọc lên; q hiện trên màn hình.
// Web chạy mỗi câu thành 3 bước: (1) chọn đáp án, chọn sai thì chọn lại; (2) khi chọn đúng, chữ của `say` hiện ra và chạy sáng theo giọng đọc như karaoke, nghe dò 2 lần; (3) chữ ẩn đi, học viên nghe và chép lại chính xác câu `say`, đúng mới sang câu sau.
// Vì vậy `say` phải là MỘT câu hoàn chỉnh, tự nhiên, 3 đến 8 từ, chỉ dùng từ đã học, đúng chính tả (học viên phải chép lại được). `q` hỏi về nội dung của chính câu `say`.
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

# QUY TẮC CHẤT LƯỢNG (QUAN TRỌNG NHẤT): CẤM SINH NỘI DUNG TỰ ĐỘNG

Lần thử trước, file bị lỗi vì **nội dung được sinh bằng vòng lặp và mẫu câu trong code**. Hậu quả: hàng chục câu lặp, lời giải thích giống hệt nhau, câu vô nghĩa ("father means a type of weather"), đáp án sai ngữ pháp ("My parents ___ funny" với đáp án "is"), options bị trùng. Vì vậy:

1. **Mỗi câu hỏi phải do bạn tự nghĩ và tự viết, từng câu một**, như một giáo viên thật soạn bài. Tuyệt đối **không** dùng vòng lặp, `random`, hàm sinh câu, mẫu có chỗ điền tên/từ, hay "template" để tạo câu. Code (nếu dùng) chỉ để **ghi file và kiểm tra**, không để sinh nội dung.
2. **Mỗi câu hỏi khác nhau có một `why` riêng** (1 đến 2 câu tiếng Việt, nêu lý do cụ thể). Không dùng chung một lời giải thích cho các câu hỏi khác nhau. Riêng khi chính câu hỏi đó được lặp lại (tối đa 3 lần), `why` giống nhau là bình thường.
3. **Tự kiểm tra ngữ pháp từng câu**: câu đúng/sai phải đúng thật. Ví dụ "My parents ___" thì đáp án là "are", không bao giờ là "is". Đáp án `answer` phải đúng với chủ ngữ.
4. **`answer` phải trùng từng ký tự (kể cả viết hoa) với một chuỗi trong `options`.** Các `options` phải **khác nhau**, không trùng. Nếu câu có chỗ trống giữa câu thì các lựa chọn viết thường ("is", "are", "am"); chỉ viết hoa khi chúng đứng đầu câu.
5. **`listenpick`**: câu hỏi `q` phải liên quan trực tiếp đến câu `say`, và đáp án phải **nghe được từ chính câu `say`**. Cấm các câu hỏi chung chung như "Who or what is mentioned?" lặp lại nhiều lần. Ví dụ tốt: say "My uncle is a doctor." / q "Chú của bạn ấy làm nghề gì?" / options doctor, driver, nurse.
6. **`truefalse`**: mỗi câu là một nhận định có nghĩa, đúng hoặc sai rõ ràng theo bài đọc, theo ngữ pháp hoặc theo nghĩa từ. Cấm nhận định phi lý (ví dụ "brother là một loại thời tiết").
7. Đa dạng hóa thật sự: đổi chủ ngữ, tình huống, từ vựng, kiểu hỏi. Không có 10 câu cùng một khuôn chỉ đổi một từ.
8. **Tên người và giới tính phải khớp.** Tên con trai (Tom, Ben, Jack, Nam, Minh, David, Peter...) chỉ đi với he/his/father/brother/grandfather/uncle/boy/man. Tên con gái (Lan, Mai, Anna, Linda, Nhi, Lucy, Sara...) chỉ đi với she/her/mother/sister/grandmother/aunt/girl/woman. **Cấm** các câu như "Tom is my grandmother", "Lan is my father". Khi viết câu về quan hệ gia đình, hãy kiểm tra lại từng câu: tên, đại từ và từ chỉ quan hệ có cùng giới tính không. Nên dùng tên ít gây nhầm (Tom, Anna) và ghi rõ giới tính trong bài đọc.
9. **Chữ hoa trong câu điền từ.** Với mọi dạng có chỗ trống `___` (`gap`, `cloze`, `form`) và với các lựa chọn của câu trắc nghiệm điền từ: nếu chỗ trống nằm **giữa câu** thì đáp án, `bank` và `options` phải viết **thường** ("is", "my", "mother"). Chỉ viết hoa khi chỗ trống đứng **đầu câu**, hoặc khi đó là danh từ riêng hay chữ "I" ("Tom", "Vietnam", "I"). Cấm viết hoa lung tung như "My ___ is Tom" với đáp án "Mother" hay "The ___ is a doctor" với đáp án "Father".
10. **Mỗi chỗ trống phải chỉ có một đáp án hợp lý** trong ngữ cảnh. Với `gap` và `cloze` có `bank`, đảm bảo mỗi từ trong bank chỉ hợp với đúng một câu (hoặc nếu hợp nhiều câu thì các câu đó phải có đáp án riêng rõ ràng), để học viên không chọn một từ hợp lý nhưng bị chấm sai.
11. Chất lượng quan trọng hơn tốc độ.

# BƯỚC BẮT BUỘC: TỰ RÀ SOÁT NGỮ PHÁP SAU KHI VIẾT MỖI PHẦN

Sau khi viết xong **mỗi phần** (mỗi file) và **trước khi lưu hay gửi**, bạn phải làm một lượt **rà soát ngữ pháp riêng**, đọc lại **từng câu một** (không đọc lướt), và kiểm tra:
1. **Chia động từ theo chủ ngữ**: I am, he/she/it is, we/you/they are, danh từ số ít dùng is, số nhiều dùng are ("My parents are", "My aunt and I are"). Đáp án điền vào chỗ trống phải làm câu **đúng ngữ pháp và đúng nghĩa**.
2. **Đáp án thật sự đúng**: với trắc nghiệm, điền từ, sửa lỗi, chuyển câu: tự làm lại từng câu như học viên và đối chiếu với `answer`. Chỉ có **một** đáp án đúng trong `options` (trừ khi `alt` ghi sẵn các đáp án chấp nhận được).
3. **Mạo từ, số ít/số nhiều, đại từ, sở hữu** (a/an, my/his/her, this/these), **chính tả**, dấu câu, chữ hoa đầu câu.
4. **Câu có nghĩa và tự nhiên**; tên người khớp giới tính; không có câu vô lý.
5. **Bản dịch tiếng Việt khớp câu tiếng Anh** (đúng từ vựng: "relative" là họ hàng, "neighbour" là hàng xóm), và `why` giải thích đúng.
6. **Các chỗ trống trong `cloze`/`gap`**: thứ tự `items` phải khớp **đúng thứ tự các chỗ trống** trong đoạn văn; số chỗ trống bằng số `items`; đoạn văn không lặp câu.
Nếu thấy lỗi ở bất kỳ câu nào, **sửa ngay** rồi rà lại. Khi gửi, ghi một dòng: "Rà ngữ pháp: đã đọc N câu, sửa M câu." Chỉ lưu hoặc gửi file **sau khi** rà xong. Không được bỏ bước này vì tiết kiệm thời gian.

# CÁCH GIAO KẾT QUẢ: TỰ LÀM HẾT 13 FILE TRONG MỘT LẦN CHẠY, KHÔNG DỪNG, KHÔNG HỎI

Bạn phải **tự làm liên tục cả 13 file trong cùng một lần chạy**. Tôi sẽ không gõ "tiếp". **Cấm** dừng giữa chừng, cấm báo "chưa hoàn thành khối lượng", cấm hỏi lại. Hãy dùng công cụ **Python / phân tích dữ liệu (nếu có)** để ghi file theo nhịp sau:

1. Lặp lại 13 lần, mỗi lần **một lần gọi công cụ ghi đúng một file** (không phải một tin nhắn dài; 13 file này chỉ là file trung gian): `week1-meta.json`, `week1-mon.json`, `week1-tue.json`, `week1-wed.json`, `week1-thu.json`, `week1-fri.json`, `week1-sat.json`, `week1-ch-mon.json`, `week1-ch-tue.json`, `week1-ch-wed.json`, `week1-ch-thu.json`, `week1-ch-fri.json`, `week1-ch-sat.json`.
2. Trong mỗi lần gọi, nội dung JSON được **dán thẳng thành chuỗi văn bản do bạn tự viết** (ví dụ `open("week1-mon.json","w").write(r'''{...}''')`), **không** dựng bằng vòng lặp hay hàm sinh câu (xem mục "Quy tắc chất lượng"). Ngay sau khi ghi, mở lại bằng `json.load` và kiểm tra: `answer` nằm trong `options`, `options` không trùng, không có `why` lặp. Nếu lỗi thì sửa file ngay trong lần chạy đó.
3. Nếu một buổi quá dài cho một lần ghi, chia thành `week1-mon-a.json` và `week1-mon-b.json` (cùng `part`, `week`, `day`, `title`; phần b chỉ chứa các `steps` còn lại).
4. Khi **cả 13 file đã xong**, dùng code **ghép** (chỉ ghép, không sửa nội dung) thành **MỘT file duy nhất `week-1.json`** có dạng: `{"schema":"a1-week/1","week":1,"title":...,"grammar":...,"subs":...,"sessions":{"mon":{"title":...,"kind":...,"steps":[...]},...,"sat":{...}},"challenges":{"mon":{"title":...,"stages":[...]},...,"sat":{...}}}`. Lấy `schema`, `week`, `title`, `grammar`, `subs` từ file meta. Với mỗi buổi, lấy `title`, `kind`, `steps` từ file session (nếu có file a và b thì nối `steps` của a rồi b). Với mỗi Challenge, lấy `title`, `stages` từ file challenge. Mở lại `week-1.json` bằng `json.load` để chắc chắn hợp lệ. **Chỉ gửi tôi file `week-1.json` này** (không gửi 13 file lẻ, không zip), kèm bảng đếm số câu từng dạng.
5. **Nếu môi trường của bạn không có công cụ tạo file**, hãy xuất lần lượt từng khối mã JSON, mỗi khối một phần, và **tiếp tục sang phần kế ngay trong cùng tin nhắn hoặc tin nhắn kế tiếp mà không chờ tôi**.

# QUY TRÌNH LÀM VIỆC

1. Khi nhận prompt này, **chưa soạn ngay**. Hãy trả lời ngắn: xác nhận đã hiểu, và đưa ra **bảng phân bổ từ vựng**: khoảng 32 từ chia theo 4 sub, kèm tên nhân vật và nghề nghiệp của từng bài đọc. Chờ tôi nói "OK".
2. Sau khi tôi nói "OK", **tự làm liên tục hết 13 file, không dừng**, theo mục "Cách giao kết quả" ở trên. Mọi câu phải tự viết, đầy đủ. Đừng rút gọn, đừng viết "...tương tự", đừng sinh bằng code.
3. Cuối cùng gửi một bảng ngắn đếm số câu từng dạng của từng buổi và từng Challenge để tôi đối chiếu với bảng số lượng. Nêu rõ nếu có phần nào bạn chưa làm kịp.
4. Nếu tôi dán lại thông báo lỗi từ web, chỉ sửa **đúng chỗ bị lỗi** và xuất lại **đúng file (phần) bị lỗi**, không làm lại các phần khác.

# TỰ KIỂM TRA TRƯỚC KHI GỬI MỖI PHẦN

- [ ] **Đã rà soát ngữ pháp từng câu (chia động từ, đáp án đúng, mạo từ, chính tả, bản dịch khớp, thứ tự chỗ trống khớp `items`) và ghi dòng "Rà ngữ pháp: đã đọc N câu, sửa M câu."**
- [ ] **Mọi câu do tôi tự viết, không sinh bằng mẫu hay vòng lặp; mỗi `why` riêng cho từng câu; đã tự kiểm tra ngữ pháp của từng đáp án.**
- [ ] `answer` trùng từng ký tự với một chuỗi trong `options`; các `options` không trùng nhau.
- [ ] Tên người, đại từ và từ chỉ quan hệ cùng giới tính ("Tom is my grandmother" là sai). Chỗ trống giữa câu thì đáp án, bank, options viết thường.
- [ ] **Không có `title` kiểu "Mcq", "Gap", "Cloze"... trong bất kỳ bộ bài nào; `instruction` bằng tiếng Việt, riêng cho từng bộ.**
- [ ] Mỗi bước `read` có `purpose` cụ thể và có bộ `role:"apply"` dùng bài đọc vào việc có ý nghĩa (không chép lại câu trong bài).
- [ ] JSON hợp lệ: nháy kép thẳng, không dấu phẩy thừa, không chú thích, `true/false` không có nháy.
- [ ] Số câu của từng bộ khớp bảng (kể cả các bộ nhỏ và Challenge); `core` đúng; `cloze` có số `___` bằng số `items`.
- [ ] `listenpick`: `say` là một câu hoàn chỉnh 3 đến 8 từ (sẽ được chép chính tả), `q` hỏi đúng về nội dung câu đó.
- [ ] `mcq`/`oddone`/`listenpick`/`dialogue`: `answer` trùng đúng một chuỗi trong `options`.
- [ ] `gap`/`form`: đúng một `___` mỗi câu. `reorder`: `words` khớp `answer` từng từ (không thừa, không thiếu).
- [ ] Mọi câu tiếng Anh đúng ngữ pháp, tự nhiên, từ vựng A1–A2; `why` bằng tiếng Việt, 1 đến 2 câu, nêu lý do.
- [ ] **Không câu nào xuất hiện quá 3 lần trong toàn file** (đã rà toàn bộ, đã thay các câu lặp từ lần thứ 4). Buổi ôn ưu tiên dạng khác và câu mới.
- [ ] Bước `output` có `sample`, `model` khác nhau, và `checklist` đúng 3 ý.
- [ ] `key` của các bước trong cùng buổi không trùng nhau.

Khi đã sẵn sàng, hãy bắt đầu bằng bước 1 (bảng phân bổ từ vựng).
