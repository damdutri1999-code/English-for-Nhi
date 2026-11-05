#!/usr/bin/env python3
"""Sinh BRIEF 9 tuan dau cho Nhi va Tri vao briefs/nhi va briefs/tri. Chay: python3 tools/make_briefs.py"""
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "briefs")

def W(s): return [x.strip() for x in s.split(",")]

# ------------------------------------------------------------------ NHI
NHI = {
 1: dict(topic="Family", grammar="to be (am / is / are) và sở hữu (my, your, his, her)", level="A2", kind="A", subs=[
     ("Relatives", W("husband, wife, son, daughter, grandparents, aunt, uncle")),
     ("Jobs", W("nurse, engineer, farmer, dentist, mechanic, accountant, shop assistant")),
     ("Describing people", W("slim, shy, polite, honest, friendly, funny, busy")),
     ("Family life", W("married, single, retired, neighbour, relative, together, close"))],
   conn="and, but, because", chars="Mai, Nam (tài xế), Lan (y tá), Minh, Hoa",
   gate=["Thứ 2, Thứ 3: chỉ câu khẳng định với am / is / are và my, his, her. KHÔNG có phủ định, KHÔNG có câu hỏi.",
         "Thứ 4: được thêm phủ định với to be (is not / isn't). Vẫn chưa có câu hỏi Yes/No.",
         "Thứ 5: ôn phủ định, KHÔNG câu hỏi. Thứ 6: bắt đầu dạy câu hỏi với to be (Is he...? Who is...?). Thứ 7: dùng cả ba dạng."],
   reading="Mai giới thiệu gia đình (Sub 1), nghề nghiệp của người thân (Sub 2), tính cách (Sub 3), cuộc sống gia đình, hàng xóm (Sub 4).",
   write=["Thứ 2: giới thiệu 3 người thân (3 đến 5 câu): tên, quan hệ, tuổi.","Thứ 4: viết về nghề và tính cách của một người (4 đến 5 câu).","Thứ 6: viết 5 câu hỏi và trả lời về một người trong gia đình (dùng Is / Who)."]),
 2: dict(topic="Family", grammar="Present simple, CHỈ câu khẳng định (I cook, she works...)", level="A2-B1", kind="B", subs=[
     ("Chores", W("cook, clean, wash up, repair, look after, take care of, shop for")),
     ("How often", W("every day, in the morning, after dinner, on Sundays, at the weekend, once a week, all together")),
     ("Feelings and relationships", W("get on well with, argue, miss, trust, support, worry about, look like, take after")),
     ("Traditions", W("tradition, celebrate, gather, generation, respect, advice, share"))],
   conn="when, who, before, after", chars="Mai, Nam, Lan, Minh, Hoa (như tuần 1) và ông bà",
   gate=["Cả tuần CHỈ câu khẳng định ở present simple (I / you / we / they + V; he / she / it + V-s/es). KHÔNG phủ định (don't / doesn't), KHÔNG câu hỏi Do / Does: các dạng này dạy ở tuần 4.",
         "Vẫn dùng được to be đã học ở tuần 1 (kể cả phủ định và câu hỏi với to be)."],
   reading="Một ngày cuối tuần của gia đình: ai làm việc nhà gì, bao lâu một lần, quan hệ, truyền thống.",
   write=["Thứ 2: kể 4 đến 5 việc nhà trong gia đình bạn.","Thứ 4: viết 5 đến 6 câu về một ngày cuối tuần (dùng when / before / after).","Thứ 6: viết 6 đến 7 câu về quan hệ và truyền thống của gia đình (dùng who)."]),
 3: dict(topic="Family (ôn)", grammar="Ôn to be + present simple khẳng định; không dạy mới", level="B1", kind="R", subs=[],
   up=W("caring, generous, strict, patient, supportive, responsible, independent, easy-going, upbringing, extended family"),
   conn="although, which, who / that, if", chars="Mai, Nam, Lan, Minh, Hoa, ông bà",
   gate=["Không dạy ngữ pháp mới; chỉ dùng to be và present simple khẳng định. Không phủ định present simple, không câu hỏi Do / Does."],
   reading="\"Three generations under one roof\": ba thế hệ sống chung (170 đến 220 từ, B1).",
   write=["Thứ 7: viết 8 đến 10 câu về gia đình lý tưởng của bạn, dùng ít nhất 5 từ nâng cấp và 2 từ nối (although, which)."]),
 4: dict(topic="A day in my life", grammar="Present simple: phủ định, câu hỏi, trạng từ tần suất", level="A2", kind="A", subs=[
     ("Morning routine", W("get up, brush teeth, take a shower, get dressed, have breakfast, leave home, catch the bus")),
     ("Work and study", W("start work, finish class, lesson, homework, colleague, lunch break, meeting")),
     ("Evening", W("cook dinner, watch TV, tidy up, relax, text friends, go to bed, stay up late")),
     ("Weekend", W("sleep in, go shopping, visit friends, rarely, hardly ever, at the weekend, once a week"))],
   conn="and, but, so, because", chars="Mai, Nam, Lan, Tom (đồng nghiệp nước ngoài)",
   gate=["Thứ 2, Thứ 3: câu khẳng định + trạng từ tần suất (always, usually, often, sometimes, never). KHÔNG don't / doesn't, KHÔNG Do / Does.",
         "Thứ 4: bắt đầu dạy phủ định (don't / doesn't). Thứ 5: ôn phủ định.",
         "Thứ 6: bắt đầu dạy câu hỏi Do / Does. Thứ 7: dùng cả ba."],
   reading="Một ngày của Mai: sáng, đi làm hoặc học, tối, cuối tuần.",
   write=["Thứ 2: kể 4 đến 5 việc buổi sáng của bạn.","Thứ 4: viết 5 câu về công việc hoặc việc học, có 2 câu phủ định.","Thứ 6: viết 5 câu hỏi Do / Does cho một người bạn rồi trả lời."]),
 5: dict(topic="A day in my life", grammar="Present continuous so với present simple", level="A2-B1", kind="B", subs=[
     ("Right now at home", W("wash up, repair, wait for, chat online, talk on the phone, clean the window, rest")),
     ("Right now outside", W("traffic, queue, rush, deliver, serve customers, crowded, in a hurry")),
     ("These days", W("prepare for, study for an exam, look for, save money, move house, learn, these days")),
     ("Simple or continuous?", W("know, understand, believe, need, want, at the moment, currently"))],
   conn="when, while, because, but", chars="Mai, Nam, Lan, Minh, Hanh (bán bánh)",
   gate=["Thứ 2, Thứ 3: present continuous khẳng định (is / are + V-ing). Chưa có phủ định và câu hỏi của present continuous.",
         "Thứ 4: thêm phủ định (isn't / aren't + V-ing). Thứ 6: thêm câu hỏi (Is he working? What are they doing?).",
         "Thứ 7: so sánh simple với continuous; động từ trạng thái (know, want...) KHÔNG dùng V-ing. Present simple đã học ở tuần 2 và 4 được dùng tự do."],
   reading="Mai gọi video cho Nam: mỗi người đang làm gì ngay lúc này, dạo này đang bận gì.",
   write=["Thứ 2: tả 4 đến 5 việc người trong nhà đang làm.","Thứ 4: tả cảnh ngoài phố (5 đến 6 câu), có 2 câu phủ định.","Thứ 6: viết 6 đến 7 câu về việc bạn đang làm dạo này so với thói quen thường ngày."]),
 6: dict(topic="A day in my life (ôn)", grammar="Ôn present simple và present continuous; không dạy mới", level="B1", kind="R", subs=[],
   up=W("exhausted, hectic, routine, schedule, deadline, commute, flexible, productive, spare time, work-life balance"),
   conn="although, which, while, so that", chars="Mai, Nam, Lan, Minh, Tom",
   gate=["Không dạy ngữ pháp mới; dùng present simple và present continuous đã học (cả phủ định và câu hỏi)."],
   reading="\"A hectic week in the city\" (170 đến 220 từ, B1).",
   write=["Thứ 7: viết 8 đến 10 câu so sánh một tuần bận rộn với một tuần thư giãn, dùng ít nhất 5 từ nâng cấp."]),
 7: dict(topic="Home and neighbourhood", grammar="There is / There are + giới từ chỉ vị trí", level="A2", kind="A", subs=[
     ("Rooms and furniture", W("living room, bedroom, bathroom, kitchen, sofa, wardrobe, shelf")),
     ("Things in the home", W("fridge, cooker, washing machine, lamp, curtain, mirror, carpet")),
     ("Places in the neighbourhood", W("post office, supermarket, pharmacy, bakery, park, bus stop, bank")),
     ("Directions", W("next to, opposite, between, behind, in front of, on the corner, near"))],
   conn="and, but, because, so, who", chars="Mai, Long (chủ nhà), Hoa, Nam",
   gate=["Thứ 2, Thứ 3: There is / There are khẳng định với a / an / some. Chưa có phủ định (isn't / aren't, any) và câu hỏi.",
         "Thứ 4: thêm phủ định và any. Thứ 5: ôn. Thứ 6: thêm câu hỏi (Is there...? Are there any...?). Thứ 7: dùng cả ba, giới thiệu giới từ vị trí cho chỉ đường."],
   reading="Mai đi xem nhà thuê cùng Long, chủ nhà: phòng, đồ đạc, khu phố.",
   write=["Thứ 2: tả phòng của bạn (4 đến 5 câu).","Thứ 4: tả căn bếp, có 2 câu phủ định.","Thứ 6: viết 5 câu hỏi về khu phố của một người bạn."]),
 8: dict(topic="Home and neighbourhood", grammar="So sánh hơn và so sánh nhất", level="A2-B1", kind="B", subs=[
     ("Size and price", W("spacious, cramped, expensive, cheap, affordable, rent, floor, view")),
     ("Location and transport", W("convenient, noisy, quiet, crowded, safe, central, suburb")),
     ("House or flat", W("garden, balcony, lift, landlord, tenant, flat, neighbourhood")),
     ("Best places in my city", W("the best, the worst, popular, lively, peaceful, modern, traditional"))],
   conn="because, so, although, which", chars="Mai, Long, Hoa, Nam",
   gate=["Thứ 2, Thứ 3: so sánh hơn khẳng định (bigger than, more expensive than). Chưa có as...as hay so sánh nhất.",
         "Thứ 4: thêm not as ... as và phủ định. Thứ 6: thêm so sánh nhất (the biggest, the most expensive) và câu hỏi so sánh.",
         "Thứ 7: dùng tất cả. There is / are (tuần 7) dùng tự do."],
   reading="Mai so sánh hai căn nhà: một căn trong thành phố, một căn ở ngoại ô.",
   write=["Thứ 2: so sánh 2 căn phòng (4 đến 5 câu).","Thứ 4: so sánh khu phố của bạn với một khu khác (5 đến 6 câu, có not as ... as).","Thứ 6: viết 6 đến 7 câu về nơi tốt nhất trong thành phố của bạn."]),
 9: dict(topic="Home and neighbourhood (ôn)", grammar="Ôn there is / are, giới từ, so sánh; không dạy mới", level="B1", kind="R", subs=[],
   up=W("cosy, spacious, convenient, peaceful, lively, modern, traditional, run-down, facilities, environment"),
   conn="although, which, who / that, whereas", chars="Mai, Long, Hoa, Nam",
   gate=["Không dạy mới; dùng there is / are, giới từ, so sánh hơn / nhất đã học."],
   reading="\"Choosing a place to live\" (170 đến 220 từ, B1).",
   write=["Thứ 7: viết 8 đến 10 câu giải thích bạn chọn sống ở đâu và vì sao, dùng ít nhất 5 từ nâng cấp và whereas."]),
}

SCHED_A = """| Thứ | Nội dung | `output` |
|---|---|---|
| 2 `new` | Sub 1 | có (Thứ 2) |
| 3 `review` | Ôn Sub 1, đọc trước Sub 2 | không |
| 4 `new` | Sub 2 | có |
| 5 `review` | Ôn Sub 1 và 2, đọc trước Sub 3 | không |
| 6 `new` | Sub 3 | có |
| 7 `week` | Ôn cả tuần, bài đọc mới hoàn toàn, giới thiệu Sub 4, báo cáo | không |"""
SCHED_R = """Tuần ôn (không có Sub mới). Mỗi buổi dùng `kind`: Thứ 2 `week`, các buổi còn lại `review`, Thứ 7 `week`.

| Thứ | Nội dung |
|---|---|
| 2 | Quiz 20 câu ôn tuần 1 và 2 của chủ đề; đọc bài B1 mới (170 đến 220 từ); chép chính tả |
| 3 | Học 10 từ nâng cấp: nghĩa, ví dụ, thay từ cũ bằng từ nâng cấp |
| 4 | Sửa lỗi và viết lại câu (nối 2 câu bằng although, which, who...) |
| 5 | Ôn sâu bằng dạng bài khác (cloze, reorder, dialogue) |
| 6 | Chép chính tả nhiều câu; viết lại đoạn |
| 7 | Viết 8 đến 10 câu (có `output`), báo cáo tuần |"""

def nhi_brief(n):
    d = NHI[n]; role = (n - 1) % 3
    lines = [f"# BRIEF Nhi, Tuần {n}: {d['topic']}", "",
      f"- **Tuần:** {n}  |  **Chủ đề:** {d['topic']}  |  **`level`:** `{d['level']}`",
      f"- **Ngữ pháp:** {d['grammar']}",
      f"- **Nhân vật:** {d['chars']}",
      f"- **Từ nối dùng trong bài:** {d['conn']} (chỉ dùng, không giảng cấu trúc mới)",
      f"- **Loại tuần:** " + {0:"tuần 1 của chủ đề (28 từ mới, bài đọc 100 đến 130 từ, câu tối đa 15 từ)",1:"tuần 2 của chủ đề (30 từ: 18 mới + 12 cũ `recycled`, bài đọc 130 đến 170 từ, câu tối đa 18 từ)",2:"tuần ôn (10 từ `upgrade`, bài đọc 170 đến 220 từ, câu tối đa 22 từ)"}[role], ""]
    if role == 2:
        lines += ["## Danh sách `vocabList` (10 từ nâng cấp, tất cả `\"upgrade\":true`, `sub` = 1)", "", ", ".join(d["up"]), "",
                  "Mỗi từ nâng cấp nên là cách nói **cao hơn** cho ý Nhi đã biết ở 2 tuần trước (ví dụ kind, nice gợi ý caring, supportive). `ex` dùng ngữ cảnh chủ đề tuần.", ""]
    else:
        prev = NHI[n-1] if role == 1 else None
        if role == 0:
            lines += ["## Danh sách `vocabList` (28 từ mới, 7 từ mỗi sub)", ""]
            for i,(sn,ws) in enumerate(d["subs"],1): lines.append(f"- **Sub {i}: {sn}** ({len(ws)} từ): " + ", ".join(ws))
        else:
            allp = [w for _,ws in prev["subs"] for w in ws]
            rec = allp[::2][:12]
            take = [5,4,5,4]
            lines += ["## Danh sách `vocabList` (30 từ: 18 mới + 12 cũ)", "", "**18 từ mới** (lấy đúng các từ sau, đã chia theo sub):", ""]
            newc = 0
            for i,(sn,ws) in enumerate(d["subs"],1):
                k = take[i-1]; newc += k
                lines.append(f"- **Sub {i}: {sn}** ({k} từ mới): " + ", ".join(ws[:k]))
            lines += ["", f"Các từ còn lại trong danh sách chủ đề (" + "; ".join(", ".join(ws[take[i]:]) for i,(_,ws) in enumerate(d['subs'])) + ") chỉ được dùng làm **từ phụ** trong `vocab` của bước đọc, KHÔNG đưa vào `vocabList`.", "",
                      "**12 từ cũ quay lại** (`\"recycled\":true`, lấy từ `vocabList` của tuần %d, gán 3 từ cho mỗi sub 1 đến 4 theo thứ tự):" % (n-1), "", ", ".join(rec), "",
                      "Đặt cho các từ cũ **ví dụ `ex` mới** (khác ví dụ tuần trước) và dùng lại trong bài đọc hoặc bài tập của tuần."]
        lines.append("")
    lines += ["## Bảng \"chưa dạy thì chưa hỏi\"", ""] + ["- " + g for g in d["gate"]] + ["",
      "## Bài đọc", "", d["reading"], "",
      "## Lịch các buổi", "", SCHED_A if role < 2 else SCHED_R, ""]
    if role < 2:
        lines += ["Tên sub: " + "; ".join(f"Sub {i}: {sn}" for i,(sn,_) in enumerate(d['subs'],1)), ""]
    lines += ["## Bài tự viết (`output`)", ""] + ["- " + w for w in d["write"]] + ["",
      "## Ghi chú cho `meta`", "", f"- `week`: {n}; `title`: \"{d['topic']}\"; `level`: \"{d['level']}\"; `grammar`: \"{d['grammar']}\"; `subs`: " + (json_list([s for s,_ in d['subs']]) if d['subs'] else "[\"Ôn tuần 1\", \"Ôn tuần 2\", \"Từ nâng cấp\", \"Viết và báo cáo\"]") + ".", ""]
    return "\n".join(lines)

def json_list(a): return "[" + ", ".join('"%s"' % x for x in a) + "]"

# ------------------------------------------------------------------ TRI
TRI = {
 1: dict(topic="Work and automation", grammar="Đảo ngữ sau trạng từ phủ định (Not only, Rarely, Never, Seldom, Hardly)", level="B2-C1", subs=[
     ("The changing job market", W("job displacement, labour market, skills gap, redundancy, gig economy, workforce, be made redundant")),
     ("The case for automation", W("boost productivity, cut costs, streamline operations, a double-edged sword, reap the benefits, cutting-edge, labour-saving")),
     ("The risks", W("widen the inequality gap, job security, erode skills, put people out of work, a growing sense of insecurity, overreliance on, fall short of")),
     ("The way forward", W("reskill, lifelong learning, adapt to, strike a balance, safety net, a pressing issue, mitigate the impact"))],
   reading="Bài luận mẫu (opinion essay) 220 đến 280 từ: tự động hóa là mối đe dọa hay cơ hội; đoạn đầu có luận điểm, có nhượng bộ ngắn.",
   write=["Thứ 2 (viết): 1 đoạn luận điểm 70 đến 100 từ, `useWords` Not only / Rarely / Never.","Thứ 3 (viết lại): đoạn yếu 60 đến 80 từ viết lại bằng đảo ngữ.","Thứ 4 (viết): lập luận có phản biện 130 đến 170 từ.","Thứ 5 (nói): phản biện 60 giây.","Thứ 6 (nói): mở đầu thuyết phục 90 giây.","Thứ 7 (viết có giờ): đoạn kết luận + dàn ý, 150 từ."]),
 2: dict(topic="Work and automation", grammar="Câu chẻ và pseudo-cleft (It is ... that, What ... is ..., The reason why ... is that ...)", level="C1", dr=True, subs=[
     ("Making a claim", W("argue that, maintain that, there is no denying that, a compelling case")),
     ("Supporting with evidence", W("according to, a growing body of evidence, a case in point")),
     ("Persuading the audience", W("appeal to, call for, advocate, sway opinion, rally support, take a stand")),
     ("Rebutting", W("dismiss the claim, counter the argument, to some extent, beside the point, on the contrary"))],
   recyc=W("job displacement, labour market, skills gap, gig economy, boost productivity, a double-edged sword, widen the inequality gap, job security, reskill, lifelong learning, strike a balance, mitigate the impact"),
   reading="Bài lập luận 280 đến 360 từ: claim, reason, evidence, phản biện; dùng nhiều câu chẻ.",
   write=["Thứ 2 (viết): đoạn claim + reason + evidence 80 đến 110 từ.","Thứ 3 (viết lại): đoạn yếu 70 từ dùng câu chẻ.","Thứ 4 (**DATA REPORT**): báo cáo số liệu 150 đến 190 từ. Biểu đồ đường (`kind:\"line\"`) tỉ lệ nhiệm vụ được tự động hóa ở hai ngành (Manufacturing, Services), 4 mốc năm, một mốc dự báo; gợi ý xu hướng, so sánh, overview; ngữ pháp C1: danh hóa và câu chẻ (What the data show is...).","Thứ 5 (nói): phản biện 60 giây.","Thứ 6 (nói): thuyết phục 60 giây.","Thứ 7 (viết có giờ): bài ngắn 180 đến 200 từ."]),
 3: dict(topic="Work and automation (ôn)", grammar="Ôn đảo ngữ và câu chẻ; không dạy mới", level="C1", up=W("displace, obsolete, adept, upheaval, prevalent, mitigate, workforce, precarious, disruption, resilience, equitable, retrain, a seismic shift, hinge on"),
   reading="Bài viết dài 380 đến 480 từ: phân tích hai phía, có số liệu minh họa.",
   write=["Thứ 7 (viết có giờ): bài luận 250 từ (`minWords` 230) trong 40 phút: Should governments slow down automation?","Thứ 7 (nói): thuyết phục 2 phút."]),
 4: dict(topic="Technology and privacy", grammar="Bị động nâng cao và cấu trúc impersonal (It is widely believed that ..., is said to, is thought to have)", level="C1", subs=[
     ("Data collection", W("harvest personal data, digital footprint, targeted advertising, informed consent, data breach, mass surveillance, terms and conditions")),
     ("The benefits", W("enhance public safety, combat crime, personalised services, streamline access, a seamless experience, predictive analytics, tailor-made")),
     ("The threats", W("erosion of privacy, invasion of privacy, be exploited for, big tech, lack of transparency, hold sb accountable, tip the balance")),
     ("Regulation", W("robust legislation, data protection laws, safeguard privacy, opt out of, impose penalties, ethical guidelines, digital literacy"))],
   reading="Discursive essay 220 đến 280 từ cân bằng hai phía về giám sát bằng camera và dữ liệu cá nhân; nhiều bị động và impersonal.",
   write=["Thứ 2: đoạn 70 đến 100 từ về dữ liệu cá nhân.","Thứ 3: viết lại đoạn yếu bằng bị động.","Thứ 4: lập luận 130 đến 170 từ có hedging.","Thứ 5: nói phản biện 60 giây.","Thứ 6: nói 90 giây về quyền riêng tư.","Thứ 7: đoạn kết luận + dàn ý 150 từ."]),
 5: dict(topic="Technology and privacy", grammar="Danh hóa (nominalisation) và văn phong học thuật", level="C1", dr=True, subs=[
     ("Academic stance", W("it is widely believed that, it has been argued that, be regarded as, to a large extent, with regard to")),
     ("Cause and effect", W("in the light of, a marked increase in, give rise to, stem from")),
     ("Evidence and implications", W("a substantial proportion of, be attributed to, hinge on, bear implications for, shed light on")),
     ("Wider consequences", W("a far-reaching consequence, in the long run, by and large, strike at the heart of"))],
   recyc=W("digital footprint, targeted advertising, informed consent, data breach, mass surveillance, enhance public safety, predictive analytics, erosion of privacy, lack of transparency, hold sb accountable, robust legislation, digital literacy"),
   reading="Bài học thuật 280 đến 360 từ về quyền riêng tư, dày danh hóa (the proliferation of, the erosion of).",
   write=["Thứ 2: đoạn học thuật 80 đến 110 từ.","Thứ 3: viết lại đoạn động từ thành danh hóa.","Thứ 4 (**DATA REPORT**): báo cáo số liệu 150 đến 190 từ. **Bảng** (`kind:\"table\"` hoặc `bar`): tỉ lệ người dùng lo ngại về quyền riêng tư theo 4 nhóm tuổi, hai năm so sánh; ngữ pháp C1: danh hóa (a marked increase in concern about), so sánh gấp.","Thứ 5: nói phản biện 60 giây.","Thứ 6: nói 60 giây dùng văn phong học thuật.","Thứ 7: bài ngắn 180 đến 200 từ."]),
 6: dict(topic="Technology and privacy (ôn)", grammar="Ôn bị động nâng cao và danh hóa; không dạy mới", level="C1", up=W("ubiquitous, pervasive, intrusive, unwarranted, scrutiny, safeguards, compromise, oversight, accountability, transparency, proliferation, ramifications, anonymity, jeopardise"),
   reading="Bài viết dài 380 đến 480 từ về giám sát và niềm tin xã hội.",
   write=["Thứ 7 (viết có giờ): luận 250 từ: Does digital convenience justify the loss of privacy?","Thứ 7 (nói): 2 phút."]),
 7: dict(topic="Environment and responsibility", grammar="Điều kiện đảo ngữ và hỗn hợp (Had it not been for ..., Were ... to ..., Should ... , mixed conditionals)", level="C1", subs=[
     ("The scale of the problem", W("climate crisis, carbon footprint, greenhouse gas emissions, irreversible damage, biodiversity loss, rising sea levels, a tipping point")),
     ("Responsibility of individuals and firms", W("shoulder the responsibility, lead by example, sustainable practices, curb emissions, offset carbon, greenwashing, green consumerism")),
     ("Government action", W("carbon tax, binding targets, phase out fossil fuels, subsidise renewables, international cooperation, enforce regulations, short-term interests")),
     ("Solutions", W("transition to clean energy, circular economy, collective action, long-term vision, intergenerational fairness, a sense of urgency, turn the tide"))],
   reading="Problem–solution essay 220 đến 280 từ về biến đổi khí hậu, có điều kiện đảo ngữ.",
   write=["Thứ 2: đoạn 70 đến 100 từ nêu vấn đề.","Thứ 3: viết lại đoạn yếu bằng điều kiện đảo ngữ.","Thứ 4: lập luận 130 đến 170 từ (problem–solution).","Thứ 5: nói phản biện 60 giây.","Thứ 6: nói 90 giây.","Thứ 7: đoạn kết + dàn ý 150 từ."]),
 8: dict(topic="Environment and responsibility", grammar="Subjunctive và cấu trúc trang trọng (It is vital that ... be, I insist that, lest, so as not to)", level="C1-C2", subs=[
     ("Calling for action", W("it is imperative that, it is vital that, I urge you to, the time to act is now, a call to arms")),
     ("Raising the stakes", W("at stake is, make no mistake, the stakes could not be higher, history will judge, there is no Planet B")),
     ("Appealing to values", W("we owe it to, a moral obligation, let us not forget, we must not allow, consider this")),
     ("Closing with impact", W("rise to the challenge, take decisive action, lest we"))],
   recyc=W("carbon footprint, greenhouse gas emissions, irreversible damage, a tipping point, shoulder the responsibility, lead by example, curb emissions, carbon tax, binding targets, international cooperation, circular economy, turn the tide"),
   reading="Bài phát biểu thuyết phục (persuasive speech) 280 đến 360 từ, có tricolon, đối lập, subjunctive.",
   write=["Thứ 2: đoạn mở bài phát biểu 80 đến 110 từ.","Thứ 3: viết lại đoạn bằng subjunctive.","Thứ 4: viết bài phát biểu ngắn 150 đến 190 từ.","Thứ 5: nói phản biện 60 giây.","Thứ 6: **nói thuyết phục 120 giây** (kêu gọi hành động).","Thứ 7: bài ngắn 180 đến 200 từ."]),
 9: dict(topic="Environment and responsibility (ôn)", grammar="Ôn điều kiện nâng cao và subjunctive; không dạy mới", level="C1-C2", up=W("unprecedented, mitigate, adverse, imperative, stringent, viable, detrimental, collective, culpable, sustainable, finite, tangible, pressing, ambitious"),
   reading="Bài viết dài 380 đến 480 từ về trách nhiệm chung.",
   write=["Thứ 7 (viết có giờ): luận 250 từ: Who should bear the cost of tackling climate change?","Thứ 7 (nói): bài phát biểu 2 phút."]),
}

SRC = {1:"McKinsey Global Institute (jobs lost and gained), World Economic Forum Future of Jobs Report, OECD Employment Outlook, The Economist và The Guardian về tự động hóa, bài trên tạp chí học thuật về lao động và công nghệ (Journal of Economic Perspectives)",
       2:"như chủ đề: dữ liệu về tỉ lệ việc làm có rủi ro tự động hóa (OECD, ILO) cho biểu đồ số liệu",
       3:"như tuần 1 và 2, thêm một bài xã luận phản biện",
       4:"The Guardian, Wired, MIT Technology Review về giám sát và dữ liệu cá nhân; Electronic Frontier Foundation; văn bản GDPR; tạp chí học thuật như Surveillance & Society",
       5:"khảo sát công khai về quan ngại quyền riêng tư (Pew Research Center, Eurobarometer) cho bảng số liệu; văn phong học thuật ở tạp chí khoa học xã hội",
       6:"như tuần 4 và 5",
       7:"báo cáo tóm tắt của IPCC, Our World in Data, Nature Climate Change, The Guardian (environment), The Economist",
       8:"bài phát biểu thật về khí hậu (ví dụ phát biểu tại Liên Hợp Quốc, TED) để học nhịp và tu từ; chỉ học cách viết, không chép",
       9:"như tuần 7 và 8"}
def tri_brief(n):
    d = TRI[n]; role = (n - 1) % 3
    lines = [f"# BRIEF Trí, Tuần {n}: {d['topic']}", "",
      f"- **Tuần:** {n}  |  **Chủ đề:** {d['topic']}  |  **`level`:** `{d['level']}`",
      f"- **Ngữ pháp C1–C2:** {d['grammar']}",
      "- **Loại tuần:** " + {0:"tuần 1 của chủ đề (28 cụm mới, bài đọc 220 đến 280 từ, câu tối đa 30 từ)",1:"tuần 2 của chủ đề (30 cụm: 18 mới + 12 cũ `recycled`, bài đọc 280 đến 360 từ, câu tối đa 35 từ)",2:"tuần ôn (14 cụm `upgrade`, bài đọc 380 đến 480 từ, câu tối đa 40 từ)"}[role],
      "- **Thời lượng:** 60 phút mỗi buổi (xem khung giờ trong prompt)",
      "- **Báo cáo số liệu (DATA REPORT):** " + ("**CÓ** (Thứ 4, xem bên dưới)" if d.get("dr") else "không trong tuần này"), ""]
    if role == 2:
        lines += ["## Danh sách `vocabList` (14 cụm nâng cấp, tất cả `\"upgrade\":true`, `sub` = 1)", "", ", ".join(d["up"]), "",
                  "Mỗi cụm là cách nói trang trọng, chính xác hơn cho một ý đã học trong 2 tuần trước; `ex` là câu trang trọng có thể dùng trong luận.", "",
                  "## Lịch các buổi (tuần ôn)", "",
                  "| Thứ | Nội dung |", "|---|---|",
                  "| 2 | Quiz 24 câu ôn hai tuần trước; bài đọc dài mới; chép chính tả |",
                  "| 3 | 14 cụm nâng cấp: nghĩa, ví dụ, thay thế cụm cũ; `output`: viết lại đoạn bằng cụm nâng cấp |",
                  "| 4 | Sửa lỗi ngữ pháp C1–C2 và register; viết lại câu nâng văn phong; `output`: viết đoạn |",
                  "| 5 | Ôn sâu bằng dạng bài khác; `output`: nói phản biện 60 giây |",
                  "| 6 | Chép chính tả câu dài; viết lại đoạn; `output`: nói 90 giây |",
                  "| 7 | Bài luận có giờ + bài nói 2 phút, báo cáo tuần |", ""]
    else:
        if role == 0:
            lines += ["## Danh sách `vocabList` (28 cụm mới, 7 cụm mỗi sub)", ""]
            for i,(sn,ws) in enumerate(d["subs"],1): lines.append(f"- **Sub {i}: {sn}**: " + ", ".join(ws))
        else:
            lines += ["## Danh sách `vocabList` (30 cụm: 18 mới + 12 cũ)", "", "**18 cụm mới**:", ""]
            for i,(sn,ws) in enumerate(d["subs"],1): lines.append(f"- **Sub {i}: {sn}** ({len(ws)} cụm): " + ", ".join(ws))
            lines += ["", f"**12 cụm cũ quay lại** (`\"recycled\":true`, lấy từ tuần {n-1}; gán 3 cụm cho mỗi sub 1 đến 4):", "", ", ".join(d["recyc"]), "",
                      "Mỗi cụm cũ có `ex` **mới** (khác ví dụ cũ) và được dùng lại trong bài đọc hoặc bài tập."]
        lines += ["", "## Lịch các buổi", "", "Theo bảng \"Lịch 6 buổi\" của prompt (mỗi buổi 60 phút, có `output` cả 6 buổi). Tên sub: " + "; ".join(f"Sub {i}: {sn}" for i,(sn,_) in enumerate(d['subs'],1)) + "."]
    lines += ["", "## Bài đọc", "", d["reading"], "", "## Nguồn thật cần tìm đọc trước khi soạn (gợi ý, bạn phải tự tìm và kiểm chứng)", "", SRC[n], "", "## Bài viết và nói (`output`)", ""] + ["- " + w for w in d["write"]]
    if d.get("dr"):
        lines += ["", "## Báo cáo số liệu (DATA REPORT)", "", "Dùng mục \"Mảng báo cáo số liệu\" của prompt. Đề: \"The chart below shows ... Summarise the information by selecting and reporting the main features, and make comparisons where relevant. Write at least 150 words.\" Số liệu là minh họa (ghi `note: \"Fictional data for practice.\"`) và **phải khớp tuyệt đối** với `sample`, `model` và mọi câu hỏi về số liệu."]
    lines += ["", "## Ghi chú cho `meta`", "", f"- `week`: {n}; `title`: \"{d['topic']}\"; `level`: \"{d['level']}\"; `grammar`: \"{d['grammar']}\"."]
    return "\n".join(lines) + "\n"

if __name__ == "__main__":
    for n in range(1, 10):
        for who, fn in (("nhi", nhi_brief), ("tri", tri_brief)):
            p = os.path.join(ROOT, who, "tuan-%02d.md" % n)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w", encoding="utf-8").write(fn(n).rstrip() + "\n")
    print("ok")
